import streamlit as st
from gtts import gTTS
import io

# Page Configuration
st.set_page_config(page_title="BIASISWA-AI", page_icon="🎓", layout="wide")

# Sidebar - Language & Accessibility Controls First
st.sidebar.header("🌐 Language / Bahasa")
language = st.sidebar.radio("Select Language / Pilih Bahasa", ["Bahasa Melayu", "English"], index=0)

st.sidebar.header("♿ Accessibility / Aksesibiliti")
accessibility_mode = st.sidebar.checkbox(
    "🔊 Voice Mode & Screen Reader (Mod Suara & Pembaca Skrin)", 
    value=True
)

# Language Dictionary Mapping
is_bm = (language == "Bahasa Melayu")

labels = {
    "title": "🎓 BIASISWA-AI" if is_bm else "🎓 BIASISWA-AI",
    "subtitle": "(Bantuan Informasi & Akses Biasiswa Pintar)" if is_bm else "(Inclusive Smart Scholarship Platform)",
    "profile_header": "📋 Profil Pelajar" if is_bm else "📋 Student Profile",
    "spm_label": "Keputusan SPM (e.g., 5A 2B)" if is_bm else "SPM Results (e.g., 5A 2B)",
    "income_label": "Kategori Pendapatan Isi Rumah" if is_bm else "Household Income Category",
    "state_label": "Negeri Asal" if is_bm else "Home State",
    "course_label": "Pilih Bidang Pengajian" if is_bm else "Select Field of Study",
    "voice_header": "🎙️ Arahan Suara (Voice Input for Visually Impaired)" if is_bm else "🎙️ Voice Command (For Visually Impaired Students)",
    "voice_instructions": "Pelajar kurang upaya penglihatan boleh menekan butang mikrofon di bawah untuk bercakap:" if is_bm else "Visually impaired students can press the microphone icon below to speak:",
    "mic_placeholder": "Tekan ikon mikrofon dan sebut soalan anda..." if is_bm else "Press the mic icon and state your query...",
    "btn_check": "🔍 Semak Padanan Biasiswa" if is_bm else "🔍 Check Scholarship Match",
    "btn_essay": "✍️ Penjana Draf Esei & Audio" if is_bm else "✍️ Generate Essay Draft & Audio",
    "chat_placeholder": "Taip soalan anda di sini..." if is_bm else "Type your query here..."
}

# Helper Function: Text-to-Speech (Dynamic Language Support)
def speak_text(text_to_speak, lang_code):
    try:
        # 'ms' for Bahasa Melayu, 'en' for English
        tts = gTTS(text=text_to_speak, lang=lang_code, slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format="audio/mp3", autoplay=True)
    except Exception as e:
        st.warning("Audio engine ready.")

# App Header
st.title(labels["title"])
st.caption(labels["subtitle"])

# Student Profile Inputs
st.sidebar.header(labels["profile_header"])
spm_results = st.sidebar.text_input(labels["spm_label"], "5A 2B")
income_group = st.sidebar.selectbox(labels["income_label"], ["B40 (< RM 4,850)", "M40", "T20"])

malaysia_states = [
    "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", "Pahang", 
    "Pulau Pinang", "Perak", "Perlis", "Sabah", "Sarawak", "Selangor", 
    "Terengganu", "Wilayah Persekutuan (KL / Putrajaya / Labuan)"
]
selected_state = st.sidebar.selectbox("Negeri / Lokasi Asal", malaysia_states)

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

course_options_en = [
    "Professional Accounting", 
    "Science, Engineering & Tech", 
    "Medicine & Health Sciences",
    "Education & Teaching",
    "TVET & Vocational Skills",
    "IT, AI & Fintech",
    "General Studies / Universities"
]

course_track = st.sidebar.selectbox(labels["course_label"], course_options_bm if is_bm else course_options_en)

# Voice Accessibility Section
st.subheader(labels["voice_header"])
st.write(labels["voice_instructions"])
audio_recording = st.audio_input(labels["mic_placeholder"])

# Interactive Buttons
col1, col2 = st.columns(2)
with col1:
    btn_check = st.button(labels["btn_check"])
with col2:
    btn_essay = st.button(labels["btn_essay"])

# Dynamic Content Matching Logic
lang_code = 'ms' if is_bm else 'en'

if btn_check or audio_recording:
    if is_bm:
        response_text = f"Padanan Biasiswa Ditemui untuk pelajar dari {selected_state} kategori {income_group}. Biasiswa utama termasuk Biasiswa Program Khas JPA, Penajaan Yayasan Peneraju, dan Bantuan Yayasan Negeri {selected_state}."
        st.success(f"**Padanan Pembiayaan Ditemui bagi {selected_state} ({income_group})!**")

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
    else:
        response_text = f"Scholarship matches found for students from {selected_state} under {income_group} category. Primary sponsorships include JPA Special Program, Yayasan Peneraju, and {selected_state} State Foundation grants."
        st.success(f"**Funding Match Found for {selected_state} ({income_group})!**")
        st.markdown(f"""
        ---
        ### 1. State Specific Assistance: {state_foundation}
* **Provider:** State Government {selected_state}
* **Eligibility:** Children born or residing in **{selected_state}**
* **Aid:** IPTA/IPTS admission registration allowance, B40 Special Scholarship, and Computer Assistance Incentive
* **Documents Required:** Identity Card (State Code {selected_state}), SPM Slip, Income Verification Form
""")

