import streamlit as st
import base64
from io import BytesIO
from gtts import gTTS

# Page Configuration
st.set_page_config(
    page_title="SMART-SCHOLAR | Biasiswa SPM 2026",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 1. SCHOLARSHIPS DATA (Embedded directly in memory)
# ---------------------------------------------------------
scholarships_data = [
  {
    "id": 1,
    "name": "Biasiswa OSK Foundation Scholarship Awards 2026",
    "provider": "OSK Foundation",
    "category": "Corporate",
    "target_income": ["B40", "M40"],
    "is_oku_friendly": True,
    "states": ["All States"],
    "courses": ["Engineering", "Quantity Surveying", "Finance & Accounting", "Perakaunan Professional", "IT & Computer Science", "Built Environment"],
    "minimum_grades": {"A": 7, "A+": 0},
    "funding_details": "Full tuition fees, monthly living allowance, laptop subsidy, and book/equipment allowances.",
    "deadline": "2026-07-27",
    "url": "https://biasiswa.index.my/biasiswa-osk-foundation-scholarship-awards/"
  },
  {
    "id": 2,
    "name": "Biasiswa Yayasan Terengganu (Siswa Cemerlang)",
    "provider": "Yayasan Terengganu",
    "category": "State Government",
    "target_income": ["B40", "M40", "T20"],
    "is_oku_friendly": True,
    "states": ["Terengganu"],
    "courses": ["Medicine", "Engineering", "Islamic Studies", "Accounting", "Perakaunan Professional", "Computer Science"],
    "minimum_grades": {"A": 7, "A+": 0},
    "funding_details": "Full scholarship / convertible loan covering tuition fees, hostel, and monthly subsistence allowance.",
    "deadline": "2026-07-09",
    "url": "https://biasiswa.index.my/biasiswa-yayasan-terengganu/"
  },
  {
    "id": 3,
    "name": "Biasiswa Cagamas Scholarship Programme",
    "provider": "Cagamas Berhad",
    "category": "Corporate",
    "target_income": ["B40", "M40"],
    "is_oku_friendly": True,
    "states": ["All States"],
    "courses": ["Finance", "Accounting", "Perakaunan Professional", "IT & Computer Science", "Data Analytics", "Law"],
    "minimum_grades": {"A": 6, "A+": 0},
    "funding_details": "Covers tuition fees, living allowances, book grants, and guaranteed internship opportunities.",
    "deadline": "2026-08-15",
    "url": "https://biasiswa.index.my/biasiswa-cagamas-scholarship-programme/"
  },
  {
    "id": 4,
    "name": "Biasiswa OCBC Scholarship",
    "provider": "OCBC Bank",
    "category": "Corporate",
    "target_income": ["B40", "M40", "T20"],
    "is_oku_friendly": False,
    "states": ["All States"],
    "courses": ["Banking & Finance", "Economics", "Computer Science", "Law", "Data Science"],
    "minimum_grades": {"A": 7, "A+": 0},
    "funding_details": "RM15,000 annually for tuition fees and academic expenses + internship placement.",
    "deadline": "2026-06-30",
    "url": "https://biasiswa.index.my/biasiswa-ocbc-scholarship/"
  },
  {
    "id": 5,
    "name": "Bantuan Kewangan KPT – Kluster B40 & M40 (BKPKK)",
    "provider": "Kementerian Pendidikan Tinggi (KPT)",
    "category": "Government",
    "target_income": ["B40", "M40"],
    "is_oku_friendly": True,
    "states": ["All States"],
    "courses": ["Technical & Vocational (TVET)", "Diploma Courses", "Certificate Courses"],
    "minimum_grades": {"A": 0, "A+": 0},
    "funding_details": "Monthly allowance of RM300 - RM360 throughout study duration in Kolej Komuniti & Polytechnics.",
    "deadline": "2026-12-31",
    "url": "https://biasiswa.index.my/bantuan-kewangan-kementerian-pendidikan-tinggi-kpt-kluster-b40-dan-m40/"
  },
  {
    "id": 6,
    "name": "Bantuan Zakat Pendidikan IPTA / IPTS MAIDAM",
    "provider": "Majlis Agama Islam dan Adat Melayu Terengganu",
    "category": "Zakat",
    "target_income": ["B40"],
    "is_oku_friendly": True,
    "states": ["Terengganu"],
    "courses": ["All Courses", "Islamic Studies", "Diploma", "Degree"],
    "minimum_grades": {"A": 0, "A+": 0},
    "funding_details": "One-off IPT registration aid + tuition assistance for Muslim Asnaf / B40 students.",
    "deadline": "2026-11-30",
    "url": "https://biasiswa.index.my/biasiswa-bantuan-zakat-ipta-ipts-maidam/"
  },
  {
    "id": 7,
    "name": "Biasiswa TVET Madani Negeri Sembilan (KYNS)",
    "provider": "Kolej Yayasan Negeri Sembilan",
    "category": "State Government",
    "target_income": ["B40", "M40"],
    "is_oku_friendly": True,
    "states": ["Negeri Sembilan"],
    "courses": ["Technical & Vocational (TVET)", "Engineering Technology", "Automotive", "Culinary Arts"],
    "minimum_grades": {"A": 0, "A+": 0},
    "funding_details": "Full tuition fee coverage and monthly skill training allowance.",
    "deadline": "2026-09-30",
    "url": "https://biasiswa.index.my/biasiswa-tvet-madani/"
  },
  {
    "id": 8,
    "name": "Biasiswa Siswi Safi 2026",
    "provider": "Safi Malaysia",
    "category": "Corporate",
    "target_income": ["B40", "M40"],
    "is_oku_friendly": True,
    "states": ["All States"],
    "courses": ["All Courses", "Mass Communication", "Business", "Sciences"],
    "minimum_grades": {"A": 3, "A+": 0},
    "funding_details": "Financial grant up to RM10,000 per student from a RM1,000,000 total pool.",
    "deadline": "2026-06-30",
    "url": "https://biasiswa.index.my/biasiswa-siswi-safi/"
  },
  {
    "id": 9,
    "name": "Biasiswa IJM Scholarship Award",
    "provider": "IJM Corporation Berhad",
    "category": "Corporate",
    "target_income": ["B40", "M40"],
    "is_oku_friendly": False,
    "states": ["All States"],
    "courses": ["Civil Engineering", "Mechanical Engineering", "Electrical Engineering", "Quantity Surveying"],
    "minimum_grades": {"A": 5, "A+": 0},
    "funding_details": "Full tuition fees, living allowance, and guaranteed employment at IJM Group upon graduation.",
    "deadline": "2026-06-30",
    "url": "https://biasiswa.index.my/biasiswa-ijm-scholarship/"
  },
  {
    "id": 10,
    "name": "Pembiayaan Yayasan Peneraju Bumiputera (PPYB)",
    "provider": "Yayasan Peneraju",
    "category": "Government",
    "target_income": ["B40", "M40"],
    "is_oku_friendly": True,
    "states": ["All States"],
    "courses": ["Finance & Accounting", "Perakaunan Professional", "Data Analytics", "ACCA / CAT", "Technology"],
    "minimum_grades": {"A": 5, "A+": 0},
    "funding_details": "Full sponsorship for professional certification, exam fees, tuition, and living stipends.",
    "deadline": "2026-10-31",
    "url": "https://biasiswa.index.my/pembiayaan-yayasan-peneraju-pendidikan-bumiputera/"
  },
  {
    "id": 11,
    "name": "Biasiswa Bantuan Elaun Khas OKU (KPT)",
    "provider": "Kementerian Pendidikan Tinggi (BKOKU)",
    "category": "Government",
    "target_income": ["B40", "M40", "T20"],
    "is_oku_friendly": True,
    "states": ["All States"],
    "courses": ["All Courses", "Diploma", "Degree", "Certificate Courses"],
    "minimum_grades": {"A": 0, "A+": 0},
    "funding_details": "RM300/month (RM3,600/year) special financial assistance for certified disabled (OKU) tertiary students.",
    "deadline": "2026-12-31",
    "url": "https://biasiswa.index.my/bantuan-elaun-khas-oku-kpt/"
  }
]

# ---------------------------------------------------------
# 2. BILINGUAL TRANSLATION DICTIONARY
# ---------------------------------------------------------
TEXT = {
    "BM": {
        "title": "🎓 SMART-SCHOLAR MALAYSIA",
        "subtitle": "Portal Biasiswa & Bantuan Kewangan khas untuk Lepasan SPM, OKU, Luar Bandar & B40",
        "badge_oku": "♿ Mesra OKU & Luar Bandar",
        "sidebar_header": "⚙️ Tetapan & Profil Pelajar",
        "lang_select": "🌐 Pilih Bahasa / Language",
        "theme_toggle": "👁️ Mod Kontras Tinggi OKU",
        "voice_nav_title": "🎙️ Kawalan Suara (Voice Command)",
        "voice_nav_btn": "Mula Bercakap",
        "voice_nav_help": "Tekan butang dan sebut nama negeri (contoh: 'Selangor') atau 'B40' untuk mengisi borang secara automatik.",
        "state_label": "📍 Negeri Asal Candidate (14 Negeri)",
        "course_label": "📚 Bidang Pengajian Diminati",
        "income_label": "💰 Kategori Pendapatan Isi Rumah",
        "oku_label": "♿ Adakah anda Pemegang Kad OKU?",
        "spm_section": "📊 Keputusan SPM (Jumlah Gred)",
        "grade_a_plus": "Bilangan A+",
        "grade_a": "Bilangan A / A-",
        "btn_generate": "🔍 CARI BIASISWA SAYA",
        "results_header": "🎯 Hasil Padanan Biasiswa & Pembiayaan",
        "matched_count": "Biasiswa Ditemui",
        "filter_all": "Semua Negeri",
        "tts_button": "🔊 Baca Senarai Ini (Text-to-Speech)",
        "apply_button": "🔗 Mohon / Maklumat Lanjut",
        "deadline_label": "Tarikh Tutup",
        "courses_label": "Kursus Dibenarkan",
        "funding_label": "Skop Bantuan",
        "no_results": "Tiada biasiswa yang padan secara tepat. Cuba kurangkan syarat kelayakan.",
        "personal_statement_tab": "✍️ Penjana Draf Kenyataan Peribadi (Personal Statement)",
        "generate_statement_btn": "Jana Draf Kenyataan Peribadi",
        "ps_placeholder": "Tekan butang di atas untuk menjana draf permohonan biasiswa..."
    },
    "EN": {
        "title": "🎓 SMART-SCHOLAR MALAYSIA",
        "subtitle": "Dedicated Scholarship & Financial Aid Portal for SPM Leavers, OKU, Rural & B40 Students",
        "badge_oku": "♿ OKU & Rural Accessible",
        "sidebar_header": "⚙️ Settings & Student Profile",
        "lang_select": "🌐 Select Language / Pilih Bahasa",
        "theme_toggle": "👁️ OKU High-Contrast Mode",
        "voice_nav_title": "🎙️ Voice Command Simulation",
        "voice_nav_btn": "Start Speaking",
        "voice_nav_help": "Click the button and say your state (e.g., 'Selangor') or 'B40' to fill the profile automatically.",
        "state_label": "📍 Candidate Hometown State (14 States)",
        "course_label": "📚 Preferred Course of Study",
        "income_label": "💰 Household Income Category",
        "oku_label": "♿ Are you a registered OKU cardholder?",
        "spm_section": "📊 SPM Results (Grade Breakdown)",
        "grade_a_plus": "Number of A+",
        "grade_a": "Number of A / A-",
        "btn_generate": "🔍 GENERATE MATCHING SCHOLARSHIPS",
        "results_header": "🎯 Matched Financial Aid & Scholarships",
        "matched_count": "Scholarships Matched",
        "filter_all": "All States",
        "tts_button": "🔊 Read List Out Loud (Text-to-Speech)",
        "apply_button": "🔗 Apply / Detailed Info",
        "deadline_label": "Deadline",
        "courses_label": "Applicable Courses",
        "funding_label": "Funding Coverage",
        "no_results": "No exact scholarship match found. Try relaxing your search criteria.",
        "personal_statement_tab": "✍️ Personal Statement Draft Generator",
        "generate_statement_btn": "Generate Personal Statement Draft",
        "ps_placeholder": "Click the button above to auto-generate a tailored application essay..."
    }
}

# ---------------------------------------------------------
# 3. STATE MANAGEMENT & LIST DEFINITIONS
# ---------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "BM"
if "high_contrast" not in st.session_state:
    st.session_state.high_contrast = False

STATES = [
    "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", 
    "Pahang", "Perak", "Perlis", "Pulau Pinang", "Sabah", 
    "Sarawak", "Selangor", "Terengganu", "Wilayah Persekutuan"
]

COURSES = [
    "All Courses", "Engineering", "Finance & Accounting", "Perakaunan Professional", 
    "IT & Computer Science", "Medicine", "Technical & Vocational (TVET)", 
    "Islamic Studies", "Law", "Mass Communication", "Built Environment"
]

INCOME_CATS = ["B40", "M40", "T20"]

# Helper for Text-To-Speech Generation
def generate_audio_player(text_to_speak, lang_code="ms"):
    try:
        tts = gTTS(text=text_to_speak, lang=lang_code, slow=False)
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        b64 = base64.b64encode(fp.read()).decode()
        md = f"""
            <audio controls autoplay style="width: 100%;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            Your browser does not support the audio element.
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Audio engine notice: {e}")

# ---------------------------------------------------------
# 4. ACCESSIBLE CUSTOM CSS STYLING
# ---------------------------------------------------------
if st.session_state.high_contrast:
    bg_color = "#000000"
    text_color = "#FFFF00"
    card_bg = "#1A1A1A"
    accent_color = "#00FF00"
    border_color = "#FFFF00"
else:
    bg_color = "#F8FAFC"
    text_color = "#0F172A"
    card_bg = "#FFFFFF"
    accent_color = "#0284C7"
    border_color = "#E2E8F0"

custom_css = f"""
<style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .scholar-card {{
        background-color: {card_bg};
        border: 2px solid {border_color};
        border-radius: 12px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}
    .badge-oku {{
        background-color: #059669;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }}
    .badge-cat {{
        background-color: {accent_color};
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.85rem;
    }}
    .stButton>button {{
        background-color: {accent_color} !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        font-size: 1.05rem !important;
        padding: 10px 24px !important;
    }}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. SIDEBAR - CONTROLS & USER PROFILE
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/illustrations/100/graduation-cap.png", width=80)
    st.header("SMART-SCHOLAR")
    
    # Bilingual Toggle
    selected_lang = st.radio(
        TEXT[st.session_state.lang]["lang_select"],
        options=["BM", "EN"],
        index=0 if st.session_state.lang == "BM" else 1,
        horizontal=True
    )
    st.session_state.lang = selected_lang
    t = TEXT[st.session_state.lang]

    # Accessibility Contrast Toggle
    st.session_state.high_contrast = st.toggle(t["theme_toggle"], value=st.session_state.high_contrast)

    st.divider()
    st.subheader(t["sidebar_header"])

    # Voice Command Simulation (HTML5 Web Speech API)
    st.markdown(f"**{t['voice_nav_title']}**")
    speech_js = """
    <script>
    function startDictation() {
        if (window.hasOwnProperty('webkitSpeechRecognition')) {
            var recognition = new webkitSpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = "ms-MY";
            recognition.start();
            recognition.onresult = function(e) {
                var transcript = e.results[0][0].transcript;
                alert("Voice Captured: " + transcript);
                recognition.stop();
            };
            recognition.onerror = function(e) {
                recognition.stop();
            }
        } else {
            alert("Web Speech API is not supported in this browser.");
        }
    }
    </script>
    <button onclick="startDictation()" style="background-color:#0284C7; color:white; border:none; padding:8px 16px; border-radius:6px; cursor:pointer;">
        🎙️ Web Speech Input
    </button>
    """
    st.components.v1.html(speech_js, height=50)
    st.caption(t["voice_nav_help"])

    st.divider()

    # Form Filters
    candidate_state = st.selectbox(t["state_label"], options=STATES, index=11)
    candidate_course = st.selectbox(t["course_label"], options=COURSES, index=0)
    candidate_income = st.radio(t["income_label"], options=INCOME_CATS, index=0, horizontal=True)
    is_oku = st.checkbox(t["oku_label"], value=False)

    st.subheader(t["spm_section"])
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        spm_a_plus = st.number_input(t["grade_a_plus"], min_value=0, max_value=12, value=1)
    with col_a2:
        spm_a = st.number_input(t["grade_a"], min_value=0, max_value=12, value=5)

    total_a = spm_a_plus + spm_a

    st.write("")
    btn_search = st.button(t["btn_generate"], use_container_width=True)

# ---------------------------------------------------------
# 6. MAIN CONTENT DASHBOARD
# ---------------------------------------------------------
st.title(t["title"])
st.caption(t["subtitle"])
st.markdown(f"<span class='badge-oku'>{t['badge_oku']}</span>", unsafe_allow_html=True)
st.divider()

# Filter Algorithm
matched_list = []
for item in scholarships_data:
    # State Match
    state_match = "All States" in item["states"] or candidate_state in item["states"]
    
    # Income Match
    income_match = candidate_income in item["target_income"]
    
    # Course Match
    course_match = (candidate_course == "All Courses") or ("All Courses" in item["courses"]) or (candidate_course in item["courses"])
    
    # OKU Priority/Match
    oku_match = True
    if is_oku and not item["is_oku_friendly"]:
        oku_match = False
        
    # Grade Requirement Match
    req_a = item["minimum_grades"].get("A", 0)
    req_a_plus = item["minimum_grades"].get("A+", 0)
    grade_match = (total_a >= req_a) and (spm_a_plus >= req_a_plus)

    if state_match and income_match and course_match and oku_match and grade_match:
        matched_list.append(item)

# Top Bar Statistics
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric(t["matched_count"], len(matched_list))
with c2:
    st.metric("State / Negeri", candidate_state)
with c3:
    st.metric("Income Tier", candidate_income)
with c4:
    st.metric("Total A Grade", f"{total_a} As")

st.divider()

# Text To Speech Readout trigger for Matched List
if matched_list:
    col_tts1, col_tts2 = st.columns([1, 3])
    with col_tts1:
        if st.button(t["tts_button"]):
            summary_text = f"Smart Scholar found {len(matched_list)} scholarships for you. "
            for s in matched_list[:3]:
                summary_text += f"{s['name']} by {s['provider']}, deadline {s['deadline']}. "
            generate_audio_player(summary_text, lang_code="ms" if st.session_state.lang == "BM" else "en")

# Display Scholarship Cards
st.subheader(t["results_header"])

if not matched_list:
    st.info(t["no_results"])
else:
    for idx, item in enumerate(matched_list):
        oku_badge = f"<span class='badge-oku'>♿ OKU Friendly</span>" if item["is_oku_friendly"] else ""
        card_html = f"""
        <div class="scholar-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <h3 style="margin: 0; color: {accent_color};">{item['name']}</h3>
                <div>{oku_badge} <span class="badge-cat">{item['category']}</span></div>
            </div>
            <p><strong>Penyedia / Provider:</strong> {item['provider']}</p>
            <p><strong>{t['funding_label']}:</strong> {item['funding_details']}</p>
            <p><strong>{t['courses_label']}:</strong> {', '.join(item['courses'])}</p>
            <p style="color: #DC2626; font-weight: bold;">⏳ {t['deadline_label']}: {item['deadline']}</p>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        
        c_link, c_audio = st.columns([1, 4])
        with c_link:
            st.markdown(f"[{t['apply_button']}]({item['url']})", unsafe_allow_html=True)
        st.write("")

st.divider()

# ---------------------------------------------------------
# 7. ACCESSIBLE PERSONAL STATEMENT GENERATOR
# ---------------------------------------------------------
st.subheader(t["personal_statement_tab"])
with st.expander("Click to generate your personal statement draft"):
    if st.button(t["generate_statement_btn"]):
        sample_ps = f"""
        Saya {candidate_state} lepasan SPM berniat untuk melanjutkan pengajian dalam bidang {candidate_course}. 
        Dengan pencapaian {total_a}A dalam SPM dan latar belakang keluarga {candidate_income}, 
        pembiayaan ini amat berharga bagi membantu saya merealisasikan cita-cita saya tanpa membebankan keluarga.
        """ if st.session_state.lang == "BM" else f"""
        As an SPM graduate from {candidate_state}, I aim to pursue my studies in {candidate_course}. 
        Achieving {total_a}As in SPM from a {candidate_income} household background, receiving this financial aid 
        will empower me to accomplish my academic aspirations without financial burden.
        """
        st.text_area("Generated Draft", sample_ps, height=140)
        generate_audio_player(sample_ps, lang_code="ms" if st.session_state.lang == "BM" else "en")
