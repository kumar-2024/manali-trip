# pages/3_🗓️_Day_by_Day_Plan.py
import streamlit as st

st.set_page_config(page_title="Day by Day Plan", page_icon="🗓️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background-color: #0D1B2A; color: #F0F4FF; }
h1,h2,h3 { font-family: 'Playfair Display', serif; color: #F0F4FF !important; }
section[data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1B2A 0%, #1B3A5C 100%); }
</style>
""", unsafe_allow_html=True)

st.title("🗓️ Day Plan")
st.markdown("*Detailed breakdown of every day — 1 Oct to 11 Oct 2026*")
st.markdown("---")

days = [
    {
        "day": "Day 1 — 1 October (Thursday)",
        "icon": "🚆",
        "title": "Ranchi → Delhi (Night Train — 12825)",
        "color": "#2D6A9F",
        "badge": "TRAVEL",
        "sections": [
            ("📍 Starting Point", "Ranchi Junction Railway Station"),
            ("🌙 Evening", """
- **11:30 PM** — Arrive at Ranchi Junction, check in luggage
- **11:55 PM** — Board **Jharkhand Sampark Kranti Express (12825)**
- **Night** — Dinner onboard / carry packed food
- **Overnight** — Sleep through the journey (~19 hrs 40 min)
"""),
            ("💡 Tips", """
- Carry snacks, charger, neck pillow
- Confirm PNR status the night before
- Keep ID proof handy for ticket checking
- Train arrives Delhi (ANVT) next day at **7:35 PM**
"""),
        ],
    },
    {
        "day": "Day 2 — 2 October (Friday)",
        "icon": "🚌",
        "title": "Delhi Transit + Night Bus to Manali",
        "color": "#2D6A9F",
        "badge": "TRAVEL",
        "sections": [
            ("📍 Location", "Anand Vihar (ANVT) → Kashmere Gate ISBT → Manali"),
            ("🌆 Evening (Delhi)", """
- **7:35 PM** — Arrive **Anand Vihar Terminal (ANVT)**
- Freshen up, have dinner near station
- Head to **Kashmere Gate ISBT** (Metro: Blue Line → Kashmere Gate, ~30 min)
"""),
            ("🚌 Late Night", """
- **11:55 PM** — Board **Deltin Travels AC Semi-Sleeper (2+2)** at Kashmere Gate / Majnu ka Tila
- 🌙 Overnight journey to Manali (~11 hrs 15 min)
"""),
            ("💡 Tips", """
- ANVT to Kashmere Gate ISBT: Metro Blue Line → interchange → Yellow Line
- Reach ISBT by **10:30 PM** to be safe
- Carry motion sickness tablets for mountain stretch
- Carry warm layer — bus AC can be cold at night
- Dinner options near ANVT: *Haldiram's*, local dhabas
"""),
        ],
    },
    {
        "day": "Day 3 — 3 October (Saturday)",
        "icon": "🏔️",
        "title": "Manali Arrival + Light Day",
        "color": "#1B4332",
        "badge": "ARRIVAL",
        "sections": [
            ("📍 Location", "Mall Road, Manali"),
            ("🌅 Morning", """
- **~11:10 AM** — Bus arrives Manali
- Auto/taxi to hotel (Mall Road area recommended)
- **Hotel check-in** + freshen up + rest
"""),
            ("🌤️ Afternoon", """
- Easy **Mall Road walk** — explore shops, local vibe
- Try Himachali food at local restaurants
- Visit **Hadimba Temple** if energy permits (2 km from Mall Road)
"""),
            ("🌙 Evening / Night", """
- Chill at café — try *Café 1947* or *Johnson's Café*
- Plan activities for upcoming days
- **Early sleep** — recovery day before adventures
"""),
            ("💡 Tips", """
- Don't overexert Day 1 — altitude acclimatization matters
- Stay hydrated, avoid alcohol on arrival day
- Book Rohtang Pass permit online today for upcoming days
"""),
        ],
    },
    {
        "day": "Day 4 — 4 October (Sunday)",
        "icon": "🪂",
        "title": "Adventure Day 1 — Solang Valley",
        "color": "#7C3AED",
        "badge": "🔥 ADVENTURE",
        "sections": [
            ("📍 Location", "Solang Valley — 14 km from Manali"),
            ("🏄 Full Day Activities", """
- **9:00 AM** — Departure from hotel
- **🪂 Paragliding** — Fly over the stunning Solang bowl
- **⚡ Zipline** — High-speed zip across the valley
- **🏍️ ATV Ride** — Off-road quad biking on mountain terrain
- **🧗 Rope Activities** — Rappelling, Burma bridge, etc.
"""),
            ("💰 Estimated Costs", """
| Activity | Approx Cost |
|----------|------------|
| Paragliding | ₹2,500–₹3,500 |
| Zipline | ₹500–₹800 |
| ATV Ride (30 min) | ₹600–₹1,000 |
| Rope Activities | ₹300–₹500 |
"""),
            ("💡 Tips", """
- Carry GoPro / camera for insane aerial shots
- Book paragliding slots before 10 AM — fills quickly
- Wear sturdy shoes, not sandals
- Carry packed lunch or eat at Solang dhabas
"""),
        ],
    },
    {
        "day": "Day 5 — 5 October (Monday)",
        "icon": "🌊",
        "title": "Rafting + Trek Day",
        "color": "#0369A1",
        "badge": "🌊 THRILL",
        "sections": [
            ("📍 Locations", "Kullu (Rafting) + Jogini Waterfall (Trek)"),
            ("🌊 Morning — River Rafting", """
- Head to **Kullu** (~40 km, ~1 hr drive)
- **River Rafting on Beas** — Grade 3–4 rapids, full thrill
- Duration: 1.5–2 hours on water
- One of the best rafting stretches in North India
"""),
            ("🥾 Afternoon — Jogini Trek", """
- Return towards Manali
- Start **Jogini Waterfall Trek** from Vashisht village
- ~2 km trek, 45–60 mins, moderately steep
- **Jogini Falls** — 30m cascading waterfall, very scenic
"""),
            ("💰 Estimated Costs", """
| Activity | Approx Cost |
|----------|------------|
| River Rafting | ₹600–₹1,000/person |
| Jogini Trek (guide opt.) | Free / ₹200–₹500 |
| Transport Manali–Kullu | ₹200–₹400/person |
"""),
            ("💡 Tips", """
- Wear swimwear under clothes for rafting
- Waterproof your phone / bag for rafting
- Start Jogini trek by 2 PM to be back before dark
- Good trekking shoes essential for Jogini
"""),
        ],
    },
    {
        "day": "Day 6 — 6 October (Tuesday)",
        "icon": "🏕️",
        "title": "Camping Day 1 — Head to the Campsite",
        "color": "#B45309",
        "badge": "🏕️ CAMPING",
        "sections": [
            ("📍 Location", "Riverside Camp near Solang / Old Manali (Beas riverbank)"),
            ("🌤️ Afternoon — Check-in", """
- **12:00 PM** — Check out hotel, transfer to campsite (most camps allow late hotel checkout coordination)
- **1:30 PM** — Arrive at riverside camp, allot tents
- Lunch at the camp (usually included in camping package)
- Free time — riverside walk, photography
"""),
            ("🔥 Evening — Bonfire & Music", """
- **6:30 PM** — Evening tea/snacks
- **7:30 PM** — Bonfire setup begins
- **8:30 PM** — Group bonfire — music, games, stories under the stars
- **9:30 PM** — Camp dinner (BBQ / local Himachali thali, depending on package)
"""),
            ("💰 Estimated Costs", """
| Item | Approx Cost |
|------|------------|
| Camping package (tent + meals) | ₹1,200–₹2,000/person/night |
| Bonfire (often included) | — |
| Bedding/sleeping bag rental | ₹200–₹300 (if needed) |
"""),
            ("💡 Tips", """
- Book a riverside camp in advance — popular ones fill up fast in October
- Carry warm clothes — nights near the river get cold (single digit °C)
- Pack a torch/flashlight, campsites have limited lighting
- Confirm whether meals are included in the camping package
"""),
        ],
    },
    {
        "day": "Day 7 — 7 October (Wednesday)",
        "icon": "🏕️",
        "title": "Camping Day 2 — Stars, Stories & Sunrise",
        "color": "#B45309",
        "badge": "🏕️ CAMPING",
        "sections": [
            ("📍 Location", "Same riverside campsite"),
            ("🌅 Early Morning", """
- **6:00 AM** — Sunrise over the mountains — great photo opportunity
- Hot tea/coffee by the riverside
- Light morning walk along the riverbank
"""),
            ("🌤️ Day — Camp Activities", """
- Breakfast at camp
- Optional: nearby short nature trail or river-side games (volleyball, cards, etc.)
- Relax, soak in the mountain silence — a true digital-detox day
"""),
            ("🌙 Evening", """
- Second bonfire night — group games, antakshari, dancing
- Dinner under the stars
- **Check out of camp by next morning** (or late checkout if arranged)
"""),
            ("💡 Tips", """
- Star-gazing is best between 9–11 PM if skies are clear
- Carry a power bank — limited charging points at most camps
- Respect campsite rules around bonfire/noise timing (usually until 10–11 PM)
- Don't litter — most riverside camps are eco-sensitive zones
"""),
        ],
    },
    {
        "day": "Day 8 — 8 October (Thursday)",
        "icon": "🛍️",
        "title": "Leisure Day + Shopping — Back to Manali",
        "color": "#1A2D3A",
        "badge": "🌤️ LEISURE",
        "sections": [
            ("📍 Location", "Manali Mall Road / Old Manali"),
            ("🌅 Morning", """
- Check out from campsite, transfer back to hotel/Manali town
- Hotel check-in, freshen up
- Relaxed breakfast/brunch at a Mall Road café
"""),
            ("🛍️ Afternoon — Shopping", """
- **Mall Road & Old Manali shopping** — woolens, Kullu shawls, caps
- Local handicrafts, dry fruits, Himachali pickles
- Try local Tibetan/Israeli cafés in Old Manali (*Drifter's Café*, *Lazy Dog*)
"""),
            ("🌙 Evening", """
- Pack bags for the return journey tomorrow
- Final dinner in Manali — treat yourselves at a favourite spot
- Early to bed — long travel day ahead
"""),
            ("💡 Tips", """
- Bargain at local markets — prices are usually negotiable
- Double-check all bags for left-behind items at hotel/camp
- Keep return tickets (bus + train) printouts/screenshots handy
"""),
        ],
    },
    {
        "day": "Day 9 — 9 October (Friday)",
        "icon": "🚌",
        "title": "Return — Manali → Delhi (HRTC Night Bus)",
        "color": "#92400E",
        "badge": "RETURN",
        "sections": [
            ("📍 Location", "Manali → Delhi Kashmere Gate ISBT (Overnight Bus)"),
            ("🌅 Morning / Afternoon", """
- Free time — last minute shopping at Mall Road
- Souvenir shopping: woolens, Himachali shawls, dry fruits
- Final Himachali meal at favourite spot
- Check out of hotel by **11:00 AM**
"""),
            ("🌙 Evening", """
- **7:00 PM** — Board **HRTC Ordinary Bus (Non-AC Seater 3+2)** at Manali Bus Stand
- 🌙 Overnight journey to Delhi (~13 hrs 30 min)
- Arrive **Kashmere Gate ISBT** next morning ~8:30 AM
"""),
            ("💡 Tips", """
- Keep luggage at hotel lobby if you check out early
- Must-buy: Kullu shawls, local honey, dried apricots, Kinnauri apples
- Carry a light blanket / warm layer — non-AC bus can get cold at night
- ₹1,000/person fixed fare — confirm before boarding
"""),
        ],
    },
    {
        "day": "Day 10 — 10 October (Saturday)",
        "icon": "🚆",
        "title": "Delhi Transit + Night Train to Ranchi (12818)",
        "color": "#1B4332",
        "badge": "TRANSIT",
        "sections": [
            ("📍 Location", "Kashmere Gate ISBT → Anand Vihar Terminal (ANVT)"),
            ("🌅 Morning", """
- **~8:30 AM** — Arrive **Kashmere Gate ISBT** from bus
- Freshen up — nearby hotel lounge, café, or station washroom
- Breakfast near ISBT / Kashmere Gate area
"""),
            ("🌤️ Afternoon", """
- Rest, explore nearby area or head to Connaught Place
- Take **Metro** to Anand Vihar Terminal (ANVT) by evening
- Reach ANVT by **7:00 PM** — plenty of buffer time
"""),
            ("🚆 Night", """
- **8:45 PM** — Board **Jharkhand Swarna Jayanti Express (12818)** from ANVT
- Dinner onboard / carry packed food
- Overnight journey to Ranchi (~18 hrs 55 min)
"""),
            ("💡 Tips", """
- Keep Ranchi train ticket ready (book in advance!)
- Kashmere Gate to ANVT: Metro ~20 min (Blue Line)
- Give yourself 2 hrs buffer before train departure
- Arrival in Ranchi: next day **3:40 PM**
"""),
        ],
    },
    {
        "day": "Day 11 — 11 October (Sunday)",
        "icon": "🏠",
        "title": "Arrive Ranchi — Trip Complete!",
        "color": "#1B4332",
        "badge": "HOME",
        "sections": [
            ("📍 Location", "Ranchi Junction"),
            ("🌤️ Afternoon", """
- **3:40 PM** — Train arrives **Ranchi Junction**
- Trip complete! 🎉
"""),
            ("📸 Post-Trip", """
- Unpack, rest, relive the memories
- Sort through photos and videos
- Share your Manali stories!
"""),
            ("💡 Summary", """
- Total trip duration: **11 days** (1 Oct – 11 Oct 2026)
- Total travel time (trains + buses): **~35 hours**
- Total transport cost per person: **~₹3,500**
- Manali stay: **6 nights** (3 Oct – 8 Oct), including 2 nights camping
"""),
        ],
    },
]

for d in days:
    st.markdown(f"""
<div style="background:rgba({','.join(str(int(d['color'].lstrip('#')[i:i+2],16)) for i in (0,2,4))},0.15);
  border-left:4px solid {d['color']};border-radius:10px;padding:20px 24px;margin-bottom:8px;">
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:4px;">
    <span style="font-size:28px">{d['icon']}</span>
    <div>
      <span style="background:{d['color']};color:white;padding:2px 10px;border-radius:12px;
        font-size:11px;font-weight:600;letter-spacing:1px;">{d['badge']}</span>
      <h3 style="margin:4px 0 0 0;font-family:'Playfair Display',serif;color:#F0F4FF;">
        {d['day']}</h3>
      <p style="color:#C9D8F0;margin:0;font-size:15px">{d['title']}</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

    with st.expander("📋 View Full Day Plan", expanded=False):
        for section_title, section_body in d["sections"]:
            st.markdown(f"**{section_title}**")
            st.markdown(section_body)
            st.markdown("")

    st.markdown("")

st.markdown("---")
st.caption("🗓️ Day by Day Plan · Ranchi–Manali–Ranchi Trip 2026")