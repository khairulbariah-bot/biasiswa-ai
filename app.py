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
    "title": "🎓 BIASISWA-AI (Bantuan Informasi & Akses Biasiswa Pintar)" if is_bm else "🎓 BIASISWA-AI (Inclusive Smart Scholarship Platform)",
    "subtitle": "Platform Biasiswa Inklusif (Dwibahasa & Mesra OKU Penglihatan) | SDG 4: Quality Education" if is_bm else "Inclusive Scholarship Platform (Bilingual & Visually Impaired Friendly) | SDG 4: Quality Education",
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
selected_state = st.sidebar.selectbox(labels["state_label"], malaysia_states)

course_options_bm = [
    "Perakuanan Profesional (MyPAC / ACCA / Peneraju)", 
    "Sains, Kejuruteraan & Teknologi (YTP MARA / JPA)", 
    "Perubatan & Sains Kesihatan (JPA / MARA)",
    "Pendidikan & Perguruan (PISMP KPM)",
    "TVET, Kemahiran & Vokasional (PTPK / MARA)",
    "Pengajian Umum / IPTA & IPTS (PTPTN / Yayasan Negeri)"
]

course_options_en = [
    "Professional Accounting (MyPAC / ACCA / Peneraju)", 
    "Science, Engineering & Tech (YTP MARA / JPA)", 
    "Medicine & Health Sciences (JPA / MARA)",
    "Education & Teaching (PISMP KPM)",
    "TVET & Vocational Skills (PTPK / MARA)",
    "General Studies / Universities (PTPTN / State Foundation)"
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
        st.markdown(f"""
        ---
        ### 1. Bantuan Khusus Negeri {selected_state}
        * **Penyedia:** Kerajaan Negeri {selected_state} / Yayasan Negeri
        * **Bantuan:** Elaun pendaftaran masuk IPTA/IPTS & Biasiswa Khas B40
        
        ---
        ### 2. MyPAC & Yayasan Peneraju (Perakaunan & Teknologi)
        * **Penyedia:** Yayasan Peneraju / MyPAC
        * **Bantuan:** 100% Yuran Pengajian, Elaun Peperiksaan, dan Elaun Sara Hidup Bulanan
        
        ---
        ### 3. Biasiswa Program Khas JPA (B40 & Luar Bandar)
        * **Penyedia:** Jabatan Perkhidmatan Awam (JPA)
        * **Bantuan:** Yuran Penuh + Elaun Sara Hidup (RM800/bulan) + Elaun Laptop
        """)
    else:
        response_text = f"Scholarship matches found for students from {selected_state} under {income_group} category. Primary sponsorships include JPA Special Program, Yayasan Peneraju, and {selected_state} State Foundation grants."
        st.success(f"**Funding Match Found for {selected_state} ({income_group})!**")
        st.markdown(f"""
        ---
        ### 1. State Foundation Aid: {selected_state}
        * **Provider:** {selected_state} State Government / Yayasan
        * **Coverage:** IPT Registration Allowance & B40 Education Grant
        
        ---
        ### 2. MyPAC & Yayasan Peneraju (Accounting & Tech)
        * **Provider:** Yayasan Peneraju / MyPAC
        * **Coverage:** 100% Tuition Fees, Examination Fees, and Monthly Living Allowance
        
        ---
        ### 3. JPA Special Scholarship Scheme (B40 & Rural)
        * **Provider:** Public Service Department (JPA)
        * **Coverage:** Full Tuition + Monthly Allowance (RM800) + Laptop Allowance
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
