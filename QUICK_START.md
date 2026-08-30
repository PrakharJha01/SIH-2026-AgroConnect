# AgroConnect - Quick Start Guide

## 🚀 Running the Application

### 1. Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. Start the Application
```bash
streamlit run app.py
```

**Application URL:** http://localhost:8502

---

## 👥 Demo Accounts

### Farmers
| Name | Phone | Location | Crop Available |
|------|-------|----------|----------------|
| Hemant Kumar | 9876543210 | Ludhiana, Punjab | 100q Potato |
| Rajesh Patel | 9876543211 | Anand, Gujarat | 150q Potato |
| Suresh Singh | 9876543212 | Ludhiana, Punjab | 250q Potato |

### Buyers
| Name | Phone | Type | Requirements |
|------|-------|------|--------------|
| Agri Traders Ltd | 9876543220 | Trader | 100q @ ₹2000/q (today) |
| Fresh Foods Processing | 9876543221 | Processor | 100q @ ₹2300/q (5 days) |
| Bulk Procurement Corp | 9876543222 | Wholesaler | 500q @ ₹2500/q (7 days) |

---

## 🔧 Useful Commands

### Reset Database
```bash
python reset_database.py
```

### Train ML Model
```bash
python -m ml.train_model
```

### Test ML Prediction
```bash
python -m ml.predict_price
```

### Evaluate Model
```bash
python -m ml.evaluate_model
```

---

## 📱 Navigation

### Public Pages
- **Home** - Landing page with features
- **Login** - Role-based authentication
- **Market Prices** - Current mandi prices

### Farmer Pages
- **Dashboard** - Overview and quick stats
- **My Crop Lots** - View all crop lots
- **Create Crop Lot** - Add new crop for sale
- **Opportunities** - View matching buyers
- **Compare Options** ⭐ - Sell Now vs Wait vs Group
- **Negotiations** - Manage offers
- **Groups/FPO** - Group aggregation

### Buyer Pages
- **Dashboard** - Overview
- **Requirements** - View posted requirements
- **Create Requirement** - Post new requirement
- **Matching Farmers** - Find suitable farmers
- **Negotiations** - Manage negotiations

---

## 🎯 Key Demo Flow

1. **Login as Farmer** (Hemant Kumar)
2. View existing Potato lot OR create new one
3. **View Opportunities** - System finds buyers
4. **Compare Options** ⭐ - See:
   - Sell Now to nearby trader
   - Wait for processor (ML predicted price)
   - Join group for bulk buyer
5. **System Recommends** best option with net realisation
6. **Start Negotiation** with buyer
7. **Confirm Deal**

---

## 🤖 ML Price Prediction

**Status:** ✅ Working

The system uses XGBoost to predict potato prices 5 days ahead:
- Trained on 31 days of historical data
- 38 engineered features
- Confidence levels: High/Medium/Low
- Trend analysis included

**Prediction Example:**
```
Current: ₹2200/quintal
Predicted (5 days): ₹2350/quintal
Confidence: Medium
Trend: ↗️ Increasing
```

---

## 📂 Project Structure

```
AgroConnect/
├── app.py                    # Main entry point
├── pages/                    # Streamlit pages
├── database/                 # Database models & seed
├── ml/                       # ML pipeline ✅
├── services/                 # Business logic
├── algorithms/               # Core algorithms
├── utils/                    # Utilities
├── data/seed/               # Seed data files
└── models/price_prediction/ # Trained ML models
```

---

## ⚠️ Troubleshooting

### Database Issues
```bash
# Reset database completely
python reset_database.py
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Port Already in Use
```bash
# Use different port
streamlit run app.py --server.port 8503
```

### Streamlit Caching Issues
```bash
# Clear cache
streamlit cache clear
```

---

## 📊 Current Implementation Status

| Feature | Status |
|---------|--------|
| Landing Page | ✅ Complete |
| Login System | ✅ Complete |
| Database | ✅ Complete |
| ML Price Prediction | ✅ Complete |
| Market Prices Display | ⚠️ Partial |
| Farmer Dashboard | ⚠️ Partial |
| Create Crop Lot | ⚠️ Needs Services |
| Buyer Matching | ❌ Needs Implementation |
| Negotiation System | ❌ Needs Implementation |
| Opportunity Comparison | ❌ Needs Implementation |
| Recommendation Engine | ❌ Needs Implementation |

---

## 🎬 What Works Now

✅ View landing page  
✅ Login as farmer/buyer  
✅ View basic dashboards  
✅ ML price prediction (backend)  
✅ Database with demo data

## 🚧 What Needs Work

❌ Create crop lot functionality  
❌ Buyer-farmer matching algorithm  
❌ Cost calculation services  
❌ Opportunity comparison UI  
❌ Negotiation workflow  
❌ Deal confirmation

---

## 📝 Notes

- This is a **prototype for SIH 2024**
- Demo authentication only
- ML model needs more data for production
- Some pages have structure but need service implementation

---

**For detailed status:** See `CURRENT_STATUS.md`  
**For ML details:** See `ML_IMPLEMENTATION.md`  
**For full setup:** See `README.md`
