# pages/7_👥_Member_List.py
import streamlit as st
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.connection import get_collection

st.set_page_config(page_title="Member List", page_icon="👥", layout="wide")

# ── Global CSS (Clean Dark Blue Theme matching form page) ─────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght=700&family=DM+Sans:wght=300;400;500&display=swap');

/* Top Header aur Deploy button hide karne ke liye */
header[data-testid="stHeader"], .stDeployButton, div[data-testid="stStatusWidget"] {
    display: none !important;
}

html, body, [class*="css"] { 
    font-family: 'DM Sans', sans-serif; 
    background-color: #0D1B2A; 
    color: #F0F4FF; 
}
h1,h2,h3 { font-family: 'Playfair Display', serif; color: #F0F4FF !important; }

section[data-testid="stSidebar"] { 
    background: rgba(13, 27, 42, 0.4) !important;
    backdrop-filter: blur(10px) !important;
    border-right: 1px solid rgba(201,216,240,0.15) !important;
}

div[data-testid="metric-container"] {
    background: rgba(13, 27, 42, 0.85);
    border: 1px solid rgba(201,216,240,0.15);
    border-radius: 12px;
    padding: 14px;
}
div[data-testid="stForm"] { background-color: transparent !important; border: none !important; }
</style>
""", unsafe_allow_html=True)

st.title("👥 Member List")
st.markdown("*Everyone registered for the Manali trip 2026*")
st.markdown("---")

# ── Load data ─────────────────────────────────────────────────────────────────
col_refresh, col_space = st.columns([1, 4])
with col_refresh:
    if st.button("🔄 Refresh"):
        st.rerun()

collection = get_collection("members")

if collection is None:
    st.error("❌ Unable to connect to database. Please check your MongoDB connection.")
    st.stop()

members = list(collection.find({}, {"_id": 0}).sort("registered_at", 1))

if not members:
    st.warning("😕 No members registered yet.")
    st.markdown("👉 Go to **📝 Registration Form** to add the first member!")
    st.stop()

# ── Stats ─────────────────────────────────────────────────────────────────────
total = len(members)
cities = set(m.get("city", "Unknown") for m in members)

s1, s2, s3 = st.columns(3)
s1.metric("👥 Total Members Joined", total)
s2.metric("🌆 Unique Cities", len(cities))
s3.metric("📅 Trip Target Year", "2026")

st.markdown("---")

# ── Search ────────────────────────────────────────────────────────────────────
search = st.text_input("🔍 Search member by name or city", placeholder="e.g. Rahul or Ranchi")

filtered = members
if search.strip():
    search_lower = search.strip().lower()
    filtered = [
        m for m in members
        if search_lower in m.get("name", "").lower()
        or search_lower in m.get("city", "").lower()
    ]

st.markdown(f"**Showing {len(filtered)} of {total} members**")
st.markdown("")

# ── Member Cards ──────────────────────────────────────────────────────────────
if not filtered:
    st.info("No members found matching your search.")
else:
    cols_per_row = 3
    for row_start in range(0, len(filtered), cols_per_row):
        row = filtered[row_start: row_start + cols_per_row]
        cols = st.columns(cols_per_row)
        for i, member in enumerate(row):
            name = member.get("name", "Unknown")
            age = member.get("age", "—")
            city = member.get("city", "—")
            phone = member.get("phone", "—")
            email = member.get("email", "—")
            activities = member.get("activities", [])
            emergency = member.get("emergency_contact", "—")
            medical = member.get("medical_info", "—")
            
            # Binary Base64 buffers from MongoDB
            photo_b64 = member.get("photo_data", "")
            id_doc_b64 = member.get("id_document_data", "")
            
            member_no = row_start + i + 1

            # Image logic: Custom placeholder display rules if buffer is empty
            if photo_b64 and photo_b64 != "Not Provided":
                avatar_html = f'<img src="data:image/jpeg;base64,{photo_b64}" style="width:54px;height:54px;border-radius:50%;object-fit:cover;border:2px solid #2D6A9F;flex-shrink:0;">'
            else:
                initials = "".join(n[0].upper() for n in name.split()[:2])
                avatar_html = f'<div style="width:54px;height:54px;border-radius:50%;background:linear-gradient(135deg,#2D6A9F,#1B4332);display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:700;color:#F0F4FF;flex-shrink:0;">{initials}</div>'

            # Clickable anchor stream definition for PDF deployment check
            if id_doc_b64 and id_doc_b64 != "[ID Document Redacted]":
                pdf_link_html = f'<a href="data:application/pdf;base64,{id_doc_b64}" download="ID_{name.replace(" ", "_")}.pdf" style="text-decoration:none; background:#2D6A9F; color:white; padding:4px 10px; border-radius:6px; font-size:11px; font-weight:500; display:inline-block; margin-top:4px;">📄 Download ID Proof</a>'
            else:
                pdf_link_html = '<span style="color:#9CA3AF; font-size:11px;">⚠️ ID Not Cached</span>'

            with cols[i]:
                st.markdown(f"""
<div style="background:rgba(201,216,240,0.06);border:1px solid rgba(201,216,240,0.15);border-radius:14px;padding:20px;margin-bottom:12px;">
  <div style="display:flex;align-items:center;gap:14px;margin-bottom:14px;">
    {avatar_html}
    <div>
      <strong style="color:#F0F4FF;font-size:16px;">#{member_no} {name}</strong><br>
      <span style="color:#C9D8F0;font-size:13px;">Age: {age} · {city}</span>
    </div>
  </div>
  <div style="display:grid;gap:6px;font-size:13px;">
    <div><span style="color:#9CA3AF;">📱 Phone: </span><span style="color:#E5E7EB;">{phone}</span></div>
    <div><span style="color:#9CA3AF;">✉️ Email: </span><span style="color:#E5E7EB;">{email}</span></div>
    <div><span style="color:#9CA3AF;">🆘 Emergency: </span><span style="color:#E5E7EB;">{emergency}</span></div>
    <div><span style="color:#9CA3AF;">🩺 Medical: </span><span style="color:#E5E7EB;">{medical}</span></div>
    <div style="margin-top:6px; margin-bottom:4px;">
        {pdf_link_html}
    </div>
    {"<div style='margin-top:8px;color:#E9A84C;font-size:12px;line-height:1.3;'>🎯 <strong>Activities:</strong> " + ", ".join(activities[:4]) + ("..." if len(activities)>4 else "") + "</div>" if activities else ""}
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── Full table view ───────────────────────────────────────────────────────────
with st.expander("📊 View as Admin Data Table"):
    table_data = []
    for m in members:
        table_data.append({
            "Name": m.get("name", ""),
            "Age": m.get("age", ""),
            "City": m.get("city", ""),
            "Phone": m.get("phone", ""),
            "Email": m.get("email", ""),
            "Emergency Contact": m.get("emergency_contact", ""),
            "Medical Conditions": m.get("medical_info", ""),
            #"Selected Activities": ", ".join(m.get("activities", [])),
        })
    st.dataframe(pd.DataFrame(table_data), use_container_width=True)

st.markdown("---")
st.caption(f"👥 Member List · {total} entries monitored · Manali Trip 2026")