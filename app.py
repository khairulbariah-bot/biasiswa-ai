import streamlit as st

# Set up page layout
st.set_page_config(page_title="BIASISWA-AI", page_icon="🎓", layout="wide")

# App Header
st.title("🎓 BIASISWA-AI (Bantuan Informasi & Akses Biasiswa Pintar)")
st.caption("Platform Pembiayaan Pintar Komprehensif IPTA & IPTS Untuk Pelajar B40 & Luar Bandar | SDG 4: Quality Education")

# Sidebar - Student Details Form
st.sidebar.header("📋 Profil Pelajar (Student Profile)")
spm_results = st.sidebar.text_input("Keputusan SPM (e.g., 5A 2B / 7A / 3 Kepujian)", "5A 2B")
income_group = st.sidebar.selectbox("Kategori Pendapatan Isi Rumah", ["B40 (Kurang RM 4,850)", "M40", "T20"])

# 1. 14 States Dropdown
malaysia_states = [
    "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", 
    "Pahang", "Pulau Pinang", "Perak", "Perlis", "Sabah", 
    "Sarawak", "Selangor", "Terengganu", "Wilayah Persekutuan (KL / Putrajaya / Labuan)"
]
selected_state = st.sidebar.selectbox("Negeri Asal Pelajar", malaysia_states)

# 2. Institution Type Selector (IPTA vs IPTS)
inst_type = st.sidebar.radio("Jenis Institusi Sasaran", ["Semua (IPTA & IPTS)", "IPTA (Universiti Awam / Politeknik / IPG)", "IPTS (Universiti / Kolej Swasta)"])

# 3. Expanded Course Track Selector
course_track = st.sidebar.selectbox(
    "Pilih Bidang Pengajian / Laluan Kursus", 
    [
        "Perakaunan Profesional", 
        "Sains, Kejuruteraan & Teknologi", 
        "Perubatan, Farmasi & Sains Kesihatan",
        "Ekonomi, Perakaunan, Kewangan, Fintech & Perniagaan",
        "Pendidikan & Perguruan",
        "TVET, Kemahiran & Vokasional",
        "Media, Seni Reka & Sains Sosial",
        "Pengajian Umum / Mana-mana Kursus IPTA & IPTS"
    ]
)

# Main Interactive Interface
st.subheader("🤖 Pembantu Biasiswa AI & Padanan Skim Pembiayaan Komprehensif")
st.write(f"Sistem sedia memadankan biasiswa, pinjaman, dan pembiayaan bagi **{course_track}** ({inst_type}) untuk pelajar dari **{selected_state}**:")

# Pre-set Query Buttons for Quick Demo
col1, col2 = st.columns(2)
with col1:
    btn_check = st.button("🔍 Semak Semua Padanan Biasiswa & Pembiayaan")
with col2:
    btn_essay = st.button("✍️ Penjana Draf Esei & Justifikasi Kewangan B40")

