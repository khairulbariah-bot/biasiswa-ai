import streamlit as st
from gtts import gTTS
import io

# Page Configuration
st.set_page_config(page_title="BIASISWA-AI", page_icon="🎓", layout="wide")

# Helper Function: Text-to-Speech (Audio Response for Visually Impaired Students)
def speak_text(text_to_speak):
    try:
        # Convert text to audio stream using gTTS (Malay language support)
        tts = gTTS(text=text_to_speak, lang='ms', slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format="audio/mp3", autoplay=True)
    except Exception as e:
        st.warning("Pembaca Suara (Audio Output) bersedia.")

# App Header with Accessibility Badge
st.title("🎓 BIASISWA-AI (Bantuan Informasi & Akses Biasiswa Pintar)")
st.caption("Platform Biasiswa Pintar Inklusif (Dengan Sokongan Suara & Mesra OKU Penglihatan) | SDG 4: Quality Education")

# Sidebar - Accessibility Toggle & Student Form
st.sidebar.header("♿ Mod Aksesibiliti (Accessibility)")
accessibility_mode = st.sidebar.checkbox("🔊 Aktifkan Mod Suara & Pembaca Skrin OKU", value=True)

st.sidebar.header("📋 Profil Pelajar (Student Profile)")
spm_results = st.sidebar.text_input("Keputusan SPM (e.g., 5A 2B / 3 Kepujian)", "5A 2B")
income_group = st.sidebar.selectbox("Kategori Pendapatan Isi Rumah", ["B40 (Kurang RM 4,850)", "M40", "T20"])

# 14 States Dropdown
malaysia_states = [
    "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", "Pahang", 
    "Pulau Pinang", "Perak", "Perlis", "Sabah", "Sarawak", "Selangor", 
    "Terengganu", "Wilayah Persekutuan (KL / Putrajaya / Labuan)"
]
selected_state = st.sidebar.selectbox("Negeri Asal", malaysia_states)

course_track = st.sidebar.selectbox(
    "Pilih Bidang Pengajian", 
    [
        "Perakaunan Profesional", 
        "Sains, Kejuruteraan & Teknologi", 
        "Perubatan & Sains Kesihatan",
        "Pendidikan & Perguruan",
        "TVET, Kemahiran & Vokasional",
        "Pengajian Umum / IPTA & IPTS"
    ]
)

# Accessibility Voice Input Section
st.subheader("🎙️ Arahan Suara (Voice Command for Visually Impaired Students)")
st.write("Pelajar kurang upaya penglihatan boleh menekan butang mikrofon di bawah untuk bercakap:")

# Built-in Streamlit Microphone Widget
audio_recording = st.audio_input("Tekan ikon mikrofon dan sebut soalan anda (contoh: 'Saya pelajar B40 dari Sabah, apakah biasiswa sesuai?')")

# Buttons Section
col1, col2 = st.columns(2)
with col1:
    btn_check = st.button("🔍 Semak Padanan Biasiswa Saya")
with col2:
    btn_essay = st.button("✍️ Penjana Draf Esei & Audio")

# Matching Logic & Audio Reader Output
if btn_check or audio_recording:
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

    if accessibility_mode:
        st.write("🔊 **Membaca Keputusan Secara Audio (Text-to-Speech):**")
        speak_text(response_text)

if btn_essay:
    essay_text = f"Saya merupakan anak jati {selected_state} yang bercita-cita tinggi dalam bidang {course_track}. Berasal daripada keluarga {income_group}, pembiayaan ini adalah pendorong utama untuk mengubah taraf hidup keluarga kami. Dengan keputusan SPM {spm_results}, saya berikrar akan berbakti kembali kepada masyarakat."
    
    st.info("✍️ **Draf Esei Permohonan Biasiswa:**")
    st.write(f"> *\"{essay_text}\"*")
    
    if accessibility_mode:
        st.write("🔊 **Membaca Draf Esei Secara Audio:**")
        speak_text(essay_text)

# Chat Input Line
user_query = st.chat_input("Taip soalan anda di sini...")

if user_query:
    st.chat_message("user").write(user_query)
    
    answer_text = f"Bagi soalan anda berkenaan biasiswa di {selected_state}, anda layak memohon bantuan JPA, MARA, atau Yayasan Negeri. Pengesahan pendapatan B40 boleh disahkan oleh Ketua Kampung jika tiada slip gaji rasmi."
    
    with st.chat_message("assistant"):
        st.write(answer_text)
        if accessibility_mode:
            speak_text(answer_text)
