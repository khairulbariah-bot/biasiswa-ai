import streamlit as st

# Set up page layout
st.set_page_config(page_title="BIASISWA-AI", page_icon="🎓", layout="wide")

# App Header
st.title("🎓 BIASISWA-AI (Bantuan Informasi & Akses Biasiswa Pintar)")
st.caption("Platform Pembiayaan Pintar Pelbagai Bidang Untuk Pelajar Lepasan SPM")

# Sidebar - Student Details Form
st.sidebar.header("📋 Profil Pelajar (Student Profile)")
spm_results = st.sidebar.text_input("Keputusan SPM (e.g., 5A 2B / 3 Kepujian)", "5A 2B")
income_group = st.sidebar.selectbox("Kategori Pendapatan Isi Rumah", ["B40 (Kurang RM 4,850)", "M40", "T20"])

# 14 States of Malaysia Dropdown Menu
malaysia_states = [
    "Johor",
    "Kedah",
    "Kelantan",
    "Melaka",
    "Negeri Sembilan",
    "Pahang",
    "Pulau Pinang",
    "Perak",
    "Perlis",
    "Sabah",
    "Sarawak",
    "Selangor",
    "Terengganu",
    "Wilayah Persekutuan (KL / Putrajaya / Labuan)"
]

selected_state = st.sidebar.selectbox("Negeri / Lokasi Asal", malaysia_states)

# Course Track Selector
course_track = st.sidebar.selectbox(
    "Pilih Bidang Pengajian / Laluan Kursus", 
    [
        "Perakaunan Profesional", 
        "Sains, Kejuruteraan & Teknologi", 
        "Perubatan & Sains Kesihatan",
        "Pendidikan & Perguruan",
        "TVET, Kemahiran & Vokasional",
        "Teknologi Maklumat, AI & Fintech",
        "Pengajian Umum / IPTA & IPTS"
    ]
)

# Main Interactive Interface
st.subheader("🤖 Pembantu Biasiswa AI & Padanan Skim Pembiayaan Pelbagai Kursus")
st.write(f"Sistem sedia memadankan skim pembiayaan bagi kursus **{course_track}** untuk pelajar dari **{selected_state}**:")

# Pre-set Query Buttons for Quick Demo
col1, col2 = st.columns(2)
with col1:
    btn_check = st.button("🔍 Semak Padanan Skim Pembiayaan")
with col2:
    btn_essay = st.button("✍️ Penjana Draf Esei & Justifikasi Kewangan B40")