# Dynamic Matching Logic Based on Selected Criteria
if btn_check:
    st.success(f"**Padanan Pembiayaan Ditemui bagi Pelajar {selected_state} ({income_group})!**")
    
    # State-Specific Foundation Matcher
    state_foundation = f"Yayasan Negeri {selected_state}"
    if selected_state == "Sabah":
        state_foundation = "Yayasan Sabah (Bantuan Tunai Pendaftaran IPT & Biasiswa Kerajaan Negeri Sabah)"
    elif selected_state == "Sarawak":
        state_foundation = "Yayasan Sarawak (Biasiswa Pinjaman Anak Sarawak & Inisiatif IPT Free Tuition)"
    elif selected_state == "Perak":
        state_foundation = "Yayasan Perak (Bantuan Mahasiswa Anak Perak & Biasiswa Kedoktoran)"
    elif selected_state == "Johor":
        state_foundation = "Yayasan Pelajaran Johor (YPJ)"
    elif selected_state == "Selangor":
        state_foundation = "Yayasan Selangor (Biasiswa DUA & Peduli IPT)"
    elif selected_state == "Kelantan":
        state_foundation = "Yayasan Kelantan Darulnaim (YAKIN)"

    st.markdown(f"""
    ---
    ### 1. Bantuan Khusus Negeri: {state_foundation}
    * **Penyedia:** Kerajaan Negeri {selected_state}
    * **Kelayakan:** Anak kelahiran atau bermastautin di **{selected_state}**
    * **Bantuan:** Elaun pendaftaran masuk IPTA/IPTS, Biasiswa Khas B40, dan Insentif Bantuan Komputer / Laptop
    * **Dokumen Diperlukan:** Kad Pengenalan (Kod Negeri {selected_state}), Slip SPM, Borang Pengesahan Pendapatan
    """)

    if "Perakaunan" in course_track:
        st.markdown("""
        ---
       ### 2. MARA Young Talent Development Programme (YTP - Perakaunan Profesional)
        * **Penyedia:** Majlis Amanah Rakyat (MARA)
        * **Laluan:** FIA (Foundation in Accountancy) -> ACCA (Kolej Profesional MARA / IPTS Platinum Partner)
        * **Syarat SPM:** Minima 6A- termasuk Bahasa Inggeris & Matematik
        * **Bantuan:** Pinjaman Boleh Ubah (PBU) MARA (Yuran Penuh + Elaun Sara Hidup)
        
        ---
        ### 3. MyPAC Professional Accounting Sponsorship (IPTS - Sunway/INTEC/KPTM)
        * **Penyedia:** Malaysian Professional Accountancy Centre (MyPAC)
        * **Laluan:** CAT / FIA / ACCA Qualification
        * **Syarat SPM:** Minima 5A (A dalam Matematik & Bahasa Inggeris)
        * **Bantuan:** 100% Yuran Pengajian & Peperiksaan ACCA + Asrama + Elaun Sara Hidup
        
        ---
        ### 4. Yayasan Peneraju Pembiayaan Profesional Perakaunan
        * **Penyedia:** Yayasan Peneraju Bumiputera
        * **Bantuan:** Yuran penuh, elaun sara hidup, elaun peperiksaan & jaminan penempatan kerja
        """)
        
    elif "Sains" in course_track or "Perubatan" in course_track:
        st.markdown("""
        ---
        ### 2. PETRONAS Education Sponsorship (PESP) (IPTA / UTP / Overseas)
        * **Penyedia:** PETRONAS
        * **Syarat SPM:** Minima 8A- mengikut subjek teras
        * **Bantuan:** Penajaan Penuh 100% (Yuran, Elaun Sara Hidup, Laptop, Jaminan Kerjaya PETRONAS)
        
        ---
        ### 3. MARA Young Talent Development Programme (YTP)
        * **Penyedia:** Majlis Amanah Rakyat (MARA)
        * **Syarat SPM:** 7A- hingga 9A (Mengikut kursus)
        * **Bantuan:** Pinjaman Boleh Ubah (PBU) MARA (Yuran + Elaun Sara Hidup + Penerbangan)
        
        ---
        ### 4. Program Khas Biasiswa JPA (B40 & Luar Bandar)
        * **Penyedia:** Jabatan Perkhidmatan Awam (JPA)
        * **Bantuan:** Yuran Penuh + Elaun Sara Hidup (RM800/bulan) + Elaun Laptop
        """)

    elif "Ekonomi" in course_track:
        st.markdown("""
        ---
        ### 2. Biasiswa Kijang Bank Negara Malaysia (BNM)
        * **Penyedia:** Bank Negara Malaysia
        * **Syarat SPM:** Minima 8A+ dalam SPM
        * **Bantuan:** Biasiswa Penuh Pengajian Pre-U & Degree (Dalam & Luar Negara) + Elaun Sara Hidup Premium
        
        ---
        ### 3. Yayasan Khazanah Global / Watan / ACCA Scholarship
        * **Penyedia:** Khazanah Nasional Berhad
        * **Bantuan:** Penajaan penuh bagi universiti terkemuka IPTA/IPTS/Luar Negara + Program Kepimpinan
        """)
        
    elif "Pendidikan" in course_track:
        st.markdown("""
        ---
        ### 2. Biasiswa Perguruan Persekutuan (PISMP KPM)
        * **Penyedia:** Kementerian Pendidikan Malaysia (IPG)
        * **Syarat SPM:** Minima 5A (Lulus ujian UKCG & temuduga)
        * **Bantuan:** Pengecualian yuran pengajian + Elaun bulanan + **Jaminan Lantikan Guru Kerajaan**
        """)
        
    elif "TVET" in course_track:
        st.markdown("""
        ---
        ### 2. Pinjaman Latihan Kemahiran PTPK (TVET Awam & Swasta)
        * **Penyedia:** Perbadanan Tabung Pembangunan Kemahiran (PTPK)
        * **Syarat SPM:** Lulus SPM / Boleh membaca & menulis (Tiada syarat minima A)
        * **Bantuan:** Pembiayaan yuran latihan 100% + Elaun sara hidup sehingga RM500/bulan
        """)

    elif "Media" in course_track:
        st.markdown("""
        ---
        ### 2. Sin Chew Daily / Star Education Fund Waiver (IPTS Swasta)
        * **Penyedia:** Media Groups & Rangkaian Universiti Swasta (Taylor's, Sunway, APU, UTAR, MMU)
        * **Syarat SPM:** 5A hingga 9A dalam SPM
        * **Bantuan:** Pengecualian Yuran Pengajian Swasta 50% hingga 100%
        """)
        
    else:
        st.markdown("""
        ---
        ### 2. Pembiayaan PTPTN (Pengecualian Biasiswa Ijazah Kelas Pertama)
        * **Penyedia:** PTPTN (Terbukti untuk Semua IPTA & IPTS)
        * **Ciri Khusus B40:** Pembiayaan 100% pinjaman + **Tukar menjadi BIASISWA PERCUMA** jika mendapat Ijazah Sarjana Muda Kelas Pertama.
        
        ---
        ### 3. Biasiswa Corporate Zakat / PayNet Fintech Fund
        * **Penyedia:** PayNet & Agensi Zakat
        * **Bantuan:** Penajaan penuh untuk pelajar B40/Asnaf dalam bidang Teknologi & Pengurusan.
        """)

