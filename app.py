import io
import streamlit as st
from gtts import gTTS
from streamlit_mic_recorder import speech_to_text

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SMART-SCHOLAR 2026 - Malaysia SPM Higher Education Funding Finder",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ACCESSIBILITY CSS STYLING (HIGH CONTRAST & ACCESSIBLE TARGETS) ---
st.markdown("""
    <style>
    .stButton > button {
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        min-height: 50px !important;
    }
    .scholarship-card {
        border: 2px solid #2e6da4;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: #f8f9fa;
    }
    .tag {
        display: inline-block;
        padding: 4px 10px;
        margin-right: 5px;
        border-radius: 5px;
        font-size: 13px;
        font-weight: bold;
    }
    .tag-ipta { background-color: #d1ecf1; color: #0c5460; }
    .tag-ipts { background-color: #fff3cd; color: #856404; }
    .tag-gov { background-color: #d4edda; color: #155724; }
    .tag-corp { background-color: #e2e3e5; color: #383d41; }
    </style>
""", unsafe_allow_html=1)

# --- HELPER FUNCTIONS FOR TEXT-TO-SPEECH ---
def text_to_audio_bytes(text: str, lang: str = "en") -> io.BytesIO:
    """Converts a given text string into an MP3 audio stream using gTTS."""
    tts = gTTS(text=text, lang=lang, slow=False)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp

