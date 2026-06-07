import streamlit as st

st.set_page_config(
    page_title="Himachal Adventure Plan",
    page_icon="🏔",
    layout="wide"
)

LOCATIONS = [
    {
        "name": "Solang Valley",
        "subtitle": "Sky & Speed",
        "color": "#1a6b8a",
        "accent": "#00c6ff",
        "activities": [
            ("🪂", "High-Fly Paragliding (Anjani Mahadev Peak)"),
            ("🏍️", "ATV Quad Bike Ride (Off-Roading)"),
            ("🧗", "Zipline — Valley Crossing"),
            ("🚀", "Bungee Rocket (Reverse Bungee)"),
        ],
        "image_url": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&q=70",
    },
    {
        "name": "Kullu",
        "subtitle": "River & Heights",
        "color": "#1a6b4a",
        "accent": "#00e676",
        "activities": [
            ("🚣", "14 KM Long Rafting (Pirdi to Jhiri)"),
            ("🪢", "Speed Flying Fox"),
            ("🧗", "Natural Rock Climbing"),
            ("🎈", "Hot Air Balloon Ride"),
        ],
        "image_url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600&q=70",
    },
    {
        "name": "Rohtang Pass",
        "subtitle": "Snow & Ice",
        "color": "#2a3a6a",
        "accent": "#82cfff",
        "activities": [
            ("⛷️", "Skiing on Snow Slopes"),
            ("🏂", "Snowboarding"),
        ],
        "image_url": "https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=600&q=70",
    },
    {
        "name": "Optional Add-ons",
        "subtitle": "More Thrills",
        "color": "#6a2a3a",
        "accent": "#ff8a65",
        "activities": [
            ("🤸", "Bungee Jumping"),
            ("⛺", "Mountain Camping (Overnight)"),
        ],
        "image_url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600&q=70",
    },
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Nunito:wght@400;600;700&display=swap');

html, body, [class*="css"] { background-color: #0a0e1a !important; color: #ffffff; }

.main-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.8rem;
    letter-spacing: 3px;
    color: #ffffff;
    margin-bottom: 2px;
}
.main-sub {
    font-family: 'Nunito', sans-serif;
    font-size: 0.95rem;
    color: #8899aa;
    margin-bottom: 1.5rem;
}
.adv-card {
    border-radius: 16px;
    overflow: hidden;
    position: relative;
    height: 300px;
    background-size: cover;
    background-position: center;
    margin-bottom: 16px;
    border: 1px solid rgba(255,255,255,0.1);
}
.adv-card-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to bottom, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0.78) 100%);
}
.adv-card-content {
    position: relative;
    z-index: 2;
    padding: 14px 16px;
    display: flex;
    flex-direction: column;
    height: 100%;
    box-sizing: border-box;
}
.adv-badge {
    display: inline-block;
    font-family: 'Nunito', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    padding: 3px 12px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.3);
    background: rgba(255,255,255,0.12);
    color: #fff;
    margin-bottom: 6px;
    width: fit-content;
}
.adv-card-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.7rem;
    letter-spacing: 1px;
    color: #ffffff;
    margin: 0 0 8px 0;
    line-height: 1;
}
.adv-divider {
    border: none;
    border-top: 0.5px solid rgba(255,255,255,0.2);
    margin: 0 0 10px 0;
}
.adv-activity {
    display: flex;
    gap: 8px;
    align-items: flex-start;
    padding: 4px 0;
    font-family: 'Nunito', sans-serif;
    font-size: 12.5px;
    color: rgba(255,255,255,0.88);
    font-weight: 600;
    border-bottom: 0.5px solid rgba(255,255,255,0.08);
}
.adv-activity:last-child { border-bottom: none; }
.adv-emoji { flex-shrink: 0; font-size: 14px; }
.adv-footer {
    margin-top: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 10px;
    border-top: 1px solid rgba(255,255,255,0.15);
    background: rgba(0,0,0,0.25);
    padding: 8px 0 0;
}
.adv-combo-label {
    font-family: 'Nunito', sans-serif;
    font-size: 11px;
    color: rgba(255,255,255,0.55);
}
.adv-price {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.4rem;
    color: #FFD700;
    letter-spacing: 1px;
}
.total-bar {
    background: #151d2e;
    border-radius: 14px;
    padding: 16px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px solid rgba(255,255,255,0.08);
    margin-top: 8px;
}
.total-label {
    font-family: 'Nunito', sans-serif;
    font-size: 13px;
    color: #8899aa;
}
.total-amount {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    color: #FFD700;
    letter-spacing: 2px;
}
[data-testid="stAppViewContainer"] { background-color: #0a0e1a !important; }
[data-testid="stHeader"] { background-color: #0a0e1a !important; }
section[data-testid="stMain"] { background-color: #0a0e1a !important; }
div[data-testid="stVerticalBlock"] { background-color: transparent; }
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">🏔 Himachal Pradesh Adventure Plan</div>', unsafe_allow_html=True)
st.markdown('<div class="main-sub">Solang Valley &nbsp;·&nbsp; Kullu &nbsp;·&nbsp; Rohtang Pass</div>', unsafe_allow_html=True)

# ── Cards Grid ─────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

for idx, loc in enumerate(LOCATIONS):
    col = col1 if idx % 2 == 0 else col2

    activities_html = "".join([
        f'<div class="adv-activity"><span class="adv-emoji">{e}</span><span>{name}</span></div>'
        for e, name in loc["activities"]
    ])

    card_html = f"""
    <div class="adv-card" style="background-image: url('{loc['image_url']}');">
        <div class="adv-card-overlay"></div>
        <div class="adv-card-content">
            <div class="adv-badge">{loc['name']}</div>
            <div class="adv-card-title">{loc['subtitle']}</div>
            <hr class="adv-divider">
            <div>{activities_html}</div>
        </div>
    </div>
    """
    with col:
        st.markdown(card_html, unsafe_allow_html=True)

# ── Total Bar ─────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="total-bar">
    <div>
        <div class="total-label">💰 Estimated Total &nbsp;(Solang + Kullu + Rohtang + Optional)</div>
        <div style="font-size:11px; color:#556677; font-family:'Nunito',sans-serif;">All 4 packages combined</div>
    </div>
    <div class="total-amount">₹12,000 – ₹14,000</div>
</div>
""", unsafe_allow_html=True)