# app.py — Main Entry Point / Home Page
import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(
    page_title="OUR TRIP - Manali Trip 2026 🏔️",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ── Helper: Local image → base64 ─────────────────────────────────────────────
def img_to_base64(path):
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return ""


# ── Background image load (app_bg — sabhi formats support) ───────────────────
@st.cache_data
def get_bg_img():
    for fname, mime in [
        ("app_bg.webp", "image/webp"),
        ("app_bg.jpg",  "image/jpeg"),
        ("app_bg.jpeg", "image/jpeg"),
        ("app_bg.png",  "image/png"),
    ]:
        img_path = os.path.join(os.path.dirname(__file__), "images", fname)
        if os.path.exists(img_path):
            with open(img_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            return f"data:{mime};base64,{b64}"
    return ""

bg_image_url = get_bg_img()


# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap');

header[data-testid="stHeader"],
.stDeployButton,
div[data-testid="stStatusWidget"] {{
    display: none !important;
}}

.stMainBlockContainer,
div[data-testid="stMainBlockContainer"] {{
    padding-top: 0rem !important;
    margin-top: 0rem !important;
}}
.stMain,
div[data-testid="stMain"] {{
    padding-top: 0rem !important;
    margin-top: 0rem !important;
}}
section.main > div {{
    padding-top: 0rem !important;
}}

:root {{
    --snow: #F0F4FF;
    --ice: #C9D8F0;
    --pine: #1B4332;
    --sky: #2D6A9F;
    --gold: #E9A84C;
    --dusk: #0D1B2A;
}}

.stApp {{
    background-image: url('{bg_image_url}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
}}

html, body, [class*="css"] {{
    font-family: 'DM Sans', sans-serif;
    color: var(--snow);
}}

section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, rgba(13,27,42,0.85) 0%, rgba(27,58,92,0.85) 100%);
    border-right: 1px solid rgba(201,216,240,0.1);
}}

h1, h2, h3 {{
    font-family: 'Playfair Display', serif;
    color: var(--snow) !important;
    text-shadow: 0 2px 10px rgba(0,0,0,0.8);
}}

div[data-testid="metric-container"] {{
    background: rgba(13,27,42,0.45);
    border: 1px solid rgba(201,216,240,0.25);
    border-radius: 12px;
    padding: 16px;
    backdrop-filter: blur(6px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}}

div.stButton > button {{
    background: linear-gradient(135deg, var(--sky), var(--pine));
    color: white;
    border: none;
    border-radius: 8px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    padding: 10px 24px;
    transition: all 0.3s ease;
}}
div.stButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(45,106,159,0.4);
}}

hr {{ border-color: rgba(201,216,240,0.25); }}
div[data-testid="stAlert"] {{ border-radius: 10px; }}

