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
st.markdown("*रांची → चंडीगढ़ → शिमला → कसोल → मनाली → चंडीगढ़ → रांची — Complete Travel Chart*")
st.markdown("---")

# ── Day-by-Day Overview ───────────────────────────────────────────────────────
st.markdown("### 🗓️ Day Overview")

data = [
    ("Day 1",  "24 Sep (Thu)",  "🚆 Ranchi → Chandigarh",   "Train 18309 dep 5:10 PM from Ranchi Jn", "#1B3A5C"),
    ("Day 2",  "25 Sep (Fri)",  "🚆 Onboard Train",         "Continuing journey towards Chandigarh", "#1B3A5C"),
    ("Day 3",  "26 Sep (Sat)",  "🏔️ Chandigarh + Shimla",  "Arrive Chandigarh 2:53 AM · Private car onward to Shimla", "#1B4332"),
    ("Day 4",  "27 Sep (Sun)",  "🎯 Shimla",                "Sightseeing — Mall Road, Ridge, Jakhoo Temple", "#2D3A1A"),
    ("Day 5",  "28 Sep (Mon)",  "🚗 Kasol",                 "Drive to Kasol, evening at leisure by Parvati River", "#0369A1"),
    ("Day 6",  "29 Sep (Tue)",  "🎯 Kasol",                 "Kasol village walk, café hopping, optional Chalal/Tosh trek", "#0369A1"),
    ("Day 7",  "30 Sep (Wed)",  "🚗 Manali",                "Drive to Manali, hotel check-in, Mall Road evening", "#1A2D3A"),
    ("Day 8",  "1 Oct (Thu)",   "🎯 Manali",                "Local sightseeing / adventure activities", "#1A2D3A"),
    ("Day 9",  "2 Oct (Fri)",   "🚗 Manali → Chandigarh",   "Private car departs Manali morning · Drops Chandigarh afternoon", "#92400E"),
    ("Day 10", "3 Oct (Sat)",   "🚆 Chandigarh → Ranchi",   "Train 18310 dep ~1:45 AM · Arrive Ranchi 8:15 AM", "#2A1A2A"),
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
| Ranchi → Chandigarh | Train 18309 (SBP–JAT Express) | 24 sep (Thu), dep 5:10 PM |
| Chandigarh → Shimla → Kasol → Manali | Private Car (full trip booking) | 26 Sep onwards |

✅ Train 18309 runs **Mon / Tue / Thu / Sat** — confirm 24 Sep run day on IRCTC before booking  
✅ Arrives Chandigarh **2:53 AM (Sat, 26 Sep)** — ~33 hr 43 min journey  
✅ Car covers Chandigarh ⇄ Shimla ⇄ Kasol ⇄ Manali ⇄ Chandigarh as one full package  
""")

with t2:
    st.markdown("""
**🔴 Return Journey (वापसी का सफर)**
| Leg | Mode | Details |
|-----|------|---------|
| Manali → Chandigarh | Private Car | 2 Oct, drop-off afternoon |
| Chandigarh → Ranchi | Train 18310 (JAT–SBP Express) | 3 Oct, dep ~1:45 AM |

✅ Car drops you in Chandigarh by afternoon on 2 Oct  
✅ Train 18310 runs **Mon / Wed / Fri / Sat** — confirm exact 2/3 Oct night run on IRCTC  
✅ Free evening in Chandigarh (2 Oct) before boarding the early-morning train (3 Oct, 1:45 AM)  
✅ Arrives Ranchi **8:15 AM (Sat, 3 Oct)**  
""")

st.markdown("---")

# ── Train Details ─────────────────────────────────────────────────────────────
st.markdown("### 🚂 Train Details")

tr1, tr2 = st.columns(2)
with tr1:
    st.markdown("""
**18309 — SBP–JAT Express (Sambalpur–Jammu Tawi)**  
🛤️ Ranchi (RNC) → Chandigarh (CDG)  
📅 24 sep 2026 (Thursday)  
⏰ Dep: 5:10 PM &nbsp;&nbsp; Arr: 26 Sep 2:53 AM  
⏱️ Journey: ~33 hrs 43 min  
🗓️ Runs on: Mon, Tue, Thu, Sat  
💺 Class: Sleeper/3AC &nbsp;&nbsp; 💰 To be confirmed on IRCTC  
""")

with tr2:
    st.markdown("""
**18310 — JAT–SBP Express (Jammu Tawi–Sambalpur)**  
🛤️ Chandigarh (CDG) → Ranchi (RNC)  
📅 Dep night of 2 Oct / early 3 Oct 2026  
⏰ Dep: ~1:45 AM &nbsp;&nbsp; Arr: 8:15 AM (same day)  
⏱️ Journey: ~6.5 hrs *(verify — confirm full schedule on IRCTC)*  
🗓️ Runs on: Mon, Wed, Fri, Sat  
💺 Class: Sleeper/3AC &nbsp;&nbsp; 💰 To be confirmed on IRCTC  
""")

st.info("ℹ️ Train numbers and run-days noted above are as provided — please do a final IRCTC check closer to the booking date, since schedules can be revised.")

st.markdown("---")

# ── Private Car (Himachal Trip) ───────────────────────────────────────────────
st.markdown("### 🚗 Private Car — Full Himachal Trip")

st.markdown("""
<div style="background:rgba(13,27,42,0.8);border:1px solid rgba(201,216,240,0.15);border-radius:12px;padding:20px;">

**Route:** Chandigarh → Shimla → Kasol → Manali → Chandigarh

| Detail | Info |
|--------|------|
| Pickup | Chandigarh, 26 Sep ~3:00 AM (on train arrival) |
| Drop-off | Chandigarh, 2 Oct afternoon |
| Duration | 7 days / 6 nights on road + local use at each stop |
| Usage | Chandigarh–Shimla, Shimla–Kasol, Kasol–Manali transfers + local sightseeing at each stop + Manali–Chandigarh return |
| Vehicle suggestion | Innova / Innova Crysta or similar (for hill roads + group + luggage) |

</div>
""", unsafe_allow_html=True)

st.info("🚗 **Booking Tip:** Book the car as a full package (point-to-point + local usage) with a Himachal-based or Chandigarh-based travel operator — confirm toll, driver allowance, and night-halt charges are included in the quote.")

st.markdown("---")

# ── Accommodation ────────────────────────────────────────────────────────────
st.markdown("### 🏨 Accommodation Summary")

st.markdown("""
| Night | Location | Type |
|-------|----------|------|
| 24 Sep | Train (18309) | Sleeper berth |
| 25 Sep | Train (18309) | Sleeper berth |
| 26 Sep – 27 Sep | Shimla | Hotel (2 nights) |
| 28 Sep – 29 Sep | Kasol | Hotel / Guesthouse (2 nights) |
| 30 Sep – 1 Oct | Manali (Mall Road area) | Hotel (2 nights) |
| 2 Oct | Chandigarh | Hotel (1 night) |
| 2 Oct – 3 Oct | Train (18310) | Sleeper berth |
""")

st.info("🏨 **Hotel Tip:** Shimla — Mall Road के पास; Kasol — Parvati river-side guesthouse; Manali — Mall Road के पास। Budget: ₹800–1500/room/night in October.")

st.markdown("---")

# ── Budget Summary ────────────────────────────────────────────────────────────
st.markdown("### 💰 Transport Budget (Per Person — Estimated)")

st.markdown("""
| Leg | Mode | Cost |
|-----|------|------|
| Ranchi → Chandigarh | Train 18309 (Sleeper, est.) | ₹800–900 |
| Chandigarh ⇄ Shimla ⇄ Kasol ⇄ Manali ⇄ Chandigarh | Private Car (shared per person, est.) | ₹2,000–3,000 |
| Chandigarh → Ranchi | Train 18310 (Sleeper, est.) | ₹800–900 |
| **Total (1 person, estimated)** | | **₹3,600–4,800** |

⚠️ Car cost depends on group size and final vehicle quote — divide total car fare by number of travelers for an accurate per-head cost.
""")

st.success("✅ कुल यात्रा (आने-जाने ट्रेन + प्राइवेट गाड़ी): अनुमानित किराया प्रति व्यक्ति ~₹3,600–4,800 — final quote car booking confirm hone ke baad update karein।")

st.markdown("---")
st.caption("📆 Time Table · Ranchi–Chandigarh–Shimla–Kasol–Manali–Chandigarh–Ranchi Trip 2026")