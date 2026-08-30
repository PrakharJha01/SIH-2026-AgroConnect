"""
Check historical market price data in database and prepare for ML training.
"""
import pandas as pd
from database.database import get_db_session
from database.models import MarketPrice

db = get_db_session()

# Query all market prices
prices = db.query(MarketPrice).all()

print("="*60)
print("DATABASE MARKET PRICES")
print("="*60)
print(f"Total records: {len(prices)}")

if prices:
    # Convert to DataFrame
    df = pd.DataFrame([{
        'date': p.date,
        'crop': p.crop,
        'quality': p.quality,
        'market': p.market,
        'state': p.state,
        'district': p.district,
        'min_price': p.min_price,
        'max_price': p.max_price,
        'modal_price': p.modal_price
    } for p in prices])

    print(f"\nDate range: {df['date'].min()} to {df['date'].max()}")
    print(f"Unique crops: {df['crop'].nunique()}")
    print(f"Unique markets: {df['market'].nunique()}")

    print("\nSample data:")
    print(df.head(10))

    print("\nPotato data:")
    potato_df = df[df['crop'] == 'Potato']
    print(f"Potato records: {len(potato_df)}")
    if len(potato_df) > 0:
        print(potato_df)

db.close()

print("\n" + "="*60)
print("CSV DATA")
print("="*60)

csv_df = pd.read_csv('data/seed/Price.csv')
print(f"CSV has {len(csv_df)} records for date: {csv_df['Arrival_Date'].unique()}")
print(f"Potato records in CSV: {len(csv_df[csv_df['Commodity'].str.contains('Potato', case=False, na=False)])}")

