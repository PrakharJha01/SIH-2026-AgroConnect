"""
Reset database - Drop all tables and recreate with fresh seed data.
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database.database import engine, init_database
from database.models import Base

def reset_database():
    """Drop all tables and recreate."""
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)
    print("✓ All tables dropped")

    print("\nCreating fresh tables...")
    init_database()
    print("✓ Database schema created")

    print("\nSeeding demo data...")
    from database.seed import seed_all
    # Import after tables are created
    from database.seed import seed_users, seed_crop_lots, seed_buyer_requirements, seed_market_prices, seed_storage_facilities
    from database.database import get_db_session

    db = get_db_session()
    try:
        seed_users(db)
        seed_crop_lots(db)
        seed_buyer_requirements(db)
        seed_market_prices(db)
        seed_storage_facilities(db)
        print("\n✅ Database reset complete!")
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    reset_database()
