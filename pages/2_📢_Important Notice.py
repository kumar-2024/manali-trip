import streamlit as st

st.set_page_config(
    page_title="Manali Trip – Important Notice",
    page_icon="🏔️",
    layout="centered"
)

st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    #MainMenu, footer, header { visibility: hidden; }

    .outer {
        padding: 8px 16px 24px 16px;
    }
    .wrap {
        max-width: 660px;
        margin: 0 auto;
        color: #c0000a;
        font-family: sans-serif;
        border: 2.5px solid #c0000a;
        padding: 28px 32px;
    }
    .header {
        text-align: center;
        border-bottom: 2px solid #c0000a;
        padding-bottom: 1.2rem;
        margin-bottom: 1.5rem;
    }
    .badge {
        font-size: 11px;
        letter-spacing: 3px;
        font-weight: 700;
        color: #c0000a;
        opacity: 0.7;
        margin-bottom: 0.5rem;
    }
    h1.trip-title {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: 5px;
        color: #c0000a;
        line-height: 1.1;
    }
    .sub {
        font-size: 0.85rem;
        letter-spacing: 1.5px;
        color: #c0000a;
        opacity: 0.65;
        margin-top: 0.4rem;
    }
    .sec-title {
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 3px;
        color: #c0000a;
        opacity: 0.55;
        margin-bottom: 0.8rem;
        margin-top: 1.4rem;
        text-transform: uppercase;
    }
    .row {
        display: flex;
        align-items: flex-start;
        gap: 10px;
        margin-bottom: 0.7rem;
        font-size: 1rem;
        line-height: 1.6;
        color: #c0000a;
    }
    .divider {
        border: none;
        border-top: 1px solid #c0000a;
        opacity: 0.15;
        margin: 1.2rem 0;
    }
    .dates {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        margin-bottom: 0.5rem;
    }
    .date-item { text-align: center; }
    .date-label {
        font-size: 0.65rem;
        letter-spacing: 2px;
        font-weight: 700;
        color: #c0000a;
        opacity: 0.55;
        margin-bottom: 0.3rem;
        text-transform: uppercase;
    }
    .date-val {
        font-size: 0.95rem;
        font-weight: 800;
        color: #c0000a;
    }
    .prohibit {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        margin-bottom: 0.5rem;
    }
    .p-item {
        text-align: center;
        font-size: 0.9rem;
        font-weight: 700;
        color: #c0000a;
        padding: 8px 4px;
    }
    .budget-num {
        font-size: 2.2rem;
        font-weight: 900;
        letter-spacing: 2px;
        color: #c0000a;
        margin: 0.4rem 0;
    }
    .budget-sub {
        font-size: 0.75rem;
        color: #c0000a;
        opacity: 0.6;
        font-weight: 600;
        letter-spacing: 1px;
    }
    .footer {
        border-top: 2px double #c0000a;
        padding-top: 1rem;
        margin-top: 1.5rem;
        text-align: center;
    }
    .footer-motto {
        font-size: 0.95rem;
        font-weight: 700;
        color: #c0000a;
        letter-spacing: 0.5px;
        line-height: 1.6;
    }
    .footer-tag {
        font-size: 0.7rem;
        color: #c0000a;
        opacity: 0.5;
        letter-spacing: 2px;
        margin-top: 0.4rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="outer">
<div class="wrap">

  <!-- HEADER -->
  <div class="header">
    <div class="badge">⚠ IMPORTANT NOTICE ⚠</div>
    <h1 class="trip-title">MANALI TRIP 2025</h1>
    <div class="sub">Registration से पहले सभी नियम ध्यान से पढ़ें</div>
  </div>

  <!-- ELIGIBILITY -->
  <div class="sec-title">👤 Eligibility Criteria</div>
  <div class="row">✅ केवल <strong>&nbsp;Bachelors (Unmarried)</strong> के लिए</div>
  <div class="row">✅ Age Limit: <strong>&nbsp;21 से 30 वर्ष</strong></div>
  <div class="row">✅ Valid Government ID अनिवार्य — Aadhaar / Driving License / Voter ID</div>
  <div class="row">⚠️ गलत जानकारी देने पर Registration रद्द किया जा सकता है।</div>

  <hr class="divider"/>

  <!-- DATES -->
  <div class="sec-title">📅 Important Dates</div>
  <div class="dates">
    <div class="date-item">
      <div class="date-label">Registration Last Date</div>
      <div class="date-val">31 August</div>
    </div>
    <div class="date-item">
      <div class="date-label">Ticket Booking</div>
      <div class="date-val">September First Week</div>
    </div>
    <div class="date-item">
      <div class="date-label">Departure</div>
      <div class="date-val">September Last Week</div>
    </div>
  </div>

  <hr class="divider"/>

  <!-- PAYMENT -->
  <div class="sec-title">💰 Payment Rules</div>
  <div class="row">1️⃣ <strong>&nbsp;First Installment:</strong>&nbsp; Ticket Booking से पहले Advance Payment अनिवार्य।</div>
  <div class="row">2️⃣ <strong>&nbsp;Second Installment:</strong>&nbsp; Manali Hotel Check-in से पहले।</div>
  <div class="row">🚫 Ticket Booking के बाद <strong>&nbsp;कोई Cancellation / Refund नहीं।</strong></div>
  <div class="row">🚫 Ticket किसी अन्य व्यक्ति को <strong>&nbsp;Transfer नहीं</strong> की जा सकेगी।</div>

  <hr class="divider"/>

  <!-- PROHIBITED -->
  <div class="sec-title">🚫 Strictly Prohibited</div>
  <div class="prohibit">
    <div class="p-item">❌ Alcohol</div>
    <div class="p-item">❌ Smoking</div>
    <div class="p-item">❌ Drugs</div>
    <div class="p-item">❌ Harassment</div>
    <div class="p-item">❌ Violence</div>
    <div class="p-item">❌ Group से अलग होना</div>
  </div>
  <div class="row">⚠️ नियम तोड़ने पर सदस्य को <strong>&nbsp;बिना Refund</strong> के ट्रिप से हटाया जा सकता है।</div>

  <hr class="divider"/>

  <!-- BUDGET -->
  <div class="sec-title">💸 Estimated Budget</div>
  <div class="budget-num">₹21,000 – ₹24,000</div>
  <div class="budget-sub">PER PERSON (अनुमानित) &nbsp;•&nbsp; Group जितना बड़ा, लागत उतनी कम</div>
  <div class="row" style="margin-top:.9rem">🏔️ Adventure Activities: ~₹11,000–13,000</div>
  <div class="row">🚌 Transport + Hotel + Food: ~₹10,000–11,000</div>

  <hr class="divider"/>

  <!-- SAFETY -->
  <div class="sec-title">⚠️ Safety & Rules</div>
  <div class="row">🛡️ Adventure Activities स्वयं की जिम्मेदारी पर होंगी।</div>
  <div class="row">👮 Group Leader के निर्देशों का पालन करना अनिवार्य।</div>
  <div class="row">📞 Emergency में तुरंत Coordinator को सूचित करें।</div>
  <div class="row">📱 सभी Updates WhatsApp Group में साझा किए जाएंगे।</div>

  <!-- FOOTER -->
  <div class="footer">
    <div class="footer-motto">🌄 Travel Together &nbsp;•&nbsp; Respect Everyone &nbsp;•&nbsp; Stay Safe &nbsp;•&nbsp; Create Memories 🏔️</div>
    <div class="footer-tag">MANALI TRIP 2025 — OFFICIAL NOTICE</div>
  </div>

</div>
</div>
""", unsafe_allow_html=True)