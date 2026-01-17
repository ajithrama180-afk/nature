import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Anusha's Nature Bakery - Artisan Cakes & Cupcakes",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #FFF8F0;
    }
    .stApp {
        background: linear-gradient(135deg, #FFF8F0 0%, #FFE8D6 100%);
    }
    h1 {
        color: #8B4513;
        font-family: 'Georgia', serif;
        text-align: center;
        padding: 20px;
    }
    h2 {
        color: #A0522D;
        font-family: 'Georgia', serif;
    }
    h3 {
        color: #CD853F;
        font-family: 'Georgia', serif;
    }
    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px;
    }
    .price-tag {
        color: #8B4513;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>🌿 Anusha's Nature Bakery 🧁</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #A0522D;'>Handcrafted Cakes & Cupcakes Made with Love</h3>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400", use_container_width=True)
    st.markdown("### 🌿 About Us")
    st.write("Welcome to Nature Bakery! We create beautiful, delicious cakes and cupcakes using natural ingredients and artistic designs.")
    
    st.markdown("### 📍 Location")
    st.write("123 Baker Street, Sweet Town")
    
    st.markdown("### 📞 Contact")
    st.write("Phone: (555) 123-4567")
    st.write("Email: hello@naturebakery.com")
    
    st.markdown("### ⏰ Hours")
    st.write("Mon-Fri: 8am - 6pm")
    st.write("Sat-Sun: 9am - 5pm")

# Navigation
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "🎂 Cakes", "🧁 Cupcakes", "📝 Order"])

with tab1:
    st.markdown("## Welcome to Nature Bakery!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=800", use_container_width=True)
        st.markdown("### Our Philosophy")
        st.write("At Nature Bakery, we believe in using only the finest natural ingredients to create stunning cakes and cupcakes that taste as good as they look.")
    
    with col2:
        st.image("https://images.unsplash.com/photo-1558636508-e0db3814bd1d?w=800", use_container_width=True)
        st.markdown("### Why Choose Us?")
        st.write("✨ Fresh, natural ingredients")
        st.write("🎨 Custom designs available")
        st.write("👩‍🍳 Expert bakers with 15+ years experience")
        st.write("💚 Eco-friendly packaging")
    
    st.markdown("---")
    st.markdown("## Featured This Week")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1535141192574-5d4897c12636?w=600", use_container_width=True)
        st.markdown("**Chocolate Dream Cake**")
        st.write("Rich chocolate layers with ganache")
    
    with col2:
        st.image("https://images.unsplash.com/photo-1614707267537-b85aaf00c4b7?w=600", use_container_width=True)
        st.markdown("**Berry Bliss Cupcakes**")
        st.write("Fresh berries with cream cheese frosting")
    
    with col3:
        st.image("https://images.unsplash.com/photo-1588195538326-c5b1e5b80d9b?w=600", use_container_width=True)
        st.markdown("**Vanilla Rose Cake**")
        st.write("Elegant vanilla cake with rose decoration")

