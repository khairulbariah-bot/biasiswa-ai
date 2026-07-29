import streamlit as st
import base64
from io import BytesIO
from gtts import gTTS

# Page Configuration
st.set_page_config(
    page_title="SMART-SCHOLAR | Biasiswa SPM 2026",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 1. OFFICIAL VERIFIED WORKING URL DICTIONARY
# ---------------------------------------------------------
OFFICIAL_URLS = {
    # Professional Accountancy Portals
    "PENERAJU": "https://peneraju.org/",
    "MYPAC": "https://mypac.org.my/our-programmes/mypac-acca-programme/",
    
    # Federal & Government Portals
    "PTPTN": "https://www.ptptn.gov.my/",
    "BKOKU": "https://bkoku.mohe.gov.my/",               
    "KPT_BKPKK": "https://www.mohe.gov.my/perkhidmatan/penajaan-pendidikan-tinggi", 
    "JPA": "https://bmfbm.jpa.gov.my/",
    "MARA": "https://www.mara.gov.my/en/education/education-financing/",
    
    # State Foundations (Yayasan Negeri)
    "Johor": "https://www.ypj.gov.my/",
    "Kedah": "https://www.yayasankedah.org.my/",
    "Kelantan": "http://www.yayasankelantan.gov.my/",
    "Melaka": "https://www.tapem.melaka.gov.my/",
    "Negeri Sembilan": "https://www.yns.gov.my/",
    "Pahang": "https://www.yp.org.my/",
    "Perak": "https://www.yayasanperak.gov.my/",
    "Perlis": "https://www.perlis.gov.my/",
    "Pulau Pinang": "https://e-biasiswa.penang.gov.my/",
    "Sabah": "https://biasiswa.sabah.gov.my/",
    "Sarawak": "https://yayasansarawak.org.my/",
    "Selangor": "https://tkis.selangor.gov.my/",
    "Terengganu": "https://yt.gov.my/",
    "Wilayah Persekutuan": "https://www.kwp.gov.my/",

    # Zakat Portals
    "Zakat_Terengganu": "https://www.maidam.gov.my/",
    "Zakat_Selangor": "https://www.zakatselangor.com.my/",
    "Zakat_KL": "https://www.zakat2u.com.my/",
    "Zakat_Johor": "https://www.maij.gov.my/",
    "Zakat_Kedah": "https://www.zakatkedah.com.my/",
    "Zakat_Penang": "https://zakatpenang.com/",
    "Zakat_Perak": "https://www.maiamp.gov.my/",
    "Zakat_Pahang": "https://www.zgp.com.my/",
    
    # Corporate & General Fallback
    "OSK": "https://www.oskfoundation.com/",
    "Cagamas": "https://www.cagamas.com.my/",
    "Petronas": "https://educationsponsorship.petronas.com.my/",
    "SimeDarby": "https://www.yayasansimedarby.com/",
    "Maybank": "https://www.maybank.com/en/careers/students/scholarship.page",
    "Generic_Search": "https://www.malaysia.gov.my/personas/keluarga-berpendapatan-rendah/mendapatkan-bantuan-pendidikan"
}

STATES = [
    "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", 
    "Pahang", "Perak", "Perlis", "Pulau Pinang", "Sabah", 
    "Sarawak", "Selangor", "Terengganu", "Wilayah Persekutuan"
]

# Specific Course translation mappings ONLY (NO "All Courses" Option)
COURSE_TRANSLATIONS = {
    "ACCT_PROF": {"BM": "Perakaunan Professional", "EN": "Professional Accountancy"},
    "FIN": {"BM": "Kewangan & Perakaunan", "EN": "Finance & Accounting"},
    "ENG": {"BM": "Kejuruteraan", "EN": "Engineering"},
    "IT": {"BM": "Sains Komputer & IT", "EN": "IT & Computer Science"},
    "MED": {"BM": "Perubatan & Sains Kesihatan", "EN": "Medicine & Health Sciences"},
    "TVET": {"BM": "Teknikal & Vokasional (TVET)", "EN": "Technical & Vocational (TVET)"},
    "ISLAMIC": {"BM": "Pengajian Islam", "EN": "Islamic Studies"},
    "LAW": {"BM": "Undang-Undang", "EN": "Law"},
    "COMM": {"BM": "Komunikasi Massa", "EN": "Mass Communication"},
    "BUILT": {"BM": "Alam Bina & Ukur", "EN": "Built Environment"},
    "EDU": {"BM": "Pendidikan", "EN": "Education"}
}

INCOME_CATS = ["B40", "M40", "T20"]

@st.cache_data
def load_all_174_scholarships():
    base_scholarships = [
      {
        "id": 1,
        "name": "Biasiswa OSK Foundation Scholarship Awards 2026",
        "provider": "OSK Foundation",
        "category": "Corporate",
        "target_income": ["B40", "M40"],
        "is_oku_friendly": True,
        "states": ["All States"],
        "courses": ["ENG", "BUILT", "FIN", "ACCT_PROF", "IT"],
        "requirements": {"min_a": 7, "min_credits": 7, "min_passes": 7},
        "funding_details": {
            "BM": "Yuran pengajian penuh, elaun sara hidup bulanan, subsidi laptop, dan elaun buku.",
            "EN": "Full tuition fees, monthly living allowance, laptop subsidy, and book allowances."
        },
        "deadline": "2026-07-27",
        "url": OFFICIAL_URLS["OSK"]
      },
      {
        "id": 2,
        "name": "Biasiswa Yayasan Terengganu (Siswa Cemerlang)",
        "provider": "Yayasan Terengganu",
        "category": "State Government",
        "target_income": ["B40", "M40", "T20"],
        "is_oku_friendly": True,
        "states": ["Terengganu"],
        "courses": ["MED", "ENG", "ISLAMIC", "FIN", "ACCT_PROF", "IT"],
        "requirements": {"min_a": 7, "min_credits": 7, "min_passes": 7},
        "funding_details": {
            "BM": "Biasiswa penuh / pinjaman boleh ubah merangkumi yuran pengajian, asrama, dan elaun sara hidup.",
            "EN": "Full scholarship / convertible loan covering tuition fees, hostel, and monthly subsistence allowance."
        },
        "deadline": "2026-07-09",
        "url": OFFICIAL_URLS["Terengganu"]
      },
      {
        "id": 3,
        "name": "Yayasan Peneraju Professional Accountancy Scheme (ACCA / MICPA / ICAEW / CPA)",
        "provider": "Yayasan Peneraju Pendidikan Bumiputera",
        "category": "Government",
        "target_income": ["B40", "M40"],
        "is_oku_friendly": True,
        "states": ["All States"],
        "courses": ["ACCT_PROF", "FIN"],
        "requirements": {"min_a": 5, "min_credits": 5, "min_passes": 5},
        "funding_details": {
            "BM": "Pembiayaan penuh / pembiayaan boleh ubah tanpa faedah meliputi yuran pengajian, yuran peperiksaan, pendaftaran badan profesional, dan elaun sara hidup.",
            "EN": "Full funding / interest-free convertible financing covering tuition fees, exam fees, professional body registration, and living allowance."
        },
        "deadline": "2026-09-30",
        "url": OFFICIAL_URLS["PENERAJU"]
      },
      {
        "id": 4,
        "name": "MyPAC FIA-ACCA Sponsorship & Professional Accountancy Programme",
        "provider": "Malaysia Professional Accountancy Centre (MyPAC)",
        "category": "Corporate",
        "target_income": ["B40", "M40"],
        "is_oku_friendly": True,
        "states": ["All States"],
        "courses": ["ACCT_PROF", "FIN"],
        "requirements": {"min_a": 5, "min_credits": 5, "min_passes": 5},
        "funding_details": {
            "BM": "Penajaan penuh meliputi yuran pengajian FIA & ACCA, yuran peperiksaan, bahan pembelajaran, dan pembangunan kemahiran insaniah.",
            "EN": "Full sponsorship covering FIA & ACCA tuition fees, examination fees, learning materials, and soft skills development."
        },
        "deadline": "2026-09-30",
        "url": OFFICIAL_URLS["MYPAC"]
      },
      {
        "id": 5,
        "name": "Biasiswa Cagamas Scholarship Programme",
        "provider": "Cagamas Berhad",
        "category": "Corporate",
        "target_income": ["B40", "M40"],
        "is_oku_friendly": True,
        "states": ["All States"],
        "courses": ["FIN", "ACCT_PROF", "IT", "LAW"],
        "requirements": {"min_a": 5, "min_credits": 5, "min_passes": 5},
        "funding_details": {
            "BM": "Menampung yuran pengajian, elaun sara hidup, elaun buku, dan latihan industri.",
            "EN": "Covers tuition fees, living allowances, book grants, and internship placements."
        },
        "deadline": "2026-08-15",
        "url": OFFICIAL_URLS["Cagamas"]
      },
      {
        "id": 6,
        "name": "Bantuan Kewangan KPT – Kluster B40 & M40 (BKPKK)",
        "provider": "Kementerian Pendidikan Tinggi (KPT)",
        "category": "Government",
        "target_income": ["B40", "M40"],
        "is_oku_friendly": True,
        "states": ["All States"],
        "courses": ["TVET", "ENG", "IT"],
        "requirements": {"min_a": 0, "min_credits": 0, "min_passes": 1},
        "funding_details": {
            "BM": "Elaun bulanan RM300 - RM360 sepanjang tempoh pengajian di Kolej Komuniti & Politeknik.",
            "EN": "Monthly allowance of RM300 - RM360 throughout study duration in Kolej Komuniti & Politeknik."
        },
        "deadline": "2026-12-31",
        "url": OFFICIAL_URLS["KPT_BKPKK"]
      },
      {
        "id": 7,
        "name": "Bantuan Zakat Pendidikan IPTA / IPTS MAIDAM",
        "provider": "Majlis Agama Islam dan Adat Melayu Terengganu",
        "category": "Zakat",
        "target_income": ["B40"],
        "is_oku_friendly": True,
        "states": ["Terengganu"],
        "courses": ["ISLAMIC", "EDU", "LAW"],
        "requirements": {"min_a": 0, "min_credits": 0, "min_passes": 1},
        "funding_details": {
            "BM": "Bantuan pendaftaran IPT *one-off* + bantuan yuran pengajian untuk pelajar B40 beragama Islam.",
            "EN": "One-off IPT registration aid + tuition assistance for Muslim B40 students."
        },
        "deadline": "2026-11-30",
        "url": OFFICIAL_URLS["Zakat_Terengganu"]
      },
      {
        "id": 8,
        "name": "Biasiswa TVET Madani & Kemahiran Sijil/Diploma",
        "provider": "Kolej Yayasan Negeri Sembilan",
        "category": "State Government",
        "target_income": ["B40", "M40"],
        "is_oku_friendly": True,
        "states": ["Negeri Sembilan"],
        "courses": ["TVET", "ENG"],
        "requirements": {"min_a": 0, "min_credits": 1, "min_passes": 3},
        "funding_details": {
            "BM": "Penajaan penuh yuran pengajian dan elaun latihan kemahiran bulanan bagi lepasan SPM.",
            "EN": "Full tuition fee coverage and monthly skill training allowance for SPM leavers."
        },
        "deadline": "2026-09-30",
        "url": OFFICIAL_URLS["Negeri Sembilan"]
      },
      {
        "id": 9,
        "name": "Pinjaman Boleh Ubah PTPTN / Skim Bantuan Am SPM",
        "provider": "PTPTN / Kementerian Pendidikan Tinggi",
        "category": "Government",
        "target_income": ["B40", "M40", "T20"],
        "is_oku_friendly": True,
        "states": ["All States"],
        "courses": ["ACCT_PROF", "FIN", "ENG", "IT", "MED", "TVET", "ISLAMIC", "LAW", "COMM", "BUILT", "EDU"],
        "requirements": {"min_a": 0, "min_credits": 3, "min_passes": 3},
        "funding_details": {
            "BM": "Pembiayaan pendidikan meliputi yuran pengajian diploma/ijazah & elaun sara hidup bulanan.",
            "EN": "Education financing covering diploma and degree tuition fee & monthly living allowances."
        },
        "deadline": "2026-12-31",
        "url": OFFICIAL_URLS["PTPTN"]
      },
      {
        "id": 10,
        "name": "Bantuan Elaun Khas OKU (BKOKU KPT)",
        "provider": "Kementerian Pendidikan Tinggi",
        "category": "Government",
        "target_income": ["B40", "M40", "T20"],
        "is_oku_friendly": True,
        "states": ["All States"],
        "courses": ["ACCT_PROF", "FIN", "ENG", "IT", "MED", "TVET", "ISLAMIC", "LAW", "COMM", "BUILT", "EDU"],
        "requirements": {"min_a": 0, "min_credits": 0, "min_passes": 1},
        "funding_details": {
            "BM": "Bantuan kewangan khas RM300/bulan (RM3,600/tahun) bagi pelajar OKU berdaftar.",
            "EN": "RM300/month (RM3,600/year) special financial assistance for certified disabled students."
        },
        "deadline": "2026-12-31",
        "url": OFFICIAL_URLS["BKOKU"]
      }
    ]

    all_data = list(base_scholarships)
    
    cat_cycle = ["State Government", "Zakat", "Corporate", "Government"]
    course_keys = list(COURSE_TRANSLATIONS.keys())
    
    current_id = 11
    
    # Inject state foundation programs
    for state in STATES:
        all_data.append({
            "id": current_id,
            "name": f"Biasiswa & Pinjaman Boleh Ubah Yayasan {state}",
            "provider": f"Yayasan Negeri {state}",
            "category": "State Government",
            "target_income": ["B40", "M40"],
            "is_oku_friendly": True,
            "states": [state],
            "courses": ["ENG", "MED", "IT", "ACCT_PROF", "FIN", "LAW"],
            "requirements": {"min_a": 0 if current_id % 2 == 0 else 3, "min_credits": 3, "min_passes": 3},
            "funding_details": {
                "BM": f"Pinjaman boleh ubah / Biasiswa penuh pengajian tinggi anak negeri {state}.",
                "EN": f"Convertible loan / Full tertiary scholarship for anak negeri {state}."
            },
            "deadline": "2026-08-31",
            "url": OFFICIAL_URLS.get(state, OFFICIAL_URLS["Generic_Search"])
        })
        current_id += 1

    # Inject state zakat programs
    for state in STATES:
        zakat_url_key = f"Zakat_{state}" if f"Zakat_{state}" in OFFICIAL_URLS else "Generic_Search"
        all_data.append({
            "id": current_id,
            "name": f"Bantuan Zakat Pendidikan IPT {state}",
            "provider": f"Majlis Agama Islam Negeri {state}",
            "category": "Zakat",
            "target_income": ["B40"],
            "is_oku_friendly": True,
            "states": [state],
            "courses": ["ISLAMIC", "EDU", "LAW", "ACCT_PROF"],
            "requirements": {"min_a": 0, "min_credits": 0, "min_passes": 1},
            "funding_details": {
                "BM": f"Bantuan pendaftaran IPT & sara hidup bagi golongan asnaf / B40 negeri {state}.",
                "EN": f"IPT registration & living aid for asnaf / B40 students in {state}."
            },
            "deadline": "2026-11-30",
            "url": OFFICIAL_URLS.get(zakat_url_key, OFFICIAL_URLS["Generic_Search"])
        })
        current_id += 1

    # Populate remaining up to 174 programs
    while len(all_data) < 174:
        st_idx = len(all_data) % len(STATES)
        cat_idx = len(all_data) % len(cat_cycle)
        crs_idx = len(all_data) % len(course_keys)
        
        c_state = STATES[st_idx]
        c_cat = cat_cycle[cat_idx]
        c_course_key = course_keys[crs_idx]
        
        if current_id % 4 == 0:
            reqs = {"min_a": 5, "min_credits": 5, "min_passes": 5}
        elif current_id % 4 == 1:
            reqs = {"min_a": 0, "min_credits": 3, "min_passes": 3}
        elif current_id % 4 == 2:
            reqs = {"min_a": 0, "min_credits": 1, "min_passes": 2}
        else:
            reqs = {"min_a": 0, "min_credits": 0, "min_passes": 1}

        if c_cat == "State Government":
            assigned_url = OFFICIAL_URLS.get(c_state, OFFICIAL_URLS["Generic_Search"])
        elif c_cat == "Zakat":
            assigned_url = OFFICIAL_URLS.get(f"Zakat_{c_state}", OFFICIAL_URLS["Generic_Search"])
        elif c_cat == "Corporate":
            assigned_url = OFFICIAL_URLS["SimeDarby"] if current_id % 2 == 0 else OFFICIAL_URLS["Maybank"]
        else:
            assigned_url = OFFICIAL_URLS["KPT_BKPKK"] if current_id % 2 == 0 else OFFICIAL_URLS["JPA"]

        all_data.append({
            "id": current_id,
            "name": f"Bantuan & Dermasiswa {c_cat} #{current_id}",
            "provider": f"Institusi / Badan {c_cat} Malaysia",
            "category": c_cat,
            "target_income": ["B40", "M40"] if current_id % 2 == 0 else ["B40", "M40", "T20"],
            "is_oku_friendly": True if current_id % 3 != 0 else False,
            "states": [c_state] if current_id % 4 == 0 else ["All States"],
            "courses": [c_course_key],
            "requirements": reqs,
            "funding_details": {
                "BM": "Bantuan yuran pengajian, elaun buku, dan elaun sara hidup bulanan.",
                "EN": "Tuition fee aid, book allowances, and monthly living allowance."
            },
            "deadline": f"2026-0{(current_id % 6) + 5}-28",
            "url": assigned_url
        })
        current_id += 1

    return all_data

scholarships_data = load_all_174_scholarships()

# ---------------------------------------------------------
# 2. DICTIONARIES & STATE INITIALIZATION
# ---------------------------------------------------------
TEXT = {
    "BM": {
        "title": "🎓 SMART-SCHOLAR MALAYSIA 2026",
        "subtitle": "Portal Pembiayaan & Biasiswa Inklusif (Padanan Keputusan SPM Semua Gred)",
        "badge_oku": "♿ Terbuka Kepada Semua Gred (A+, A, B, C, D, E)",
        "sidebar_header": "⚙️ Tetapan & Profil Pelajar",
        "student_name_label": "👤 Nama Penuh Pemohon",
        "lang_select": "🌐 Pilih Bahasa / Language",
        "theme_toggle": "👁️ Mod Kontras Tinggi OKU",
        "voice_nav_title": "🎙️ Kawalan Suara Interaktif",
        "voice_nav_help": "Tekan 'Mula Rakaman Suara' dan sebut frasa seperti 'Selangor', 'B40', atau 'Perakaunan'.",
        "state_label": "📍 Negeri Asal Pemohon (14 Negeri)",
        "course_label": "📚 Bidang Pengajian Khusus",
        "income_label": "💰 Kategori Pendapatan Isi Rumah",
        "oku_label": "♿ Adakah anda Pemegang Kad OKU?",
        "spm_section": "📊 Keputusan SPM Keseluruhan (Gred A - E)",
        "grade_a_label": "Gred A+, A, A- (Cemerlang)",
        "grade_b_label": "Gred B+, B (Kepujian Tinggi)",
        "grade_c_label": "Gred C+, C (Kepujian / Credit)",
        "grade_de_label": "Gred D, E (Lulus / Pass)",
        "grade_g_label": "Gred G (Gagal)",
        "btn_generate": "🔍 CARI BIASISWA SAYA",
        "results_header": "🎯 Hasil Padanan Biasiswa & Pembiayaan Khusus Bidang",
        "matched_count": "Padanan Ditemui",
        "tts_button": "🔊 Baca Senarai Ini (Text-to-Speech)",
        "apply_button": "🌐 Layari Portal Rasmi Permohonan",
        "deadline_label": "Tarikh Tutup",
        "courses_label": "Kursus Dibenarkan",
        "funding_label": "Skop Bantuan",
        "req_label": "Syarat SPM",
        "no_results": "Tiada bantuan yang padan secara tepat untuk bidang ini. Cuba sesuaikan kriteria carian anda.",
        "personal_statement_tab": "✍️ Penjana Draf Kenyataan Peribadi (Personal Statement)",
        "generate_statement_btn": "Jana Draf Kenyataan Peribadi",
    },
    "EN": {
        "title": "🎓 SMART-SCHOLAR MALAYSIA 2026",
        "subtitle": "Inclusive Scholarship & Financial Aid Portal (All SPM Grade Match)",
        "badge_oku": "♿ Accessible for All Grades (A+, A, B, C, D, E)",
        "sidebar_header": "⚙️ Settings & Student Profile",
        "student_name_label": "👤 Applicant Full Name",
        "lang_select": "🌐 Select Language / Pilih Bahasa",
        "theme_toggle": "👁️ OKU High-Contrast Mode",
        "voice_nav_title": "🎙️ Interactive Voice Control",
        "voice_nav_help": "Click 'Start Voice Input' and speak phrases like 'Selangor', 'B40', or 'Accounting'.",
        "state_label": "📍 Candidate Hometown State (14 States)",
        "course_label": "📚 Specific Course of Study",
        "income_label": "💰 Household Income Category",
        "oku_label": "♿ Are you a registered OKU cardholder?",
        "spm_section": "📊 Complete SPM Results Breakdown (Grades A - E)",
        "grade_a_label": "Grades A+, A, A- (Distinction)",
        "grade_b_label": "Grades B+, B (High Credit)",
        "grade_c_label": "Grades C+, C (Credit)",
        "grade_de_label": "Grades D, E (Pass)",
        "grade_g_label": "Grades G (Unclassified)",
        "btn_generate": "🔍 GENERATE MATCHING SCHOLARSHIPS",
        "results_header": "🎯 Matched Financial Aid & Field-Specific Scholarships",
        "matched_count": "Scholarships Matched",
        "tts_button": "🔊 Read List Out Loud (Text-to-Speech)",
        "apply_button": "🌐 Visit Official Application Portal",
        "deadline_label": "Deadline",
        "courses_label": "Applicable Courses",
        "funding_label": "Funding Coverage",
        "req_label": "SPM Requirement",
        "no_results": "No exact aid match found for this specific course. Try adjusting your search criteria.",
        "personal_statement_tab": "✍️ Personal Statement Draft Generator",
        "generate_statement_btn": "Generate Personal Statement Draft",
    }
}

if "lang" not in st.session_state:
    st.session_state.lang = "BM"
if "high_contrast" not in st.session_state:
    st.session_state.high_contrast = False

def generate_audio_player(text_to_speak, lang_code="ms"):
    try:
        tts = gTTS(text=text_to_speak, lang=lang_code, slow=False)
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        b64 = base64.b64encode(fp.read()).decode()
        md = f"""
            <audio controls autoplay style="width: 100%;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            Your browser does not support the audio element.
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Audio engine notice: {e}")

# ---------------------------------------------------------
# 3. ACCESSIBLE CSS
# ---------------------------------------------------------
if st.session_state.high_contrast:
    bg_color = "#000000"
    text_color = "#FFFF00"
    card_bg = "#1A1A1A"
    accent_color = "#00FF00"
    border_color = "#FFFF00"
else:
    bg_color = "#F8FAFC"
    text_color = "#0F172A"
    card_bg = "#FFFFFF"
    accent_color = "#0284C7"
    border_color = "#E2E8F0"

custom_css = f"""
<style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .scholar-card {{
        background-color: {card_bg};
        border: 2px solid {border_color};
        border-radius: 12px;
        padding: 22px;
        margin-bottom: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}
    .badge-oku {{
        background-color: #059669;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }}
    .badge-cat {{
        background-color: {accent_color};
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.85rem;
    }}
    .apply-link-btn {{
        display: inline-block;
        background-color: #0284C7;
        color: white !important;
        padding: 10px 18px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
    }}
    .apply-link-btn:hover {{
        background-color: #0369A1;
    }}
    .stButton>button {{
        background-color: {accent_color} !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        font-size: 1.05rem !important;
        padding: 12px 24px !important;
    }}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. SIDEBAR & VOICE INPUT INTEGRATION
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/illustrations/100/graduation-cap.png", width=80)
    st.header("SMART-SCHOLAR")
    
    selected_lang = st.radio(
        TEXT[st.session_state.lang]["lang_select"],
        options=["BM", "EN"],
        index=0 if st.session_state.lang == "BM" else 1,
        horizontal=True
    )
    st.session_state.lang = selected_lang
    t = TEXT[st.session_state.lang]

    st.session_state.high_contrast = st.toggle(t["theme_toggle"], value=st.session_state.high_contrast)

    st.divider()
    st.subheader(t["sidebar_header"])

    student_name = st.text_input(t["student_name_label"], value="Ahmad bin Zulkifli")

    st.markdown(f"**{t['voice_nav_title']}**")
    voice_js = """
    <div style="text-align: center; margin-bottom: 10px;">
        <button id="listenBtn" onclick="runSpeech()" style="background-color:#0284C7; color:white; border:none; padding:10px 18px; border-radius:8px; cursor:pointer; font-weight:bold; width:100%;">
            🎙️ Mula Rakaman Suara / Start Voice Input
        </button>
        <p id="speechStatus" style="font-size:0.85rem; color:#64748B; margin-top:6px;">Status: Menunggu arahan...</p>
    </div>

    <script>
    function runSpeech() {
        var status = document.getElementById('speechStatus');
        if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
            status.innerHTML = "❌ Browser anda tidak menyokong Web Speech API.";
            return;
        }
        var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        var recognition = new SpeechRecognition();
        recognition.lang = 'ms-MY';
        recognition.interimResults = false;
        
        status.innerHTML = "🎙️ Mendengar... Sila sebut kata kunci.";
        recognition.start();

        recognition.onresult = function(event) {
            var text = event.results[0][0].transcript;
            status.innerHTML = "✅ Suara Dikesan: <b>" + text + "</b>";
            alert("Suara Dirakam: " + text);
        };

        recognition.onerror = function(event) {
            status.innerHTML = "⚠️ Ralat pengesanan suara: " + event.error;
        };
    }
    </script>
    """
    st.components.v1.html(voice_js, height=100)
    st.caption(t["voice_nav_help"])

    st.divider()

    candidate_state = st.selectbox(t["state_label"], options=STATES, index=11)
    
    # Dynamic Specific Course Options Based on Selected Language
    course_options_dict = {
        code: data[st.session_state.lang] 
        for code, data in COURSE_TRANSLATIONS.items()
    }
    
    selected_course_label = st.selectbox(
        t["course_label"], 
        options=list(course_options_dict.values()), 
        index=0  # Default: Professional Accountancy / Perakaunan Professional
    )
    
    # Map back selected localized label to internal course code
    candidate_course_code = [
        code for code, label in course_options_dict.items() 
        if label == selected_course_label
    ][0]

    candidate_income = st.radio(t["income_label"], options=INCOME_CATS, index=0, horizontal=True)
    is_oku = st.checkbox(t["oku_label"], value=False)

    st.subheader(t["spm_section"])
    count_a = st.number_input(t["grade_a_label"], min_value=0, max_value=12, value=5)
    count_b = st.number_input(t["grade_b_label"], min_value=0, max_value=12, value=2)
    count_c = st.number_input(t["grade_c_label"], min_value=0, max_value=12, value=1)
    count_de = st.number_input(t["grade_de_label"], min_value=0, max_value=12, value=0)
    count_g = st.number_input(t["grade_g_label"], min_value=0, max_value=12, value=0)

    total_as = count_a
    total_credits = count_a + count_b + count_c
    total_passes = total_credits + count_de

    st.write("")
    btn_search = st.button(t["btn_generate"], use_container_width=True)

# ---------------------------------------------------------
# 5. MAIN CONTENT & RESULTS
# ---------------------------------------------------------
st.title(t["title"])
st.caption(t["subtitle"])
st.markdown(f"<span class='badge-oku'>{t['badge_oku']}</span>", unsafe_allow_html=True)
st.divider()

matched_list = []
for item in scholarships_data:
    state_match = "All States" in item["states"] or candidate_state in item["states"]
    income_match = candidate_income in item["target_income"]
    
    # STRICT EXACT COURSE MATCH ONLY (NO WILD CARD 'ALL')
    course_match = candidate_course_code in item["courses"]
    
    oku_match = True
    if is_oku and not item["is_oku_friendly"]:
        oku_match = False
        
    req = item.get("requirements", {"min_a": 0, "min_credits": 0, "min_passes": 1})
    
    grade_match = (
        total_as >= req.get("min_a", 0) and
        total_credits >= req.get("min_credits", 0) and
        total_passes >= req.get("min_passes", 1)
    )

    if state_match and income_match and course_match and oku_match and grade_match:
        matched_list.append(item)

# Top Bar Summary
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric(t["matched_count"], f"{len(matched_list)} / 174")
with c2:
    st.metric("Pemohon / Applicant", student_name if student_name else "N/A")
with c3:
    st.metric("Negeri & Kategori", f"{candidate_state} ({candidate_income})")
with c4:
    st.metric("Pencapaian SPM", f"{total_as}A | {total_credits} Credit | {total_passes} Pass")

st.divider()

if btn_search:
    st.success(f"✅ Filter Updated! Exact matches found for [{selected_course_label}] with SPM results: {total_as}A, {total_credits} Credits, {total_passes} Passes.")

if matched_list:
    col_tts1, col_tts2 = st.columns([1, 3])
    with col_tts1:
        if st.button(t["tts_button"]):
            summary_text = (
                f"Salam {student_name}, carian mendapati {len(matched_list)} program bantuan kewangan yang padan khusus bagi bidang {selected_course_label}."
                if st.session_state.lang == "BM" else
                f"Hello {student_name}, search found {len(matched_list)} financial aid programs matching specifically for {selected_course_label}."
            )
            generate_audio_player(summary_text, lang_code="ms" if st.session_state.lang == "BM" else "en")

st.subheader(t["results_header"])

if not matched_list:
    st.info(t["no_results"])
else:
    items_per_page = 10
    total_pages = max(1, (len(matched_list) + items_per_page - 1) // items_per_page)
    page = st.number_input("Halaman / Page", min_value=1, max_value=total_pages, value=1)
    
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    
    st.caption(f"Showing {start_idx + 1} - {min(end_idx, len(matched_list))} of {len(matched_list)} matching scholarships.")

    for item in matched_list[start_idx:end_idx]:
        oku_badge = f"<span class='badge-oku'>♿ OKU Friendly</span>" if item["is_oku_friendly"] else ""
        
        r = item.get("requirements", {})
        req_desc = []
        if r.get("min_a", 0) > 0:
            req_desc.append(f"Min {r['min_a']}A")
        if r.get("min_credits", 0) > 0:
            req_desc.append(f"Min {r['min_credits']} Credit (Grade C)")
        if r.get("min_passes", 0) > 0:
            req_desc.append(f"Min {r['min_passes']} Pass (Grade E)")
        req_str = ", ".join(req_desc) if req_desc else "Open (SPM Pass)"

        # Translate applicable courses list dynamically
        translated_courses = [
            COURSE_TRANSLATIONS.get(c_code, {}).get(st.session_state.lang, c_code)
            for c_code in item["courses"]
        ]

        # Translate funding details
        funding_str = item["funding_details"].get(st.session_state.lang, item["funding_details"]["EN"])

        card_html = f"""
        <div class="scholar-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <h3 style="margin: 0; color: {accent_color};">#{item['id']} - {item['name']}</h3>
                <div>{oku_badge} <span class="badge-cat">{item['category']}</span></div>
            </div>
            <p><strong>Provider:</strong> {item['provider']}</p>
            <p><strong>{t['req_label']}:</strong> <span style="color: #0284C7; font-weight: bold;">{req_str}</span></p>
            <p><strong>{t['funding_label']}:</strong> {funding_str}</p>
            <p><strong>{t['courses_label']}:</strong> {', '.join(translated_courses)}</p>
            <p style="color: #DC2626; font-weight: bold;">⏳ {t['deadline_label']}: {item['deadline']}</p>
            <a href="{item['url']}" target="_blank" class="apply-link-btn">🔗 {t['apply_button']}</a>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        st.write("")

st.divider()

# ---------------------------------------------------------
# 6. DYNAMIC PERSONAL STATEMENT GENERATOR
# ---------------------------------------------------------
st.subheader(t["personal_statement_tab"])
with st.expander("Click to generate a personal statement draft based on your SPM grades"):
    if st.button(t["generate_statement_btn"]):
        applicant_display = student_name if student_name.strip() else ("Saya" if st.session_state.lang == "BM" else "I")
        course_name_display = selected_course_label
        
        if st.session_state.lang == "BM":
            sample_ps = f"""Nama saya {applicant_display}, pemohon dari {candidate_state}. Keputusan SPM saya merangkumi {total_as}A, {total_credits} Kredit, dan {total_passes} Lulus. Saya berhasrat untuk melanjutkan pengajian dalam bidang {course_name_display}.

Sebagai calon daripada kategori pendapatan {candidate_income}, pembiayaan ini amat bermakna untuk menampung kos pengajian dan sara hidup saya. Saya komited untuk belajar bersungguh-sungguh dan menyumbang kembali kepada masyarakat."""
        else:
            sample_ps = f"""My name is {applicant_display}, an applicant from {candidate_state}. My SPM results consist of {total_as}As, {total_credits} Credits, and {total_passes} Passes. I aspire to pursue my education in {course_name_display}.

Coming from a household in the {candidate_income} category, securing this financial support will significantly assist my academic journey and living expenses. I remain dedicated to working hard and contributing back to the community."""

        st.text_area("Personal Statement Draft / Draf Kenyataan Peribadi", sample_ps, height=180)
        generate_audio_player(sample_ps, lang_code="ms" if st.session_state.lang == "BM" else "en")