if "Certification" in course_track:
st.markdown("""
---
### 2. MyPAC Professional Accounting Sponsorship
* **Provider:** Malaysian Professional Accountancy Centre (MyPAC)
* **Path:** CAT / FIA / ACCA Qualification
* **SPM Requirements:** Minimum 5A (A in Mathematics & English)
* **Aid:** 100% ACCA Tuition & Examination Fees + Dormitory + Living Allowance

---
### 3. Yayasan Peneraju Accounting Professional Financing
* **Provider:** Yayasan Peneraju
* **Grant:** Full fees, living allowance, examination allowance & job guarantee
""")

elif "Science" in course_track or "Medicine" in course_track:
st.markdown("""
---
### 2. MARA Young Talent Development Programme (YTP)
* **Provider:** Majlis Amanah Rakyat (MARA)
* **Fields:** Engineering, Medicine, Data Science, Biotechnology
* **SPM Requirements:** 7A- to 9A (Depending on the course)
* **Grant:** MARA Convertible Loan (PBU) (Fees + Living Allowance + Flight)

---
### 3. JPA Special Scholarship Programme (B40 & Rural)
* **Provider:** Public Service Department (JPA)
* **Grant:** Full Fees + Living Allowance (RM800/month) + Laptop Allowance
""")

elif "Education" in course_track:
st.markdown("""
---
### 2. Bachelor of Teaching Degree Programme (PISMP KPM)
* **Provider:** Ministry of Education Malaysia (KPM)
* **SPM Requirements:** Minimum 5A (Pass UKCG test & interview)
* **Grant:** Tuition fee exemption + Monthly allowance + **Government Teacher Appointment Guarantee**
""")

elif "TVET" in course_track:
st.markdown("""
---
### 2. PTPK Skills Training Loan (TVET)
* **Provider:** Perbadanan Tabung Pembangunan Kemahiran (PTPK)
* **SPM Requirements:** Passed SPM / Can read & write (No minimum requirement A)
* **Grant:** 100% training fee financing + Living allowance up to RM500/month
""")

else:
st.markdown("""
---
### 2. PTPTN Financing (First Class Degree Scholarship Exemption)
* **Provider:** PTPTN
* **B40 Special Features:** 100% loan financing + **Convert to FREE SCHOLARSHIP** if you get a First Class Bachelor's Degree.

---
### 3. Corporate Zakat / PayNet Fintech Fund Scholarship
* **Provider:** PayNet & State Zakat Agency
* **Benefits:** Full sponsorship for B40/Asnaf students in the fields of Technology & Management.
""")

    if accessibility_mode:
        st.write("🔊 **Reading Results Aloud (Text-to-Speech):**" if not is_bm else "🔊 **Membaca Keputusan Secara Audio:**")
        speak_text(response_text, lang_code)

if btn_essay:
    if is_bm:
        essay_text = f"Saya merupakan anak jati {selected_state} yang bercita-cita tinggi dalam bidang {course_track}. Berasal daripada keluarga {income_group}, pembiayaan ini adalah pendorong utama untuk mengubah taraf hidup keluarga kami. Dengan keputusan SPM {spm_results}, saya berikrar akan berbakti kembali kepada masyarakat."
    else:
        essay_text = f"I am a student from {selected_state} with strong aspirations in the field of {course_track}. Coming from a {income_group} household, this scholarship is the key driver to transforming my family's livelihood. With my SPM results of {spm_results}, I pledge to contribute back to society upon graduation."

    st.info("✍️ **Draf Esei Permohonan / Essay Draft:**")
    st.write(f"> *\"{essay_text}\"*")
    
    if accessibility_mode:
        st.write("🔊 **Reading Essay Aloud:**" if not is_bm else "🔊 **Membaca Draf Esei Secara Audio:**")
        speak_text(essay_text, lang_code)

# Chat Input Line
user_query = st.chat_input(labels["chat_placeholder"])

if user_query:
    st.chat_message("user").write(user_query)
    
    if is_bm:
        answer_text = f"Bagi soalan anda berkenaan biasiswa di {selected_state}, anda layak memohon bantuan JPA, MARA, atau Yayasan Negeri. Pengesahan pendapatan B40 boleh disahkan oleh Ketua Kampung jika tiada slip gaji rasmi."
    else:
        answer_text = f"Regarding your query for scholarships in {selected_state}, you are eligible to apply for JPA, MARA, or State Foundation aid. B40 income verification can be endorsed by a Village Head (Ketua Kampung) if formal payslips are unavailable."
        
    with st.chat_message("assistant"):
        st.write(answer_text)
        if accessibility_mode:
            speak_text(answer_text, lang_code)
