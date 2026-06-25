import streamlit as st
import sys
import os
import base64
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.connection import get_collection

st.set_page_config(page_title="Posts", page_icon="📸", layout="wide")

# ── Global CSS (Clean Dark Blue Theme matching other pages) ───────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght=700&family=DM+Sans:wght=300;400;500&display=swap');

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

div[data-testid="stForm"] {
    background-color: rgba(13, 27, 42, 0.85) !important;
    border: 1px solid rgba(201, 216, 240, 0.2) !important;
    border-radius: 16px !important;
    padding: 24px !important;
}

div.stButton > button {
    background: linear-gradient(135deg, #2D6A9F, #1B4332);
    color: white; border: none; border-radius: 10px;
    font-size: 15px; padding: 10px 28px;
    font-family: 'DM Sans', sans-serif; font-weight: 600;
    transition: all 0.3s;
}
div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(45,106,159,0.4); }

.insta-btn {
    display: inline-flex; align-items: center; gap: 8px;
    text-decoration: none;
    background: linear-gradient(135deg, #f58529, #dd2a7b, #8134af, #515bd4);
    color: white !important;
    padding: 10px 22px;
    border-radius: 10px;
    font-weight: 600;
    font-size: 15px;
    margin-bottom: 6px;
}
.insta-btn:hover { opacity: 0.9; }
</style>
""", unsafe_allow_html=True)

# ── ⚙️ CONFIG: Change your Instagram link here ─────────────────────────────────
INSTAGRAM_LINK = "https://www.instagram.com/ourtrip_2026"

MAX_UPLOAD_MB = 12  # safety margin under MongoDB's 16MB document limit

st.title("📸 Trip Posts")
st.markdown("*Photos & videos from the Manali trip 2026*")

st.markdown(
    f'<a href="{INSTAGRAM_LINK}" target="_blank" class="insta-btn">📷 Follow us on Instagram</a>',
    unsafe_allow_html=True,
)

st.markdown("---")

collection = get_collection("posts")

if collection is None:
    st.error("❌ Unable to connect to database. Please check your MongoDB connection.")
    st.stop()

# ── Admin Section (password-gated upload) ──────────────────────────────────────
with st.expander("🔐 Admin: Upload a new post"):
    if "posts_admin_unlocked" not in st.session_state:
        st.session_state.posts_admin_unlocked = False

    if not st.session_state.posts_admin_unlocked:
        admin_pw = st.text_input("Admin Password", type="password", key="posts_admin_pw")
        if st.button("Unlock"):
            correct = st.secrets.get("posts_admin_password", None)
            if correct is None:
                st.error("❌ No admin password configured. Add `posts_admin_password` to secrets.toml.")
            elif admin_pw == correct:
                st.session_state.posts_admin_unlocked = True
                st.rerun()
            else:
                st.error("❌ Incorrect password.")
    else:
        st.success("✅ Admin unlocked")

        with st.form("new_post_form", clear_on_submit=True):
            caption = st.text_input("Caption", placeholder="e.g. Sunset at Solang Valley 🌄")
            uploaded_file = st.file_uploader(
                "Upload Photo or Video",
                type=["jpg", "jpeg", "png", "mp4", "mov"],
            )
            post_submitted = st.form_submit_button("📤 Post")

        if post_submitted:
            if not uploaded_file:
                st.error("❌ Please select a photo or video to upload.")
            else:
                file_bytes = uploaded_file.read()
                size_mb = len(file_bytes) / (1024 * 1024)

                if size_mb > MAX_UPLOAD_MB:
                    st.error(
                        f"❌ File is {size_mb:.1f}MB. Please keep uploads under "
                        f"{MAX_UPLOAD_MB}MB (large videos aren't supported here)."
                    )
                else:
                    file_ext = uploaded_file.name.split(".")[-1].lower()
                    is_video = file_ext in ["mp4", "mov"]
                    mime = f"video/{file_ext}" if is_video else f"image/{file_ext if file_ext != 'jpg' else 'jpeg'}"

                    file_b64 = base64.b64encode(file_bytes).decode()

                    post_doc = {
                        "caption": caption.strip(),
                        "media_data": file_b64,
                        "media_type": "video" if is_video else "image",
                        "mime": mime,
                        "posted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    result = collection.insert_one(post_doc)
                    if result.inserted_id:
                        st.success("✅ Posted!")
                        st.rerun()
                    else:
                        st.error("❌ Failed to save post. Please try again.")

        if st.button("🔒 Lock admin panel"):
            st.session_state.posts_admin_unlocked = False
            st.rerun()

st.markdown("---")

# ── Public feed (visible to everyone, no password needed) ──────────────────────
posts = list(collection.find({}, {"_id": 0}).sort("posted_at", -1))

if not posts:
    st.info("😕 No posts yet. Check back soon!")
    st.stop()

st.markdown(f"**{len(posts)} post(s)**")
st.markdown("")

for post in posts:
    caption = post.get("caption", "")
    media_data = post.get("media_data", "")
    media_type = post.get("media_type", "image")
    mime = post.get("mime", "image/jpeg")
    posted_at = post.get("posted_at", "")

    st.markdown(f"""
<div style="background:rgba(201,216,240,0.06);border:1px solid rgba(201,216,240,0.15);
  border-radius:14px;padding:16px;margin-bottom:20px;">
""", unsafe_allow_html=True)

    if media_type == "video":
        st.video(f"data:{mime};base64,{media_data}")
    else:
        st.markdown(
            f'<img src="data:{mime};base64,{media_data}" '
            f'style="width:100%;max-width:500px;border-radius:10px;display:block;margin:0 auto;">',
            unsafe_allow_html=True,
        )

    if caption:
        st.markdown(f"<p style='margin-top:10px;color:#F0F4FF;font-size:15px;'>{caption}</p>", unsafe_allow_html=True)
    st.caption(f"🕒 {posted_at}")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption(f"📸 Posts · {len(posts)} shared · Manali Trip 2026")