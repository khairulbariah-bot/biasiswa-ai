import streamlit as st

# Set up page layout
st.set_page_config(
    page_title="BIASISWA-AI / SCHOLARSHIP-AI", 
    layout="wide"
)

# -----------------------------------------------------------------------------
# 1. BILINGUAL DICTIONARY
# -----------------------------------------------------------------------------
TRANS = {
    "bm": {
        "title": "BIASISWA-AI (Bantuan Informasi & Akses Biasiswa Pintar)",
        "caption": "Platform Pembiayaan Pintar Komprehensif IPTA & IPTS Untuk Pelajar B40 & Luar Bandar | SDG 4: Pendidikan Berkualiti",
        "lang_selector": "Pilih Bahasa / Select Language",
        "sidebar_header": "Profil Pelajar",
        "spm_label": "Keputusan SPM (cth: 5A 2B / 7A / 3 Kepujian)",
        "income_label": "Kategori Pendapatan Isi Rumah",
        "state_label": "Negeri Asal Pelajar",
        "inst_label": "Jenis Institusi Sasaran",
        "inst_options": [
            "Semua (IPTA & IPTS)",
            "IPTA (Universiti Awam / Politeknik / IPG)",
            "IPTS (Universiti / Kolej Swasta)"
        ],
        "course_label": "Pilih Bidang Pengajian / Laluan Kursus",
        "course_options": [
            "Perakuanan Profesional (MyPAC / ACCA / Peneraju)",
            "Sains, Kejuruteraan & Teknologi (PETRONAS / YTP MARA / JPA)",
            "Perubatan, Farmasi & Sains Kesihatan (JPA / MARA / BNM)",
            "Ekonomi, Kewangan, Fintech & Perniagaan (BNM / PayNet / Khazanah)",
            "Pendidikan & Perguruan (PISMP KPM)",
            "TVET, Kemahiran & Vokasional (PTPK / MARA / ILP)",
            "Media, Seni Reka & Sains Sosial (Star/Sin Chew / IPTS Waivers)",
            "Pengajian Umum / Mana-mana Kursus IPTA & IPTS (PTPTN / Yayasan Negeri)"
        ],
        "main_header": "Pembantu Biasiswa AI & Padanan Skim Pembiayaan Komprehensif",
        "matching_for": "Sistem sedia memadankan biasiswa, pinjaman, dan pembiayaan bagi **{course}** ({inst}) untuk pelajar dari **{state}**:",
        "btn_check": "Semak Semua Padanan Biasiswa & Pembiayaan",
        "btn_essay": "Penjana Draf Esei & Justifikasi Kewangan B40",
        "match_found": "Padanan Pembiayaan Ditemui bagi Pelajar {state} ({income})!",
        "essay_title": "Draf Esei Permohonan Pembiayaan (Jana AI Instant):",
        "essay_body": "Saya merupakan anak jati {state} yang bercita-cita tinggi untuk mengejar kelayakan dalam bidang {course} ({inst}). Menginsafi latar belakang keluarga saya dalam kategori {income}, pembiayaan ini adalah pendorong utama yang dapat mengubah garis takdir kewangan keluarga kami. Dengan keputusan SPM {spm}, saya berikrar akan memanfaatkan penajaan ini untuk menjadi profesional berkaliber yang memberi sumbangan bakti kembali kepada negara dan negeri {state}.",
        "chat_placeholder": "Taip soalan anda di sini (cth: Apakah pembiayaan IPTS swasta atau IPTA awam yang sesuai untuk saya?)...",
        "chat_ans_title": "Jawapan BIASISWA-AI:",
        "chat_ans_1": "1. **Universiti Awam (IPTA):** Biasiswa persekutuan utama seperti JPA, MARA YTP, PISMP KPM, dan PTPTN menanggung yuran serta sara hidup secara penuh.",
        "chat_ans_2": "2. **Universiti Swasta (IPTS):** Anda boleh memanfaatkan penajaan khas Yayasan Peneraju, MyPAC, PETRONAS (UTP), Biasiswa Sin Chew / The Star, serta Skim PTPTN (Pinjaman ke Biasiswa).",
        "chat_ans_3": "3. **Anak Negeri {state}:** Sila pastikan anda membuat permohonan elaun pendaftaran awal IPT melalui {foundation}."
    },
    "en": {
        "title": "SCHOLARSHIP-AI (Smart Scholarship Information & Access Helper)",
        "caption": "Comprehensive Smart Financing Platform for Public & Private Higher Education for B40 & Rural Students | SDG 4: Quality Education",
        "lang_selector": "Select Language / Pilih Bahasa",
        "sidebar_header": "Student Profile",
        "spm_label": "SPM Results (e.g., 5A 2B / 7A / 3 Credits)",
        "income_label": "Household Income Category",
        "state_label": "Home State",
        "inst_label": "Target Institution Type",
        "inst_options": [
            "All (Public & Private)",
            "Public (Public Universities / Polytechnics / IPG)",
            "Private (Private Universities / Colleges)"
        ],
        "course_label": "Select Field of Study / Course Track",
        "course_options": [
            "Professional Accounting (MyPAC / ACCA / Peneraju)",
            "Science, Engineering & Technology (PETRONAS / YTP MARA / JPA)",
            "Medicine, Pharmacy & Health Sciences (JPA / MARA / BNM)",
            "Economics, Finance, Fintech & Business (BNM / PayNet / Khazanah)",
            "Education & Teaching (PISMP KPM)",
            "TVET, Skills & Vocational (PTPK / MARA / ILP)",
            "Media, Design & Social Sciences (Star/Sin Chew / IPTS Waivers)",
            "General Studies / Any Course (PTPTN / State Foundations)"
        ],
        "main_header": "AI Scholarship Assistant & Comprehensive Funding Matcher",
        "matching_for": "System ready to match scholarships, loans, and funding for **{course}** ({inst}) for students from **{state}**:",
        "btn_check": "Check All Matching Scholarships & Funding",
        "btn_essay": "Generate Application Essay Draft & B40 Financial Justification",
        "match_found": "Funding Matches Found for Student from {state} ({income})!",
        "essay_title": "Funding Application Essay Draft (Instant AI):",
        "essay_body": "I am a native student from {state} with high aspirations to pursue qualifications in {course} ({inst}). Understanding my family's financial background in the {income} category, this funding is the primary stepping stone that can transform our family's future. With my SPM results of {spm}, I pledge to utilize this sponsorship to become a high-caliber professional who contributes back to the nation and the state of {state}.",
        "chat_placeholder": "Type your question here (e.g., What private or public higher education funding is suitable for me?)...",
        "chat_ans_title": "SCHOLARSHIP-AI Answer:",
        "chat_ans_1": "1. **Public Universities:** Major federal scholarships like JPA, MARA YTP, PISMP KPM, and PTPTN fully cover tuition fees and living allowances.",
        "chat_ans_2": "2. **Private Universities:** You can leverage specialized sponsorships such as Yayasan Peneraju, MyPAC, PETRONAS (UTP), Sin Chew / The Star Scholarships, and PTPTN (Loan-to-Scholarship scheme).",
        "chat_ans_3": "3. **Native Student of {state}:** Please ensure you submit an application for early university registration allowances via {foundation}."
    }
}

