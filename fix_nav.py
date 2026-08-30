import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Just replace from '# Shared pages' to the end of the file.
pattern = r'# Shared pages \(visible to everyone\).*'
replacement = """# Shared pages (visible to everyone)
shared_pages = [
    st.Page("pages/00_Home.py", title="Home", icon="🏠"),
    st.Page("pages/01_Login.py", title="Login", icon="🔑"),
    st.Page("pages/02_Market_Prices.py", title="Market Prices", icon="📊"),
]

# Farmer pages
farmer_pages = [
    st.Page("pages/10_Farmer_Dashboard.py", title="Dashboard", icon="🏠"),
    st.Page("pages/11_Farmer_Lots.py", title="My Crop Lots", icon="🌾"),
    st.Page("pages/12_Create_Lot.py", title="Create Lot", icon="➕"),
    st.Page("pages/14_Opportunities.py", title="Opportunities", icon="🎯"),
    st.Page("pages/15_Opportunity_Comparison.py", title="Compare Options", icon="💰"),
    st.Page("pages/16_Negotiations.py", title="Negotiations", icon="🤝"),
    st.Page("pages/17_Farmer_Groups.py", title="Groups & FPO", icon="👥"),
]

# Buyer pages
buyer_pages = [
    st.Page("pages/20_Buyer_Dashboard.py", title="Dashboard", icon="🏠"),
    st.Page("pages/21_Buyer_Requirements.py", title="My Requirements", icon="📋"),
    st.Page("pages/22_Create_Requirement.py", title="Create Requirement", icon="➕"),
    st.Page("pages/23_Buyer_Matches.py", title="Matches", icon="🎯"),
    st.Page("pages/24_Buyer_Negotiations.py", title="Negotiations", icon="🤝"),
]

# Build navigation based on login state
if is_logged_in():
    user_role = get_user_role()

    if user_role == ROLE_FARMER:
        nav = st.navigation({
            "🌾 AgroConnect": shared_pages,
            "👨‍🌾 Farmer": farmer_pages,
        })
    elif user_role == ROLE_BUYER:
        nav = st.navigation({
            "🌾 AgroConnect": shared_pages,
            "🏢 Buyer": buyer_pages,
        })
    else:
        nav = st.navigation({
            "🌾 AgroConnect": shared_pages,
        })
else:
    nav = st.navigation({
        "🌾 AgroConnect": shared_pages,
    })

nav.run()
"""

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated app.py")
