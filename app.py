import streamlit as st
from gtts import gTTS
import io

# Set up page layout
st.set_page_config(page_title="BIASISWA-AI (Accessible)", page_icon="🎓", layout="wide")

# Helper function to convert text to speech audio
def text_to_speech(text, lang_code):
    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp
    except Exception as e:
        return None

# Sidebar - Language Selection & Accessibility Toggle
st.sidebar.header("⚙️ Accessibility & Language / Aksesibiliti & Bahasa")
lang = st.sidebar.radio("🌐 Choose Interface Language / Pilih Bahasa:", ["Bahasa Melayu", "English"])
enable_audio = st.sidebar.checkbox("🔊 Enable Voice Reader (For Blind/Visually Impaired Students)", value=True)

# Language Dictionaries
if lang == "Bahasa Melayu":
    title_text = "🎓 SMART-SCHOLAR"
    caption_text = "Platform Akses Biasiswa"
    profile_header = "📋 Profil Pelajar"
    spm_label = "Keputusan SPM (e.g., 5A 2B / 3 Kepujian)"
    income_label = "Kategori Pendapatan Isi Rumah"
    state_label = "Negeri / Lokasi Asal"
    course_label = "Pilih Bidang Pengajian"
    btn_check_label = "🔍 Semak Padanan Skim Pembiayaan"
    btn_essay_label = "✍️ Penjana Draf Esei & Justifikasi Kewangan"
    audio_lang_code = "ms"
    voice_guide_text = "Sistem membaca maklumat biasiswa secara automatik untuk pembantu suara anda."
else:
    title_text = "🎓 BIASISWA-AI (Accessible Smart Scholarship Assistant)"
    caption_text = "Accessible Financial Scheme Matcher for Visually Impaired & B40 Students | SDG 4 & 10"
    profile_header = "📋 Student Profile"
    spm_label = "SPM Results (e.g., 5A 2B / 3 Credits)"
    income_label = "Household Income Category"
    state_label = "Home State / Location"
    course_label = "Select Field of Study"
    btn_check_label = "🔍 Check Matched Financial Schemes"
    btn_essay_label = "✍️ Generate Essay Draft & B40 Financial Justification"
    audio_lang_code = "en"
    voice_guide_text = "Voice Assistant activated. The system will read matching scholarship details out loud."

# App Header
st.title(title_text)
st.caption(caption_text)

if enable_audio:
    st.info(f"🎙️ **Voice Accessibility Active:** {voice_guide_text}")

# 14 States of Malaysia
malaysia_states = [
    "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", "Pahang", 
    "Pulau Pinang", "Perak", "Perlis", "Sabah", "Sarawak", "Selangor", 
    "Terengganu", "Wilayah Persekutuan (KL / Putrajaya / Labuan)"
]

# Sidebar Student Profile Inputs
st.sidebar.header(profile_header)
spm_results = st.sidebar.text_input(spm_label, "5A 2B")
income_group = st.sidebar.selectbox(income_label, ["B40 (Kurang RM 4,850)", "M40", "T20"])
selected_state = st.sidebar.selectbox(state_label, malaysia_states)

course_options = [
    "Perakuanan Profesional", 
    "Sains, Kejuruteraan & Teknologi", 
    "Perubatan & Sains Kesihatan",
    "Pendidikan & Perguruan",
    "TVET, Kemahiran & Vokasional"
] if lang == "Bahasa Melayu" else [
    "Professional Accounting",
    "Science, Engineering & Tech",
    "Medicine & Health Sciences",
    "Education & Teaching",
    "TVET & Vocational Skills"
]

course_track = st.sidebar.selectbox(course_label, course_options)

# Interactive Interface
st.subheader("🤖 Smart Matcher & Audio Voice Output")

col1, col2 = st.columns(2)
with col1:
    btn_check = st.button(btn_check_label)
with col2:
    btn_essay = st.button(btn_essay_label)

# Dynamic Matching Logic
if btn_check:
    if lang == "Bahasa Melayu":
        match_summary = f"Padanan Pembiayaan Ditemui bagi {selected_state} untuk kategori {income_group}."
        scholarship_detail = (
            f"1. Bantuan Kerajaan Negeri {selected_state}. Biasiswa dan elaun sara hidup bagi anak negeri {selected_state}.\n"
            f"2. Biasiswa Program Khas JPA & Dermaiswa B40. Penajaan penuh yuran pengajian dan elaun bulanan RM800.\n"
            f"3. Skim Yayasan Peneraju dan MyPAC. Penajaan penuh yuran dan peperiksaan untuk bidang {course_track}."
        )
    else:
        match_summary = f"Matching Financial Schemes Found for {selected_state} under {income_group} category."
        scholarship_detail = (
            f"1. State Foundation Support for {selected_state}. Registration allowance and state student aid.\n"
            f"2. JPA B40 Special Scholarship. Full tuition waiver and RM800 monthly living stipend.\n"
            f"3. Yayasan Peneraju & MyPAC Schemes. Full sponsorship for course fees and exams in {course_track}."
        )

    st.success(match_summary)
    st.markdown(scholarship_detail)

    # Audio Output Generation for Blind/Visually Impaired Users
    if enable_audio:
        full_audio_script = f"{match_summary}. {scholarship_detail}"
        audio_file = text_to_speech(full_audio_script, audio_lang_code)
        if audio_file:
            st.write("🔊 **Audio Voice Reader (Listen Now):**")
            st.audio(audio_file, format="audio/mp3")

if btn_essay:
    if lang == "Bahasa Melayu":
        essay_text = f"Saya merupakan anak jati {selected_state} yang berazam tinggi mengejar cita-cita dalam bidang {course_track}. Walaupun berasal daripada keluarga {income_group}, dengan keputusan SPM {spm_results}, saya berikrar akan memanfaatkan biasiswa ini untuk berbakti semula kepada masyarakat."
    else:
        essay_text = f"I am a student from {selected_state} determined to pursue my studies in {course_track}. Coming from a {income_group} household background, securing this scholarship with my SPM result of {spm_results} will allow me to uplift my family and serve the community."

    st.info("✍️ **Generated Personal Statement Draft:**")
    st.write(f"> *\"{essay_text}\"*")

    if enable_audio:
        audio_file = text_to_speech(essay_text, audio_lang_code)
        if audio_file:
            st.write("🔊 **Listen to Generated Essay:**")
            st.audio(audio_file, format="audio/mp3")

# Accessible Chat Input
user_query = st.chat_input("🎤 Type or Use Screen Reader Voice Command to ask a question...")

if user_query:
    st.chat_message("user").write(user_query)
    
    response_text = (
        f"BIASISWA-AI: Biasiswa untuk {selected_state} dan bidang {course_track} merangkumi penajaan penuh yuran, asrama, dan elaun sara hidup."
        if lang == "Bahasa Melayu" else
        f"BIASISWA-AI: Scholarships for {selected_state} in {course_track} include full tuition waivers, hostel accommodation, and living stipends."
    )
    
    with st.chat_message("assistant"):
        st.write(response_text)
        if enable_audio:
            audio_file = text_to_speech(response_text, audio_lang_code)
            if audio_file:
                st.audio(audio_file, format="audio/mp3")