with tab2:
    st.markdown("## 🎂 Our Signature Cakes")
    st.write("Each cake is made to order with the finest ingredients and can be customized to your preferences.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800", use_container_width=True)
        st.markdown("### Floral Fantasy Cake")
        st.write("A stunning multi-tiered cake decorated with edible flowers and delicate buttercream work.")
        st.markdown("<p class='price-tag'>Starting at $85</p>", unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1557925923-cd4648e211a0?w=800", use_container_width=True)
        st.markdown("### Chocolate Indulgence")
        st.write("Decadent chocolate layers with rich ganache and chocolate shavings.")
        st.markdown("<p class='price-tag'>Starting at $75</p>", unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=800", use_container_width=True)
        st.markdown("### Lemon Lavender Delight")
        st.write("Light lemon cake with lavender-infused buttercream.")
        st.markdown("<p class='price-tag'>Starting at $70</p>", unsafe_allow_html=True)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=800", use_container_width=True)
        st.markdown("### Rainbow Layer Cake")
        st.write("Colorful layers of moist vanilla cake with cream cheese frosting.")
        st.markdown("<p class='price-tag'>Starting at $80</p>", unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1535141192574-5d4897c12636?w=800", use_container_width=True)
        st.markdown("### Red Velvet Romance")
        st.write("Classic red velvet with cream cheese frosting and elegant decoration.")
        st.markdown("<p class='price-tag'>Starting at $75</p>", unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1588195538326-c5b1e5b80d9b?w=800", use_container_width=True)
        st.markdown("### Strawberry Dream")
        st.write("Fresh strawberries with vanilla cake and whipped cream.")
        st.markdown("<p class='price-tag'>Starting at $78</p>", unsafe_allow_html=True)

with tab3:
    st.markdown("## 🧁 Delightful Cupcakes")
    st.write("Perfect for parties, gifts, or treating yourself! Minimum order: 6 cupcakes")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1614707267537-b85aaf00c4b7?w=600", use_container_width=True)
        st.markdown("### Berry Bliss")
        st.write("Mixed berries with cream cheese frosting")
        st.markdown("<p class='price-tag'>$4.50 each</p>", unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1576618148400-f54bed99fcfd?w=600", use_container_width=True)
        st.markdown("### Vanilla Dream")
        st.write("Classic vanilla with buttercream swirl")
        st.markdown("<p class='price-tag'>$4.00 each</p>", unsafe_allow_html=True)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1587668178277-295251f900ce?w=600", use_container_width=True)
        st.markdown("### Chocolate Heaven")
        st.write("Rich chocolate with chocolate ganache")
        st.markdown("<p class='price-tag'>$4.50 each</p>", unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1603532648955-039310d9ed75?w=600", use_container_width=True)
        st.markdown("### Lemon Zest")
        st.write("Tangy lemon with lemon buttercream")
        st.markdown("<p class='price-tag'>$4.25 each</p>", unsafe_allow_html=True)
    
    with col3:
        st.image("https://images.unsplash.com/photo-1426869981800-95ebf51ce900?w=600", use_container_width=True)
        st.markdown("### Caramel Delight")
        st.write("Salted caramel with caramel drizzle")
        st.markdown("<p class='price-tag'>$4.75 each</p>", unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1599785209796-786432b228bc?w=600", use_container_width=True)
        st.markdown("### Red Velvet")
        st.write("Classic red velvet with cream cheese")
        st.markdown("<p class='price-tag'>$4.50 each</p>", unsafe_allow_html=True)

with tab4:
    st.markdown("## 📝 Place Your Order")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("order_form"):
            st.markdown("### Order Details")
            
            name = st.text_input("Your Name *")
            email = st.text_input("Email Address *")
            phone = st.text_input("Phone Number *")
            
            product_type = st.selectbox(
                "Product Type *",
                ["Select...", "Custom Cake", "Signature Cake", "Cupcakes"]
            )
            
            if product_type == "Custom Cake":
                flavor = st.selectbox(
                    "Cake Flavor",
                    ["Vanilla", "Chocolate", "Red Velvet", "Lemon", "Strawberry", "Carrot"]
                )
                size = st.selectbox(
                    "Size",
                    ["6 inch (serves 8-10)", "8 inch (serves 12-16)", "10 inch (serves 20-25)", "Multi-tier"]
                )
            elif product_type == "Cupcakes":
                quantity = st.number_input("Quantity (minimum 6)", min_value=6, max_value=100, value=12)
                flavors = st.multiselect(
                    "Select Flavors",
                    ["Vanilla Dream", "Chocolate Heaven", "Berry Bliss", "Lemon Zest", "Caramel Delight", "Red Velvet"]
                )
            
            pickup_date = st.date_input("Pickup Date")
            pickup_time = st.time_input("Pickup Time")
            
            special_requests = st.text_area("Special Requests or Custom Design Details")
            
            submitted = st.form_submit_button("Submit Order Request")
            
            if submitted:
                if name and email and phone and product_type != "Select...":
                    st.success("✅ Thank you! Your order request has been received. We'll contact you within 24 hours to confirm details and pricing.")
                    st.balloons()
                else:
                    st.error("Please fill in all required fields marked with *")
    
    with col2:
        st.image("https://images.unsplash.com/photo-1486427944299-d1955d23e34d?w=400", use_container_width=True)
        st.markdown("### 📋 Order Information")
        st.write("**Lead Time:** Please order at least 3 days in advance for cakes, 2 days for cupcakes.")
        st.write("**Payment:** We accept cash, credit cards, and digital payments.")
        st.write("**Delivery:** Available for orders over $100 within 10 miles.")
        st.write("**Cancellation:** Free cancellation up to 48 hours before pickup.")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #8B4513; padding: 20px;'>
        <p>🌿 Nature Bakery - Where Every Bite is a Delight 🌿</p>
        <p>Follow us on social media: @NatureBakery</p>
        <p>© 2024 Nature Bakery. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)
