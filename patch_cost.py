with open('pages/23_Buyer_Matches.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re

replacement = '''        m_col1, m_col2 = st.columns(2)
        m_col1.metric("Distance", f"{dist_km:.2f} km")
        m_col2.metric("Estimated Drive Time", f"{time_min:.0f} mins")
        st.caption(f"Source: {distance_source}")

        if route_error:
            st.warning(
                f"{route_error} Showing a straight-line estimate and the two endpoints on the map."
            )

        st.markdown("#### 💰 Cost Estimator")
        
        truck_options = {
            "32 ft MXL (₹71.69/km)": 71.69,
            "32 ft SXL (₹54.71/km)": 54.71,
            "24 ft (₹39.62/km)": 39.62,
            "22 ft (₹41.50/km)": 41.50,
            "20 ft (₹36.79/km)": 36.79,
            "19 ft open container (₹54.71/km)": 54.71
        }
        selected_truck = st.selectbox(
            "Select Truck Type for logistics transport:", 
            list(truck_options.keys()), 
            key=f"truck_{lot_id}"
        )
        truck_rate = truck_options[selected_truck]
        
        base_transport_cost = dist_km * truck_rate
        
        qty = float(match.get("quantity", 0))
        unit = str(match.get("unit", "quintal")).lower().strip()
        if unit == "quintal" or unit == "q":
            qty_mt = qty / 10.0
        elif unit == "kg":
            qty_mt = qty / 1000.0
        elif unit == "tonne" or unit == "mt":
            qty_mt = qty
        else:
            qty_mt = qty / 10.0
            
        base_storage_cost = qty_mt * 6000.0
        
        t_low = max(0, base_transport_cost - 10)
        t_high = base_transport_cost + 10
        s_low = max(0, base_storage_cost - 10)
        s_high = base_storage_cost + 10
        
        tc1, tc2 = st.columns(2)
        tc1.metric("Est. Transport Cost", f"₹{t_low:,.2f} - ₹{t_high:,.2f}")
        tc2.metric("Est. Storage Cost", f"₹{s_low:,.2f} - ₹{s_high:,.2f}")
        
        st.info("💡 Note: Storage calculated at ₹6,000/MT setup. Transport based on geo-distance × selective truck rate. A standard ₹10 variance margin is applied.")
'''
# Using regex to replace the old metrics block
text = re.sub(r'        m_col1, m_col2 = st\.columns\(2\)\n.*?Showing a straight-line estimate and the two endpoints on the map\."\n            \)', replacement, text, flags=re.DOTALL)

with open('pages/23_Buyer_Matches.py', 'w', encoding='utf-8') as f:
    f.write(text)
