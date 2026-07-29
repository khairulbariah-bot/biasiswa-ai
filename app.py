import json
import streamlit as st
import pandas as pd

# Page setup & layout configuration
st.set_page_config(
    page_title="SMART-SCHOLAR | SPM Financial Aid Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Accessible CSS Styling
ACCESSIBLE_CSS = """
<style>
    /* High contrast accessible styling */
    .stApp {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 24px;
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .scholarship-card {
        background-color: #ffffff;
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .scholarship-card:hover {
        border-color: #2a5298;
        box-shadow: 0 6px 12px rgba(42,82,152,0.15);
    }
    .badge-oku {
        background-color: #8b5cf6;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
    }
    .badge-b40 {
        background-color: #10b981;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
    }
    .apply-btn {
        background-color: #2563eb;
        color: white !important;
        padding: 8px 16px;
        text-decoration: none;
        border-radius: 6px;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
    }
</style>
"""
st.markdown(ACCESSIBLE_CSS, unsafe_allow_html=True)

# Load Scholarship Dataset
@st.cache_data
def load_data():
    try:
        with open("scholarships.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("⚠️ `scholarships.json` file not found in directory!")
        return []

data = load_data()

# Web Speech API JS Component (Accessibility Feature for OKU/Visually Impaired)
def embed_voice_assistant(lang_code="en-US"):
    voice_js = f"""
    <script>
    function startDictation() {{
        if (window.hasOwnProperty('webkitSpeechRecognition')) {{
            var recognition = new webkitSpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = "{lang_code}";
            recognition.start();
            recognition.onresult = function(e) {{
                document.getElementById('speech_output').innerText = e.results[0][0].transcript;
                recognition.stop();
            }};
            recognition.onerror = function(e) {{ recognition.stop(); }}
        }} else {{
            alert("Speech recognition is not supported in this browser. Please use Chrome/Edge.");
        }}
    }}
    function readText(text) {{
        var msg = new SpeechSynthesisUtterance();
        msg.text = text;
        msg.lang = "{lang_code}";
        window.speechSynthesis.speak(msg);
    }}
    </script>
    <div style="background:#f1f5f9; padding:15px; border-radius:8px; border:1px solid #cbd5e1; margin-bottom:15px;">
        <p style="font-weight:bold; margin-bottom:5px;">🎙️ OKU Voice Command & Audio Reader Helper / Pembantu Suara</p>
        <button onclick="startDictation()" style="background:#2563eb; color:white; border:none; padding:8px 12px; border-radius:5px; cursor:pointer;">🎤 Click & Speak / Tekan & Cakap</button>
        <span id="speech_output" style="margin-left:10px; font-weight:bold; color:#1e293b;"></span>
    </div>
    """
    st.components.v1.html(voice_js, height=100)

# Sidebar - Settings & Filters
st.sidebar.title("🛠️ Platform Settings")

# Feature 7: Bilingual Support
lang = st.sidebar.radio("🌐 Select Language / Pilih Bahasa", ["Bahasa Melayu", "English"])
is_bm = lang == "Bahasa Melayu"

# Dictionary Translations
txt = {
    "title": "SMART-SCHOLAR: Portal Biasiswa & Bantuan Kewangan SPM" if is_bm else "SMART-SCHOLAR: SPM Financial Aid Portal",
    "subtitle": "Platform carian biasiswa mesra OKU, Golongan B40 & Pelajar Luar Bandar" if is_bm else "Accessible scholarship discovery platform for OKU, B40 & Rural students",
    "hometown": "Negeri Asal Candidate" if is_bm else "Candidate Hometown State",
    "income": "Pendapatan Isirumah Bulanan (RM)" if is_bm else "Monthly Household Income (RM)",
    "spm_a": "Jumlah Gred A (A+, A, A-) Dalam SPM" if is_bm else "Total A Grades (A+, A, A-) in SPM",
    "course": "Bidang Pengajian Pilihan" if is_bm else "Preferred Course Field",
    "oku_check": "Saya adalah pelajar OKU" if is_bm else "I am an OKU student",
    "rural_check": "Saya menetap di kawasan luar bandar" if is_bm else "I live in a rural area",
    "search_btn": "Cari Biasiswa" if is_bm else "Search Scholarships",
    "results_found": "Biasiswa & Bantuan Kewangan Ditemui" if is_bm else "Scholarships & Financial Aids Found",
    "deadline": "Tarikh Tutup" if is_bm else "Deadline",
    "coverage": "Liputan Bantuan" if is_bm else "Funding Coverage",
    "courses_allowed": "Kursus Layak" if is_bm else "Applicable Courses",
    "apply_now": "Mohon / Maklumat Lanjut" if is_bm else "Apply / More Info"
}

st.markdown(f"""
<div class="main-header">
    <h1>🎓 SMART-SCHOLAR</h1>
    <p style="font-size:1.1rem; margin-top:5px;">{txt['subtitle']}</p>
</div>
""", unsafe_allow_html=True)

# Feature 1: Embedded Accessibility Voice Assistant
embed_voice_assistant("ms-MY" if is_bm else "en-US")

# Search Filters Section
st.subheader("🔍 " + ("Borang Semakan Kelayakan Candidate" if is_bm else "Candidate Eligibility Checker"))

col1, col2 = st.columns(2)

# Feature 3: 14 States in Malaysia List
MALAYSIA_STATES = [
    "All / Semua State", "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", 
    "Pahang", "Perak", "Perlis", "Pulau Pinang", "Sabah", "Sarawak", 
    "Selangor", "Terengganu", "Wilayah Persekutuan (KL/Putrajaya/Labuan)"
]

# Course Categories
COURSE_LIST = [
    "All Courses / Semua Bidang", "Accounting & Finance", "Engineering", 
    "Computer Science & IT", "Medicine & Healthcare", "TVET & Technical", 
    "Business & Administration", "Law", "Islamic Studies"
]

with col1:
    user_state = st.selectbox(txt["hometown"], MALAYSIA_STATES)
    user_course = st.selectbox(txt["course"], COURSE_LIST)
    # Feature 4: Household Income
    user_income = st.number_input(txt["income"], min_value=0, max_value=50000, value=3000, step=250)

with col2:
    # Feature 5: SPM Grade Alignment
    user_spm_as = st.slider(txt["spm_a"], min_value=0, max_value=12, value=5)
    
    # Feature 1 & B40 Target Tags
    is_oku = st.checkbox(txt["oku_check"])
    is_rural = st.checkbox(txt["rural_check"])

# Logic: Categorize Household Income (B40 <= 5250, M40 <= 11819)
income_category = "B40" if user_income <= 5250 else ("M40" if user_income <= 11819 else "T20")

st.markdown("---")

# Filter Logic Application
filtered_results = []
for item in data:
    # State Filter
    state_match = "All" in item["target_states"] or "All / Semua State" in user_state or user_state in item["target_states"]
    
    # Income Filter
    income_match = user_income <= item["max_household_income"]
    
    # SPM Grade Match
    spm_match = user_spm_as >= item["min_spm_straight_as"]
    
    # Course Filter
    course_match = ("All Courses / Semua Bidang" in user_course) or any(user_course.split(" ")[0].lower() in c.lower() for c in item["courses"])
    
    # Special Category Boost (OKU / Rural)
    oku_match = True if not is_oku else item["oku_friendly"]

    if state_match and income_match and spm_match and course_match and oku_match:
        filtered_results.append(item)

# Output Display Section
st.subheader(f"📋 {len(filtered_results)} {txt['results_found']}")

if income_category == "B40":
    st.info("💡 **B40 Auto-Match:** You are eligible for high-priority government welfare schemes, Zakat funds, and targeted corporate scholarships." if not is_bm else "💡 **Padanan B40:** Anda layak untuk menerima keutamaan bantuan zakat negeri, skim kebajikan kerajaan, dan biasiswa korporat khas.")

if len(filtered_results) == 0:
    st.warning("No financial aids found matching your exact criteria. Try adjusting your income or course selection." if not is_bm else "Tiada bantuan kewangan dijumpai yang memenuhi kriteria anda. Sila laraskan semula carian anda.")
else:
    for idx, sch in enumerate(filtered_results):
        title = sch["name_ms"] if is_bm else sch["name_en"]
        coverage = sch["funding_coverage_ms"] if is_bm else sch["funding_coverage_en"]
        
        # Accessibility Tags
        oku_tag = f'<span class="badge-oku">♿ OKU Friendly</span> ' if sch["oku_friendly"] else ""
        b40_tag = f'<span class="badge-b40">🟢 B40 Priority</span> ' if "B40" in sch["target_groups"] else ""
        
        # Scholarship Card Box
        card_html = f"""
        <div class="scholarship-card">
            <h3>{title}</h3>
            <p><strong>Penyedia / Provider:</strong> {sch['provider']} | <strong>Category:</strong> {sch['category']}</p>
            <p>{oku_tag}{b40_tag}</p>
            <hr style="margin: 10px 0;">
            <p><strong>{txt['coverage']}:</strong> {coverage}</p>
            <p><strong>{txt['courses_allowed']}:</strong> {', '.join(sch['courses'])}</p>
            <p><strong>📅 {txt['deadline']}:</strong> <span style="color:#dc2626; font-weight:bold;">{sch['deadline']}</span></p>
            <!-- Feature 6: Direct Application Link -->
            <a href="{sch['apply_url']}" target="_blank" class="apply-btn">🔗 {txt['apply_now']}</a>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

# Footer Note
st.markdown("---")
st.caption("SMART-SCHOLAR Platform © 2026 | Empowring B40, OKU, & Rural Students across 14 States in Malaysia.")
