import streamlit as st

# Set up page layout
st.set_page_config(page_title="BIASISWA-AI", page_icon="🎓", layout="wide")

# App Header
st.title("🎓 BIASISWA-AI (Bantuan Informasi & Akses Biasiswa Pintar)")
st.caption("Platform Biasiswa Pintar Untuk Pelajar B40 & Luar Bandar | SDG 4: Quality Education")

# Sidebar - Student Details Form
st.sidebar.header("📋 Profil Pelajar (Student Profile)")
spm_results = st.sidebar.text_input("Keputusan SPM (e.g., 5A 3B)", "5A 2B")
income_group = st.sidebar.selectbox("Kategori Pendapatan Isi Rumah", ["B40 (Kurang RM 4,850)", "M40", "T20"])
location = st.sidebar.text_input("Lokasi / Negeri", "Sabah (Keningau)")
interest = st.sidebar.selectbox("Bidang Minat", ["Sains & Teknologi / IT", "Pengurusan & Perniagaan", "TVET / Kemahiran", "Perubatan / Sains Kesihatan"])

# Main Interactive Interface
st.subheader("🤖 Pembantu Biasiswa AI")
st.write("Sila pilih jawapan atau taip soalan anda di bawah untuk menyemak padanan biasiswa:")

# Pre-set Query Buttons for Quick Demo
col1, col2 = st.columns(2)
with col1:
    btn_check = st.button("🔍 Semak Padanan Biasiswa Saya")
with col2:
    btn_essay = st.button("✍️ Penjana Draf Esei Biasiswa")

# Mock Database Logic (Simulating AI Matcher)
if btn_check:
    st.success(f"**Padanan Biasiswa Ditemui untuk Pelajar {income_group} dari {location}!**")
    
    st.markdown("""
    ---
    ### 1. Biasiswa Program Khas JPA (B40 & Luar Bandar)
    * **Penyedia:** Jabatan Perkhidmatan Awam (JPA)
    * **Syarat SPM:** Minimum 5A (Termasuk BM & Sejarah)
    * **Bantuan:** Yuran pengajian penuh + Elaun Sara Hidup (RM800/bulan) + Elaun Laptop
    * **Dokumen Diperlukan:** Slip SPM, Pengesahan Pendapatan Ibu Bapa (Borang EA / Surat Ketua Kampung)
    * **Tarikh Tutup:** 30 Jun 2026
    
    ---
    ### 2. Anugerah Pelajaran MARA (Sabah & Sarawak Special Fund)
    * **Penyedia:** MARA
    * **Syarat SPM:** Minimum 3 Kepujian (Credit)
    * **Bantuan:** Pengecualian yuran Diploma/TVET + Elaun Bulanan
    * **Dokumen Diperlukan:** Kad Pengenalan, Surat Pengesahan Pendapatan, Sah Pengesahan
    * **Tarikh Tutup:** 15 Ogos 2026
    """)

if btn_essay:
    st.info("✍️ **Draf Esei Permohonan Biasiswa (Jana AI Instant):**")
    st.write(f"""
    > *"Saya merupakan seorang pelajar SPM dari {location} yang berazam tinggi untuk melanjutkan pelajaran dalam bidang {interest}. Walaupun berasal daripada keluarga berpendapatan {income_group}, cabaran kewangan tidak pernah menghalang semangat saya untuk mencapai keputusan {spm_results} dalam SPM. Biasiswa ini akan menjadi platform utama bagi saya untuk mengubah taraf hidup keluarga serta menyumbang kembali kepada pembangunan komuniti luar bandar melalui kepakaran yang bakal saya timba."*
    """)

# Chat input line
user_query = st.chat_input("Taip soalan anda di sini (cth: Bagaimanakah cara pengesahan pendapatan jika tiada slip gaji?)...")

if user_query:
    st.chat_message("user").write(user_query)
    
    # Instant Smart Answer Simulation
    with st.chat_message("assistant"):
        st.write("""
        **Jawapan BIASISWA-AI:**
        
        Bagi keluarga luar bandar atau B40 yang tiada slip gaji rasmi (bekerja sendiri/petani/nelayan):
        1. Anda boleh mendapatkan **Surat Pengesahan Pendapatan** yang disahkan oleh **Ketua Kampung**, **Penghulu**, atau **Pegawai Pembangunan Masyarakat**.
        2. Sistem BIASISWA-AI boleh menjana draf borang pengesahan pendapatan ini secara automatik untuk dicetak dan ditandatangani.
        """)
