import re

with open('pages/14_Opportunities.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. We must move matches = find_buyers_for_lot(lot_id) or [] 
#    up above the 3-metric summary.

replacement = '''
# ---------------------------------------------------------------------------
# 3-metric summary: Mandi / ML Predicted / Best Buyer Offer
# ---------------------------------------------------------------------------
with st.spinner("Loading market data and price prediction..."):
    mandi_price = get_latest_modal_price(lot.crop) or 0.0
    try:
        prediction = predict_future_price(lot.crop, days_ahead=5)
    except Exception as exc:  # noqa: BLE001
        prediction = {"success": False, "error": str(exc)}
        
with st.spinner("🔍 Finding matching buyers..."):
    matches = find_buyers_for_lot(lot_id) or []

best_buyer_offer = float(max((m["offer_price"] for m in matches), default=0.0)) if matches else 0.0
best_buyer_name = max(matches, key=lambda x: x["offer_price"])["buyer_name"] if matches else "—"

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
'''

text = re.sub(
    r'# ---------------------------------------------------------------------------\n# 3-metric summary: Mandi / ML Predicted / Best Buyer Offer\n# ---------------------------------------------------------------------------\nwith st\.spinner\("Loading market data and price prediction\.\.\."\):\n\s+mandi_price = get_latest_modal_price\(lot\.crop\) or 0\.0\n\s+try:\n\s+prediction = predict_future_price\(lot\.crop, days_ahead=5\)\n\s+except Exception as exc:  # noqa: BLE001\n\s+prediction = {"success": False, "error": str\(exc\)}\n\n# Best buyer offer \(will fill in after we load matches below; placeholder now\)\nbest_buyer_offer = 0\.0\nbest_buyer_name = "[^"]+"\n\ncol1, col2, col3 = st\.columns\(3\)\nwith col1:\n\s+st\.metric\(', 
    replacement, 
    text
)

# 2. Down in the matching section, remove the second loader and duplicate assign.
replacement2 = '''# ---------------------------------------------------------------------------
# Per-buyer match cards
# ---------------------------------------------------------------------------
st.markdown("## 🤝 Matching Buyers")

if not matches:
    st.info("No matching buyers right now. Try lowering the asking price, widening the date, or check back as more buyers register.")
else:
    st.success(f"✅ Found {len(matches)} matching buyer{'s' if len(matches) != 1 else ''}.")
'''

text = re.sub(
    r'# ---------------------------------------------------------------------------\n# Per-buyer match cards\n# ---------------------------------------------------------------------------\nst\.markdown\("## ðŸ¤  Matching Buyers"\)\nwith st\.spinner\("ðŸ”  Finding matching buyers\.\.\."\):\n\s+matches = find_buyers_for_lot\(lot_id\) or \[\]\n\nif not matches:\n\s+st\.info\("No matching buyers right now\. Try lowering the asking price, widening the date, or check back as more buyers register\."\)\nelse:\n\s+# Update the best-offer metric now that we have matches\n\s+if matches:\n\s+best_buyer_offer = float\(matches\[0\]\["offer_price"\]\)\n\s+best_buyer_name = matches\[0\]\["buyer_name"\]\n\n\s+st\.success\(f"âœ… Found \{len\(matches\)\} matching buyer\{\'s\' if len\(matches\) != 1 else \'\'\}\."\)',
    replacement2,
    text
)

with open('pages/14_Opportunities.py', 'w', encoding='utf-8') as f:
    f.write(text)
