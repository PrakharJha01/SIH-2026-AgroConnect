# 🚀 AgroConnect - Quick Start Guide

## Smart India Hackathon 2024 - Problem Statement ID: 26132

---

## 📋 Prerequisites

- Python 3.10 or higher
- Windows/Linux/Mac
- 2 GB free disk space

---

## ⚡ Quick Start (3 Steps)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Streamlit (Web framework)
- XGBoost (ML price prediction)
- SQLAlchemy (Database)
- Pandas, NumPy (Data processing)
- Plotly (Visualizations)
- Folium (Maps)
- Pydantic (Validation)

### Step 2: Initialize & Seed Database

```bash
python setup.py
```

This will:
- ✅ Create SQLite database at `data/agroconnect.db`
- ✅ Seed 5 demo farmers (Hemant, Priya, Rajesh, Suresh, Meena)
- ✅ Seed 4 demo buyers (GreenFresh Traders, AgriProcess India, Metro Wholesale, FreshMart Retail)
- ✅ Create 5 crop lots
- ✅ Create 5 buyer requirements
- ✅ Generate 2160 historical market price records (180 days × 4 commodities)
- ✅ Train ML price prediction models for Potato, Wheat, Rice, Onion

**Expected output:**
```
📦 Step 1: Initializing database...
✅ Database initialized successfully

🌱 Step 2: Seeding database with demo data...
✅ Database seeded successfully
   - 5 Farmers created
   - 4 Buyers created
   - 5 Crop lots created
   ...

🤖 Step 3: Training ML price prediction models...
✅ Trained 4 ML models successfully
   - Potato: R² = 0.782, RMSE = ₹87
   - Wheat: R² = 0.756, RMSE = ₹102
   ...

✅ Setup Complete!
```

### Step 3: Launch the Application

```bash
streamlit run app.py
```

Your browser will automatically open to: **http://localhost:8501**

---

## 🎬 Demo Walkthrough (SIH Evaluation)

### **As a Farmer (Hemant from Lucknow):**

1. **Login:**
   - Click "Login / Get Started"
   - Select "Farmer" → Choose "Hemant (Lucknow, Uttar Pradesh)"
   - Click "Login & Continue"

2. **View Dashboard:**
   - See active crop lots (100q Potato)
   - View market prices

3. **Explore Opportunities:**
   - Click "View Opportunities" on the Potato lot
   - See matching buyers:
     - GreenFresh Traders (nearby, ₹2000/q)
     - AgriProcess India (processor, ₹2300/q)
     - Metro Wholesale (bulk buyer, ₹2500/q for 500q)

4. **Compare Selling Options (KEY DEMO SCREEN):**
   - Click "Compare Options"
   - See side-by-side comparison:
     - **Option A: Sell Now** → ₹1,95,000 net
     - **Option B: Wait & Store** → ₹2,15,000 net
     - **Option C: Group Sale** → ₹2,18,000 net (RECOMMENDED)
   - View ML price prediction
   - See cost breakdowns

5. **View Group Aggregation:**
   - See that Hemant (100q) + Priya (150q) + Rajesh (250q) = 500q
   - Fulfills Metro Wholesale bulk requirement
   - Shared transport saves costs

### **As a Buyer (GreenFresh Traders):**

1. **Login:**
   - Select "Buyer" → Choose "GreenFresh Traders (Delhi)"

2. **View Requirements:**
   - See posted requirements (Potato 100q, Wheat 200q)

3. **Find Matching Farmers:**
   - Click "View Matches"
   - See farmers with match scores
   - View match explanations

4. **Start Negotiation:**
   - Make offer to farmer
   - Exchange counter-offers
   - Confirm deal

---

## 📂 Project Structure

```
AgroConnect/
├── app.py                      # Landing page
├── pages/                      # Streamlit pages
│   ├── 01_Login.py
│   ├── 02_Market_Prices.py
│   ├── 10_Farmer_Dashboard.py
│   ├── 20_Buyer_Dashboard.py
│   └── ...
├── components/                 # Reusable UI components
├── services/                   # Business logic
│   ├── market_service.py
│   ├── matching_service.py
│   ├── recommendation_service.py
│   └── ...
├── ml/                         # ML pipeline
│   ├── train_model.py
│   ├── predict_price.py
│   └── ...
├── algorithms/                 # Core algorithms
│   ├── matching/
│   ├── aggregation/
│   └── recommendation/
├── database/                   # Database layer
│   ├── models.py
│   └── seed.py
├── utils/                      # Utilities
├── data/                       # SQLite database
└── models/                     # Trained ML models
```

---

## 🔑 Key Features to Demonstrate

### 1. **ML Price Prediction** (Phase 9)
- Navigate to any crop lot details
- See "Predicted Future Price" section
- Shows 5-day forecast with confidence interval
- Based on XGBoost model trained on 180 days of data

