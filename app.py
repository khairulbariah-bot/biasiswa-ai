import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. PAGE CONFIG & MODERN YOUTH-FOCUSED CSS DESIGN
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="SMART-SCHOLAR | Comprehensive SPM Scholarship & Funding Matcher", 
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
        padding: 2.2rem 2rem;
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
        font-size: 1.05rem !important;
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
        font-size: 0.82rem;
        font-weight: 600;
        margin-bottom: 10px;
    }

    .badge-provider {
        background: #065f46;
        color: #a7f3d0;
    }

    /* Accessibility Focus Rings */
    button:focus, input:focus, select:focus {
        outline: 3px solid #38bdf8 !important;
        outline-offset: 2px !important;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. BILINGUAL DICTIONARY & COMPREHENSIVE 2026 SCHOLARSHIP DATABASE
# -----------------------------------------------------------------------------
TRANS = {
    "bm": {
        "hero_title": "SMART-SCHOLAR",
        "hero_sub": "Platform Pembiayaan Pintar Komprehensif IPTA & IPTS Untuk Pelajar SPM (B40, M40 & Luar Bandar)",
        "sidebar_header": "Profil Pelajar SPM",
        "spm_label": "Keputusan SPM (Gred Asas)",
        "income_label": "Kategori Pendapatan Isi Rumah",
        "state_label": "Negeri Asal Pelajar",
        "inst_label": "Jenis Institusi Sasaran",
        "inst_options": ["Semua (IPTA & IPTS)", "IPTA (Universiti Awam / Politeknik / Matrikulasi / IPG)", "IPTS (Universiti / Kolej Swasta)"],
        "course_label": "Pilih Bidang Pengajian / Laluan Kursus",
        "course_options": [
            "Perakuanan Profesional & Kewangan (MyPAC / ACCA / Peneraju / BNM)",
            "Sains, Kejuruteraan, Teknologi & AI (PETRONAS / YTP MARA / JPA / YTN / Shell / Gamuda)",
            "Perubatan, Farmasi & Sains Kesihatan (JPA / MARA / Yayasan UEM / Sime Darby)",
            "Ekonomi, Business, Fintech & Undang-Undang (Khazanah / BNM / SC / PayNet)",
            "Pendidikan & Perguruan (PISMP KPM)",
            "TVET, Kemahiran & Vokasional (PTPK / MARA / ILP / Kolej Komuniti)",
            "Media, Seni Reka, Komunikasi & Sains Sosial (Star/Sin Chew / IPTS Merit Waivers)",
            "Pengajian Umum / Mana-mana Kursus IPTA & IPTS (PTPTN / Biasiswa Yayasan Negeri)"
        ],
        "main_header": "Padanan Skim Pembiayaan Komprehensif Malaysia 2026",
        "matching_for": "Sistem sedia memadankan biasiswa, pinjaman boleh ubah, dan bantuan pembiayaan bagi **{course}** ({inst}) untuk pelajar dari **{state}**:",
        "btn_check": "Semak Semua Padanan Biasiswa 2026",
        "btn_essay": "Jana Draf Esei Justifikasi Kewangan B40",
        "match_found": "Padanan Pembiayaan Ditemui bagi Pelajar {state} ({income})!",
        "essay_title": "Draf Esei Permohonan Pembiayaan (Jana AI Instant):",
        "essay_body": "Saya merupakan anak jati {state} yang bercita-cita tinggi untuk mengejar kelayakan dalam bidang {course} ({inst}). Menginsafi latar belakang keluarga saya dalam kategori {income}, pembiayaan ini adalah pendorong utama yang dapat mengubah garis takdir kewangan keluarga kami. Dengan keputusan SPM {spm}, saya berikrar akan memanfaatkan penajaan ini untuk menjadi profesional berkaliber yang memberi sumbangan bakti kembali kepada negara dan negeri {state}."
    },
    "en": {
        "hero_title": "SMART-SCHOLAR",
        "hero_sub": "Comprehensive Smart Higher Education Funding Platform for SPM Leavers (Public & Private)",
        "sidebar_header": "SPM Student Profile",
        "spm_label": "SPM Results (Base Grade)",
        "income_label": "Household Income Category",
        "state_label": "Home State",
        "inst_label": "Target Institution Type",
        "inst_options": ["All (Public & Private)", "Public (Public Universities / Polytechnics / Matriculation / IPG)", "Private (Private Universities / Colleges)"],
        "course_label": "Select Field of Study / Course Track",
        "course_options": [
            "Professional Accounting & Finance (MyPAC / ACCA / Peneraju / BNM)",
            "Science, Engineering, Tech & AI (PETRONAS / YTP MARA / JPA / YTN / Shell / Gamuda)",
            "Medicine, Pharmacy & Health Sciences (JPA / MARA / Yayasan UEM / Sime Darby)",
            "Economics, Business, Fintech & Law (Khazanah / BNM / SC / PayNet)",
            "Education & Teaching (PISMP KPM)",
            "TVET, Skills & Vocational (PTPK / MARA / ILP / Community Colleges)",
            "Media, Design, Communication & Social Sciences (Star/Sin Chew / IPTS Merit Waivers)",
            "General Studies / Any Course (PTPTN / State Foundation Grants)"
        ],
        "main_header": "Comprehensive Malaysia 2026 Funding Matcher",
        "matching_for": "System ready to match scholarships, convertible loans, and financial aid for **{course}** ({inst}) for students from **{state}**:",
        "btn_check": "Check All 2026 Scholarship Matches",
        "btn_essay": "Generate B40 Financial Justification Essay Draft",
        "match_found": "Funding Matches Found for Student from {state} ({income})!",
        "essay_title": "Funding Application Essay Draft (Instant AI):",
        "essay_body": "I am a native student from {state} with high aspirations to pursue qualifications in {course} ({inst}). Understanding my family's financial background in the {income} category, this funding is the primary stepping stone that can transform our family's future. With my SPM results of {spm}, I pledge to utilize this sponsorship to become a high-caliber professional who contributes back to the nation and the state of {state}."
    }
}

# Dynamic State Foundations Data Mapping (All 14 States/Territories)
STATE_FOUNDATIONS = {
    "Sabah": {
        "title": "Yayasan Sabah & Bantuan Kerajaan Negeri Sabah (BKNS)",
        "details": "Bantuan Pendaftaran IPT Tunai (RM2,000 ONE-OFF untuk IPTA/IPTS), Biasiswa Kerajaan Negeri Sabah (BKNS), dan Anugerah Biasiswa Cemerlang Negeri Sabah (ABCNS).",
        "eligibility": "Anak jati Sabah / Ibu atau bapa lahir di Sabah."
    },
    "Sarawak": {
        "title": "Yayasan Sarawak & Inisiatif IPT Free Tuition",
        "details": "Biasiswa Pinjaman Anak Sarawak, Bantuan Kemasukan IPT (RM1,200 - RM2,000), serta Program Yuran Percuma IPT (Undergraduate Free Tuition in Swinburne, Curtin, UTS, i-ATS).",
        "eligibility": "Anak anak Sarawak (KPT K / IC Negeri Sarawak)."
    },
    "Perak": {
        "title": "Yayasan Perak (Bantuan Mahasiswa & Biasiswa Kedoktoran)",
        "details": "Bantuan Sara Diri dan Pendaftaran IPT (RM500 - RM1,200) serta Biasiswa Pelajaran Yayasan Perak.",
        "eligibility": "Anak kelahiran Perak atau pemastautin tetap melebihi 10 tahun."
    },
    "Johor": {
        "title": "Yayasan Pelajaran Johor (YPJ)",
        "details": "Skim Bantuan Pendaftaran IPT YPJ, Biasiswa Kenangan Dato' Onn, dan Pinjaman Pelajaran YPJ (Conversion to Scholarship upon First Class Degree).",
        "eligibility": "Anak jati Johor (Kod Kad Pengenalan 01/23/24) / Pemastautin Johor."
    },
    "Selangor": {
        "title": "Yayasan Selangor & Peduli IPT",
        "details": "Hadiah Pengajian IPT (RM1,000 ONE-OFF B40), Biasiswa DUA, dan Pinjaman Boleh Ubah Yayasan Selangor.",
        "eligibility": "Lahir di Selangor atau pemastautin melebihi 10 tahun."
    },
    "Kelantan": {
        "title": "Yayasan Kelantan Darulnaim (YAKIN) & Tabung Bantuan IPT",
        "details": "Pinjaman Boleh Ubah YAKIN dan Bantuan Zakat/Baitulmal Kedatangan IPT.",
        "eligibility": "Anak jati Kelantan."
    },
    "Terengganu": {
        "title": "Yayasan Terengganu (YT)",
        "details": "Biasiswa Skim Anugerah Sarjana Terengganu, Bantuan Persediaan IPT, dan Pinjaman Boleh Ubah YT.",
        "eligibility": "Rakyat Terengganu (Ibu/Bapa lahir Terengganu)."
    },
    "Kedah": {
        "title": "Yayasan Kedah & Lembaga Zakat Negeri Kedah (LZNK)",
        "details": "Bantuan Awal Pengajian IPT LZNK dan Pinjaman Pelajaran Yayasan Kedah.",
        "eligibility": "Anak Negeri Kedah / Bermastautin di Kedah."
    },
    "Pahang": {
        "title": "Yayasan Pahang (YP)",
        "details": "Biasiswa Kecemerlangan Yayasan Pahang, Bantuan Awal IPT, dan Pinjaman Boleh Ubah YP.",
        "eligibility": "Anak jati Pahang."
    },
    "Pulau Pinang": {
        "title": "Tabung Pendidikan Negeri Pulau Pinang (TPNPP) & Penang Future Foundation (PFF)",
        "details": "Biasiswa Penang Future Foundation (Mutiara & Penang Scholar - Up to 100% Tuition + Monthly Stipend).",
        "eligibility": "Anak Pulau Pinang / Lulusan SPM di Penang."
    },
    "Negeri Sembilan": {
        "title": "Yayasan Negeri Sembilan (YNS)",
        "details": "Bantuan Pendaftaran IPTA/IPTS, Biasiswa Anugerah Cemerlang YNS, dan Pinjaman Boleh Ubah.",
        "eligibility": "Anak Negeri Sembilan."
    },
    "Melaka": {
        "title": "Tabung Amanah Pendidikan Negeri Melaka (TAPEM)",
        "details": "Bantuan Pendaftaran Pengajian Tinggi TAPEM dan Pinjaman Pengajian Tinggi Melaka.",
        "eligibility": "Anak kelahiran Melaka."
    },
    "Perlis": {
        "title": "Yayasan Islam Perlis & Majlis Agama Islam Perlis (MAIPs)",
        "details": "Bantuan Biasiswa IPT MAIPs (Khas B40/Asnaf) dan Bantuan Pendaftaran IPT Yayasan Perlis.",
        "eligibility": "Anak Perlis."
    },
    "Wilayah Persekutuan": {
        "title": "Majlis Agama Islam Wilayah Persekutuan (MAIWP) & Yayasan Wilayah Persekutuan",
        "details": "Bantuan Zakat Pendidikan MAIWP (Yuran + Sara Hidup) dan Bantuan Pengajian IPT YWP.",
        "eligibility": "Bermastautin di WP Kuala Lumpur / Putrajaya / Labuan."
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
            🎙️ <b>Voice Accessibility Helper (Blind & Visually Impaired / Pembantu Suara)</b>
        </p>
        <button id="micBtn" onclick="startDictation()" aria-label="Start Voice Input" style="background: #38bdf8; color: #0f172a; border: none; padding: 10px 18px; border-radius: 8px; font-weight: 700; cursor: pointer; margin-right: 10px;">
            🎤 Speak Query (Cakap Soalan)
        </button>
        <button id="speakBtn" onclick="readPageContent()" aria-label="Read Output Aloud" style="background: #a855f7; color: #ffffff; border: none; padding: 10px 18px; border-radius: 8px; font-weight: 700; cursor: pointer;">
            🔊 Read Output Aloud (Dengar Hasil)
        </button>
        <p id="speechStatus" style="color: #94a3b8; font-size: 12px; margin-top: 8px;" role="status" aria-live="polite">Status: Ready / Sedia</p>
    </div>

    <script>
        function startDictation() {{
            if (window.hasOwnProperty('webkitSpeechRecognition') || window.hasOwnProperty('SpeechRecognition')) {{
                var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                var recognition = new SpeechRecognition();
                recognition.continuous = false;
                recognition.interimResults = false;
                recognition.lang = "{'ms-MY' if language_code == 'bm' else 'en-US'}";
                
                document.getElementById('speechStatus').innerText = "Listening... Speak now / Sedia mendengar...";
                recognition.start();

                recognition.onresult = function(e) {{
                    var textResult = e.results[0][0].transcript;
                    document.getElementById('speechStatus').innerText = "Heard / Didengar: " + textResult;
                    window.parent.document.querySelector('textarea[data-testid="stChatInputTextArea"]').value = textResult;
                }};

                recognition.onerror = function(e) {{
                    document.getElementById('speechStatus').innerText = "Error: " + e.error;
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
            var utterThis = new SpeechSynthesisUtterance(contentToRead.substring(0, 1200)); 
            utterThis.lang = "{'ms-MY' if language_code == 'bm' else 'en-US'}";
            synth.speak(utterThis);
            document.getElementById('speechStatus').innerText = "Reading page content aloud...";
        }}
    </script>
    """
    components.html(js_code, height=130)

# -----------------------------------------------------------------------------
# 4. MAIN STREAMLIT APP LOGIC
# -----------------------------------------------------------------------------
# Language Selector
lang_choice = st.sidebar.radio("Bahasa / Language", ["Bahasa Melayu", "English"], index=0)
lang = "bm" if lang_choice == "Bahasa Melayu" else "en"
txt = TRANS[lang]

# Hero Banner
st.markdown(f"""
    <div class="hero-box">
        <h1 class="hero-title">🎓 {txt['hero_title']}</h1>
        <p class="hero-subtitle">{txt['hero_sub']}</p>
    </div>
""", unsafe_allow_html=True)

# Voice Assistant Widget
render_voice_assistant(lang)

# Sidebar Student Profile
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

# -----------------------------------------------------------------------------
# 5. DYNAMIC SCHOLARSHIP MATCHING ENGINE
# -----------------------------------------------------------------------------
if btn_check:
    st.markdown(f"""
        <div aria-live="polite" role="status" style="margin-top: 15px;">
            <h3 style="color: #38bdf8;">✅ {txt['match_found'].format(state=selected_state, income=income_group)}</h3>
        </div>
    """, unsafe_allow_html=True)

    # 1. State-Specific Foundation Card
    st_info = STATE_FOUNDATIONS.get(selected_state, {
        "title": f"Yayasan Negeri {selected_state}",
        "details": "Bantuan Kemasukan IPTA/IPTS, Biasiswa Negeri, dan Insentif Komputer/Laptop.",
        "eligibility": f"Anak negeri kelahiran atau pemastautin {selected_state}."
    })
    
    st.markdown(f"""
    <div class="scholarship-card" tabindex="0">
        <span class="badge-tag">Bantuan Khusus Negeri</span>
        <span class="badge-tag badge-provider">Kerajaan Negeri {selected_state}</span>
        <h3 style="color: #f8fafc; margin-top: 5px;">1. {st_info['title']}</h3>
        <p><b>Jenis Bantuan:</b> {st_info['details']}</p>
        <p><b>Syarat Kelayakan:</b> {st_info['eligibility']}</p>
    </div>
    """, unsafe_allow_html=True)

    # 2. National Universal Schemes (PTPTN & JPA)
    st.markdown("""
    <div class="scholarship-card" tabindex="0">
        <span class="badge-tag">Pembiayaan Persekutuan (Semua Kursus)</span>
        <span class="badge-tag badge-provider">PTPTN & JPA</span>
        <h3 style="color: #f8fafc; margin-top: 5px;">2. Skim PTPTN & Program Biasiswa JPA PIDN / Program Khas B40</h3>
        <p><b>PTPTN Conversion:</b> Pinjaman 100% untuk IPTA & IPTS yang bertukar menjadi <b>BIASISWA PERCUMA 100%</b> sekiranya mendapat Ijazah Sarjana Muda Kelas Pertama.</p>
        <p><b>JPA PIDN / LSPCN:</b> Penajaan Biasiswa Penuh untuk Pengajian Ijazah Pertama di IPTA awam dan IPTS terpilih (UTP/MMU/UNITEN/Sunway/Taylor's).</p>
        <p><b>Program Khas JPA B40:</b> Biasiswa penuh yuran + Elaun Sara Hidup RM800+/bulan + Elaun Laptop bagi pelajar B40 & Luar Bandar.</p>
    </div>
    """, unsafe_allow_html=True)

    # 3. Track-Specific Expanded Schemes
    track_idx = txt["course_options"].index(course_track)

    if track_idx == 0:  # Accounting & Finance
        st.markdown("""
        <div class="scholarship-card" tabindex="0">
            <span class="badge-tag">Sponsorship Perakaunan & Kewangan</span>
            <span class="badge-tag badge-provider">MyPAC / Peneraju / BNM</span>
            <h3 style="color: #f8fafc; margin-top: 5px;">3. MyPAC, Peneraju Profesional, & Biasiswa Kijang BNM</h3>
            <p><b>MyPAC Sponsorship:</b> 100% Penajaan yuran tuition & exam ACCA/CAT/FIA + Elaun Sara Hidup + Asrama di IPTS (Sunway, INTEC, KPTM).</p>
            <p><b>Yayasan Peneraju Perakaunan:</b> Pembiayaan penuh tajaan Bumiputera untuk laluan ACCA / CPA Australia / MICPA.</p>
            <p><b>Biasiswa Kijang / Bank Negara Malaysia:</b> Biasiswa penuh Pengajian Pre-U & Degree Dalam/Luar Negara bagi SPM minima 8A+.</p>
        </div>
        """, unsafe_allow_html=True)

    elif track_idx == 1:  # STEM, Engineering & AI
        st.markdown("""
        <div class="scholarship-card" tabindex="0">
            <span class="badge-tag">Sains, Kejuruteraan & Teknologi AI</span>
            <span class="badge-tag badge-provider">PETRONAS / MARA / YTN / Shell / Gamuda</span>
            <h3 style="color: #f8fafc; margin-top: 5px;">3. PESP PETRONAS, MARA YTP, Tenaga Nasional (YTN), Shell & Gamuda</h3>
            <p><b>PETRONAS Education Sponsorship (PESP):</b> Penajaan Penuh 100% (Universiti Teknologi PETRONAS / IPTA / Overseas) + Laptop + Elaun Sara Hidup + Penempatan Kerjaya.</p>
            <p><b>MARA Young Talent Development Programme (YTP):</b> Pinjaman Boleh Ubah (PBU) MARA untuk persediaan Pre-U dan Degree STEM tempatan/luar negara (Syarat SPM 7A- ke atas).</p>
            <p><b>Yayasan Tenaga Nasional (YTN) & Gamuda Scholarship:</b> Penajaan penuh kursus Kejuruteraan, Computer Science, Data & AI di IPTA & IPTS.</p>
        </div>
        """, unsafe_allow_html=True)

    elif track_idx == 2:  # Medicine & Health
        st.markdown("""
        <div class="scholarship-card" tabindex="0">
            <span class="badge-tag">Perubatan & Sains Kesihatan</span>
            <span class="badge-tag badge-provider">JPA / MARA / Yayasan UEM / Sime Darby</span>
            <h3 style="color: #f8fafc; margin-top: 5px;">3. Biasiswa Perubatan JPA, MARA YTP Medical, Yayasan UEM & Sime Darby</h3>
            <p><b>Program Ijazah Dalam Negara (JPA Medical):</b> Biasiswa penuh pengajian Perubatan, Farmasi & Pergigian di IPTA.</p>
            <p><b>MARA YTP Perubatan:</b> Pinjaman Boleh Ubah pengajian Perubatan tempatan & luar negara bagi pelajar Bumiputera.</p>
            <p><b>Yayasan UEM & Sime Darby:</b> Penajaan ikatan perkhidmatan bagi pengajian Sains Kesihatan & Farmasi di IPTA/IPTS utama.</p>
        </div>
        """, unsafe_allow_html=True)

    elif track_idx == 3:  # Business, Fintech & Law
        st.markdown("""
        <div class="scholarship-card" tabindex="0">
            <span class="badge-tag">Ekonomi, Fintech, Perniagaan & Law</span>
            <span class="badge-tag badge-provider">Yayasan Khazanah / BNM / Securities Commission / PayNet</span>
            <h3 style="color: #f8fafc; margin-top: 5px;">3. Biasiswa Khazanah Global/Watan, SC, & PayNet B40 Tech Fund</h3>
            <p><b>Yayasan Khazanah (Global & Watan):</b> Penajaan biasiswa penuh kepimpinan di universiti terkemuka IPTA/IPTS/Luar Negara.</p>
            <p><b>Securities Commission Malaysia (SC) Scholarship:</b> Biasiswa penuh pengajian Undang-undang, Finance & Fintech.</p>
            <p><b>PayNet B40 Fintech Fund:</b> Biasiswa tajaan penuh khas pelajar B40 yang menceburi bidang Teknologi Maklumat & Kewangan.</p>
        </div>
        """, unsafe_allow_html=True)

    elif track_idx == 4:  # Education & Teaching
        st.markdown("""
        <div class="scholarship-card" tabindex="0">
            <span class="badge-tag">Pendidikan & Perguruan</span>
            <span class="badge-tag badge-provider">KPM (Kementerian Pendidikan Malaysia)</span>
            <h3 style="color: #f8fafc; margin-top: 5px;">3. Biasiswa Perguruan Persekutuan (PISMP KPM)</h3>
            <p><b>Program Ijazah Sarjana Muda Perguruan (PISMP):</b> Pengecualian 100% Yuran Pengajian di Institut Pendidikan Guru (IPG) + Elaun Sara Hidup Bulanan RM430+ + <b>Jaminan Lantikan Pegawai Perkhidmatan Pendidikan (Guru Kerajaan Gred DG41)</b> setelah tamat pengajian.</p>
        </div>
        """, unsafe_allow_html=True)

    elif track_idx == 5:  # TVET & Vocational
        st.markdown("""
        <div class="scholarship-card" tabindex="0">
            <span class="badge-tag">TVET & Vokasional</span>
            <span class="badge-tag badge-provider">PTPK / MARA TVET / ILP</span>
            <h3 style="color: #f8fafc; margin-top: 5px;">3. Pinjaman Latihan Kemahiran PTPK & Bantuan MARA TVET</h3>
            <p><b>Perbadanan Tabung Pembangunan Kemahiran (PTPK):</b> Pembiayaan 100% Yuran Latihan Kemahiran di Pusat Bertauliah Awam/Swasta + Elaun Sara Hidup RM500/bulan + Elaun Pengangkutan.</p>
            <p><b>Syarat Kemasukan:</b> Boleh membaca, menulis dan berminat (Tiada syarat minima kredit SPM A/B required).</p>
        </div>
        """, unsafe_allow_html=True)

    elif track_idx == 6:  # Media & IPTS Waivers
        st.markdown("""
        <div class="scholarship-card" tabindex="0">
            <span class="badge-tag">Media, Seni & IPTS Waivers</span>
            <span class="badge-tag badge-provider">Sin Chew / Star Education Fund / IPTS Merit</span>
            <h3 style="color: #f8fafc; margin-top: 5px;">3. Sin Chew Daily, Star Education Fund & IPTS Merit Scholarships</h3>
            <p><b>Sin Chew / Star Education Fund:</b> Pengecualian Yuran Pengajian Swasta 50% hingga 100% di Taylor's, Sunway, APU, UTAR, MMU, Monash Malaysia & Curtin.</p>
            <p><b>IPTS SPM Merit Discount:</b> Pengecualian yuran automatik mengikut jumlah A SPM (e.g., 5A = 30%, 7A = 50%, 9A = 100% Full Waiver).</p>
        </div>
        """, unsafe_allow_html=True)

    else:  # General Studies
        st.markdown("""
        <div class="scholarship-card" tabindex="0">
            <span class="badge-tag">Pembiayaan Am & Zakat</span>
            <span class="badge-tag badge-provider">Zakat Negeri & NGO</span>
            <h3 style="color: #f8fafc; margin-top: 5px;">3. Skim Bantuan Zakat Pendidikan IPT & Bantuan Dermasiswa</h3>
            <p><b>Zakat Pendidikan (Asnaf/B40):</b> Bantuan sara hidup bulanan + yuran pendaftaran penuh melalui Agensi Zakat Negeri masing-masing.</p>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. ESSAY DRAFT GENERATOR & CHAT BOT
# -----------------------------------------------------------------------------
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

# Chat Assistant Box
st.markdown("---")
user_query = st.chat_input("Taip atau sebut soalan anda (cth: Apakah biasiswa perubatan atau kejuruteraan IPTA/IPTS yang sesuai untuk saya?)...")

if user_query:
    st.chat_message("user").write(user_query)
    with st.chat_message("assistant"):
        st.write(f"**Jawapan SMART-SCHOLAR (Carian 2026):**")
        st.write(f"Bagi soalan anda *'{user_query}'* untuk bidang **{course_track}** ({selected_state}):")
        st.write("1. **Pilihan Utama IPTA:** Tajaan penuh JPA PIDN, MARA YTP, atau PTPTN (Pengecualian Kelas Pertama).")
        st.write("2. **Pilihan Utama IPTS:** Tajaan khas PETRONAS (UTP), Yayasan Peneraju, MyPAC, Biasiswa Sin Chew/Star, dan Diskaun Merit SPM.")
        st.write(f"3. **Inisiatif Negeri {selected_state}:** Sila pastikan anda mendaftar borang bantuan kemasukan awal IPT di bawah **{STATE_FOUNDATIONS.get(selected_state, {}).get('title', 'Yayasan Negeri')}**.")
