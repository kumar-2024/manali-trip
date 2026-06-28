# app.py — Main Entry Point / Home Page
import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(
    page_title="OUR TRIP - himachal Trip 2026 🏔️",
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
    background-color: var(--dusk);
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
_hero_b64 = img_to_base64("images/poster.png")
_hero_style = (
    f"background-image: url('data:image/png;base64,{_hero_b64}'); background-size: 100% 100%; background-repeat: no-repeat;"
    if _hero_b64
    else "background: rgba(0,0,0,);"
)

st.markdown(f"""
<div style="
{_hero_style}
border-radius: 20px;
padding: 40px 36px;
margin-bottom: 30px;
margin-top: 0px;
position: relative;
overflow: hidden;
box-shadow: 0 8px 25px rgba(0,0,0,0.0);
min-height: 400px;
display: flex;
flex-direction: column;
justify-content: flex-end;
">
  <p style="color: #FFFFFF; text-shadow: 2px 2px 5px rgba(0,0,0,0.8); letter-spacing:4px; font-size:16px; text-transform:uppercase; margin-bottom:50px; font-weight:700;">
  ✈️ Ranchi → himachal  → Ranchi
</p>

<div style="display:flex;gap:12px;flex-wrap:wrap;">
      <span style="background:rgba(23,16,76,1);border:1px solid rgba(233,168,76,0.55);
        color:#E9A84C;padding:6px 16px;border-radius:20px;font-size:13px;font-weight:500;">
        🗓 10 days
      </span>
      <span style="background:rgba(45,106,159,1);border:1px solid rgba(45,106,159,0.6);
        color:#C9D8F0;padding:6px 16px;border-radius:20px;font-size:13px;font-weight:500;">
        💰 ₹22,000–₹26,000 / head
      </span>
      <span style="background:rgba(27,67,50,1);border:1px solid rgba(27,67,50,0.8);
        color:#6EE7B7;padding:6px 16px;border-radius:20px;font-size:13px;font-weight:500;">
        🌡 October · Clear Views
      </span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── Route Overview ────────────────────────────────────────────────────────────
st.markdown("### 🗺️ Himachal, Route & Highlights")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div style="background:rgba(13,27,42,0.35);padding:20px;border-radius:12px;
  border:1px solid rgba(201,216,240,0.18);backdrop-filter:blur(8px);box-shadow:0 4px 15px rgba(0,0,0,0.15);">
  <strong style="color:#F0F4FF;font-size:16px;">📍 Full Route</strong><br><br>
  <pre style="background:transparent;color:#C9D8F0;border:none;padding:10px 0 0 0;
    font-family:monospace;font-size:14px;line-height:1.4;">
<pre>
Ranchi ─🚆→ Chandigarh ─🚌→ Shimla ─🚌→ Kasol ─🚌→ Manali<br><br>
 ─🚌→ Chandigarh ─🚆→ Ranchi<br><br>
</pre>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div style="background:rgba(13,27,42,0.35);padding:20px;border-radius:12px;
  border:1px solid rgba(201,216,240,0.18);backdrop-filter:blur(8px);box-shadow:0 4px 15px rgba(0,0,0,0.15);">
<strong style="color:#F0F4FF;font-size:16px;">📍 Location</strong><br><br>
<strong>📍shimla</strong> — 🍁 Pleasant weather<br><br>
<strong>📍kasol</strong> — 🥾 Trekking + 🏕️ Camping<br><br>
<strong>📍manali</strong> — 🎯 Activities<br><br>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ── Navigation Buttons ────────────────────────────────────────────────────────
st.markdown("### 📖 Explore App Pages")

pages_info = [
    ("⚠️ Important Notice",  "Registration rules, eligibility & guidelines", "Important_Notice"),
    ("📝 Registration Form",  "Register yourself for the trip",               "Registration_Form"),
    ("🏔️ About himachal ",       "Destination guide, weather & packing tips",    "About_himachal"),
    ("📸 Posts",              "Photos & videos from the trip",               "Posts"),
    ("🧗 Activities List",     "All activities & adventure options",          "Activities_List"),
    ("📆 Time Table",          "Full trip schedule at a glance",              "Time_Table"),
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


# ── Trip Organizer ────────────────────────────────────────────────────────────
img2 = img_to_base64("images/profile kishan.jpeg")

def make_img_tag(b64):
    if b64:
        return f'<img src="data:image/jpeg;base64,{b64}" style="width:150px;height:150px;border-radius:50%;object-fit:cover;border:4px solid #E9A84C;display:block;margin:0 auto;">'
    return '<div style="width:150px;height:150px;border-radius:50%;background:rgba(27,58,92,0.5);border:4px solid #E9A84C;margin:0 auto;display:flex;align-items:center;justify-content:center;font-size:55px;">👤</div>'

# --- Heading ---
st.markdown("""
<div style="
  background: transparent;
  border: 1px solid rgba(201,216,240,0.2);
  border-radius: 16px;
  padding: 18px 20px;
  text-align: center;
  backdrop-filter: blur(0px);
  margin-bottom: 12px;
">
  <h2 style="color:#F0F4FF; margin:0; font-family:Georgia,serif; font-size:22px; text-shadow:0 2px 6px rgba(0,0,0,0.6);">
    👤 Trip Organizer
  </h2>
</div>
""", unsafe_allow_html=True)

# --- Single centered profile ---
col_l, col_mid, col_r = st.columns([1, 2, 1])

with col_mid:
    st.markdown(f"""
<div style="
  background: rgba(0, 0, 0, 0.6);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 20px;
  padding: 28px 20px;
  text-align: center;
  color: #C9D8F0;
  backdrop-filter: blur(6px);
">
  {make_img_tag(img2)}
  <h3 style="color:#F0F4FF; margin:14px 0 10px; font-size:18px; text-shadow:0 1px 4px rgba(0,0,0,0.5);">Kishan Kumar</h3>
  <p style="line-height:2.2; font-size:14px; margin:0 0 16px 0;">
    📧 KumarKrishna70503@gmail.com
  </p>
  <div style="display:flex; justify-content:center; gap:10px; flex-wrap:wrap;">
    <a href="https://www.instagram.com/ourtrip_2026/" target="_blank" style="
      text-decoration:none; color:white; font-weight:600; font-size:13px;
      padding:9px 16px; border-radius:10px;
      background:linear-gradient(135deg, #f58529, #dd2a7b, #8134af, #515bd4);">
      📷 Instagram
    </a>
    <a href="tel:9693240618" style="
      text-decoration:none; color:white; font-weight:600; font-size:13px;
      padding:9px 16px; border-radius:10px;
      background:linear-gradient(135deg, #2D6A9F, #1B4332);">
      📞 Call
    </a>
    <a href="https://wa.me/7050311718" target="_blank" style="
      text-decoration:none; color:white; font-weight:600; font-size:13px;
      padding:9px 16px; border-radius:10px;
      background:#25D366;">
      💬 WhatsApp
    </a>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-bottom:20px;'></div>", unsafe_allow_html=True)

st.caption("🏔️ Manali Trip 2026 · Built with Streamlit + MongoDB · October Adventure")