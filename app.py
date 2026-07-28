import streamlit as st

# Set up page layout
st.set_page_config(page_title="BIASISWA-AI", page_icon="🎓", layout="wide")

# App Header
st.title("🎓 BIASISWA-AI (Bantuan Informasi & Akses Biasiswa Pintar)")
st.caption("Platform Pembiayaan Pintar Pelbagai Bidang Untuk Pelajar B40 & Luar Bandar | SDG 4: Quality Education")

# Sidebar - Student Details Form
st.sidebar.header("📋 Profil Pelajar (Student Profile)")
spm_results = st.sidebar.text_input("Keputusan SPM (e.g., 5A 2B / 3 Kepujian)", "5A 2B")
income_group = st.sidebar.selectbox("Kategori Pendapatan Isi Rumah", ["B40 (Kurang RM 4,850)", "M40", "T20"])
location = st.sidebar.text_input("Lokasi / Negeri", "Sabah (Keningau)")

# Expanded Course Selector
course_track = st.sidebar.selectbox(
    "Pilih Bidang Pengajian / Laluan Kursus", 
    [
        "Perakaunan Professional", 
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
st.write(f"Sistem sedia memadankan skim pembiayaan khusus bagi **{course_track}**:")

# Pre-set Query Buttons for Quick Demo
col1, col2 = st.columns(2)
with col1:
    btn_check = st.button("🔍 Semak Padanan Skim Pembiayaan Kursus Ini")
with col2:
    btn_essay = st.button("✍️ Penjana Draf Esei & Justifikasi Kewangan B40")

# Mock Database Logic (Simulating Multi-Course Matching)
if btn_check:
    st.success(f"**Padanan Pembiayaan Ditemui bagi Bidang '{course_track}' ({income_group}, {location})!**")
    
    if "Perakaunan" in course_track:
        st.markdown("""
        ---
        ### 1. MyPAC Professional Accounting Sponsorship
        * **Penyedia:** Malaysian Professional Accountancy Centre (MyPAC)
        * **Laluan:** CAT / FIA / ACCA Qualification
        * **Syarat SPM:** Minima 5A (A dalam Matematik & Bahasa Inggeris)
        * **Bantuan:** 100% Yuran Pengajian & Peperiksaan ACCA + Asrama + Elaun Sara Hidup
        
        ---
        ### 2. Yayasan Peneraju Pembiayaan Profesional Perakaunan
        * **Penyedia:** Yayasan Peneraju
        * **Bantuan:** Yuran penuh, elaun sara hidup, elaun peperiksaan & jaminan kerja
        """)
        
    elif "Sains" in course_track or "Perubatan" in course_track:
        st.markdown("""
        ---
        ### 1. MARA Young Talent Development Programme (YTP)
        * **Penyedia:** Majlis Amanah Rakyat (MARA)
        * **Bidang:** Kejuruteraan, Perubatan, Sains Data, Bioteknologi
        * **Syarat SPM:** 7A- hingga 9A (Mengikut kursus)
        * **Bantuan:** Pinjaman Boleh Ubah (PBU) MARA (Yuran + Elaun Sara Hidup + Penerbangan)
        
        ---
        ### 2. Program Khas Biasiswa JPA (B40 & Luar Bandar)
        * **Penyedia:** Jabatan Perkhidmatan Awam (JPA)
        * **Bantuan:** Yuran Penuh + Elaun Sara Hidup (RM800/bulan) + Elaun Dizitalkom/Laptop
        """)
        
    elif "Pendidikan" in course_track:
        st.markdown("""
        ---
        ### 1. Program Ijazah Sarjana Muda Perguruan (PISMP KPM)
        * **Penyedia:** Kementerian Pendidikan Malaysia (KPM)
        * **Syarat SPM:** Minima 5A (Lulus ujian UKCG & temuduga)
        * **Bantuan:** Pengecualian yuran pengajian + Elaun bulanan + **Jaminan Lantikan Guru Kerajaan**
        """)
        
    elif "TVET" in course_track:
        st.markdown("""
        ---
        ### 1. Pinjaman Latihan Kemahiran PTPK (TVET)
        * **Penyedia:** Perbadanan Tabung Pembangunan Kemahiran (PTPK)
        * **Syarat SPM:** Lulus SPM / Boleh membaca & menulis (Tiada syarat minima A)
        * **Bantuan:** Pembiayaan yuran latihan 100% + Elaun sara hidup sehingga RM500/bulan
        """)
        
    else:
        st.markdown("""
        ---
        ### 1. Pembiayaan PTPTN (Pengecualian Biasiswa Ijazah Kelas Pertama)
        * **Penyedia:** PTPTN
        * **Ciri Khusus B40:** Pembiayaan 100% pinjaman + **Tukar menjadi BIASISWA PERCUMA** jika mendapat Ijazah Sarjana Muda Kelas Pertama.
        
        ---
        ### 2. Biasiswa Corporate Zakat / PayNet Fintech Fund
        * **Penyedia:** PayNet & Agensi Zakat
        * **Bantuan:** Penajaan penuh untuk pelajar B40/Asnaf dalam bidang Teknologi & Pengurusan.
        """)

if btn_essay:
    st.info("✍️ **Draf Esei Permohonan Pembiayaan (Jana AI Instant):**")
    st.write(f"""
    > *"Saya merupakan pelajar SPM dari {location} yang bercita-cita tinggi untuk mengejar kelayakan dalam bidang **{course_track}**. Menginsafi latar belakang keluarga saya dalam kategori {income_group}, pembiayaan ini adalah pendorong utama yang dapat mengubah garis takdir kewangan keluarga kami. Dengan keputusan SPM {spm_results}, saya berikrar akan memanfaatkan penajaan ini untuk menjadi profesional berkaliber yang memberi sumbangan bakti kembali kepada komuniti luar bandar."*
    """)

# Chat input line
user_query = st.chat_input("Taip soalan anda di sini (cth: Apakah pembiayaan terbaik untuk TVET atau Kursus Perguruan?)...")

if user_query:
    st.chat_message("user").write(user_query)
    
    with st.chat_message("assistant"):
        st.write("""
        **Jawapan BIASISWA-AI:**
        
        Sistem BIASISWA-AI menyokong pelbagai bidang pengajian:
        1. **TVET / Kemahiran:** Ditaja penuh oleh **PTPK** dan **MARA** tanpa memerlukan gred A yang tinggi.
        2. **Perguruan:** Ditaja penuh melalui program **PISMP KPM** dengan elaun bulanan dan jaminan kerja.
        3. **Perakaunan & Tech:** Ditaja oleh **MyPAC**, **Yayasan Peneraju**, dan **PayNet**.
        4. **Semua Kursus IPTA/IPTS:** Dilindungi oleh **PTPTN** (Boleh bertukar menjadi Biasiswa jika score First Class).
        """)