### 2. **Net Realisation Comparison** (Phase 10 - MOST IMPORTANT)
- The hero feature for SIH
- Shows 3 columns: Sell Now | Wait & Store | Group Sale
- Each option shows:
  - Gross revenue
  - Transport cost
  - Storage cost
  - **Net realisation** (the actual money farmer gets)
- Recommendation with reasoning

### 3. **Explainable Matching** (Phase 5)
- Buyer-farmer matching with scores
- Shows breakdown: Crop 40% + Quantity 25% + Distance 20% + Date 15%
- Explains each match with reasons

### 4. **Group Aggregation** (Phase 7)
- Multiple farmers combine quantities
- Fulfill bulk buyer requirements
- Shared transport costs
- Shows per-farmer benefit

### 5. **Structured Negotiation** (Phase 6)
- Offer/counter-offer system
- Accept/reject
- Deal confirmation

---

## 🧪 Testing

Run the test suite:

```bash
pytest -v
```

Tests cover:
- Net realisation calculations
- Matching algorithm
- Aggregation logic
- Recommendation engine
- ML feature engineering

---

## 🐛 Troubleshooting

### Database Already Exists Error
```bash
# Delete and recreate
rm data/agroconnect.db
python setup.py
```

### Module Not Found Error
```bash
# Make sure you're in the project directory
cd AgroConnect
pip install -r requirements.txt
```

### Streamlit Port Already in Use
```bash
streamlit run app.py --server.port 8502
```

### ML Models Not Training
- XGBoost might not be installed properly
- App will work without ML predictions
- Try: `pip install xgboost --force-reinstall`

---

## 📊 Demo Data Overview

**Farmers:**
- Hemant (Lucknow) - 100q Potato
- Priya (Agra) - 150q Potato
- Rajesh (Kanpur) - 250q Potato
- Suresh (Varanasi) - 200q Wheat
- Meena (Jaipur) - 50q Onion

**Buyers:**
- GreenFresh Traders (Delhi) - Trader, needs 100q Potato
- AgriProcess India (Noida) - Processor, needs 100q Potato (5 days later, higher price)
- Metro Wholesale (Gurgaon) - Wholesaler, needs 500q Potato (bulk)
- FreshMart Retail (Lucknow) - Retailer, needs 50q Onion

**The Demo Scenario:**
Hemant can either:
1. Sell 100q to GreenFresh now → ₹1,95,000 net
2. Wait and sell to AgriProcess → ₹2,15,000 net
3. Join with Priya + Rajesh and sell 500q to Metro → ₹2,18,000 net ✅ BEST

---

## 🎯 Core Innovation

The platform answers: **"Where should I sell to get the highest NET return?"**

Formula:
```
Net Realisation = Gross Sale Value 
                - Transport Cost 
                - Storage Cost 
                - Other Costs
```

A higher selling price doesn't always mean more profit!

---

## 📱 Navigation Flow

```
Landing Page (app.py)
    ↓
Login (01_Login.py)
    ↓
Farmer Dashboard (10_) ← → Buyer Dashboard (20_)
    ↓                           ↓
My Lots (11_)               My Requirements (21_)
    ↓                           ↓
Opportunities (14_)         Matches (23_)
    ↓                           ↓
Compare Options (15_) ← → Negotiations (16_/24_)
    ↓
Deal Confirmed
```

---

## 💡 Tips for SIH Presentation

1. **Start with the problem:** Farmers don't know where to sell for best profit
2. **Show the landing page:** Clean, professional, green theme
3. **Login as Hemant:** Relatable farmer persona
4. **Navigate to Compare Options page:** The hero screen
5. **Highlight the 3-option comparison:** Visual, clear, data-driven
6. **Show ML prediction:** AI/ML component with confidence levels
7. **Demonstrate group aggregation:** FPO/collective power
8. **Show the recommendation:** Explainable AI reasoning
9. **Emphasize "Net Realisation":** Not just price, but actual profit

---

## 🏆 Judging Criteria Coverage

✅ **Innovation:** ML-powered decision support + multi-option comparison
✅ **Feasibility:** Python-only, works offline, SQLite database
✅ **Impact:** Directly increases farmer income by ₹20k-30k per lot
✅ **Scalability:** Modular architecture, can connect to real APIs
✅ **Technology:** XGBoost, Streamlit, SQLAlchemy, proper software engineering
✅ **User Experience:** Clean UI, role-aware navigation, visual comparisons

---

## 📞 Support

For issues during setup:
1. Check that you're in the project directory
2. Verify Python version: `python --version` (should be 3.10+)
3. Delete `data/agroconnect.db` and run `python setup.py` again
4. Check that all dependencies installed: `pip list`

---

## 🎉 You're Ready!

Run the application:
```bash
streamlit run app.py
```

Navigate to **http://localhost:8501** and start exploring!

**Good luck with Smart India Hackathon! 🏆**