# -----------------------------------------------------------------------------
# 2. LANGUAGE SELECTOR & ACCESSIBILITY ARIA SETUP
# -----------------------------------------------------------------------------
lang_choice = st.sidebar.radio("Language / Bahasa", ["Bahasa Melayu", "English"], index=0)
lang = "bm" if lang_choice == "Bahasa Melayu" else "en"
txt = TRANS[lang]

# Dynamic State Foundation Mapping
def get_state_foundation(state):
    foundations = {
        "Sabah": "Yayasan Sabah (Bantuan Tunai Pendaftaran IPT & Biasiswa Kerajaan Negeri Sabah)",
        "Sarawak": "Yayasan Sarawak (Biasiswa Pinjaman Anak Sarawak & Inisiatif IPT Free Tuition)",
        "Perak": "Yayasan Perak (Bantuan Mahasiswa Anak Perak & Biasiswa Kedoktoran)",
        "Johor": "Yayasan Pelajaran Johor (YPJ)",
        "Selangor": "Yayasan Selangor (Biasiswa DUA & Peduli IPT)",
        "Kelantan": "Yayasan Kelantan Darulnaim (YAKIN)"
    }
    return foundations.get(state, f"Yayasan Negeri {state}")

# App Header
st.title(txt["title"])
st.caption(txt["caption"])

