# pages/1_🏔️_About_himachal.py
import streamlit as st
import base64
import os

st.set_page_config(page_title="About Himachal", page_icon="🏔️", layout="wide")

# ── Load Rohtang Image and return base64 ──────────────────────────────────────
@st.cache_data
def get_bg_img():
    """Load the Rohtang image from images folder and return base64 data URL for page background."""
    # Yeh code pages/ folder se bahar nikal kar images/ folder se file pick karega
    img_path = os.path.join(os.path.dirname(__file__), "..", "images", "Rohtang-pass.jpg")
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        return f"data:image/jpeg;base64,{b64}"
    return ""

bg_image_url = get_bg_img()

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght=700;900&family=DM+Sans:wght=300;400;500&display=swap');

/* Top Header aur Deploy button hide karne ke liye */
header[data-testid="stHeader"], .stDeployButton, div[data-testid="stStatusWidget"] {{
    display: none !important;
}}

:root {{
    --snow:#F0F4FF; --ice:#C9D8F0; --pine:#1B4332;
    --sky:#2D6A9F; --gold:#E9A84C; --dusk:#0D1B2A;
    --mist:rgba(13, 27, 42, 0.8);
}}

/* Rohtang Pass wallpaper with 55% dark visibility layer */
.stApp {{
    background-image: linear-gradient(rgba(13, 27, 42, 0.55), rgba(13, 27, 42, 0.55)), url('{bg_image_url}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
}}

html, body, [class*="css"] {{ 
    font-family: 'DM Sans', sans-serif; 
    color: #F0F4FF; 
}}

h1, h2, h3 {{ 
    font-family: 'Playfair Display', serif; 
    color: #F0F4FF !important; 
    text-shadow: 0 2px 10px rgba(0,0,0,0.8);
}}

/* Sidebar styling keeping glassmorphism texture */
section[data-testid="stSidebar"] {{ 
    background: rgba(13, 27, 42, 0.4) !important;
    backdrop-filter: blur(10px) !important;
    border-right: 1px solid rgba(201,216,240,0.15) !important;
}}

/* Sidebar navigation targets */
div[data-testid="stSidebarNav"] {{ background-color: transparent !important; padding-top: 2rem; }}
div[data-testid="stSidebarNav"] ul {{ background-color: transparent !important; }}
div[data-testid="stSidebarNav"] ul li div a {{
    background-color: transparent !important; color: #F0F4FF !important; border-radius: 8px; margin: 4px 0; transition: all 0.3s ease;
}}
div[data-testid="stSidebarNav"] ul li div a:hover {{ background-color: rgba(233, 168, 76, 0.15) !important; color: #E9A84C !important; }}
div[data-testid="stSidebarNav"] ul li div[data-selected="true"] a {{ background-color: rgba(45, 106, 159, 0.25) !important; color: #E9A84C !important; }}

/* Metric widgets customization */
div[data-testid="metric-container"] {{ 
    background: var(--mist); 
    border: 1px solid rgba(201,216,240,0.3); 
    border-radius: 12px; 
    padding: 16px; 
    backdrop-filter: blur(8px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}}

/* Element cleanups */
hr {{ border-color: rgba(201,216,240,0.25); }}
div[data-testid="stAlert"] {{ border-radius: 10px; background-color: rgba(13,27,42,0.85); border: 1px solid rgba(201,216,240,0.15); }}
div.stExpander {{ background: rgba(13,27,42,0.45); border: 1px solid rgba(201,216,240,0.15); border-radius: 10px; backdrop-filter: blur(4px); margin-bottom: 8px; }}
</style>
""", unsafe_allow_html=True)

st.title("🏔️ About Himachal")
st.markdown("*Your complete destination guide for October 2026*")

st.markdown("---")

# ── Overview ──────────────────────────────────────────────────────────────────
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
### 🌄 Why Manali in October?
October is arguably the **best month** to visit Manali:
- ❄️ **Fresh snow** on Rohtang Pass (often accessible)
- 🌤️ **Clear skies** for panoramic Himalayan views
- 🍂 **Crisp autumn air** with temperatures 5–18°C
- 🚫 **Post-monsoon** — no landslide risks
- 📸 **Photogenic landscapes** — golden trees + snowy peaks
- 💸 **Off-peak pricing** — hotels & activities cheaper than summer
""")

with col2:
    st.markdown("""
<div style="background:rgba(13,27,42,0.5);border:1px solid rgba(201,216,240,0.2);
  border-radius:12px;padding:20px;text-align:center;backdrop-filter:blur(6px);box-shadow: 0 4px 15px rgba(0,0,0,0.25);">
  <div style="font-size:40px">🏔️</div>
  <div style="color:#E9A84C;font-weight:700;font-size:18px;">2,050 m</div>
  <div style="color:#C9D8F0;font-size:13px;">Manali Elevation</div>
  <hr style="border-color:rgba(201,216,240,0.15)">
  <div style="color:#E9A84C;font-weight:700;font-size:18px;">~570 km</div>
  <div style="color:#C9D8F0;font-size:13px;">From Delhi</div>
  <hr style="border-color:rgba(201,216,240,0.15)">
  <div style="color:#E9A84C;font-weight:700;font-size:18px;">Himachal</div>
  <div style="color:#C9D8F0;font-size:13px;">Pradesh, India</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── Weather ───────────────────────────────────────────────────────────────────
st.markdown("### 🌡️ October Weather in himachal")

w1, w2, w3, w4 = st.columns(4)
w1.metric("🌅 Day Temp", "12–18°C", "Pleasant & sunny")
w2.metric("🌙 Night Temp", "2–8°C", "Carry woolens!")
w3.metric("❄️ Rohtang", "-2 to 5°C", "Snow likely")
w4.metric("🌧️ Rainfall", "Low", "Post-monsoon clear")

st.info("💡 **Pro Tip:** Layers are key! Morning & evenings get very cold. Pack thermal inners, a heavy jacket, and gloves — especially for Rohtang.")

st.markdown("---")

# ── Key Destinations ──────────────────────────────────────────────────────────
st.markdown("### 📍 Key Destinations on Your Trip")

destinations = [
    {
        "name": "🛍️ Mall Road, Manali",
        "desc": "The heart of Manali — lined with shops, cafés, and restaurants. Great for evening strolls and local food.",
        "tip": "Try Café 1947 or Johnson's Café for amazing food.",
        "distance": "Town centre",
    },
    {
        "name": "🪂 Solang Valley",
        "desc": "Adventure hub with paragliding, zipline, ATV, and rope activities. Snow-covered in winter.",
        "tip": "Book activities in advance during October — slots fill up fast.",
        "distance": "14 km from Manali",
    },
    {
        "name": "🌊 Kullu (Rafting)",
        "desc": "The Beas River near Kullu offers Grade 3–4 rapids — perfect for a full adrenaline rafting experience.",
        "tip": "October water levels are ideal — not too high, not too low.",
        "distance": "40 km from Manali",
    },
    {
        "name": "💧 Jogini Waterfall",
        "desc": "A 2–3 km trek from Vashisht village leads to this stunning 30m waterfall. Rocky trail, very rewarding.",
        "tip": "Wear good trekking shoes. The trail is steep but manageable.",
        "distance": "3 km trek from Vashisht",
    },
    {
        "name": "❄️ Rohtang Pass",
        "desc": "At 3,978m, Rohtang offers breathtaking snow views. Requires permit (book online via HP tourism portal).",
        "tip": "⚠️ Book the Rohtang permit online at least 2 days before. Limited daily passes.",
        "distance": "51 km from Manali",
    },
    {
        "name": "🚇 Atal Tunnel",
        "desc": "World's longest highway tunnel (9.02 km) connecting Manali to Lahaul valley. Engineering marvel.",
        "tip": "Stop at Sissu on the other side — the valley views are jaw-dropping.",
        "distance": "25 km from Manali",
    },
]

for dest in destinations:
    with st.expander(f"{dest['name']} — {dest['distance']}"):
        st.markdown(dest["desc"])
        st.success(f"💡 **Tip:** {dest['tip']}")

st.markdown("---")

# ── Function to load image as base64 ─────────────────────────
@st.cache_data
def get_bg(img_name):
    img_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "images",
        img_name
    )

    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            return f"data:image/webp;base64,{base64.b64encode(f.read()).decode()}"

    return ""

# Different images for each card
clothing_bg = get_bg("clothing.webp.webp")
essentials_bg = get_bg("essentials.webp.png")
health_bg = get_bg("health.webp.webp")

inner_style = """
background:rgba(0,0,0,0.55);
padding:12px;
border-radius:8px;
font-size:13px;
line-height:1.9;
"""

col_a, col_b, col_c = st.columns(3)

# ── Clothing Card ─────────────────────────────────────────
with col_a:
    card_style = f"""
    background-image:url('{clothing_bg}');
    background-size:cover;
    background-position:center;
    padding:16px;
    border-radius:10px;
    border:1px solid rgba(201,216,240,0.15);
    color:white;
    """
    
    st.markdown(
        f'''
        <div style="{card_style}">
            <div style="{inner_style}">
                <strong style="font-size:15px;">🧥 Clothing</strong><br><br>
                ☐ Thermal inners (top + bottom)<br>
                ☐ Heavy winter jacket<br>
                ☐ Fleece / sweatshirts (2–3)<br>
                ☐ T-shirts (2–3)<br>
                ☐ Jeans / trek pants<br>
                ☐ Warm socks (3+ pairs)<br>
                ☐ Gloves & woolen cap<br>
                ☐ Scarf / neck warmer<br>
                ☐ Waterproof shoes / boots
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

# ── Essentials Card ───────────────────────────────────────
with col_b:
    card_style = f"""
    background-image:url('{essentials_bg}');
    background-size:cover;
    background-position:center;
    padding:16px;
    border-radius:10px;
    border:1px solid rgba(201,216,240,0.15);
    color:white;
    """
    
    st.markdown(
        f'''
        <div style="{card_style}">
            <div style="{inner_style}">
                <strong style="font-size:15px;">🎒 Essentials</strong><br><br>
                ☐ Aadhar / Govt ID (mandatory)<br>
                ☐ Rohtang permit (book online)<br>
                ☐ Cash (ATMs can be spotty)<br>
                ☐ Power bank<br>
                ☐ Universal adapter<br>
                ☐ Water bottle<br>
                ☐ Sunglasses (UV protection)<br>
                ☐ Sunscreen SPF 50+<br>
                ☐ Lip balm
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

# ── Health Card ───────────────────────────────────────────
with col_c:
    card_style = f"""
    background-image:url('{health_bg}');
    background-size:cover;
    background-position:center;
    padding:16px;
    border-radius:10px;
    border:1px solid rgba(201,216,240,0.15);
    color:white;
    """
    
    st.markdown(
        f'''
        <div style="{card_style}">
            <div style="{inner_style}">
                <strong style="font-size:15px;">💊 Health & Safety</strong><br><br>
                ☐ Diamox (altitude sickness)<br>
                ☐ Basic first-aid kit<br>
                ☐ Personal medicines<br>
                ☐ ORS packets<br>
                ☐ Motion sickness tablets<br>
                ☐ Pain reliever<br>
                ☐ Raincoat / poncho<br>
                ☐ Insect repellent<br>
                ☐ Hand sanitizer
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

st.markdown("---")



# ── Food Card Background Images ─────────────────────────────
food_bg1 = get_bg("food.webp")
food_bg2 = get_bg("cafe.avif")

food_col1, food_col2 = st.columns(2)

with food_col1:
    card_style1 = f"""
    background-image:url('{food_bg1}');
    background-size:cover;
    background-position:center;
    padding:16px;
    border-radius:10px;
    border:1px solid rgba(201,216,240,0.15);
    color:white;
    """

    st.markdown(
        f"""
        <div style="{card_style1}">
            <div style="background:rgba(0,0,0,0.55);padding:12px;border-radius:8px;">
                <strong>🥘 Local Dishes to Try</strong><br><br>
                • <strong>Siddu</strong> — Himachali steamed bread with ghee<br>
                • <strong>Dham</strong> — Traditional Himachali thali<br>
                • <strong>Trout fish</strong> — Fresh Himalayan river fish<br>
                • <strong>Chha Gosht</strong> — Marinated lamb curry<br>
                • <strong>Aktori</strong> — Buckwheat pancake<br>
                • <strong>Babru</strong> — Deep-fried kachori variation
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with food_col2:
    card_style2 = f"""
    background-image:url('{food_bg2}');
    background-size:cover;
    background-position:center;
    padding:16px;
    border-radius:10px;
    border:1px solid rgba(201,216,240,0.15);
    color:white;
    """

    st.markdown(
        f"""
        <div style="{card_style2}">
            <div style="background:rgba(0,0,0,0.55);padding:12px;border-radius:8px;">
                <strong>☕ Café Recommendations</strong><br><br>
                • <strong>Café 1947</strong> — Best coffee + Himachali food<br>
                • <strong>Johnson's Café</strong> — Cosy, trout specialties<br>
                • <strong>Drifter's Inn</strong> — Backpacker favourite<br>
                • <strong>Café Amigos</strong> — Budget friendly<br>
                • <strong>Lazy Dog Lounge</strong> — Great views<br>
                • <strong>Moondance Restaurant</strong> — Evening hangout
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("🏔️ About Manali · Manali Trip 2026")