if btn_essay:
    st.info("✍️ **Draf Esei Permohonan Pembiayaan (Jana AI Instant):**")
    st.write(f"""
    > *"Saya merupakan anak jati **{selected_state}** yang bercita-cita tinggi untuk mengejar kelayakan dalam bidang **{course_track}** ({inst_type}). Menginsafi latar belakang keluarga saya dalam kategori {income_group}, pembiayaan ini adalah pendorong utama yang dapat mengubah garis takdir kewangan keluarga kami. Dengan keputusan SPM {spm_results}, saya berikrar akan memanfaatkan penajaan ini untuk menjadi profesional berkaliber yang memberi sumbangan bakti kembali kepada negara dan negeri {selected_state}."*
    """)

# Chat input line
user_query = st.chat_input(f"Taip soalan anda di sini (cth: Apakah pembiayaan IPTS swasta atau IPTA awam yang sesuai untuk saya dari {selected_state}?)...")

if user_query:
    st.chat_message("user").write(user_query)
    
    with st.chat_message("assistant"):
        st.write(f"""
        **Jawapan BIASISWA-AI:**
        
        Bagi pelajar dari negeri **{selected_state}** yang memohon kursus **{course_track}**:
        1. **Universiti Awam (IPTA):** Biasiswa persekutuan utama seperti **JPA, MARA YTP, PISMP KPM, dan PTPTN** menanggung yuran serta sara hidup secara penuh.
        2. **Universiti Swasta (IPTS):** Anda boleh memanfaatkan penajaan khas **Yayasan Peneraju, MyPAC, PETRONAS (UTP), Biasiswa Sin Chew / The Star, serta Skim PTPTN (Loan-to-Scholarship)**.
        3. **Anak Negeri {selected_state}:** Sila pastikan anda membuat permohonan elaun pendaftaran awal IPT melalui **{state_foundation}**.
        """)
