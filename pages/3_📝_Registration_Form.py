# pages/2_📝_Registration_Form.py
import streamlit as st
import sys
import os
import base64
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.connection import get_collection

st.set_page_config(page_title="Registration Form", page_icon="📝", layout="wide")

# ── Load single image and return base64 for page background ───────────────────
@st.cache_data
def get_bg_img():
    """Load the Rohtang image from images folder and return base64 data URL."""
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
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght=700&family=DM+Sans:wght=300;400;500&display=swap');

/* Top Header aur Deploy button hide karne ke liye */
header[data-testid="stHeader"], .stDeployButton, div[data-testid="stStatusWidget"] {{
    display: none !important;
}}

/* Main Application Background Layout (Solid Dark, No Image) */
.stApp {{
    background-color: #0D1B2A !important;
}}

html, body, [class*="css"] {{ font-family: 'DM Sans', sans-serif; color: #F0F4FF; }}
h1,h2,h3,h4 {{ font-family: 'Playfair Display', serif; color: #F0F4FF !important; text-shadow: 0 2px 10px rgba(0,0,0,0.8); }}

section[data-testid="stSidebar"] {{ 
    background: rgba(13, 27, 42, 0.4) !important;
    backdrop-filter: blur(10px) !important;
    border-right: 1px solid rgba(201,216,240,0.15) !important;
}}

/* ❌ FORM AREA MEIN KOI BACKGROUND IMAGE NAHI - FIXED TRANS-DARK COLOR */
div[data-testid="stForm"] {{
    background-color: rgba(13, 27, 42, 0.85) !important;
    border: 1px solid rgba(201, 216, 240, 0.2) !important;
    border-radius: 16px !important;
    padding: 30px !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4) !important;
}}

div[data-baseweb="input"] input,
div[data-baseweb="select"] input,
div[data-baseweb="select"] div,
div[data-baseweb="select"] span,
div[data-baseweb="textarea"] textarea,
div[data-baseweb="base-input"] input,
div[data-baseweb="base-input"] {{
    background-color: #15293E !important;
    border: 1px solid rgba(201,216,240,0.2) !important;
    color: #F0F4FF !important;
    -webkit-text-fill-color: #F0F4FF !important;
    caret-color: #F0F4FF !important;
    border-radius: 8px !important;
}}

/* Select / dropdown ka closed-state box bhi solid dark rahe (light mode override) */
div[data-baseweb="select"] > div {{
    background-color: #15293E !important;
}}

/* Number input ke +/- buttons ka wrapper bhi dark */
div[data-testid="stNumberInput"] > div {{
    background-color: #15293E !important;
}}

/* Placeholder text bhi visible rahe */
div[data-baseweb="input"] input::placeholder,
div[data-baseweb="textarea"] textarea::placeholder {{
    color: rgba(240,244,255,0.5) !important;
    -webkit-text-fill-color: rgba(240,244,255,0.5) !important;
}}

/* Number input ke andar ka text (age field) */
div[data-testid="stNumberInput"] input {{
    background-color: #15293E !important;
    color: #F0F4FF !important;
    -webkit-text-fill-color: #F0F4FF !important;
}}

/* Selectbox ka dropdown panel (jo niche khulta hai - Blood Group, Gender, T-Shirt Size) */
div[data-baseweb="popover"] {{
    background-color: #15293E !important;
}}
div[data-baseweb="popover"] ul,
div[data-baseweb="menu"] ul {{
    background-color: #15293E !important;
}}
div[data-baseweb="popover"] li,
div[data-baseweb="menu"] li {{
    background-color: #15293E !important;
    color: #F0F4FF !important;
}}
div[data-baseweb="popover"] li:hover,
div[data-baseweb="menu"] li:hover {{
    background-color: #2D6A9F !important;
    color: #FFFFFF !important;
}}

label {{ color: #C9D8F0 !important; font-size: 14px !important; font-weight: 500; }}
div.stButton > button {{
    background: linear-gradient(135deg, #2D6A9F, #1B4332);
    color: white; border: none; border-radius: 10px;
    font-size: 16px; padding: 12px 32px; width: 100%;
    font-family: 'DM Sans', sans-serif; font-weight: 600;
    transition: all 0.3s;
}}
div.stButton > button:hover {{ transform: translateY(-2px); box-shadow: 0 8px 24px rgba(45,106,159,0.4); }}
div[data-testid="stExpander"] {{ background: rgba(13,27,42,0.45); border: 1px solid rgba(201,216,240,0.15); border-radius: 10px; backdrop-filter: blur(4px); }}
</style>
""", unsafe_allow_html=True)

st.title("📝 Trip Registration Form")
st.markdown("<p style='color:#C9D8F0; font-style:italic;'>Fill in your details to officially join the Manali trip</p>", unsafe_allow_html=True)

st.markdown("""
<div style="background:#15293E;border:1px solid rgba(201,216,240,0.2);
  border-radius:10px;padding:14px 18px;margin-bottom:24px;color:#F0F4FF;">
  <span style="color:#F0F4FF;">🏔️ Registration date &nbsp;|&nbsp;
  📅 1 july to 2 august &nbsp;|&nbsp;
  manali trip 2026🏔️</span>
</div>
""", unsafe_allow_html=True)

# ── Session state for success ─────────────────────────────────────────────────
if "registration_success" not in st.session_state:
    st.session_state.registration_success = False

if st.session_state.registration_success:
    st.balloons()
    st.success("🎉 Registration successful! You're officially on the Manali trip!")
    st.markdown("""
<div style="background:rgba(13,27,42,0.75);border:1px solid rgba(16,185,129,0.3);
  border-radius:12px;padding:24px;text-align:center;backdrop-filter: blur(6px);">
  <div style="font-size:48px">🏔️</div>
  <h3 style="color:#6EE7B7;">Welcome to the crew!</h3>
  <p style="color:#C9D8F0;">Your details and verification documents have been securely processed. Check the Member List page to see your registration.</p>
</div>
""", unsafe_allow_html=True)
    if st.button("📝 Register Another Person"):
        st.session_state.registration_success = False
        st.rerun()
    st.stop()

# ── Form ──────────────────────────────────────────────────────────────────────
with st.form("registration_form", clear_on_submit=True):

    st.markdown("#### 👤 Personal Details (Compulsory)")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name *", placeholder="e.g. Rahul Kumar Singh")
        age = st.number_input("Age *", min_value=16, max_value=60, value=22, step=1)
        gender = st.selectbox("Gender *", ["Male", "Female", "Other", "Prefer not to say"])
        emergency_contact = st.text_input("Emergency Contact Name + Number *",
                                          placeholder="e.g. Mom - 9876543210")
    with col2:
        city = st.text_input("City *", placeholder="e.g. Ranchi")
        phone = st.text_input("Phone Number *", placeholder="e.g. 9876543210", max_chars=10)
        email = st.text_input("Email Address *", placeholder="you@email.com")
        tshirt_size = st.selectbox("T-Shirt Size *", ["S", "M", "L", "XL", "XXL"])
    st.markdown("---")
    st.markdown("#### 🩸 Health & Sizing Info (Compulsory)")
    col3, col4 = st.columns(2)
    with col3:
        blood_group = st.selectbox("Blood Group *",
            ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "Don't Know"])
    with col4:
       medical_info = st.text_input("Medical Conditions / Allergies *",
                                     placeholder="e.g. None / Asthma / Peanut allergy")

    st.markdown("---")
    st.markdown("#### 📁 Document & Photo Verification (Compulsory)")
    doc_col1, doc_col2 = st.columns(2)
    with doc_col1:
        uploaded_photo = st.file_uploader("Upload Profile Photo * (JPG/PNG)", type=["jpg", "jpeg", "png"])
    with doc_col2:
        uploaded_id_doc = st.file_uploader("Upload ID Document PDF * (Verification Proof)", type=["pdf"])



    st.markdown("---")
    st.markdown("#### 📋 Additional Info")
    notes = st.text_area("Any special requests or notes?",
                         placeholder="e.g. Need lower floor room...",
                         height=80)

    agree = st.checkbox("✅ I confirm all details and verification documents are accurate and I agree to the trip terms.")

    st.markdown("")
    submitted = st.form_submit_button("🏔️ Register for Manali Trip!")

# ── Handle submission ─────────────────────────────────────────────────────────
if submitted:
    # Validation Rules
    errors = []
    if not name.strip():
        errors.append("Full Name is required")
    if not city.strip():
        errors.append("City is required")
    if not phone.strip() or not phone.strip().isdigit() or len(phone.strip()) != 10:
        errors.append("Valid 10-digit phone number is required")
    if not email.strip():
        errors.append("Email Address is required")
    if not uploaded_photo:
        errors.append("Profile Photo upload is mandatory")
    if not uploaded_id_doc:
        errors.append("Verification Identity Document PDF is mandatory")
    if not emergency_contact.strip():
        errors.append("Emergency contact is required")
    if not medical_info.strip():
        errors.append("Medical information or alignment details are required")
    if not agree:
        errors.append("Please confirm and agree to the trip terms")

    if errors:
        for err in errors:
            st.error(f"❌ {err}")
    else:
        collection = get_collection("members")
        if collection is None:
            st.error("❌ Database connection failed. Please try again later.")
        else:
            # Check duplicate phone
            existing = collection.find_one({"phone": phone.strip()})
            if existing:
                st.warning(f"⚠️ A member with phone {phone} is already registered as **{existing.get('name')}**.")
            else:
                # Base64 parsing for file binaries to save safely into database collections
                photo_b64 = base64.b64encode(uploaded_photo.read()).decode()
                id_doc_b64 = base64.b64encode(uploaded_id_doc.read()).decode()

                member_doc = {
                    "name": name.strip(),
                    "age": age,
                    "gender": gender,
                    "city": city.strip(),
                    "phone": phone.strip(),
                    "email": email.strip(),
                    "blood_group": blood_group,
                    "tshirt_size": tshirt_size,
                    "photo_data": photo_b64,
                    "id_document_data": "[ID Document Redacted]",
                    "emergency_contact": emergency_contact.strip(),
                    "medical_info": medical_info.strip(),
                    "notes": notes.strip(),
                    "registered_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }

                result = collection.insert_one(member_doc)
                if result.inserted_id:
                    st.session_state.registration_success = True
                    st.rerun()
                else:
                    st.error("❌ Failed to save registration. Please try again.")

st.markdown("---")

with st.expander("🛠️ Setup Instructions (for organizer)"):
    st.markdown("""
**MongoDB Database Config:**
Ensure your secrets/environment properties are configured correctly to process file buffers into the binary stream collection layer.
""")

st.markdown("---")
st.caption("📝 Registration Form · Manali Trip 2026")