.nav-button-link {{
    text-decoration: none !important;
    display: block;
    margin-bottom: 12px;
}}
.nav-glass-button {{
    background: rgba(13,27,42,0.30);
    border: 1px solid rgba(201,216,240,0.25);
    border-radius: 12px;
    padding: 16px 20px;
    backdrop-filter: blur(4px);
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    cursor: pointer;
    text-align: left;
}}
.nav-glass-button:hover {{
    background: rgba(233,168,76,0.18);
    border-color: rgba(233,168,76,0.5);
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(233,168,76,0.2);
}}
</style>
""", unsafe_allow_html=True)


# ── Top Brand Bar ─────────────────────────────────────────────────────────────
_logo_b64 = ""
_logo_mime = "image/png"
for _fname, _mime in [("logo.png","image/png"), ("logo.jpg","image/jpeg"), ("logo.jpeg","image/jpeg"), ("logo.webp","image/webp")]:
    _logo_b64 = img_to_base64(f"images/{_fname}")
    if _logo_b64:
        _logo_mime = _mime
        break

_logo_tag = (
    f'<img src="data:{_logo_mime};base64,{_logo_b64}" style="width:50px;height:50px;border-radius:50%;object-fit:cover;border:2px solid #E9A84C;">'
    if _logo_b64 else '<span style="font-size:36px;">🏔️</span>'
)

st.markdown(f"""
<div style="
background: rgba(13,27,42,0.35);
border: 1px solid rgba(201,216,240,0.25);
border-radius: 18px;
padding: 15px 30px;
margin-top: 0px;
margin-bottom: 15px;
display: flex;
align-items: center;
justify-content: center;
gap: 15px;
backdrop-filter: blur(8px);
box-shadow: 0 4px 20px rgba(0,0,0,0.2);
">
{_logo_tag}
<h2 style="color:#F0F4FF;margin:0;text-shadow:0 2px 8px rgba(0,0,0,0.7);">OUR TRIP</h2>
</div>
""", unsafe_allow_html=True)


# ── Hero Banner ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="
background: rgba(13,27,42,0.40);
border: 1px solid rgba(201,216,240,0.2);
border-radius: 20px;
padding: 23px 30px;
margin-bottom: 30px;
margin-top: 0px;
position: relative;
overflow: hidden;
backdrop-filter: blur(10px);
box-shadow: 0 8px 25px rgba(0,0,0,0.25);
">
  <div style="position:absolute;top:-40px;right:-40px;width:200px;height:200px;
    background:radial-gradient(circle,rgba(233,168,76,0.12),transparent 70%);border-radius:50%;"></div>
  <div style="position:absolute;bottom:-60px;left:-30px;width:250px;height:250px;
    background:radial-gradient(circle,rgba(45,106,159,0.15),transparent 70%);border-radius:50%;"></div>

  <p style="color:#E9A84C;letter-spacing:4px;font-size:12px;text-transform:uppercase;margin-bottom:8px;text-shadow:0 1px 4px rgba(0,0,0,0.6);">
    ✈️ Ranchi → Manali → Ranchi
  </p>
  <h1 style="font-family:'Playfair Display',serif;font-size:clamp(32px,5vw,60px);
    font-weight:900;color:#F0F4FF;line-height:1.1;margin-bottom:16px;text-shadow:0 2px 8px rgba(0,0,0,0.7);">
    Manali Trip 2026 🏔️
  </h1>
  <p style="color:#C9D8F0;font-size:18px;font-weight:300;max-width:600px;margin-bottom:24px;text-shadow:0 1px 4px rgba(0,0,0,0.5);">
    28 September 2026 → 5 October 2026 &nbsp;•&nbsp; 8 Days &nbsp;•&nbsp; Paragliding · Rafting · Snow · Rohtang
  </p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;">
    <span style="background:rgba(233,168,76,0.18);border:1px solid rgba(233,168,76,0.45);
      color:#E9A84C;padding:6px 16px;border-radius:20px;font-size:13px;font-weight:500;">
      🗓 8 Days · 7 Nights
    </span>
    <span style="background:rgba(45,106,159,0.18);border:1px solid rgba(45,106,159,0.5);
      color:#C9D8F0;padding:6px 16px;border-radius:20px;font-size:13px;font-weight:500;">
      💰 ₹22,000–₹26,000 / head
    </span>
    <span style="background:rgba(27,67,50,0.35);border:1px solid rgba(27,67,50,0.7);
      color:#6EE7B7;padding:6px 16px;border-radius:20px;font-size:13px;font-weight:500;">
      🌡 October · Clear Views
    </span>
  </div>
</div>
""", unsafe_allow_html=True)


# ── Trip Organizers ───────────────────────────────────────────────────────────

img1 = img_to_base64("images/profile anima.jpeg")
img2 = img_to_base64("images/profile kishan.jpeg")

def make_img_tag(b64):
    if b64:
        return f'<img src="data:image/jpeg;base64,{b64}" style="width:150px;height:150px;border-radius:50%;object-fit:cover;border:4px solid #E9A84C;display:block;margin:0 auto;">'
    return '<div style="width:150px;height:150px;border-radius:50%;background:rgba(27,58,92,0.5);border:4px solid #E9A84C;margin:0 auto;display:flex;align-items:center;justify-content:center;font-size:55px;">👤</div>'

# --- Heading ---
st.markdown("""
<div style="
  background: rgba(13,27,42,0.38);
  border: 1px solid rgba(201,216,240,0.2);
  border-radius: 16px;
  padding: 18px 20px;
  text-align: center;
  backdrop-filter: blur(10px);
  margin-bottom: 12px;
">
  <h2 style="color:#F0F4FF; margin:0; font-family:Georgia,serif; font-size:22px; text-shadow:0 2px 6px rgba(0,0,0,0.6);">
    👥 Trip Organizers
  </h2>
</div>
""", unsafe_allow_html=True)

# --- Anima Tirkey ---
st.markdown(f"""
<div style="
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 20px;
  padding: 28px 20px;
  text-align: center;
  color: #C9D8F0;
  backdrop-filter: blur(6px);
  margin-bottom: 12px;
">
  {make_img_tag(img1)}
  <h3 style="color:#F0F4FF; margin:14px 0 10px; font-size:18px; text-shadow:0 1px 4px rgba(0,0,0,0.5);">Anima Tirkey</h3>
  <p style="line-height:2.2; font-size:14px; margin:0;">
    📞 Call: 7485 841562<br>
    💬 WhatsApp: 7485 841562<br>
    📧 animatirkey306@gmail.com
  </p>
</div>
""", unsafe_allow_html=True)

