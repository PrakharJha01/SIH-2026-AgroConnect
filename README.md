# AgroConnect - Smart Market Linkages Platform

**Smart India Hackathon 2024**  
**Problem Statement ID:** 26132  
**Problem Statement:** Strengthening Market Linkages and Price Discovery for Farmers

---

## 🌾 Overview

AgroConnect is a Python-based Streamlit web application that helps farmers discover the **best selling option** for their crops by comparing multiple opportunities and calculating **net realisation** after all costs.

### Key Features

- 📊 **Market Intelligence** - Real-time mandi prices and ML-powered price predictions
- 🎯 **Smart Matching** - Automatic farmer-buyer matching based on crop, location, and requirements
- 💡 **Net Realisation Calculator** - Compare actual returns after transport, storage, and other costs
- 🤝 **Group Aggregation** - Farmers can collaborate to fulfill bulk buyer requirements
- 💬 **Structured Negotiation** - Transparent price negotiation between farmers and buyers
- 🏆 **AI Recommendations** - Smart recommendations for maximum profit realization

---

## 🚀 Technology Stack

**Language:** Python Only

**Framework:** Streamlit

**Core Libraries:**
- `streamlit` - Web application framework
- `pandas`, `numpy` - Data processing
- `plotly` - Interactive visualizations
- `scikit-learn`, `xgboost` - Machine learning
- `sqlalchemy` - Database ORM
- `pydantic` - Data validation
- `folium`, `streamlit-folium` - Maps and geolocation

**Database:** SQLite (for prototype)

---

## 📁 Project Structure

```
AgroConnect/
├── app.py                          # Main application entry point
├── pages/                          # Streamlit pages
│   ├── 01_Login.py
│   ├── 02_Market_Prices.py
│   ├── 10_Farmer_Dashboard.py
│   ├── 20_Buyer_Dashboard.py
│   └── ... (more pages in later phases)
├── database/
│   ├── database.py                # Database connection
│   ├── models.py                  # SQLAlchemy models
│   └── seed.py                    # Demo data seeding
├── utils/
│   ├── constants.py               # Application constants
│   ├── session.py                 # Session management
│   └── formatting.py              # Formatting utilities
├── services/                      # Business logic services (Phase 4+)
├── ml/                           # ML models (Phase 9)
├── components/                    # Reusable UI components (Phase 2+)
├── data/                         # Seed and cache data
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Step 1: Clone or Download

```bash
cd AgroConnect
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file:

```bash
cp .env.example .env
```

The default values in `.env.example` are suitable for running the demo.

### Step 5: Initialize Database and Seed Data

```bash
python database/seed.py
```

This will:
- Create the SQLite database
- Create all tables
- Seed demo users, crop lots, buyer requirements, market prices, and storage facilities

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 👤 Demo Accounts

### Farmers

1. **Hemant Kumar** (9876543210)
   - Location: Malerkotla, Ludhiana, Punjab
   - Has: 100 quintals Potato

2. **Rajesh Patel** (9876543211)
   - Location: Karamsad, Anand, Gujarat
   - Has: 150 quintals Potato

3. **Suresh Singh** (9876543212)
   - Location: Dehlon, Ludhiana, Punjab
   - Has: 250 quintals Potato

### Buyers

1. **Agri Traders Ltd** (9876543220)
   - Type: Trader
   - Location: Ludhiana, Punjab
   - Needs: 100 quintals, Offer: ₹2000/quintal

2. **Fresh Foods Processing** (9876543221)
   - Type: Processor
   - Location: Amritsar, Punjab
   - Needs: 100 quintals, Offer: ₹2300/quintal (5 days later)

3. **Bulk Procurement Corp** (9876543222)
   - Type: Wholesaler
   - Location: Karnal, Haryana
   - Needs: 500 quintals, Offer: ₹2500/quintal (bulk)

---

## 🎯 Phase 1 Implementation Status

### ✅ Completed

- [x] Project structure setup
- [x] Database schema and models
- [x] SQLite database initialization
- [x] Demo data seeding
- [x] Landing page
- [x] Login page with role selection
- [x] Farmer dashboard
- [x] Buyer dashboard
- [x] Market prices page with charts
- [x] Session state management
- [x] Basic navigation
- [x] Custom styling and UI

### 🎯 Features Demonstrated

1. **Landing Page** - Overview of platform features
2. **Role-Based Login** - Select farmer or buyer role, choose demo account
3. **Market Prices** - View current mandi prices with historical trends
4. **Farmer Dashboard** - Overview with quick stats and actions
5. **Buyer Dashboard** - Overview for buyers
6. **Database** - Fully seeded with realistic demo data

---

## 📋 Upcoming Phases

### Phase 2 - Role Navigation
- Enhanced role-based navigation
- Improved session management

### Phase 3 - Crop Lots & Requirements
- Create crop lot (farmer)
- Create buyer requirement
- List and view details

### Phase 4 - Market Data Integration
- Data.gov.in API integration
- Historical price analysis

### Phase 5 - Matching Algorithm
- Farmer-buyer matching
- Match scoring and explanations

### Phase 6 - Negotiation System
- Offer and counter-offer
- Deal confirmation

### Phase 7 - Group Aggregation
- FPO/group formation
- Bulk opportunity matching

### Phase 8 - Cost Calculations
- Transport cost estimation
- Storage cost calculation
- Net realisation algorithm

### Phase 9 - ML Price Prediction
- Historical data preprocessing
- Model training (XGBoost/Random Forest)
- Future price prediction service

### Phase 10 - Recommendation Engine
- Sell Now vs Wait vs Group comparison
- Risk analysis
- Smart recommendations

### Phase 11 - UI Polish & Integration
- Final UI improvements
- Maps integration
- End-to-end testing

---

## 🧪 Testing

Run tests (when available in later phases):

```bash
pytest tests/
```

---

## 🔒 Security Notes

- This is a **prototype/demo application**
- Demo authentication is used (no real security)
- Do not use in production without proper authentication and security measures
- API keys should be stored in `.env` (not committed to git)

---

## 📝 Configuration

Key configuration options in `.env`:

- `DATABASE_URL` - SQLite database path
- `TRANSPORT_COST_PER_KM` - Transport cost estimation (₹/km)
- `BASIC_STORAGE_COST_PER_QUINTAL_PER_DAY` - Basic storage cost
- `COLD_STORAGE_COST_PER_QUINTAL_PER_DAY` - Cold storage cost
- `ML_MODEL_ENABLED` - Enable/disable ML predictions
- `DEMO_MODE` - Enable demo mode features

---

## 🤝 Contributing

This is a Smart India Hackathon prototype. For development:

1. Follow the phase-by-phase implementation plan
2. Keep code modular and testable
3. Use Python type hints
4. Write clear docstrings
5. Test business logic independently from UI

---

## 📄 License

This project is created for Smart India Hackathon 2024.

---

## 👥 Team

Smart India Hackathon 2024 Team

---

## 📞 Support

For issues or questions about this prototype, please refer to the implementation documentation.

---

## 🎉 Acknowledgments

- Smart India Hackathon 2024
- Ministry of Agriculture & Farmers Welfare
- Data.gov.in for market price data APIs
- Open-source community

---

**Status:** Phase 1 Complete ✅

**Next Step:** Wait for user to say "start next phase" to continue with Phase 2
