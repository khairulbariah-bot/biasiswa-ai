import streamlit as st

# Set up page layout
st.set_page_config(page_title="BIASISWA-AI", page_icon="🎓", layout="wide")

# App Header
st.title("🎓 BIASISWA-AI (Bantuan Informasi & Akses Biasiswa Pintar)")
st.caption("Platform Biasiswa Pintar Untuk Pelajar B40 & Luar Bandar | SDG 4: Quality Education")

# Sidebar - Student Details Form
st.sidebar.header("📋 Profil Pelajar (Student Profile)")
spm_results = st.sidebar.text_input("Keputusan SPM (e.g., 7A 1B / 5A 2B)", "7A 1B")
income_group = st.sidebar.selectbox("Kategori Pendapatan Isi Rumah", ["B40 (Kurang RM 4,850)", "M40", "T20"])
location = st.sidebar.text_input("Lokasi / Negeri", "Sabah (Keningau)")
interest = st.sidebar.selectbox(
    "Bidang Minat & Laluan", 
    [
        "Perakaunan Profesional (FIA ACCA / ACCA / ICAEW)", 
        "Sains, Teknologi & Kejuruteraan", 
        "TVET & Sijil Kemahiran", 
        "Perubatan & Sains Kesihatan",
        "Pengurusan & Perniagaan"
    ]
)

# Main Interactive Interface
st.subheader("🤖 Pembantu Biasiswa AI & Padanan Skim Pembiayaan")
st.write("Klik butang di bawah untuk menyemak pembiayaan khusus seperti **Yayasan Peneraju, YTP MARA, MyPAC, dan JPA**:")

# Pre-set Query Buttons for Quick Demo
col1, col2 = st.columns(2)
with col1:
    btn_check = st.button("🔍 Semak Padanan Biasiswa & Skim Pembiayaan")
with col2:
    btn_essay = st.button("✍️ Penjana Draf Esei & Justifikasi Kewangan B40")

# Mock Database Logic (Simulating AI Matcher)
if btn_check:
    st.success(f"**Padanan Pembiayaan Ditemui untuk Minat '{interest}' ({income_group}, {location})!**")
    
    st.markdown("""
    ---
    ### 1. Program Sponsorship MyPAC (Professional Accounting for B40)
    * **Penyedia:** Malaysian Professional Accountancy Centre (MyPAC)
    * **Laluan:** CAT / FIA / ACCA Professional Qualification
    * **Syarat SPM:** Minima 5A (A dalam Matematik & Bahasa Inggeris)
    * **Bantuan:** 100% Yuran Pengajian & Peperiksaan ACCA + Asrama + Elaun Bulanan + Program Pembangunan Sahsiah
    * **Khusus B40:** **YA** (Utama kepada pendapatan isi rumah < RM4,850)
    
    ---
    ### 2. Yayasan Peneraju Pembiayaan Profesional (Accounting & Tech)
    * **Penyedia:** Yayasan Peneraju
    * **Syarat SPM:** Minima 5 Kepujian (Termasuk Matematik & BM)
    * **Bantuan:** Yuran penuh, elaun sara hidup, elaun peperiksaan, dan jaminan latihan industri / penempatan kerja
    * **Dokumen Diperlukan:** Slip SPM, Borang Pengesahan Pendapatan / Surat Ketua Kampung
    
    ---
    ### 3. Young Talent Development Programme (YTP MARA)
    * **Penyedia:** Majlis Amanah Rakyat (MARA)
    * **Laluan:** Persediaan / Asasi / Ijazah Pertama (Dalam & Luar Negara)
    * **Syarat SPM:** Minima 7A- (Mengikut bidang kejuruteraan/sains/perakaunan)
    * **Bantuan:** Pinjaman Boleh Ubah (PBU) MARA (Yuran + Elaun Sara Hidup + Tiket Penerbangan)
    
    ---
    ### 4. Biasiswa Program Khas JPA (B40 & Luar Bandar)
    * **Penyedia:** Jabatan Perkhidmatan Awam (JPA)
    * **Syarat SPM:** Minima 5A- (BM & Sejarah Kepujian)
    * **Bantuan:** Yuran Penuh + Elaun Sara Hidup (RM800/bulan) + Elaun Dizitalkom/Laptop
    """)

if btn_essay:
    st.info("✍️ **Draf Esei Permohonan Pembiayaan (Jana AI Instant):**")
    st.write(f"""
    > *"Saya merupakan pelajar SPM dari {location} yang bercita-cita tinggi untuk mengejar kelayakan dalam bidang {interest}. Menginsafi latar belakang keluarga saya dalam kategori {income_group}, pembiayaan daripada pihak **(Yayasan Peneraju / MyPAC / MARA YTP)** adalah pendorong utama yang dapat mengubah garis takdir kewangan keluarga kami. Dengan keputusan SPM {spm_results}, saya berikrar akan memanfaatkan sepenuhnya penajaan ini untuk menjadi profesional berkaliber yang bakal memberi sumbangan bakti kembali kepada komuniti luar bandar."*
    """)

# Chat input line
user_query = st.chat_input("Taip soalan anda di sini (cth: Apakah beza syarat Yayasan Peneraju dan MyPAC for ACCA?)...")

if user_query:
    st.chat_message("user").write(user_query)
    
    # Instant Smart Answer Simulation
    with st.chat_message("assistant"):
        st.write("""
        **Jawapan BIASISWA-AI:**
        
        * **MyPAC:** Fokus khusus kepada **pelajar B40** yang mahu mengambil sijil akauntan bertauliah (ACCA/CAT) dengan bantuan sokongan asrama dan pembinaan sahsiah penuh.
        * **Yayasan Peneraju:** Menawarkan skop lebih luas termasuk perakaunan profesional, sains data, kejuruteraan, dan teknologi, terbuka kepada Bumiputera B40/M40.
        * **Pengesahan Pendapatan:** Jika ibu bapa tiada slip gaji rasmi, kedua-dua penaja menerima **Surat Pengesahan Pendapatan** yang disahkan oleh Ketua Kampung atau Penghulu.
        """)