# --- COMPREHENSIVE 2026 MALAYSIA SCHOLARSHIP & LOAN DATABASE FOR SPM LEAVERS ---
SCHOLARSHIPS_2026 = [
    # 1. Government & Federal Agencies
    {
        "id": "jpa-ppn",
        "title": "JPA Program Penajaan Nasional (PPN) 2026",
        "provider": "Jabatan Perkhidmatan Awam (JPA)",
        "type": "Government Scholarship",
        "institution_scope": "Overseas / Top Global Universities",
        "spm_requirement": "Minimum 9A+ in SPM",
        "coverage": "Full Tuition + Monthly Allowance + Airfare",
        "description": "Sponsorship for top SPM performers to pursue A-Levels or Foundation leading to premier top-ranked universities worldwide.",
        "target_group": "Bumiputera & Non-Bumiputera Top Achievers"
    },
    {
        "id": "jpa-jkpj",
        "title": "JPA Program Khas Jepun, Korea, Perancis & Jerman (JKPJ) 2026",
        "provider": "Jabatan Perkhidmatan Awam (JPA)",
        "type": "Government Scholarship",
        "institution_scope": "Overseas Prep (IPTA / Pre-U Local prior to departure)",
        "spm_requirement": "Minimum 7A-8A in SPM (Including Math, Add Math, Physics)",
        "coverage": "Full Tuition + Living Allowance",
        "description": "Special government sponsorship to prepare SPM leavers for engineering and technical degree programs in Japan, Korea, France, and Germany.",
        "target_group": "STEM & Engineering Students"
    },
    {
        "id": "mara-ytp",
        "title": "MARA Young Talent Development Programme (YTP) 2026",
        "provider": "Majlis Amanah Rakyat (MARA)",
        "type": "Convertible Loan / Scholarship",
        "institution_scope": "Public (IPTA) & Private (IPTS) & Overseas",
        "spm_requirement": "Minimum 7A - 9A in SPM",
        "coverage": "Full Tuition + Monthly Allowance + Hostel",
        "description": "Convertible loan sponsorship for Bumiputera SPM leavers pursuing Pre-U, Diploma, or Foundation leading to top local IPTA, IPTS (e.g., UniKL), or overseas studies.",
        "target_group": "Bumiputera SPM Leavers"
    },
    {
        "id": "ptptn-loan",
        "title": "PTPTN Education Financing Scheme & First Class Exemption",
        "provider": "Perbadanan Tabung Pendidikan Tinggi Nasional",
        "type": "Education Loan / Convertible Scholarship",
        "institution_scope": "Public (IPTA) & Private (IPTS)",
        "spm_requirement": "Pass SPM with 3 Credits (Diploma) / Pass SPM for Foundation",
        "coverage": "RM 4,000 - RM 16,000 per year (Up to 100% for B40)",
        "description": "Malaysia's most accessible higher education financing scheme. Full loan-to-scholarship conversion (100% waiver) is granted if the student graduates with First Class Honors (CGPA 3.50+ / B40 incentive).",
        "target_group": "All Malaysian Students (B40, M40, T20)"
    },
    {
        "id": "ptpk-tvet",
        "title": "PTPK Skills Development Training Loan (TVET)",
        "provider": "Perbadanan Tabung Pembangunan Kemahiran (PTPK)",
        "type": "Government TVET Loan Scheme",
        "institution_scope": "Public & Private TVET Academies / Polytechnics",
        "spm_requirement": "Pass SPM / SPMV",
        "coverage": "Full Training Fees + RM 400-500 Monthly Allowance",
        "description": "Government funding for SPM leavers entering Malaysian Skills Certificate (SKM) and Diploma (DKM) technical/vocational fields.",
        "target_group": "TVET & Vocational Students"
    },

    # 2. Major Corporate Foundations
    {
        "id": "petronas-pesp",
        "title": "PETRONAS Education Sponsorship Programme (PESP) 2026",
        "provider": "PETRONAS",
        "type": "Corporate Scholarship",
        "institution_scope": "Universiti Teknologi PETRONAS (UTP) & Top Overseas",
        "spm_requirement": "Minimum 8A in SPM",
        "coverage": "Full Tuition + Allowance + Book & Device Allowance",
        "description": "Prestigious corporate scholarship for SPM leavers pursuing Engineering, Geosciences, Data Science, and Business at UTP or top overseas universities.",
        "target_group": "High Achievers in STEM & Commercial studies"
    },
    {
        "id": "bnm-kijang",
        "title": "Bank Negara Malaysia Kijang Scholarship 2026",
        "provider": "Bank Negara Malaysia (BNM)",
        "type": "Corporate Scholarship",
        "institution_scope": "Local Pre-U (KTT) & Overseas First Tier Universities",
        "spm_requirement": "Minimum 8A+ in SPM",
        "coverage": "Full Tuition + High Monthly Allowance + Laptop + Career Guarantee",
        "description": "Awarded to Malaysia's most exceptional SPM talents pursuing Economics, Finance, Actuarial Science, Law, Computer Science, and Data Analytics.",
        "target_group": "Top SPM Achievers Nationwide"
    },
    {
        "id": "khazanah-watan",
        "title": "Yayasan Khazanah Global & Watan Scholarship 2026",
        "provider": "Yayasan Khazanah (Khazanah Nasional)",
        "type": "Corporate Scholarship",
        "institution_scope": "Public IPTA & Selected IPTS (e.g. Taylor's, Monash, Sunway)",
        "spm_requirement": "Minimum 8A / 9A in SPM",
        "coverage": "Full Tuition Fees + Living Allowance + Leadership Development",
        "description": "Offers full financial support and structured leadership development for students admitted to local top IPTS or top overseas institutions.",
        "target_group": "High Leadership Potential & Academic Merit"
    },
    {
        "id": "ytm-scholarship",
        "title": "Yayasan TM (YTM) Future Leaders Scholarship 2026",
        "provider": "Yayasan Telekom Malaysia",
        "type": "Corporate Scholarship",
        "institution_scope": "Multimedia University (MMU) & Public IPTA",
        "spm_requirement": "Minimum 6A to 8A in SPM",
        "coverage": "Full Tuition Fees + Monthly Stipend + Hostel + Internship at TM",
        "description": "Sponsors SPM leavers to study Foundation or Diploma in Information Technology, Computer Science, AI, Engineering, and Creative Multimedia.",
        "target_group": "Tech & Multimedia Enthusiasts"
    },
    {
        "id": "shell-scholarship",
        "title": "Shell Malaysia National Scholarship 2026",
        "provider": "Shell Malaysia",
        "type": "Corporate Scholarship",
        "institution_scope": "Local Pre-U & Top Local/Overseas Universities",
        "spm_requirement": "Minimum 8As in SPM",
        "coverage": "Full Tuition + Living Expenses + Internship Opportunities",
        "description": "Full sponsorship for undergraduate studies in Engineering, Data Science, Geosciences, and Renewable Energy.",
        "target_group": "STEM SPM Graduates"
    },
    {
        "id": "yuem-scholarship",
        "title": "Yayasan UEM Global & Local Scholarship 2026",
        "provider": "UEM Group Berhad",
        "type": "Corporate Scholarship",
        "institution_scope": "Kolej Yayasan UEM (KYUEM) & IPTA / IPTS",
        "spm_requirement": "Minimum 7A - 9A in SPM",
        "coverage": "Full Boarding School Fees + Tuition + University Allowance",
        "description": "Covers A-Levels at KYUEM followed by degree studies in Civil Engineering, Mechanical Engineering, IT, Finance, and Business.",
        "target_group": "All Malaysian SPM Leavers"
    },

    # 3. State Foundations & Zakat Funds
    {
        "id": "ypj-johor",
        "title": "Pinjaman Boleh Ubah & Biasiswa Yayasan Pelajaran Johor (YPJ)",
        "provider": "Yayasan Pelajaran Johor",
        "type": "State Convertible Loan / Scholarship",
        "institution_scope": "Public IPTA & Kolej YPJ / IPTS",
        "spm_requirement": "Pass SPM with 5 Credits",
        "coverage": "RM 5,000 - RM 12,000 per year + Early Admission Aid",
        "description": "Financial assistance specifically for Johor-born students pursuing Diploma or Degree studies in public or state-recognized IPTS.",
        "target_group": "Anak Negeri Johor (B40 & M40)"
    },
    {
        "id": "yt-terengganu",
        "title": "Biasiswa / Pinjaman Pelajaran Yayasan Terengganu 2026",
        "provider": "Yayasan Terengganu",
        "type": "State Scholarship & Loan",
        "institution_scope": "Public IPTA & Selected IPTS",
        "spm_requirement": "Minimum 6A - 8A in SPM",
        "coverage": "Full Tuition Fees + Living Allowance + Skim Penyerapan Biasiswa",
        "description": "Sponsorship and convertible loan schemes for Terengganu-born SPM leavers pursuing Foundation, Diploma, and Bachelor Degrees.",
        "target_group": "Anak Negeri Terengganu"
    },
    {
        "id": "zakat-maidam",
        "title": "Bantuan Zakat Pendidikan IPTA/IPTS MAIDAM / LZS",
        "provider": "Majlis Agama Islam Negeri (MAIDAM / LZS / MAIWP)",
        "type": "Islamic Zakat Grant (Non-repayable)",
        "institution_scope": "Public (IPTA) & Private (IPTS)",
        "spm_requirement": "Pass SPM & Admitted into IPTA/IPTS",
        "coverage": "RM 1,000 Initial Registration Aid + Full Yearly Tuition",
        "description": "Direct zakat financial grant for Muslim B40/Asnaf students accepted into Diploma or Degree programs in Malaysia.",
        "target_group": "Muslim B40 & Asnaf Students"
    },

    # 4. Private University Merit Waivers (IPTS)
    {
        "id": "sunway-merit",
        "title": "Sunway University & College SPM Merit Scholarship 2026",
        "provider": "Sunway Education Group",
        "type": "IPTS Merit Tuition Waiver",
        "institution_scope": "Sunway University & Sunway College (IPTS)",
        "spm_requirement": "5A to 9A+ in SPM",
        "coverage": "20% to 100% Full Tuition Fee Waiver",
        "description": "Automatic or application-based tuition waivers for SPM leavers entering Foundation, Pre-U (A-Levels, CIMP, MUFY), or Diploma programs at Sunway.",
        "target_group": "High Achieving SPM Graduates entering IPTS"
    },
    {
        "id": "taylors-merit",
        "title": "Taylor's University College Excellence & Community Scholarship",
        "provider": "Taylor's University (IPTS)",
        "type": "IPTS Tuition Waiver & Scholarship",
        "institution_scope": "Taylor's University & College (IPTS)",
        "spm_requirement": "Minimum 6A to 9A in SPM",
        "coverage": "30% to 100% Tuition Fee Exemption",
        "description": "Scholarships for top SPM graduates enrolled in Taylor's Foundation, Diploma, or American Degree Transfer Programme (ADTP).",
        "target_group": "All SPM Leavers entering Taylor's"
    },
    {
        "id": "apu-merit",
        "title": "Asia Pacific University (APU) Tech Merit Awards 2026",
        "provider": "APU (Asia Pacific University)",
        "type": "IPTS Tuition Waiver",
        "institution_scope": "APU (IPTS)",
        "spm_requirement": "5A to 10A in SPM",
        "coverage": "10% to 100% Tuition Fee Reduction",
        "description": "Merit scholarships for SPM students pursuing Technology, AI, Cybersecurity, Game Development, and Engineering at APU.",
        "target_group": "IT & Tech Enthusiasts"
    },
    {
        "id": "utar-merit",
        "title": "UTAR / Tunku Abdul Rahman University Management Merit Scholarship",
        "provider": "UTAR & TAR UMT",
        "type": "IPTS Tuition Waiver",
        "institution_scope": "UTAR & TAR UMT (IPTS)",
        "spm_requirement": "5A to 9A in SPM",
        "coverage": "up to 100% Tuition Fee Discount",
        "description": "Affordable higher education pathway with generous automatic merit fee waivers based on SPM results.",
        "target_group": "All Malaysian SPM Students"
    }
]