# --- Kishan Kumar ---
st.markdown(f"""
<div style="
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 20px;
  padding: 28px 20px;
  text-align: center;
  color: #C9D8F0;
  backdrop-filter: blur(6px);
  margin-bottom: 20px;
">
  {make_img_tag(img2)}
  <h3 style="color:#F0F4FF; margin:14px 0 10px; font-size:18px; text-shadow:0 1px 4px rgba(0,0,0,0.5);">Kishan Kumar</h3>
  <p style="line-height:2.2; font-size:14px; margin:0;">
    📞 Call: 969 324 0618<br>
    💬 WhatsApp: 7050 311718<br>
    📧 KumarKrishna70503@gmail.com
  </p>
</div>
""", unsafe_allow_html=True)

# ── Quick Stats ───────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
c1.metric("🚆 Train Days",   "2",  "Rajdhani Express")
c2.metric("🚌 Bus Nights",   "2",  "Volvo Sleeper")
c3.metric("🏔️ Manali Days", "6",  "Full experience")
c4.metric("🎯 Activities",   "4+", "Adventure packed")

st.markdown("---")


# ── Route Overview ────────────────────────────────────────────────────────────
st.markdown("### 🗺️ Route & Highlights")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div style="background:rgba(13,27,42,0.35);padding:20px;border-radius:12px;
  border:1px solid rgba(201,216,240,0.18);backdrop-filter:blur(8px);box-shadow:0 4px 15px rgba(0,0,0,0.15);">
  <strong style="color:#F0F4FF;font-size:16px;">📍 Full Route</strong>
  <pre style="background:transparent;color:#C9D8F0;border:none;padding:10px 0 0 0;
    font-family:monospace;font-size:14px;line-height:1.4;">
Ranchi ──🚆──► Delhi ──🚌──► Manali
  ↑                               ↓
Ranchi ◄──🚆── Delhi ◄──🚌── Manali</pre>
  <span style="display:inline-block;margin-top:10px;">🏨 <strong>Base:</strong> Mall Road, Manali</span>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div style="background:rgba(13,27,42,0.35);padding:20px;border-radius:12px;
  border:1px solid rgba(201,216,240,0.18);backdrop-filter:blur(8px);box-shadow:0 4px 15px rgba(0,0,0,0.15);">
  <strong style="color:#F0F4FF;font-size:16px;">🔥 Adventure Days</strong><br><br>
  🪂 <strong>Day 4</strong> — Solang: Paragliding + Zipline + ATV + Zorbing + Rope<br><br>
  🌊 <strong>Day 5</strong> — Kullu: River Rafting + Jogini Waterfall Trek<br><br>
  ❄️ <strong>Day 6</strong> — Rohtang Pass + Atal Tunnel + Sissu
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ── Navigation Buttons ────────────────────────────────────────────────────────
st.markdown("### 📖 Explore App Pages")

pages_info = [
    ("⚠️ Important Notice",  "Registration rules, eligibility & guidelines", "Important_Notice"),
    ("📝 Registration Form",  "Register yourself for the trip",               "Registration_Form"),
    ("🏔️ About Manali",       "Destination guide, weather & packing tips",    "About_Manali"),
    ("🧗 Activities List",     "All activities & adventure options",          "Activities_List"),
    ("📆 Time Table",          "Full trip schedule at a glance",              "Time_Table"),
    ("🗓️ Day Plan",           "Detailed per-day breakdown",                  "Day_Plan"),
    ("⏰ Time Plan",           "Hour-by-hour itinerary",                      "Time_Plan"),
    ("👥 Member List",         "View registered trip members",                "Member_List"),
]

cols = st.columns(2)
for i, (name, desc, url_path) in enumerate(pages_info):
    with cols[i % 2]:
        st.markdown(f"""
<a href="/{url_path}" target="_self" class="nav-button-link">
  <div class="nav-glass-button"
     style="
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(255,255,255,0.12);
        backdrop-filter: blur(12px);
        border-radius: 12px;
        padding: 12px;
     ">
    <strong style="color:#E9A84C;font-size:16px;text-shadow:0 1px 4px rgba(0,0,0,0.8);">
        {name}
    </strong><br>
    <span style="color:#FFFFFF;font-size:13px;font-weight:400;text-shadow:0 1px 3px rgba(0,0,0,0.8);opacity:0.9;">
        {desc}
    </span>
</div>
</a>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("🏔️ Manali Trip 2026 · Built with Streamlit + MongoDB · October Adventure")