# pages/4_⏰_Time_to_Time_Plan.py
import streamlit as st

st.set_page_config(page_title="Time Plan", page_icon="⏰", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&family=JetBrains+Mono:wght@400&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background-color: #0D1B2A; color: #F0F4FF; }
h1,h2,h3 { font-family: 'Playfair Display', serif; color: #F0F4FF !important; }
section[data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1B2A 0%, #1B3A5C 100%); }
</style>
""", unsafe_allow_html=True)

st.title("⏰ Time-to-Time Plan")
st.markdown("*Hour-by-hour breakdown of every day — 28 Sep to 5 Oct 2026*")
st.markdown("---")

day_selector = st.selectbox(
    "Select a Day to View",
    [
        "Day 1 — 28 Sep (Mon): Ranchi → Delhi 🚆",
        "Day 2 — 29 Sep (Tue): Delhi Transit + Night Bus 🚌",
        "Day 3 — 30 Sep (Wed): Manali Arrival 🏔️",
        "Day 4 — 1 Oct (Thu): Solang Valley 🪂",
        "Day 5 — 2 Oct (Fri): Rafting + Trek 🌊",
        "Day 6 — 3 Oct (Sat): Return Bus — Manali → Delhi 🚌",
        "Day 7 — 4 Oct (Sun): Delhi Transit + Night Train 🚆",
        "Day 8 — 5 Oct (Mon): Arrive Ranchi 🏠",
    ]
)

# ── Timeline data per day ────────────────────────────────────────────────────
timelines = {
    "Day 1 — 28 Sep (Mon): Ranchi → Delhi 🚆": [
        ("🌅", "8:00 AM", "Final packing + preparation", "Pack everything — ID, tickets, warm clothes, medicines"),
        ("🍽️", "12:00 PM", "Lunch at home", "Eat well before the long journey"),
        ("🚗", "10:00 PM", "Leave for Ranchi Junction", "Keep 1.5 hr buffer for station formalities"),
        ("🚆", "11:30 PM", "Station arrival + boarding", "Check berth number, store luggage, settle in"),
        ("🍽️", "11:55 PM", "Train departs — Ranchi Junction", "Train 12825 (Jharkhand Sampark Kranti Express)"),
        ("😴", "Night", "Overnight journey", "Sleep well — arrive Delhi (ANVT) next day at 7:35 PM"),
    ],
    "Day 2 — 29 Sep (Tue): Delhi Transit + Night Bus 🚌": [
        ("🚆", "7:35 PM", "Arrive Anand Vihar Terminal (ANVT)", "Collect luggage, freshen up at station"),
        ("🍽️", "8:00–9:00 PM", "Dinner near ANVT", "Haldiram's / local dhabas near station"),
        ("🚇", "9:00 PM", "Metro to Kashmere Gate ISBT", "Blue Line from ANVT → Kashmere Gate (~30 min)"),
        ("🎫", "10:00 PM", "Reach Kashmere Gate ISBT", "Find Deltin Travels counter / Majnu ka Tila stop"),
        ("🚌", "10:30 PM", "Board / settle in bus area", "Confirm seat, store luggage in bus"),
        ("🚌", "11:55 PM", "Bus departs — Deltin Travels AC Semi-Sleeper (2+2)", "Kashmere Gate / Majnu ka Tila → Manali"),
        ("😴", "Night", "Overnight bus journey (~11 hrs 15 min)", "Arrive Manali ~11:10 AM next morning"),
    ],
    "Day 3 — 30 Sep (Wed): Manali Arrival 🏔️": [
        ("🏔️", "~11:10 AM", "Arrive Manali Bus Stand", "Grab auto/taxi to hotel — negotiate fare"),
        ("🏨", "12:00 PM", "Hotel check-in + freshen up", "Rest, shower, have lunch"),
        ("☕", "1:00 PM", "Late lunch / brunch", "Local Himachali food or café"),
        ("🚶", "3:00–5:00 PM", "Mall Road stroll", "Explore shops, feel the mountain vibe"),
        ("🛕", "5:00–6:30 PM", "Hadimba Temple (optional)", "15 min from Mall Road, beautiful cedar forest"),
        ("🍽️", "7:30 PM", "Dinner at local restaurant", "Try Siddu or Dham for Himachali flavours"),
        ("📱", "8:30 PM", "Plan + book activities for next 2 days", "Book Rohtang permit online if including snow day"),
        ("😴", "9:30 PM", "Early sleep", "Rest well — big adventure day tomorrow!"),
    ],
    "Day 4 — 1 Oct (Thu): Solang Valley 🪂": [
        ("⏰", "7:00 AM", "Wake up + quick breakfast", "Light breakfast — big day ahead"),
        ("🚗", "8:30 AM", "Depart for Solang Valley", "14 km — ~30 mins by taxi/auto"),
        ("🪂", "9:00–11:00 AM", "Paragliding", "Book slot on arrival; wait time varies"),
        ("⚡", "11:00 AM–12:30 PM", "Zipline", "High adrenaline — multiple runs if possible"),
        ("🍽️", "12:30–1:30 PM", "Lunch at Solang dhabas", "Hot Maggi, chai, simple dhabas available"),
        ("🏍️", "1:30–3:00 PM", "ATV Ride", "30–60 min session on mountain terrain"),
        ("🧗", "3:00–4:30 PM", "Rope activities", "Burma bridge, rappelling, flying fox"),
        ("📸", "4:30–5:30 PM", "Explore valley + photos", "Golden hour shots in Solang bowl"),
        ("🚗", "5:30 PM", "Return to Manali", "~30 min drive back"),
        ("🍽️", "7:30 PM", "Dinner", "Celebrate the adventure day!"),
        ("😴", "9:30 PM", "Sleep", "Rest well — rafting + trek tomorrow"),
    ],
    "Day 5 — 2 Oct (Fri): Rafting + Trek 🌊": [
        ("⏰", "7:00 AM", "Wake up + breakfast", "Eat well — very active day ahead"),
        ("🚗", "8:00 AM", "Drive to Kullu", "~40 km, 1 hour drive"),
        ("🌊", "9:30–11:30 AM", "River Rafting on Beas", "Grade 3–4 rapids, 1.5–2 hrs on water"),
        ("🍽️", "12:00–1:00 PM", "Lunch near Kullu", "Riverside dhabas or Kullu town"),
        ("🚗", "1:00–2:00 PM", "Drive back to Vashisht", "Near Manali — starting point for Jogini"),
        ("🥾", "2:00–4:00 PM", "Jogini Waterfall Trek", "~2 km, 45–60 mins up"),
        ("💧", "4:00–4:30 PM", "At Jogini Waterfall", "Take photos, enjoy the view, cool off"),
        ("🥾", "4:30–5:30 PM", "Trek back down", "45 mins descent"),
        ("☕", "5:30–6:30 PM", "Vashisht hot springs (optional)", "Natural sulphur hot springs in village"),
        ("🛍️", "7:00–8:00 PM", "Quick Mall Road shopping", "Last evening in Manali — pick up souvenirs"),
        ("🍽️", "8:00 PM", "Farewell dinner in Manali", "Make it special — last night here!"),
        ("🧳", "9:00 PM", "Pack bags for departure", "Bus leaves tomorrow evening at 7:00 PM"),
        ("😴", "10:00 PM", "Sleep", "Early checkout prep tomorrow"),
    ],
    "Day 6 — 3 Oct (Sat): Return Bus — Manali → Delhi 🚌": [
        ("⏰", "8:00 AM", "Wake up + last Manali breakfast", "Savour it — last morning in the mountains!"),
        ("🏨", "10:00–11:00 AM", "Hotel checkout", "Store bags at hotel lobby after checkout"),
        ("🛍️", "11:00 AM–2:00 PM", "Final shopping at Mall Road", "Kullu shawls, local honey, dry fruits, trinkets"),
        ("🍽️", "2:00–3:00 PM", "Lunch at favourite spot", "Last Himachali meal!"),
        ("☕", "3:00–5:30 PM", "Café time / rest + photos", "Final memories, chill with the crew"),
        ("🚌", "6:00 PM", "Head to Manali Bus Stand", "Collect bags from hotel, reach bus stand"),
        ("🚌", "7:00 PM", "Bus departs — HRTC Ordinary Bus (Non-AC 3+2)", "Manali → Delhi Kashmere Gate ISBT"),
        ("😴", "Night", "Overnight bus journey (~13 hrs 30 min)", "Arrive Kashmere Gate ISBT ~8:30 AM"),
    ],
    "Day 7 — 4 Oct (Sun): Delhi Transit + Night Train 🚆": [
        ("🌅", "~8:30 AM", "Arrive Kashmere Gate ISBT", "Freshen up at washrooms, stretch legs"),
        ("🍳", "9:00–10:00 AM", "Breakfast near ISBT / Kashmere Gate", "McDonald's / Haldiram's / local options"),
        ("🚇", "10:00 AM", "Metro to Anand Vihar (ANVT)", "Blue Line from Kashmere Gate → ANVT (~20 min)"),
        ("🏨", "10:30 AM–5:00 PM", "Rest near ANVT / explore area", "Hotel day-use or rest at station lounge"),
        ("🛒", "12:00–3:00 PM", "Optional: explore Connaught Place", "Or rest — long train journey tonight"),
        ("🚇", "6:00 PM", "Reach Anand Vihar Terminal (ANVT)", "Check platform, confirm train details"),
        ("🚆", "8:45 PM", "Board Train 12818", "Jharkhand Swarna Jayanti Express — ANVT to Ranchi"),
        ("🍽️", "9:30 PM", "Dinner onboard / carry packed food", "Relax and enjoy the journey home"),
        ("😴", "Night", "Overnight journey (~18 hrs 55 min)", "Arrive Ranchi next day at 3:40 PM"),
    ],
    "Day 8 — 5 Oct (Mon): Arrive Ranchi 🏠": [
        ("🚆", "3:40 PM", "Arrive Ranchi Junction", "Trip complete! 🎉 Collect luggage"),
        ("🚗", "4:00 PM", "Head home", "Auto / cab from Ranchi Junction"),
        ("🏠", "5:00 PM", "Home!", "Unpack, rest, relive the memories"),
        ("📸", "Evening", "Sort photos + videos", "Relive every moment of the trip"),
        ("❤️", "Night", "Trip summary", "8 days · ~35 hrs travel · ~₹3,500 transport/person · Priceless memories"),
    ],
}

selected_key = day_selector
timeline = timelines.get(selected_key, [])

st.markdown(f"### {selected_key}")
st.markdown("")

for i, (icon, time, activity, note) in enumerate(timeline):
    col_time, col_dot, col_content = st.columns([1.2, 0.1, 5])

    with col_time:
        st.markdown(f"""
<div style="text-align:right;padding-top:12px;">
  <span style="font-family:'JetBrains Mono',monospace;color:#E9A84C;font-size:13px;font-weight:600;">
    {time}
  </span>
</div>
""", unsafe_allow_html=True)

    with col_dot:
        is_last = (i == len(timeline) - 1)
        st.markdown(f"""
<div style="display:flex;flex-direction:column;align-items:center;height:100%;">
  <div style="width:12px;height:12px;border-radius:50%;background:#2D6A9F;
    border:2px solid #E9A84C;margin-top:14px;flex-shrink:0;"></div>
  {'<div style="width:2px;flex:1;background:linear-gradient(#2D6A9F,transparent);margin-top:2px;min-height:40px;"></div>' if not is_last else ''}
</div>
""", unsafe_allow_html=True)

    with col_content:
        st.markdown(f"""
<div style="background:rgba(201,216,240,0.06);border:1px solid rgba(201,216,240,0.1);
  border-radius:8px;padding:12px 16px;margin-bottom:12px;">
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">
    <span style="font-size:18px">{icon}</span>
    <strong style="color:#F0F4FF;">{activity}</strong>
  </div>
  <p style="color:#C9D8F0;font-size:13px;margin:0;">{note}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("⏰ Time-to-Time Plan · Ranchi–Manali–Ranchi Trip 2026")