# --- APP HEADER ---
st.title("🎓 SMART-SCHOLAR 2026")
st.subheader("Voice-Accessible Scholarship, Loan & Financing Finder for SPM Leavers")
st.markdown(
    "Welcome to **SMART-SCHOLAR 2026**. This accessible platform connects Malaysian SPM leavers to the latest "
    "**Government Scholarships (JPA, MARA), Corporate Grants (Petronas, BNM, Khazanah), PTPTN/PTPK Loans, State Zakat Funds, "
    "and Private University (IPTS) Merit Waivers**."
)

st.info("♿ **Accessibility Feature**: Use the microphone button to speak your search, or click the audio buttons to hear search results read aloud.")

st.divider()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Filter Funding Options")

scope_filter = st.sidebar.multiselect(
    "Institution Scope",
    options=["Public (IPTA)", "Private (IPTS)", "Overseas Prep", "TVET / Polytechnic"],
    default=[]
)

type_filter = st.sidebar.multiselect(
    "Funding Category",
    options=["Government Scholarship", "Corporate Scholarship", "Convertible Loan / Scholarship", "Education Loan", "IPTS Tuition Waiver", "Islamic Zakat Grant"],
    default=[]
)

st.sidebar.markdown("---")
st.sidebar.caption("SMART-SCHOLAR • Updated for 2026 Malaysia Academic Intake")

