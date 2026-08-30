"""End-to-end smoke test for the buyer-initiated negotiation flow.

Mirrors smoke_test_negotiation.py but exercises the buyer path:
  1. Create a fresh farmer + lot
  2. Create a fresh buyer + requirement
  3. find_lots_for_requirement  (the same call pages/23_Buyer_Matches.py uses)
  4. Buyer-initiated start_negotiation  (the same call the inline form uses)
  5. Buyer counter-offer
  6. Farmer counter-offer
  7. Buyer accepts → Deal
  8. Verify lot.status='sold', req.status='fulfilled'
  9. Reject path on a fresh pair
 10. List buyer negotiations + deals via the same service functions the page uses
"""
import os
import sys
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database.database import init_database, get_db_session
from database.models import User, Profile, CropLot, BuyerRequirement
from utils.auth import hash_password
from utils.constants import ROLE_FARMER, ROLE_BUYER

from services.lot_service import create_lot
from services.buyer_service import create_requirement
from services.negotiation_service import (
    start_negotiation,
    make_offer,
    accept_negotiation,
    reject_negotiation,
    get_negotiation,
    get_buyer_negotiations,
    get_farmer_negotiations,
    get_deals,
)
from services.matching_service import find_lots_for_requirement


def get_or_create_user(name: str, phone: str, role: str, district: str = "Demo District") -> int:
    db = get_db_session()
    try:
        u = db.query(User).filter(User.phone == phone).first()
        if u:
            print(f"  → reusing {role} '{name}' id={u.id}")
            return u.id
        u = User(
            name=name,
            phone=phone,
            role=role,
            password_hash=hash_password("smoke"),
            verification_status="verified",
        )
        db.add(u)
        db.commit()
        db.refresh(u)
        db.add(Profile(
            user_id=u.id, state="Punjab", district=district, village=district,
            latitude=30.9, longitude=75.85,
            buyer_type="trader" if role == ROLE_BUYER else None,
        ))
        db.commit()
        print(f"  → created {role} '{name}' id={u.id}")
        return u.id
    finally:
        db.close()


