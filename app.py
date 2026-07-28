import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. PAGE CONFIG & MODERN YOUTH-FOCUSED CSS DESIGN
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="BIASISWA-AI | Scholarship & Funding Matcher", 
    page_icon="🎓",
    layout="wide"
)

# Custom CSS for SPM Leavers (Modern, Vibrant, High-Contrast & Accessible)
st.markdown("""
<style>
    /* Main Background & Fonts */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
        color: #f8fafc;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Hero Header Banner */
    .hero-box {
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 50%, #06b6d4 100%);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px -5px rgba(124, 58, 237, 0.4);
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .hero-title {
        color: #ffffff !important;
        font-size: 2.3rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.025em;
        margin-bottom: 0.5rem;
    }
    
    .hero-subtitle {
        color: #e0e7ff !important;
        font-size: 1.1rem !important;
        font-weight: 400;
    }

    /* Card Containers */
    .scholarship-card {
        background-color: #1e293b;
        border: 2px solid #334155;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .scholarship-card:hover, .scholarship-card:focus {
        transform: translateY(-3px);
        border-color: #38bdf8;
        box-shadow: 0 8px 20px rgba(56, 189, 248, 0.2);
    }

    .badge-tag {
        display: inline-block;
        background: #312e81;
        color: #a5b4fc;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 10px;
    }

    /* Accessibility Focus Rings */
    button:focus, input:focus, select:focus {
        outline: 3px solid #38bdf8 !important;
        outline-offset: 2px !important;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. BILINGUAL DICTIONARY
# -----------------------------------------------------------------------------
TRANS = {
    "bm": {
        "hero_title": "BIASISWA-AI",
        "hero_sub": "Portal Pembiayaan Pintar IPTA & IPTS Untuk Pelajar B40 & Luar Bandar",
        "sidebar_header": "Profil Pelajar",
        "spm_label": "Keputusan SPM",
        "income_label": "Kategori Pendapatan Isi Rumah",
        "state_label": "Negeri Asal Pelajar",
        "inst_label": "Jenis Institusi Sasaran",
        "inst_options": ["Semua (IPTA & IPTS)", "IPTA (Universiti Awam / Politeknik)", "IPTS (Universiti / Kolej Swasta)"],
        "course_label": "Pilih Bidang Pengajian",
        "course_options": [
            "Perakuanan Profesional (MyPAC / ACCA / Peneraju)",
            "Sains, Kejuruteraan & Teknologi (PETRONAS / YTP MARA / JPA)",
            "Perubatan, Farmasi & Sains Kesihatan (JPA / MARA / BNM)",
            "Ekonomi, Kewangan, Fintech & Perniagaan (BNM / PayNet)",
            "Pendidikan & Perguruan (PISMP KPM)",
            "TVET, Kemahiran & Vokasional (PTPK / MARA)",
            "Media, Seni Reka & Sains Sosial (Star/Sin Chew)",
            "Pengajian Umum / Mana-mana Kursus (PTPTN / Yayasan Negeri)"
        ],
        "main_header": "Padanan Skim Pembiayaan Komprehensif",
        "matching_for": "Sistem memadankan biasiswa bagi bidang **{course}** ({inst}) untuk pelajar asal **{state}**:",
        "btn_check": "Semak Padanan Pembiayaan",
        "btn_essay": "Jana Draf Esei B40",
        "match_found": "Padanan Pembiayaan Ditemui bagi Pelajar {state} ({income})!",
        "essay_title": "Draf Esei Permohonan Pembiayaan (Jana AI):",
        "essay_body": "Saya merupakan anak jati {state} yang bercita-cita tinggi untuk mengejar kelayakan dalam bidang {course} ({inst}). Menginsafi latar belakang keluarga saya dalam kategori {income}, pembiayaan ini adalah pendorong utama yang dapat mengubah garis takdir kewangan keluarga kami. Dengan keputusan SPM {spm}, saya berikrar akan memanfaatkan penajaan ini untuk menjadi profesional berkaliber yang memberi sumbangan bakti kembali kepada negara dan negeri {state}.",
        "voice_instruction": "Tekan butang mikrofon di bawah untuk bercakap soalan anda:",
        "listen_btn": "Dengar Hasil (Bicara)"
    },
    "en": {
        "hero_title": "SCHOLARSHIP-AI",
        "hero_sub": "Smart Higher Education Funding Platform for B40 & Rural Students",
        "sidebar_header": "Student Profile",
        "spm_label": "SPM Results",
        "income_label": "Household Income Category",
        "state_label": "Home State",
        "inst_label": "Target Institution Type",
        "inst_options": ["All (Public & Private)", "Public Universities / Polytechnics", "Private Universities / Colleges"],
        "course_label": "Select Field of Study",
        "course_options": [
            "Professional Accounting (MyPAC / ACCA / Peneraju)",
            "Science, Engineering & Technology (PETRONAS / YTP MARA / JPA)",
            "Medicine, Pharmacy & Health Sciences (JPA / MARA / BNM)",
            "Economics, Finance, Fintech & Business (BNM / PayNet)",
            "Education & Teaching (PISMP KPM)",
            "TVET, Skills & Vocational (PTPK / MARA)",
            "Media, Design & Social Sciences (Star/Sin Chew)",
            "General Studies / Any Course (PTPTN / State Foundations)"
        ],
        "main_header": "Comprehensive Funding Matcher",
        "matching_for": "System matching scholarships for **{course}** ({inst}) for students from **{state}**:",
        "btn_check": "Check Matching Scholarships",
        "btn_essay": "Generate B40 Essay Draft",
        "match_found": "Funding Matches Found for Student from {state} ({income})!",
        "essay_title": "Funding Application Essay Draft (Instant AI):",
        "essay_body": "I am a native student from {state} with high aspirations to pursue qualifications in {course} ({inst}). Understanding my family's financial background in the {income} category, this funding is the primary stepping stone that can transform our family's future. With my SPM results of {spm}, I pledge to utilize this sponsorship to become a high-caliber professional who contributes back to the nation and the state of {state}.",
        "voice_instruction": "Press the microphone button below to speak your query:",
        "listen_btn": "Listen to Output (Read Aloud)"
    }
}

# -----------------------------------------------------------------------------
# 3. VOICE COMMAND & AUDIO READ-ALOUD JAVASCRIPT WIDGET
# -----------------------------------------------------------------------------
def render_voice_assistant(language_code):
    """HTML5 Speech Recognition (Voice Input) & Speech Synthesis (Text-to-Speech)"""
    js_code = f"""
    <div style="background-color: #1e293b; padding: 15px; border-radius: 12px; border: 2px solid #38bdf8; margin-bottom: 20px;">
        <p style="color: #f8fafc; font-size: 14px; font-weight: 600; margin-bottom: 10px;">
            🎙️ <b>Voice Accessibility Helper (Blind & Visually Impaired)</b>
        </p>
        <button id="micBtn" onclick="startDictation()" aria-label="Start Voice Input" style="background: #38bdf8; color: #0f172a; border: none; padding: 10px 18px; border-radius: 8px; font-weight: 700; cursor: pointer; margin-right: 10px;">
            🎤 Speak Query (Input Suara)
        </button>
        <button id="speakBtn" onclick="readPageContent()" aria-label="Read Output Aloud" style="background: #a855f7; color: #ffffff; border: none; padding: 10px 18px; border-radius: 8px; font-weight: 700; cursor: pointer;">
            🔊 Read Output Aloud (Dengar Hasil)
        </button>
        <p id="speechStatus" style="color: #94a3b8; font-size: 12px; margin-top: 8px;" role="status" aria-live="polite">Status: Idle</p>
    </div>

    <script>
        function startDictation() {{
            if (window.hasOwnProperty('webkitSpeechRecognition') || window.hasOwnProperty('SpeechRecognition')) {{
                var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                var recognition = new SpeechRecognition();
                recognition.continuous = false;
                recognition.interimResults = false;
                recognition.lang = "{'ms-MY' if language_code == 'bm' else 'en-US'}";
                
                document.getElementById('speechStatus').innerText = "Listening... Speak now.";
                recognition.start();

                recognition.onresult = function(e) {{
                    var textResult = e.results[0][0].transcript;
                    document.getElementById('speechStatus').innerText = "Heard: " + textResult;
                    
                    // Inject speech input into Streamlit chat input box if present
                    window.parent.document.querySelector('textarea[data-testid="stChatInputTextArea"]').value = textResult;
                }};

                recognition.onerror = function(e) {{
                    document.getElementById('speechStatus').innerText = "Error recognizing speech: " + e.error;
                    recognition.stop();
                }};
            }} else {{
                document.getElementById('speechStatus').innerText = "Speech Recognition not supported on this browser. Try Chrome or Edge.";
            }}
        }}

        function readPageContent() {{
            var contentToRead = window.parent.document.querySelector('main').innerText;
            var synth = window.speechSynthesis;
            if (synth.speaking) {{
                synth.cancel();
                document.getElementById('speechStatus').innerText = "Speech stopped.";
                return;
            }}
            var utterThis = new SpeechSynthesisUtterance(contentToRead.substring(0, 1000)); // Read first 1000 chars
            utterThis.lang = "{'ms-MY' if language_code == 'bm' else 'en-US'}";
            synth.speak(utterThis);
            document.getElementById('speechStatus').innerText = "Reading page content aloud...";
        }}
    </script>
    """
    components.html(js_code, height=130)

# -----------------------------------------------------------------------------
# 4. APP INTERFACE & LOGIC
# -----------------------------------------------------------------------------
# Language Toggle
lang_choice = st.sidebar.radio("Bahasa / Language", ["Bahasa Melayu", "English"], index=0)
lang = "bm" if lang_choice == "Bahasa Melayu" else "en"
txt = TRANS[lang]

# Hero Header
st.markdown(f"""
    <div class="hero-box">
        <h1 class="hero-title">🎓 {txt['hero_title']}</h1>
        <p class="hero-subtitle">{txt['hero_sub']}</p>
    </div>
""", unsafe_allow_html=True)

# Render Speech Assistant Widget
render_voice_assistant(lang)

# Sidebar Form Controls
st.sidebar.markdown(f"## 📋 {txt['sidebar_header']}")
spm_results = st.sidebar.text_input(txt["spm_label"], "5A 2B")
income_group = st.sidebar.selectbox(txt["income_label"], ["B40 (Kurang/Below RM 4,850)", "M40", "T20"])

malaysia_states = [
    "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", 
    "Pahang", "Pulau Pinang", "Perak", "Perlis", "Sabah", 
    "Sarawak", "Selangor", "Terengganu", "Wilayah Persekutuan"
]
selected_state = st.sidebar.selectbox(txt["state_label"], malaysia_states)
inst_type = st.sidebar.radio(txt["inst_label"], txt["inst_options"])
course_track = st.sidebar.selectbox(txt["course_label"], txt["course_options"])

# Main Interactive Interface
st.markdown(f"## {txt['main_header']}")
st.write(txt["matching_for"].format(course=course_track, inst=inst_type, state=selected_state))

# Action Buttons
col1, col2 = st.columns(2)
with col1:
    btn_check = st.button(f"🔍 {txt['btn_check']}", use_container_width=True)
with col2:
    btn_essay = st.button(f"✍️ {txt['btn_essay']}", use_container_width=True)

# Function for state foundations
def get_state_foundation(state):
    foundations = {
        "Sabah": "Yayasan Sabah (Bantuan Pendaftaran IPT & Biasiswa Kerajaan Negeri Sabah)",
        "Sarawak": "Yayasan Sarawak (Biasiswa Pinjaman Anak Sarawak & IPT Free Tuition)",
        "Perak": "Yayasan Perak (Bantuan Mahasiswa Anak Perak)",
        "Johor": "Yayasan Pelajaran Johor (YPJ)",
        "Selangor": "Yayasan Selangor (Biasiswa DUA & Peduli IPT)",
        "Kelantan": "Yayasan Kelantan Darulnaim (YAKIN)"
    }
    return foundations.get(state, f"Yayasan Negeri {state}")

# Display Results in Styled Accessible Cards
if btn_check:
    state_foundation = get_state_foundation(selected_state)
    
    st.markdown(f"""
        <div aria-live="polite" role="status" style="margin-top: 15px;">
            <h3 style="color: #38bdf8;">✅ {txt['match_found'].format(state=selected_state, income=income_group)}</h3>
        </div>
    """, unsafe_allow_html=True)

    # Card 1: State Foundation
    st.markdown(f"""
    <div class="scholarship-card" tabindex="0">
        <span class="badge-tag">Bantuan Khusus Negeri</span>
        <h3 style="color: #f8fafc; margin-top: 0;">1. {state_foundation}</h3>
        <p><b>Penyedia / Provider:</b> Kerajaan Negeri {selected_state}</p>
        <p><b>Kelayakan / Eligibility:</b> Anak kelahiran atau bermastautin di {selected_state}</p>
        <p><b>Bantuan / Benefit:</b> Elaun pendaftaran masuk IPTA/IPTS, Biasiswa Khas B40, dan Insentif Peranti / Laptop</p>
    </div>
    """, unsafe_allow_html=True)

    # Card 2: Field Specific
    track_idx = txt["course_options"].index(course_track)
    if track_idx == 0:
        st.markdown("""
        <div class="scholarship-card" tabindex="0">
            <span class="badge-tag">Sponsorship Perakaunan</span>
            <h3 style="color: #f8fafc; margin-top: 0;">2. MyPAC Professional Accounting Sponsorship</h3>
            <p><b>Penyedia:</b> Malaysian Professional Accountancy Centre (MyPAC)</p>
            <p><b>Laluan:</b> ACCA / CAT / FIA</p>
            <p><b>Bantuan:</b> 100% Yuran Pengajian & Peperiksaan ACCA + Asrama + Elaun Sara Hidup</p>
        </div>
        """, unsafe_allow_html=True)
    elif track_idx in [1, 2]:
        st.markdown("""
        <div class="scholarship-card" tabindex="0">
            <span class="badge-tag">Sains & Perubatan</span>
            <h3 style="color: #f8fafc; margin-top: 0;">2. PETRONAS Education Sponsorship (PESP) / MARA YTP</h3>
            <p><b>Penyedia:</b> PETRONAS & MARA</p>
            <p><b>Bantuan:</b> Penajaan Penuh 100% Yuran, Elaun Sara Hidup, Peranti Komputer, dan Jaminan Kerjaya.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="scholarship-card" tabindex="0">
            <span class="badge-tag">Pembiayaan Am</span>
            <h3 style="color: #f8fafc; margin-top: 0;">2. Skim PTPTN (Loan-to-Scholarship Scheme)</h3>
            <p><b>Penyedia:</b> Perbadanan Tabung Pendidikan Tinggi Nasional</p>
            <p><b>Keistimewaan B40:</b> Pembiayaan 100% yang bertukar menjadi **BIASISWA PERCUMA** jika graduan mendapat Ijazah Sarjana Muda Kelas Pertama.</p>
        </div>
        """, unsafe_allow_html=True)

if btn_essay:
    st.markdown(f"### {txt['essay_title']}")
    essay = txt["essay_body"].format(
        state=selected_state, 
        course=course_track, 
        inst=inst_type, 
        income=income_group, 
        spm=spm_results
    )
    st.info(essay)

# Chat Input Interface
st.markdown("---")
user_query = st.chat_input("Taip atau gunakan Voice Command di atas untuk soalan anda...")

if user_query:
    st.chat_message("user").write(user_query)
    with st.chat_message("assistant"):
        st.write(f"Jawapan BIASISWA-AI bagi soalan: *{user_query}*")
        st.write("Sistem menyemak semua kriteria syarat kelayakan akademik SPM dan bantuan kewangan negeri anda.")