# --- VOICE & TEXT INPUT SECTION ---
st.header("1. Speak or Type Your Search Query")

if "search_query" not in st.session_state:
    st.session_state["search_query"] = ""

col1, col2 = st.columns([1, 2])

with col1:
    st.write("🎙️ **Voice Search Input:**")
    st.caption("Click to start speaking (e.g. 'JPA', 'B40', 'Engineering', 'Private University', 'Loan').")
    
    # Audio Recording & Speech Recognition Component
    spoken_text = speech_to_text(
        language='en',
        start_prompt="🔴 Start Recording Voice",
        stop_prompt="⏹️ Stop & Process",
        just_once=True,
        key='voice_input'
    )
    
    if spoken_text:
        st.session_state["search_query"] = spoken_text

with col2:
    st.write("⌨️ **Text Search Input:**")
    user_query = st.text_input(
        label="Type search terms or SPM grades (e.g., '9A', 'Petronas', 'Johor', 'B40', 'Diploma')",
        value=st.session_state["search_query"],
        key="text_query_input"
    )
    st.session_state["search_query"] = user_query

st.divider()

# --- FILTERING LOGIC ---
raw_query = st.session_state["search_query"].strip().lower()

filtered_list = []

for item in SCHOLARSHIPS_2026:
    # 1. Scope filter match
    if scope_filter:
        scope_match = any(s.lower() in item["institution_scope"].lower() or s.lower() in item["description"].lower() for s.lower() in scope_filter)
        if not scope_match:
            continue
            
    # 2. Type filter match
    if type_filter:
        if item["type"] not in type_filter:
            continue
            
    # 3. Query text match
    if raw_query:
        searchable_blob = f"{item['title']} {item['provider']} {item['type']} {item['institution_scope']} {item['spm_requirement']} {item['coverage']} {item['description']} {item['target_group']}".lower()
        if raw_query not in searchable_blob:
            continue
            
    filtered_list.append(item)