def main() -> int:
    init_database()
    print("=" * 60)
    print("BUYER-INITIATED NEGOTIATION SMOKE TEST")
    print("=" * 60)

    # ------------------------------------------------------------------
    # 1. Users
    # ------------------------------------------------------------------
    print("\n[1] Users")
    farmer_id = get_or_create_user("BuyerTest Farmer", "+911000000111", ROLE_FARMER, "Ludhiana")
    buyer_id = get_or_create_user("BuyerTest Buyer", "+911000000222", ROLE_BUYER, "Delhi")
    farmer2_id = get_or_create_user("BuyerTest Farmer 2", "+911000000333", ROLE_FARMER, "Amritsar")
    buyer2_id = get_or_create_user("BuyerTest Reject Buyer", "+911000000444", ROLE_BUYER, "Jaipur")

    # ------------------------------------------------------------------
    # 2. Lot (fresh, active) and requirement
    # ------------------------------------------------------------------
    print("\n[2] Lot + requirement")
    lot = create_lot({
        "farmer_id": farmer_id,
        "crop": "Rice",
        "quality": "Grade A",
        "quantity": 80.0,
        "unit": "quintal",
        "location_name": "Ludhiana",
        "state": "Punjab",
        "latitude": 30.9,
        "longitude": 75.85,
        "harvest_date": date.today(),
        "can_store": True,
        "price_expected": 3200.0,
    })
    assert lot is not None
    print(f"  → lot_id={lot.id}")

    req = create_requirement({
        "buyer_id": buyer_id,
        "crop": "Rice",
        "quality": "Grade A",
        "quantity_needed": 60.0,
        "unit": "quintal",
        "location_name": "Delhi",
        "state": "Delhi",
        "latitude": 28.7,
        "longitude": 77.1,
        "offer_price": 3300.0,
        "required_by_date": date.today() + timedelta(days=5),
        "is_negotiable": True,
    })
    assert req is not None
    print(f"  → req_id (accept path)={req.id}")

    req_rej = create_requirement({
        "buyer_id": buyer2_id,
        "crop": "Rice",
        "quality": "Grade A",
        "quantity_needed": 50.0,
        "unit": "quintal",
        "location_name": "Jaipur",
        "state": "Rajasthan",
        "latitude": 26.9,
        "longitude": 75.8,
        "offer_price": 2900.0,
        "required_by_date": date.today() + timedelta(days=7),
        "is_negotiable": True,
    })
    assert req_rej is not None
    print(f"  → req_id (reject path)={req_rej.id}")

    # ------------------------------------------------------------------
    # 3. find_lots_for_requirement — same call as page 23
    # ------------------------------------------------------------------
    print("\n[3] find_lots_for_requirement")
    matches = find_lots_for_requirement(req.id)
    print(f"  → {len(matches)} matches")
    assert len(matches) >= 1
    for m in matches[:3]:
        print(f"     - {m['farmer_name']}: score={m['match_score']}, lot_id={m['lot_id']}, dist={m['distance_km']}km")
    target_match = next((m for m in matches if m["lot_id"] == lot.id), matches[0])
    assert "lot_id" in target_match, "match dict must carry lot_id for the inline form to work"
    assert "farmer_id" in target_match, "match dict must carry farmer_id"
    assert "latitude" in target_match and "longitude" in target_match, (
        "match dict must carry lat/lon so the logistics panel can render a route"
    )
    assert target_match["latitude"] is not None and target_match["longitude"] is not None, (
        "lot lat/lon must be populated — required for the route panel"
    )
    print(f"  → lot has lat/lon ({target_match['latitude']}, {target_match['longitude']})")

    # ------------------------------------------------------------------
    # 4. start_negotiation (buyer-initiated) — same call the form makes
    # ------------------------------------------------------------------
    print("\n[4] start_negotiation (buyer-initiated)")
    neg = start_negotiation(
        lot_id=target_match["lot_id"],
        requirement_id=req.id,
        initiator_role="buyer",
        initial_price=3300.0,
        initial_quantity=60.0,
        message="Buyer's opening: 3300/q for 60q, can pick up Saturday.",
    )
    assert neg is not None
    print(f"  → negotiation_id={neg.id}, status={neg.current_status}, price={neg.current_price}, qty={neg.current_quantity}")
    assert neg.current_status in ("active", "pending")
    assert neg.initiated_by == buyer_id, f"expected initiated_by=buyer {buyer_id}, got {neg.initiated_by}"

    # ------------------------------------------------------------------
    # 5. Buyer counter
    # ------------------------------------------------------------------
    print("\n[5] make_offer (buyer counter)")
    b_offer = make_offer(
        negotiation_id=neg.id,
        actor_id=buyer_id,
        actor_role="buyer",
        price=3250.0,
        quantity=60.0,
        message="Best I can do is 3250 if you confirm this week.",
    )
    assert b_offer is not None
    print(f"  → offer_id={b_offer.id}, price={b_offer.price}")
    refreshed = get_negotiation(neg.id)
    assert refreshed["current_price"] == 3250.0

    # ------------------------------------------------------------------
    # 6. Farmer counter
    # ------------------------------------------------------------------
    print("\n[6] make_offer (farmer counter)")
    f_offer = make_offer(
        negotiation_id=neg.id,
        actor_id=farmer_id,
        actor_role="farmer",
        price=3280.0,
        quantity=60.0,
        message="Can do 3280, lot is graded A.",
    )
    assert f_offer is not None
    print(f"  → offer_id={f_offer.id}, price={f_offer.price}")
    refreshed = get_negotiation(neg.id)
    assert refreshed["current_price"] == 3280.0

    # ------------------------------------------------------------------
    # 7. Buyer accepts
    # ------------------------------------------------------------------
    print("\n[7] accept_negotiation (buyer)")
    deal = accept_negotiation(neg.id, actor_id=buyer_id)
    assert deal is not None
    expected_total = 3280.0 * 60.0
    print(f"  → deal_id={deal.id}, final_price={deal.final_price}, qty={deal.final_quantity}, total={deal.total_value}")
    assert abs(deal.total_value - expected_total) < 0.01

    # ------------------------------------------------------------------
    # 8. Verify lot locked + req fulfilled
    # ------------------------------------------------------------------
    print("\n[8] verify lot.status and req.status")
    db = get_db_session()
    try:
        lot_after = db.query(CropLot).filter(CropLot.id == lot.id).first()
        req_after = db.query(BuyerRequirement).filter(BuyerRequirement.id == req.id).first()
        print(f"  → lot.status={lot_after.status}, req.status={req_after.status}")
        assert lot_after.status == "sold", f"expected 'sold', got '{lot_after.status}'"
        assert req_after.status == "fulfilled", f"expected 'fulfilled', got '{req_after.status}'"
    finally:
        db.close()

    # ------------------------------------------------------------------
    # 9. Reject path on a fresh pair
    # ------------------------------------------------------------------
    print("\n[9] reject path on a fresh lot")
    lot2 = create_lot({
        "farmer_id": farmer2_id,
        "crop": "Rice",
        "quality": "Grade A",
        "quantity": 90.0,
        "unit": "quintal",
        "location_name": "Amritsar",
        "state": "Punjab",
        "latitude": 31.6,
        "longitude": 74.9,
        "harvest_date": date.today(),
        "can_store": False,
        "price_expected": 3100.0,
    })
    assert lot2 is not None
    neg2 = start_negotiation(
        lot_id=lot2.id,
        requirement_id=req_rej.id,
        initiator_role="buyer",
        initial_price=2900.0,
        initial_quantity=50.0,
        message="Will pay 2900",
    )
    assert neg2 is not None
    ok = reject_negotiation(neg2.id, actor_id=buyer2_id, reason="Need higher grade")
    assert ok
    refreshed2 = get_negotiation(neg2.id)
    assert refreshed2["current_status"] == "rejected"
    print(f"  → negotiation #{neg2.id} status={refreshed2['current_status']}")

    # ------------------------------------------------------------------
    # 10. Lists — same calls the buyer page makes
    # ------------------------------------------------------------------
    print("\n[10] buyer lists")
    buyer_negs = get_buyer_negotiations(buyer_id)
    farmer_negs = get_farmer_negotiations(farmer_id)
    print(f"  → buyer {buyer_id} has {len(buyer_negs)} negotiations")
    print(f"  → farmer {farmer_id} has {len(farmer_negs)} negotiations")
    assert len(buyer_negs) >= 1
    assert len(farmer_negs) >= 1
    # Status the list-mode page relies on
    for n in buyer_negs:
        assert "current_status" in n, "list dicts must expose current_status"
        assert "current_price" in n
        assert "lot" in n and "crop" in n["lot"]
        assert "farmer" in n and "name" in n["farmer"]

    print("\n[11] buyer deals")
    buyer_deals = get_deals(buyer_id, "buyer")
    print(f"  → {len(buyer_deals)} deal(s)")
    assert len(buyer_deals) >= 1
    for d in buyer_deals:
        assert "final_quantity" in d, "deal dicts must expose final_quantity for the deals tab"
        assert "total_value" in d
        print(f"     • {d.get('deal_id', d.get('id'))}: {d['crop']} {d['final_quantity']} {d['unit']} @ ₹{d['final_price']} = ₹{d['total_value']:,.0f}")

    # ------------------------------------------------------------------
    # 12. Idempotency on a still-pending pair
    # ------------------------------------------------------------------
    print("\n[12] idempotency on a still-pending pair")
    # The accept path above closed the original negotiation, so we can't
    # check idempotency against it. Instead, start a fresh negotiation on
    # the reject path's lot, then re-call start_negotiation — it must
    # return the same row.
    lot3 = create_lot({
        "farmer_id": farmer_id,
        "crop": "Rice",
        "quality": "Grade A",
        "quantity": 25.0,
        "unit": "quintal",
        "location_name": "Ludhiana",
        "state": "Punjab",
        "latitude": 30.9,
        "longitude": 75.85,
        "harvest_date": date.today(),
        "can_store": True,
        "price_expected": 3200.0,
    })
    req3 = create_requirement({
        "buyer_id": buyer_id,
        "crop": "Rice",
        "quality": "Grade A",
        "quantity_needed": 20.0,
        "unit": "quintal",
        "location_name": "Delhi",
        "state": "Delhi",
        "latitude": 28.7,
        "longitude": 77.1,
        "offer_price": 3300.0,
        "required_by_date": date.today() + timedelta(days=5),
        "is_negotiable": True,
    })
    assert lot3 is not None and req3 is not None
    first = start_negotiation(
        lot_id=lot3.id, requirement_id=req3.id, initiator_role="buyer",
        initial_price=3300.0, initial_quantity=20.0, message="first",
    )
    second = start_negotiation(
        lot_id=lot3.id, requirement_id=req3.id, initiator_role="buyer",
        initial_price=3200.0, initial_quantity=20.0, message="second",
    )
    assert first is not None and second is not None
    assert first.id == second.id, f"idempotency broken: first={first.id}, second={second.id}"
    print(f"  → both calls returned negotiation #{first.id} (idempotent ✓)")

    print("\n" + "=" * 60)
    print("✅ ALL BUYER-INITIATED SMOKE TESTS PASSED")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())