# Dynamic Matching Logic Based on Selected State & Course
if btn_check:
    st.success(f"**Padanan Pembiayaan Ditemui bagi {selected_state} ({income_group})!**")
    
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

    st.markdown(f"""
    ---
    ### 1. Bantuan Khusus Negeri: {state_foundation}
    * **Penyedia:** Kerajaan Negeri {selected_state}
    * **Kelayakan:** Anak kelahiran atau bermastautin di **{selected_state}**
    * **Bantuan:** Elaun pendaftaran masuk IPTA/IPTS, Biasiswa Khas B40, dan Insentif Bantuan Komputer
    * **Dokumen Diperlukan:** Kad Pengenalan (Kod Negeri {selected_state}), Slip SPM, Borang Pengesahan Pendapatan
    """)

    if "Perakaunan" in course_track:
        st.markdown("""
        ---
        ### 2. MyPAC Professional Accounting Sponsorship
        * **Penyedia:** Malaysian Professional Accountancy Centre (MyPAC)
        * **Laluan:** CAT / FIA / ACCA Qualification
        * **Syarat SPM:** Minima 5A (A dalam Matematik & Bahasa Inggeris)
        * **Bantuan:** 100% Yuran Pengajian & Peperiksaan ACCA + Asrama + Elaun Sara Hidup
        
        ---
        ### 3. Yayasan Peneraju Pembiayaan Profesional Perakaunan
        * **Penyedia:** Yayasan Peneraju
        * **Bantuan:** Yuran penuh, elaun sara hidup, elaun peperiksaan & jaminan kerja
        """)
        
    elif "Sains" in course_track or "Perubatan" in course_track:
        st.markdown("""
        ---
        ### 2. MARA Young Talent Development Programme (YTP)
        * **Penyedia:** Majlis Amanah Rakyat (MARA)
        * **Bidang:** Kejuruteraan, Perubatan, Sains Data, Bioteknologi
        * **Syarat SPM:** 7A- hingga 9A (Mengikut kursus)
        * **Bantuan:** Pinjaman Boleh Ubah (PBU) MARA (Yuran + Elaun Sara Hidup + Penerbangan)
        
        ---
        ### 3. Program Khas Biasiswa JPA (B40 & Luar Bandar)
        * **Penyedia:** Jabatan Perkhidmatan Awam (JPA)
        * **Bantuan:** Yuran Penuh + Elaun Sara Hidup (RM800/bulan) + Elaun Laptop
        """)
        
    elif "Pendidikan" in course_track:
        st.markdown("""
        ---
        ### 2. Program Ijazah Sarjana Muda Perguruan (PISMP KPM)
        * **Penyedia:** Kementerian Pendidikan Malaysia (KPM)
        * **Syarat SPM:** Minima 5A (Lulus ujian UKCG & temuduga)
        * **Bantuan:** Pengecualian yuran pengajian + Elaun bulanan + **Jaminan Lantikan Guru Kerajaan**
        """)
        
    elif "TVET" in course_track:
        st.markdown("""
        ---
        ### 2. Pinjaman Latihan Kemahiran PTPK (TVET)
        * **Penyedia:** Perbadanan Tabung Pembangunan Kemahiran (PTPK)
        * **Syarat SPM:** Lulus SPM / Boleh membaca & menulis (Tiada syarat minima A)
        * **Bantuan:** Pembiayaan yuran latihan 100% + Elaun sara hidup sehingga RM500/bulan
        """)
        
    else:
        st.markdown("""
        ---
        ### 2. Pembiayaan PTPTN (Pengecualian Biasiswa Ijazah Kelas Pertama)
        * **Penyedia:** PTPTN
        * **Ciri Khusus B40:** Pembiayaan 100% pinjaman + **Tukar menjadi BIASISWA PERCUMA** jika mendapat Ijazah Sarjana Muda Kelas Pertama.
        
        ---
        ### 3. Biasiswa Corporate Zakat / PayNet Fintech Fund
        * **Penyedia:** PayNet & Agensi Zakat Negeri
        * **Bantuan:** Penajaan penuh untuk pelajar B40/Asnaf dalam bidang Teknologi & Pengurusan.
        """)

if btn_essay:
    st.info("✍️ **Draf Esei Permohonan Pembiayaan (Jana AI Instant):**")
    st.write(f"""
    > *"Saya merupakan anak jati **{selected_state}** yang bercita-cita tinggi untuk mengejar kelayakan dalam bidang **{course_track}**. Menginsafi latar belakang keluarga saya dalam kategori {income_group}, pembiayaan ini adalah pendorong utama yang dapat mengubah garis takdir kewangan keluarga kami. Dengan keputusan SPM {spm_results}, saya berikrar akan memanfaatkan penajaan ini untuk menjadi profesional berkaliber yang memberi sumbangan bakti kembali kepada komuniti di {selected_state}."*
    """)

# Chat input line
user_query = st.chat_input(f"Taip soalan anda di sini (cth: Apakah insentif khas biasiswa untuk pelajar dari {selected_state}?)...")

if user_query:
    st.chat_message("user").write(user_query)
    
    with st.chat_message("assistant"):
        st.write(f"""
        **Jawapan BIASISWA-AI:**
        
        Bagi pelajar dari negeri **{selected_state}**:
        1. **Bantuan Kerajaan Negeri:** Anda layak memohon insentif pendaftaran awal IPTA melalui Yayasan Negeri {selected_state}.
        2. **Agensi Persekutuan:** Biasiswa Kebangsaan seperti **JPA, MARA, Yayasan Peneraju, MyPAC, dan PTPTN** terbuka kepada semua pemohon dari {selected_state} mengikut kriteria kelayakan akademik dan pendapatan B40.
        """)