# --- DISPLAY RESULTS AND TEXT-TO-SPEECH ---
st.header("2. Matching 2026 Funding Opportunities")

st.write(f"Displaying **{len(filtered_list)}** funding options out of {len(SCHOLARSHIPS_2026)} available schemes.")

if not filtered_list:
    no_results_msg = f"No scholarship or loan scheme found matching '{st.session_state['search_query']}'. Please try adjusting your filters or search terms."
    st.warning(no_results_msg)
    
    # Audio output for empty results
    audio_fp = text_to_audio_bytes(no_results_msg)
    st.audio(audio_fp, format="audio/mp3")

else:
    # Compile Audio Summary for Blind / Visually Impaired Students
    summary_text = f"Found {len(filtered_list)} matching funding opportunities for SPM leavers. "
    for idx, sch in enumerate(filtered_list[:5], 1): # summarize top 5 in overall voice
        summary_text += f"Option {idx}: {sch['title']} provided by {sch['provider']}. Requirement: {sch['spm_requirement']}. Coverage: {sch['coverage']}. "
    
    if len(filtered_list) > 5:
        summary_text += f"And {len(filtered_list) - 5} more options listed below."

    st.subheader("🔊 Voice Summary (For Visually Impaired Students)")
    st.caption("Click play to hear the search results read aloud:")
    audio_stream = text_to_audio_bytes(summary_text)
    st.audio(audio_stream, format="audio/mp3")

    st.markdown("---")

    # Display Individual Result Cards
    for idx, sch in enumerate(filtered_list, 1):
        st.markdown(f"""
        <div class="scholarship-card">
            <h2>{idx}. {sch['title']}</h2>
            <p><strong>Provider:</strong> {sch['provider']}</p>
            <p><strong>Category:</strong> <span class="tag tag-gov">{sch['type']}</span></p>
            <p><strong>Institution Scope:</strong> {sch['institution_scope']}</p>
            <p><strong>SPM Requirement:</strong> 🥇 <code>{sch['spm_requirement']}</code></p>
            <p><strong>Funding Coverage:</strong> 💰 {sch['coverage']}</p>
            <p><strong>Target Group:</strong> {sch['target_group']}</p>
            <p>{sch['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Audio Player for individual scholarship card
        item_speech = (
            f"Option {idx}: {sch['title']}. Provider: {sch['provider']}. "
            f"SPM Requirement: {sch['spm_requirement']}. Coverage: {sch['coverage']}. {sch['description']}"
        )
        item_audio = text_to_audio_bytes(item_speech)
        
        st.audio(item_audio, format="audio/mp3")
        st.markdown("<br>", unsafe_allow_html=True)

# --- FOOTER ---
st.caption("SMART-SCHOLAR 2026 • Inclusive & Accessible Higher Education Financing Portal for SPM Graduates")
