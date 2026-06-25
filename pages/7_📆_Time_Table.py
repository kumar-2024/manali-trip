# pages/2_📆_Time_Table.py
import streamlit as st

st.set_page_config(page_title="Time Table", page_icon="📆", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background-color: #0D1B2A; color: #F0F4FF; }
h1,h2,h3 { font-family: 'Playfair Display', serif; color: #F0F4FF !important; }
section[data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1B2A 0%, #1B3A5C 100%); }
table { width: 100%; border-collapse: collapse; }
thead tr { background: rgba(45,106,159,0.3); }
th { padding: 12px 16px; text-align: left; color: #E9A84C; font-family: 'DM Sans', sans-serif; border-bottom: 2px solid rgba(201,216,240,0.2); }
td { padding: 10px 16px; border-bottom: 1px solid rgba(201,216,240,0.08); color: #F0F4FF; }
tr:hover td { background: rgba(201,216,240,0.05); }
</style>
""", unsafe_allow_html=True)

st.title("📆 Full Trip Time Table")
st.markdown("*रांची → मनाली → रांची — Complete Travel Chart*")
st.markdown("---")

# ── Day-by-Day Overview ───────────────────────────────────────────────────────
st.markdown("### 🗓️ Day Overview")

data = [
    ("Day 1", "28 Sep (Mon)", "🚆 Ranchi → Delhi", "Train 12825 dep 11:55 PM from RNC", "#1B3A5C"),
    ("Day 2", "29 Sep (Tue)", "🏙️ Delhi Transit + Bus", "Arrive ANVT 7:35 PM · Bus dep 11:55 PM (KG ISBT)", "#1B3A5C"),
    ("Day 3", "30 Sep (Wed)", "🏔️ Manali Arrival", "Arrive ~11:10 AM · Check-in · Mall Road · Rest", "#1B4332"),
    ("Day 4", "1 Oct (Thu)",  "🎯 Manali Explore",  "Local sightseeing / adventure activities", "#2D3A1A"),
    ("Day 5", "2 Oct (Fri)",  "🎯 Manali Explore",  "Rohtang / Solang / Rafting / Trekking", "#1A2D3A"),
    ("Day 6", "3 Oct (Sat)",  "🚌 Manali → Delhi",  "HRTC Bus dep 7:00 PM from Manali", "#1B3A5C"),
    ("Day 7", "4 Oct (Sun)",  "🏙️ Delhi Transit + Train", "Arrive KG ISBT ~8:30 AM · Train 12818 dep 8:45 PM (ANVT)", "#1B3A5C"),
    ("Day 8", "5 Oct (Mon)",  "🚆 Delhi → Ranchi",  "Arrive Ranchi 3:40 PM", "#2A1A2A"),
]

html_rows = ""
for day, date, theme, notes, bg in data:
    html_rows += f"""
<tr style="background:{bg}22;">
  <td><strong style="color:#E9A84C">{day}</strong></td>
  <td style="color:#C9D8F0">{date}</td>
  <td><strong>{theme}</strong></td>
  <td style="color:#C9D8F0;font-size:13px">{notes}</td>
</tr>"""

st.markdown(f"""
<div style="background:rgba(13,27,42,0.8);border:1px solid rgba(201,216,240,0.15);border-radius:12px;overflow:hidden;">
<table>
<thead><tr>
  <th>Day</th><th>Date</th><th>Theme</th><th>Notes</th>
</tr></thead>
<tbody>{html_rows}</tbody>
</table>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── Transport Summary ─────────────────────────────────────────────────────────
st.markdown("### 🚆 Transport at a Glance")

t1, t2 = st.columns(2)
with t1:
    st.markdown("""
**🟢 Onward Journey (जाने का सफर)**
| Leg | Mode | Details |
|-----|------|---------|
| Ranchi → Delhi | Train 12825 | 28 Sep, dep 11:55 PM |
| Delhi → Manali | Deltin Travels AC Bus | 29 Sep, dep 11:55 PM (KG/Majnu ka Tila) |

✅ Book train in advance (Tatkal if needed)  
✅ ISBT Kashmere Gate for Manali buses  
✅ Arrive Delhi by ~7:35 PM (ANVT) — enough time to reach ISBT  
""")

with t2:
    st.markdown("""
**🔴 Return Journey (वापसी का सफर)**
| Leg | Mode | Details |
|-----|------|---------|
| Manali → Delhi | HRTC Ordinary Bus | 3 Oct, dep 7:00 PM |
| Delhi → Ranchi | Train 12818 | 4 Oct, dep 8:45 PM (ANVT) |

✅ Arrive Delhi ~8:30 AM — ample time before train  
✅ Book Rajdhani/Express return well in advance  
✅ ~13.5 hr overnight bus journey  
""")

st.markdown("---")

# ── Train Details ─────────────────────────────────────────────────────────────
st.markdown("### 🚂 Train Details")

tr1, tr2 = st.columns(2)
with tr1:
    st.markdown("""
**Jharkhand Sampark Kranti Express (12825)**  
🛤️ Ranchi (RNC) → Anand Vihar (ANVT)  
📅 28 Sep 2026 (Monday)  
⏰ Dep: 11:55 PM &nbsp;&nbsp; Arr: 29 Sep 7:35 PM  
⏱️ Journey: 19 hrs 40 min  
💺 Class: Sleeper &nbsp;&nbsp; 💰 ~₹700/person  
""")

with tr2:
    st.markdown("""
**Jharkhand Swarna Jayanti Express (12818)**  
🛤️ Anand Vihar (ANVT) → Ranchi (RNC)  
📅 4 Oct 2026 (Sunday)  
⏰ Dep: 8:45 PM &nbsp;&nbsp; Arr: 5 Oct 3:40 PM  
⏱️ Journey: 18 hrs 55 min  
💺 Class: Sleeper &nbsp;&nbsp; 💰 ~₹700/person  
""")

st.markdown("---")

# ── Bus Details ───────────────────────────────────────────────────────────────
st.markdown("### 🚌 Bus Details")

b1, b2 = st.columns(2)
with b1:
    st.markdown("""
**Deltin Travels (AC Semi-Sleeper 2+2)**  
🛤️ Delhi (KG ISBT / Majnu ka Tila) → Manali  
📅 29 Sep 2026 (Tuesday)  
⏰ Dep: 11:55 PM &nbsp;&nbsp; Arr: 30 Sep ~11:10 AM  
⏱️ Journey: ~11 hrs 15 min  
💰 ~₹1,100/person  
""")

with b2:
    st.markdown("""
**HRTC Ordinary Bus (Non-AC Seater 3+2)**  
🛤️ Manali → Delhi (KG ISBT)  
📅 3 Oct 2026 (Saturday)  
⏰ Dep: 7:00 PM &nbsp;&nbsp; Arr: 4 Oct ~8:30 AM  
⏱️ Journey: ~13 hrs 30 min  
💰 ₹1,000/person (fixed fare)  
""")

st.markdown("---")

# ── Accommodation ────────────────────────────────────────────────────────────
st.markdown("### 🏨 Accommodation Summary")

st.markdown("""
| Night | Location | Type |
|-------|----------|------|
| 28 Sep | Train (12825) | Sleeper berth |
| 29 Sep | Bus (Deltin Travels) | AC Semi-Sleeper |
| 30 Sep – 2 Oct | Manali (Mall Road area) | Hotel (3 nights) |
| 3 Oct | Bus (HRTC) | Non-AC Seater |
| 4 Oct | Train (12818) | Sleeper berth |
""")

st.info("🏨 **Hotel Tip:** Mall Road के पास रहें — transport, food और market सब पास। Budget: ₹800–1500/room/night in October.")

st.markdown("---")

# ── Budget Summary ────────────────────────────────────────────────────────────
st.markdown("### 💰 Transport Budget (Per Person)")

st.markdown("""
| Leg | Mode | Cost |
|-----|------|------|
| Ranchi → Delhi | Train 12825 (Sleeper) | ₹700 |
| Delhi → Manali | Deltin Travels AC Bus | ₹1,100 |
| Manali → Delhi | HRTC Ordinary Bus | ₹1,000 |
| Delhi → Ranchi | Train 12818 (Sleeper) | ₹700 |
| **Total (1 person)** | | **₹3,500** |
| **Total (2 persons)** | | **₹7,000** |
""")

st.success("✅ कुल यात्रा समय (आने-जाने): ~35 घंटे &nbsp;|&nbsp; कुल किराया (प्रति व्यक्ति): ~₹3,500 — बेहद किफायती बजट!")

st.markdown("---")
st.caption("📆 Time Table · Ranchi–Manali–Ranchi Trip 2026")