# Sidebar - Student Profile Form
st.sidebar.markdown(f"## {txt['sidebar_header']}")
spm_results = st.sidebar.text_input(txt["spm_label"], "5A 2B")
income_group = st.sidebar.selectbox(txt["income_label"], ["B40 (Kurang/Below RM 4,850)", "M40", "T20"])

malaysia_states = [
    "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", 
    "Pahang", "Pulau Pinang", "Perak", "Perlis", "Sabah", 
    "Sarawak", "Selangor", "Terengganu", "Wilayah Persekutuan (KL / Putrajaya / Labuan)"
]
selected_state = st.sidebar.selectbox(txt["state_label"], malaysia_states)
inst_type = st.sidebar.radio(txt["inst_label"], txt["inst_options"])
course_track = st.sidebar.selectbox(txt["course_label"], txt["course_options"])

# Main Interactive Interface
st.markdown(f"## {txt['main_header']}")
st.write(txt["matching_for"].format(course=course_track, inst=inst_type, state=selected_state))

# Buttons
col1, col2 = st.columns(2)
with col1:
    btn_check = st.button(txt["btn_check"], use_container_width=True)
with col2:
    btn_essay = st.button(txt["btn_essay"], use_container_width=True)

# -----------------------------------------------------------------------------
# 3. ACCESSIBLE CONTENT CONTAINERS (ARIA-LIVE SUPPORT FOR SCREEN READERS)
# -----------------------------------------------------------------------------
if btn_check:
    state_foundation = get_state_foundation(selected_state)
    
    # Accessible announcement region
    st.markdown(f"""
        <div aria-live="polite" role="status">
            <h3>{txt['match_found'].format(state=selected_state, income=income_group)}</h3>
        </div>
    """, unsafe_allow_html=True)

    # State Scholarship Info
    st.markdown("---")
    st.markdown(f"### 1. Bantuan Khusus / State Assistance: {state_foundation}")
    st.markdown(f"""
    * **Penyedia / Provider:** Kerajaan Negeri {selected_state}
    * **Kelayakan / Eligibility:** Anak kelahiran atau bermastautin di {selected_state}
    * **Bantuan / Benefit:** Elaun pendaftaran, Biasiswa B40, Insentif Peranti / Laptop
    """)

    # Track Specific logic
    track_idx = txt["course_options"].index(course_track)
    
    if track_idx == 0:  # Accounting
        st.markdown("""
        ---
        ### 2. MyPAC Professional Accounting Sponsorship
        * **Penyedia / Provider:** Malaysian Professional Accountancy Centre (MyPAC)
        * **Laluan / Track:** CAT / FIA / ACCA Qualification
        * **Syarat SPM:** Minima 5A (A dalam Matematik & Bahasa Inggeris)
        * **Bantuan:** 100% Yuran Pengajian, Peperiksaan ACCA, Asrama, Elaun Sara Hidup

        ---
        ### 3. Yayasan Peneraju Pembiayaan Profesional Perakaunan
        * **Penyedia / Provider:** Yayasan Peneraju Bumiputera
        * **Bantuan:** Yuran penuh, elaun sara hidup, elaun peperiksaan & jaminan penempatan kerja
        """)

    elif track_idx in [1, 2]:  # Science & Medicine
        st.markdown("""
        ---
        ### 2. PETRONAS Education Sponsorship (PESP)
        * **Penyedia / Provider:** PETRONAS
        * **Syarat SPM:** Minima 8A- mengikut subjek teras
        * **Bantuan:** Penajaan Penuh 100% (Yuran, Elaun Sara Hidup, Laptop, Jaminan Kerjaya)

        ---
        ### 3. MARA Young Talent Development Programme (YTP)
        * **Penyedia / Provider:** Majlis Amanah Rakyat (MARA)
        * **Syarat SPM:** 7A- hingga 9A
        * **Bantuan:** Pinjaman Boleh Ubah (PBU) MARA

        ---
        ### 4. Program Khas Biasiswa JPA (B40 & Luar Bandar)
        * **Penyedia / Provider:** Jabatan Perkhidmatan Awam (JPA)
        * **Bantuan:** Yuran Penuh + Elaun Sara Hidup + Elaun Laptop
        """)

    elif track_idx == 3:  # Finance / Economics
        st.markdown("""
        ---
        ### 2. Biasiswa Kijang Bank Negara Malaysia (BNM)
        * **Penyedia / Provider:** Bank Negara Malaysia
        * **Syarat SPM:** Minima 8A+ dalam SPM
        * **Bantuan:** Biasiswa Penuh Pre-U & Degree + Elaun Sara Hidup

        ---
        ### 3. Yayasan Khazanah Global / Watan / ACCA Scholarship
        * **Penyedia / Provider:** Khazanah Nasional Berhad
        * **Bantuan:** Penajaan penuh bagi universiti terkemuka + Program Kepimpinan
        """)

    elif track_idx == 4:  # Education
        st.markdown("""
        ---
        ### 2. Biasiswa Perguruan Persekutuan (PISMP KPM)
        * **Penyedia / Provider:** Kementerian Pendidikan Malaysia (IPG)
        * **Syarat SPM:** Minima 5A (Lulus ujian UKCG & temuduga)
        * **Bantuan:** Pengecualian yuran + Elaun bulanan + Jaminan Lantikan Guru Kerajaan
        """)

    elif track_idx == 5:  # TVET
        st.markdown("""
        ---
        ### 2. Pinjaman Latihan Kemahiran PTPK
        * **Penyedia / Provider:** Perbadanan Tabung Pembangunan Kemahiran (PTPK)
        * **Syarat SPM:** Lulus SPM / Boleh membaca & menulis
        * **Bantuan:** Pembiayaan yuran latihan 100% + Elaun sara hidup
        """)

    elif track_idx == 6:  # Media
        st.markdown("""
        ---
        ### 2. Sin Chew Daily / Star Education Fund Waiver
        * **Penyedia / Provider:** Media Groups & Rangkaian Universiti Swasta
        * **Syarat SPM:** 5A hingga 9A dalam SPM
        * **Bantuan:** Pengecualian Yuran Pengajian Swasta 50% hingga 100%
        """)

    else:  # General
        st.markdown("""
        ---
        ### 2. Pembiayaan PTPTN (Loan-to-Scholarship Conversion)
        * **Penyedia / Provider:** PTPTN
        * **Ciri Khusus B40:** Pembiayaan 100% pinjaman; ditukar menjadi **BIASISWA PERCUMA** jika mendapat Ijazah Sarjana Muda Kelas Pertama.

        ---
        ### 3. Biasiswa Corporate Zakat / PayNet Fintech Fund
        * **Penyedia / Provider:** PayNet & Agensi Zakat
        * **Bantuan:** Penajaan penuh untuk pelajar B40/Asnaf
        """)

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

# Chat section
st.markdown("---")
user_query = st.chat_input(txt["chat_placeholder"])

if user_query:
    st.chat_message("user").write(user_query)
    
    with st.chat_message("assistant"):
        state_foundation = get_state_foundation(selected_state)
        st.markdown(f"**{txt['chat_ans_title']}**")
        st.markdown(txt["chat_ans_1"])
        st.markdown(txt["chat_ans_2"])
        st.markdown(txt["chat_ans_3"].format(state=selected_state, foundation=state_foundation))
