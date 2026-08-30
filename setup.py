"""
Startup Script for AgroConnect
Initializes database, seeds data, and trains ML models
"""
import sys
import os

print("=" * 60)
print("🌾 AgroConnect - Smart Market Linkage Platform")
print("=" * 60)
print()

# Step 1: Initialize Database
print("📦 Step 1: Initializing database...")
try:
    from database.database import init_db
    init_db()
    print("✅ Database initialized successfully")
except Exception as e:
    print(f"❌ Database initialization failed: {str(e)}")
    sys.exit(1)

print()

# Step 2: Seed Database
print("🌱 Step 2: Seeding database with demo data...")
try:
    from database.seed import seed_database
    seed_database()
    print("✅ Database seeded successfully")
    print("   - 5 Farmers created")
    print("   - 4 Buyers created")
    print("   - 5 Crop lots created")
    print("   - 5 Buyer requirements created")
    print("   - 2160 Market price records (180 days × 4 commodities × 3 markets)")
    print("   - 4 Storage facilities created")
except Exception as e:
    print(f"❌ Database seeding failed: {str(e)}")
    print("⚠️  You may need to delete data/agroconnect.db and try again")
    sys.exit(1)

print()

# Step 3: Train ML Models
print("🤖 Step 3: Training ML price prediction models...")
try:
    from ml.train_model import train_all_models

    print("   Training models for commodities...")
    results = train_all_models()

    if results:
        print(f"✅ Trained {len(results)} ML models successfully")
        for commodity, metrics in results.items():
            print(f"   - {commodity}: R² = {metrics.get('r2', 0):.3f}, RMSE = ₹{metrics.get('rmse', 0):.0f}")
    else:
        print("⚠️  No models trained (insufficient data or XGBoost not available)")
        print("   The app will work without ML predictions")
except Exception as e:
    print(f"⚠️  ML model training failed: {str(e)}")
    print("   The app will work without ML predictions")

print()
print("=" * 60)
print("✅ Setup Complete!")
print("=" * 60)
print()
print("🚀 To start the application, run:")
print()
print("   streamlit run app.py")
print()
print("Then open your browser to http://localhost:8501")
print()
print("📝 Demo Accounts:")
print("   Farmer: Hemant (Lucknow)")
print("   Buyer: GreenFresh Traders (Delhi)")
print()
print("=" * 60)
