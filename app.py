import streamlit as st
from datetime import datetime

# ---------- PDF ----------
try:
    from pypdf import PdfReader
    PYPDF_AVAILABLE = True
except ImportError:
    PYPDF_AVAILABLE = False

# ---------- Gemini ----------
try:
    from google import genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False


# ============================================================
# MY LAWYER FRIEND — V1.4
# Premium Indian Legal Information Platform
# ============================================================

st.set_page_config(
    page_title="My Lawyer Friend",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

APP_NAME = "My Lawyer Friend"
APP_VERSION = "1.4"
GEMINI_MODEL = "gemini-2.5-flash"

PAGES = [
    "Home",
    "Explain a Judgment",
    "Legal Q&A",
    "Search Cases",
    "Know Your Rights",
    "History",
    "About",
]


# ============================================================
# SAFE SECRETS
# ============================================================

def get_secret(key, default=""):
    try:
        return st.secrets.get(key, default)
    except Exception:
        return default


GEMINI_API_KEY = get_secret("GEMINI_API_KEY", "")
client = None
if GEMINI_API_KEY and GENAI_AVAILABLE:
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
    except Exception:
        client = None


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"
if "history" not in st.session_state:
    st.session_state.history = []
if st.session_state.page not in PAGES:
    st.session_state.page = "Home"


# ============================================================
# PREMIUM CSS  (image-cards, filters, polish)
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 5% 0%, rgba(99,102,241,.08), transparent 28%),
        radial-gradient(circle at 100% 100%, rgba(245,158,11,.06), transparent 30%),
        #f6f7fb;
}

.block-container {
    max-width: 1280px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #08111f 0%, #0b1220 100%);
    border-right: 1px solid rgba(255,255,255,.05);
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb;
}

section[data-testid="stSidebar"] .stRadio label {
    color: #e5e7eb !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 7px 10px;
    border-radius: 10px;
    transition: background .2s;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,.07);
}

section[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,.10) !important;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    background:
        radial-gradient(circle at 90% 20%, rgba(99,102,241,.35), transparent 30%),
        linear-gradient(135deg, #08111f 0%, #12223e 55%, #214b78 100%);
    border-radius: 28px;
    padding: 52px 48px;
    color: white;
    box-shadow: 0 25px 70px rgba(15,23,42,.22);
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}

.hero::after {
    content: "";
    position: absolute;
    top: -40%; right: -15%;
    width: 480px; height: 480px;
    background: radial-gradient(circle, rgba(245,158,11,.18), transparent 65%);
    border-radius: 50%;
    pointer-events: none;
}

.hero-badge {
    display: inline-block;
    padding: 8px 15px;
    border-radius: 999px;
    background: rgba(255,255,255,.09);
    border: 1px solid rgba(255,255,255,.15);
    color: #e5e7eb;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 18px;
    position: relative;
    z-index: 2;
}

.hero-title {
    font-size: 52px;
    line-height: 1.04;
    font-weight: 900;
    letter-spacing: -2.2px;
    margin: 0;
    color: #fff !important;
    position: relative;
    z-index: 2;
}

.hero-highlight {
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-description {
    max-width: 720px;
    margin-top: 18px;
    color: #dbe4f0 !important;
    font-size: 17px;
    line-height: 1.75;
    position: relative;
    z-index: 2;
}


/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {
    color: #101828 !important;
    font-size: 27px;
    font-weight: 800;
    margin-top: 38px;
    margin-bottom: 6px;
    letter-spacing: -0.5px;
}

.section-subtitle {
    color: #667085 !important;
    font-size: 15px;
    margin-bottom: 20px;
}


/* ============================================================
   ★★★★★  IMAGE-CARDS  ★★★★★
   ============================================================ */

.img-card {
    background: #ffffff;
    border: 1px solid #e4e7ec;
    border-radius: 22px;
    overflow: hidden;
    margin-bottom: 20px;
    transition: all .28s cubic-bezier(.4,0,.2,1);
    box-shadow: 0 4px 16px rgba(16,24,40,.05);
    height: 100%;
    display: flex;
    flex-direction: column;
}

.img-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 22px 45px rgba(16,24,40,.13);
    border-color: #c7d2fe;
}

/* Illustrated banner */
.img-card-banner {
    height: 128px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

.img-card-banner::after {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 30% 20%, rgba(255,255,255,.25), transparent 55%);
    pointer-events: none;
}

.img-card-icon {
    font-size: 52px;
    filter: drop-shadow(0 4px 10px rgba(0,0,0,.20));
    z-index: 1;
}

/* Gradient themes */
.bg-indigo   { background: linear-gradient(135deg, #6366f1, #4338ca); }
.bg-amber    { background: linear-gradient(135deg, #f59e0b, #b45309); }
.bg-emerald  { background: linear-gradient(135deg, #10b981, #047857); }
.bg-rose     { background: linear-gradient(135deg, #f43f5e, #be123c); }
.bg-sky      { background: linear-gradient(135deg, #0ea5e9, #0369a1); }
.bg-violet   { background: linear-gradient(135deg, #8b5cf6, #6d28d9); }
.bg-orange   { background: linear-gradient(135deg, #fb923c, #c2410c); }
.bg-teal     { background: linear-gradient(135deg, #14b8a6, #0f766e); }
.bg-slate    { background: linear-gradient(135deg, #475569, #1e293b); }
.bg-fuchsia  { background: linear-gradient(135deg, #d946ef, #a21caf); }
.bg-lime     { background: linear-gradient(135deg, #84cc16, #4d7c0f); }
.bg-cyan     { background: linear-gradient(135deg, #06b6d4, #0e7490); }

.img-card-body {
    padding: 20px 22px 22px 22px;
    flex: 1;
    display: flex;
    flex-direction: column;
}

.img-card-tag {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 999px;
    background: #eef2ff;
    color: #4338ca;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    margin-bottom: 10px;
    width: fit-content;
}

.img-card-title {
    color: #101828 !important;
    font-size: 18px;
    font-weight: 800;
    margin: 0 0 8px 0;
    letter-spacing: -0.3px;
}

.img-card-text {
    color: #475467 !important;
    font-size: 13.5px;
    line-height: 1.6;
    margin: 0;
    flex: 1;
}


/* ============================================================
   FILTER PILLS  (client-side look)
   ============================================================ */

.filter-pill {
    display: inline-block;
    padding: 7px 15px;
    border-radius: 999px;
    background: #ffffff;
    border: 1.5px solid #e4e7ec;
    color: #344054;
    font-size: 13px;
    font-weight: 600;
    margin-right: 8px;
    margin-bottom: 8px;
    transition: all .2s;
    cursor: pointer;
}

.filter-pill:hover {
    border-color: #6366f1;
    color: #4338ca;
    background: #eef2ff;
}

.filter-pill-active {
    background: linear-gradient(135deg, #101828, #263f63);
    color: #ffffff !important;
    border-color: #101828;
}


/* ============================================================
   STAT CHIPS (hero metrics)
   ============================================================ */

.stat-strip {
    display: flex;
    gap: 34px;
    margin-top: 26px;
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
}

.stat-num {
    font-size: 24px;
    font-weight: 900;
    color: #fbbf24 !important;
    letter-spacing: -0.5px;
}

.stat-label {
    font-size: 12.5px;
    color: #94a3b8 !important;
    margin-top: 2px;
}


/* ============================================================
   BUTTONS
   ============================================================ */

.stButton > button {
    width: 100%;
    min-height: 44px;
    border-radius: 12px;
    border: 1px solid #d0d5dd;
    background: #ffffff;
    color: #101828 !important;
    font-weight: 700;
    transition: all .2s ease;
}

.stButton > button:hover {
    border-color: #6366f1;
    color: #4338ca !important;
    transform: translateY(-1px);
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #101828, #263f63);
    color: #fff !important;
    border: none;
    box-shadow: 0 7px 20px rgba(16,24,40,.18);
}

.stButton > button[kind="primary"]:hover {
    color: #fff !important;
    background: linear-gradient(135deg, #17243a, #31527f);
    transform: translateY(-2px);
}


/* ============================================================
   INPUTS / SELECTS / UPLOADER
   ============================================================ */

.stTextInput input,
.stTextArea textarea {
    background: #ffffff !important;
    color: #101828 !important;
    border-radius: 12px !important;
    border: 1px solid #d0d5dd !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #98a2b3 !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,.12) !important;
}

div[data-baseweb="select"] > div {
    background: #fff !important;
    border-radius: 12px !important;
    color: #101828 !important;
}

section[data-testid="stFileUploaderDropzone"] {
    background: #ffffff;
    border: 2px dashed #c7d2fe;
    border-radius: 16px;
}

section[data-testid="stFileUploaderDropzone"] * {
    color: #475467 !important;
}


/* ============================================================
   ALERT BOXES
   ============================================================ */

.warning-box {
    background: #fffbeb;
    border: 1px solid #fcd34d;
    border-left: 5px solid #f59e0b;
    border-radius: 14px;
    padding: 20px 24px;
    color: #78350f !important;
    line-height: 1.65;
    margin-top: 20px;
}

.info-box {
    background: #eef2ff;
    border: 1px solid #c7d2fe;
    border-left: 5px solid #6366f1;
    border-radius: 14px;
    padding: 20px 24px;
    color: #312e81 !important;
    line-height: 1.65;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    color: #667085 !important;
    padding-top: 40px;
    margin-top: 60px;
    border-top: 1px solid #e4e7ec;
    line-height: 1.8;
    font-size: 13px;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px) {
    .block-container { padding: 1rem .85rem 3rem .85rem; }
    .hero { padding: 32px 22px; border-radius: 22px; }
    .hero-title { font-size: 34px; letter-spacing: -1px; }
    .hero-description { font-size: 14px; line-height: 1.65; }
    .section-title { font-size: 22px; margin-top: 28px; }
    .img-card-banner { height: 100px; }
    .img-card-icon { font-size: 42px; }
    .stat-strip { gap: 22px; }
    .stat-num { font-size: 20px; }
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# REUSABLE: IMAGE-CARD RENDERER
# ============================================================

def image_card(icon, title, text, theme="bg-indigo", tag=None):
    """Render a premium image card."""
    tag_html = f'<div class="img-card-tag">{tag}</div>' if tag else ""
    st.markdown(
        f"""
        <div class="img-card">
            <div class="img-card-banner {theme}">
                <div class="img-card-icon">{icon}</div>
            </div>
            <div class="img-card-body">
                {tag_html}
                <div class="img-card-title">{title}</div>
                <div class="img-card-text">{text}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HELPERS
# ============================================================

def add_history(category, text):
    st.session_state.history.append(
        {
            "category": category,
            "text": text,
            "time": datetime.now().strftime("%d %b %Y · %I:%M %p"),
        }
    )


def go_to(page):
    if page in PAGES:
        st.session_state.page = page


def require_ai():
    if not GENAI_AVAILABLE:
        st.error("Google Gemini package is not installed.")
        st.code("pip install google-genai")
        return False
    if not GEMINI_API_KEY:
        st.error("Gemini API key is not configured.")
        st.info("Add `GEMINI_API_KEY` in Streamlit Cloud → Settings → Secrets.")
        return False
    if client is None:
        st.error("Gemini client could not be initialized.")
        return False
    return True


def generate_ai(prompt):
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )
    return getattr(response, "text", None) or "No response was returned."


def extract_pdf_text(uploaded_file):
    if not PYPDF_AVAILABLE:
        raise ImportError("pypdf is not installed. Add `pypdf` to requirements.txt.")
    reader = PdfReader(uploaded_file)
    parts = []
    for i, page in enumerate(reader.pages):
        if i >= 200:
            break
                    st.markdown("""
<div class="stat-num">AI</div>
""", unsafe_allow_html=True)
                    <div class="stat-label">Powered by Gemini</div>
                </div>
                <div>
                    <div class="stat-num">Free</div>
                    <div class="stat-label">For every Indian citizen</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---------- QUICK ACTIONS ----------
    st.markdown('<div class="section-title">🚀 Quick actions</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Start with one of the tools below.</div>',
        unsafe_allow_html=True,
    )

    q1, q2, q3 = st.columns(3)
    with q1:
        if st.button("📄 Explain Judgment", key="quick_judgment", type="primary"):
            go_to("Explain a Judgment")
            st.rerun()
    with q2:
        if st.button("🧠 Ask Legal Question", key="quick_qa", type="primary"):
            go_to("Legal Q&A")
            st.rerun()
    with q3:
        if st.button("🔍 Search Cases", key="quick_cases", type="primary"):
            go_to("Search Cases")
            st.rerun()

    # ---------- FEATURE CARDS (IMAGE CARDS) ----------
    st.markdown('<div class="section-title">✨ What can you do here?</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Simple tools for common legal-information needs.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        image_card(
            "📄",
            "Explain a Judgment",
            "Upload a court judgment PDF and get a structured, plain-language explanation with key takeaways.",
            theme="bg-indigo",
            tag="AI POWERED",
        )
        if st.button("Open tool →", key="feature_judgment"):
            go_to("Explain a Judgment")
            st.rerun()
    with c2:
        image_card(
            "🧠",
            "Legal Q&A",
            "Ask general legal-information questions and receive clear, jargon-free explanations.",
            theme="bg-amber",
            tag="INSTANT",
        )
        if st.button("Ask a question →", key="feature_qa"):
            go_to("Legal Q&A")
            st.rerun()
    with c3:
        image_card(
            "🔍",
            "Search Cases",
            "Search Indian legal resources by case name, topic or court with curated official links.",
            theme="bg-emerald",
            tag="RESEARCH",
        )
        if st.button("Search cases →", key="feature_cases"):
            go_to("Search Cases")
            st.rerun()

    # ---------- POPULAR TOPICS (IMAGE CARDS + FILTER) ----------
    st.markdown('<div class="section-title">🔥 Popular topics</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Browse common legal topics — each card is a starting point.</div>',
        unsafe_allow_html=True,
    )

    # filter row
    topic_filter = st.radio(
        "Filter topics",
        ["All", "Everyday", "Business", "Family", "Constitutional"],
        horizontal=True,
        label_visibility="collapsed",
        key="topic_filter",
    )

    ALL_TOPICS = [
        ("🛍️", "Consumer Rights", "Everyday", "bg-orange",
         "Complaints, refunds, defective products and consumer protection."),
        ("🏠", "Property", "Everyday", "bg-sky",
         "Ownership, rent, tenancy, and property-related legal concepts."),
        ("🚔", "FIR & Police", "Everyday", "bg-slate",
         "How FIRs work, police procedures and complaint filing."),
        ("💻", "Cyber Crime", "Everyday", "bg-violet",
         "Online fraud, identity theft, and how to report cybercrime."),
        ("👨‍👩‍👧", "Family Law", "Family", "bg-rose",
         "Marriage, divorce, maintenance, custody and succession basics."),
        ("💼", "Employment", "Business", "bg-teal",
         "Workplace rights, contracts, salary disputes and termination."),
        ("📄", "RTI", "Constitutional", "bg-cyan",
         "Right to Information — filing, appeals and transparency."),
        ("⚖️", "Fundamental Rights", "Constitutional", "bg-indigo",
         "Your constitutional rights under the Indian Constitution."),
        ("💳", "Cheque Bounce", "Business", "bg-fuchsia",
         "Section 138 NI Act, notices, and legal remedies."),
    ]

    visible = ALL_TOPICS if topic_filter == "All" else [t for t in ALL_TOPICS if t[2] == topic_filter]

    if not visible:
        st.info("No topics in this category yet.")
    else:
        cols = st.columns(3)
        for i, (icon, title, cat, theme, desc) in enumerate(visible):
            with cols[i % 3]:
                image_card(icon, title, desc, theme=theme, tag=cat)

    # ---------- AUDIENCE ----------
    st.markdown('<div class="section-title">👥 Built for everyone</div>', unsafe_allow_html=True)

    a, b, c = st.columns(3)
    with a:
        image_card("👨‍👩‍👧", "Common People",
                   "Understand legal terminology and everyday legal concepts more easily.",
                   theme="bg-emerald", tag="EVERYONE")
    with b:
        image_card("🎓", "Students",
                   "Learn legal concepts through simplified explanations and structured summaries.",
                   theme="bg-violet", tag="LEARNING")
    with c:
        image_card("💼", "Professionals",
                   "Quickly explore general information before consulting a professional.",
                   theme="bg-slate", tag="PRO")

    # ---------- DISCLAIMER ----------
    st.markdown(
        """
        <div class="warning-box">
            <strong>⚠️ Important</strong><br><br>
            My Lawyer Friend provides general legal information for educational
            and informational purposes.<br><br>
            It does not provide legal representation, create a lawyer-client
            relationship, or replace advice from a qualified legal professional.<br><br>
            Always verify important information against official legal sources.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# EXPLAIN A JUDGMENT
# ============================================================

elif st.session_state.page == "Explain a Judgment":

    st.title("📄 Explain a Judgment")
    st.write("Upload an Indian court judgment PDF and understand it in simpler language.")

    st.info("💡 Text-based PDFs work best. Scanned/image-only PDFs may require OCR.")

    uploaded_file = st.file_uploader(
        "Upload judgment PDF",
        type=["pdf"],
        help="Upload a court judgment PDF.",
    )

    if uploaded_file:
        size_kb = uploaded_file.size / 1024
        st.success(f"✅ {uploaded_file.name} uploaded")
        st.caption(f"File size: {size_kb:,.1f} KB")
        st.divider()

        if st.button("⚖️ Analyze Judgment", type="primary", use_container_width=True):
            if not require_ai():
                st.stop()

            try:
                with st.spinner("📖 Reading the judgment..."):
                    document_text = extract_pdf_text(uploaded_file)

                if not document_text.strip():
                    st.error("No readable text was found inside this PDF.")
                    st.info("This appears to be a scanned/image-only PDF. OCR support can be added later.")
                    st.stop()

                document_text = document_text[:60000]

                prompt = f"""
You are "My Lawyer Friend", an Indian legal-information assistant.

Analyze the court judgment provided below. The user wants a simple
explanation, not personalized legal advice.

IMPORTANT RULES:
1. Only use information contained in the document.
2. Do not invent facts, sections or laws.
3. If something is unavailable, write: "Not stated in the document."
4. Clearly distinguish the court's decision from your explanation.
5. Preserve important legal terminology.
6. Do not claim to be a lawyer.
7. Do not provide personalized legal advice.

Use exactly these sections:

# 1. Case Title
# 2. Court
# 3. Date
# 4. Parties
# 5. Case Background
# 6. Important Facts
# 7. Legal Issues
# 8. Arguments
# 9. Important Laws / Sections
# 10. Court's Reasoning
# 11. Final Decision
# 12. Simple Explanation
# 13. Important Takeaways

COURT JUDGMENT:

{document_text}
"""

                with st.spinner("🧠 AI is analyzing the judgment..."):
                    analysis = generate_ai(prompt)

                st.success("✅ Judgment analysis completed")
                st.divider()
                st.subheader("⚖️ Judgment Explanation")
                st.markdown(analysis)

                st.download_button(
                    label="⬇️ Download Explanation",
                    data=analysis,
                    file_name="my_lawyer_friend_analysis.txt",
                    mime="text/plain",
                    use_container_width=True,
                )

                add_history("Judgment Analysis", uploaded_file.name)

                st.divider()
                st.warning(
                    "⚠️ AI-generated legal information may contain errors. "
                    "Verify important details against the original judgment "
                    "and consult a qualified lawyer for specific legal matters."
                )

            except Exception as error:
                st.error("Something went wrong while analyzing the judgment.")
                st.caption(f"Technical details: {error}")

    else:
        st.markdown('<div class="section-title">What you will get</div>', unsafe_allow_html=True)

        features = [
            ("📌", "Case title & court", "bg-indigo"),
            ("📅", "Judgment date", "bg-sky"),
            ("👥", "Parties involved", "bg-violet"),
            ("📖", "Background & facts", "bg-amber"),
            ("⚖️", "Legal issues", "bg-orange"),
            ("🗣️", "Arguments", "bg-teal"),
            ("📚", "Laws & sections", "bg-emerald"),
            ("🧠", "Court's reasoning", "bg-rose"),
            ("🏛️", "Final decision", "bg-slate"),
            ("💡", "Simple explanation", "bg-fuchsia"),
            ("📝", "Key takeaways", "bg-cyan"),
        ]

        cols = st.columns(3)
        for i, (icon, title, theme) in enumerate(features):
            with cols[i % 3]:
                image_card(icon, title, "Included in the AI-generated explanation.", theme=theme)


# ============================================================
# LEGAL Q&A
# ============================================================

elif st.session_state.page == "Legal Q&A":

    st.title("🧠 Legal Q&A")
    st.write("Ask a general legal-information question in simple language.")

    question = st.text_area(
        "Your question",
        placeholder="Example: What is an FIR and when can a person file one?",
        height=150,
    )

    if st.button("🤖 Get Explanation", type="primary", use_container_width=True):
        if not question.strip():
            st.warning("Please enter your question first.")
        elif not require_ai():
            st.stop()
        else:
            try:
                prompt = f"""
You are "My Lawyer Friend", an Indian legal-information assistant.

Answer the following question for an ordinary person in India.

QUESTION:
{question}

RULES:
- Provide general legal information only.
- Do not claim to be the user's lawyer.
- Do not provide personalized legal advice.
- Do not create a lawyer-client relationship.
- Do not invent laws or facts.
- Explain complicated concepts simply.
- Mention relevant legal provisions only when reasonably supported.
- State when information may depend on facts.
- Laws can change — recommend checking official sources for important matters.
"""

                with st.spinner("🧠 Preparing explanation..."):
                    answer = generate_ai(prompt)

                st.success("Explanation generated")
                st.divider()
                st.markdown(answer)

                add_history("Legal Q&A", question)

                st.warning(
                    "⚠️ General legal information only. For a specific legal "
                    "matter, consult a qualified legal professional."
                )

            except Exception as error:
                st.error("Unable to generate the explanation.")
                st.caption(f"Technical details: {error}")

    # Suggested prompts as image cards
    st.markdown('<div class="section-title">💡 Try these questions</div>', unsafe_allow_html=True)

    suggestions = [
        ("🚔", "How do I file an FIR?", "bg-slate"),
        ("🛍️", "What are my consumer rights?", "bg-orange"),
        ("🏠", "Can my landlord evict me without notice?", "bg-sky"),
        ("💼", "Can my employer withhold my salary?", "bg-teal"),
        ("📄", "How do I file an RTI application?", "bg-cyan"),
        ("💳", "What happens if a cheque bounces?", "bg-fuchsia"),
    ]

    cols = st.columns(3)
    for i, (icon, q, theme) in enumerate(suggestions):
        with cols[i % 3]:
            image_card(icon, q, "Click 'Get Explanation' after pasting this into the box.", theme=theme, tag="EXAMPLE")


# ============================================================
# SEARCH CASES
# ============================================================

elif st.session_state.page == "Search Cases":

    st.title("🔍 Search Cases")
    st.write("Find Indian legal resources by case name, keyword or court.")

    st.info(
        "🚧 Live case-data integration is under development. "
        "Below is a working filter foundation plus curated official links."
    )

    # -------- FILTER BAR --------
    f1, f2, f3 = st.columns([2, 2, 2])
    with f1:
        search_term = st.text_input("Case name or keyword", placeholder="e.g. consumer protection")
    with f2:
        court = st.selectbox(
            "Court",
            ["All Courts", "Supreme Court of India", "High Courts", "District Courts"],
        )
    with f3:
        category = st.selectbox(
            "Category",
            ["All Categories", "Constitutional", "Criminal", "Civil", "Consumer", "Family", "Tax"],
        )

    if st.button("🔍 Search", type="primary", use_container_width=True):
        if not search_term.strip():
            st.warning("Please enter a search term.")
        else:
            add_history("Case Search", f"{search_term} · {court} · {category}")
            st.success("Search request prepared.")
            st.write(f"**Keyword:** {search_term}")
            st.write(f"**Court:** {court}")
            st.write(f"**Category:** {category}")

    st.divider()

    # -------- OFFICIAL LINKS (IMAGE CARDS) --------
    st.markdown('<div class="section-title">🇮🇳 Official legal resources</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Verified government sources for authentic information.</div>',
        unsafe_allow_html=True,
    )

    resources = [
        ("⚖️", "Supreme Court of India", "https://www.sci.gov.in/", "bg-indigo",
         "Official judgments, cause lists, and court information."),
        ("🏛️", "eCourts Services", "https://ecourts.gov.in/", "bg-emerald",
         "Case status, orders, and court services across India."),
        ("📚", "India Code", "https://www.indiacode.nic.in/", "bg-amber",
         "Central laws and legislation of India."),
        ("📜", "Indian Kanoon", "https://indiankanoon.org/", "bg-slate",
         "Free search across Indian judgments and statutes."),
        ("🛡️", "NHRC", "https://nhrc.nic.in/", "bg-rose",
         "National Human Rights Commission."),
        ("👩", "NCW", "https://ncw.nic.in/", "bg-fuchsia",
         "National Commission for Women."),
    ]

    cols = st.columns(3)
    for i, (icon, name, url, theme, desc) in enumerate(resources):
        with cols[i % 3]:
            image_card(icon, name, desc, theme=theme, tag="OFFICIAL")
            st.link_button("Visit website →", url, use_container_width=True)


# ============================================================
# KNOW YOUR RIGHTS
# ============================================================

elif st.session_state.page == "Know Your Rights":

    st.title("⚖️ Know Your Rights")
    st.write("Explore general legal-information topics.")

    # -------- FILTER --------
    rights_filter = st.radio(
        "Filter",
        ["All", "Everyday", "Constitutional", "Workplace"],
        horizontal=True,
        label_visibility="collapsed",
        key="rights_filter",
    )

    ALL_RIGHTS = [
        ("🚔", "Police & FIR", "Everyday", "bg-slate",
         "General information about complaints, FIRs and police procedures."),
        ("🛍️", "Consumer Rights", "Everyday", "bg-orange",
         "Consumer complaints, refunds, and consumer protection."),
        ("💻", "Cyber Crime", "Everyday", "bg-violet",
         "Online fraud, cybercrime and how to report incidents."),
        ("🏠", "Property", "Everyday", "bg-sky",
         "Property-related legal concepts and disputes."),
        ("💼", "Employment", "Workplace", "bg-teal",
         "Workplace rights, salaries, and employment-related concepts."),
        ("📄", "RTI", "Constitutional", "bg-cyan",
         "Right to Information — filing, appeals and transparency."),
        ("👨‍👩‍👧", "Family Law", "Everyday", "bg-rose",
         "Common family-law concepts."),
        ("🛡️", "Fundamental Rights", "Constitutional", "bg-indigo",
         "Fundamental rights under the Indian Constitution."),
    ]

    visible = ALL_RIGHTS if rights_filter == "All" else [r for r in ALL_RIGHTS if r[2] == rights_filter]

    if not visible:
        st.info("No topics in this category yet.")
    else:
        cols = st.columns(3)
        for i, (icon, title, cat, theme, desc) in enumerate(visible):
            with cols[i % 3]:
                image_card(icon, title, desc, theme=theme, tag=cat)

    st.markdown(
        """
        <div class="info-box">
            <strong>📌 Important</strong><br><br>
            The information on this page is educational and general in nature.
            Specific legal rights and procedures can depend on the facts and
            applicable law.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HISTORY
# ============================================================

elif st.session_state.page == "History":

    st.title("📚 History")
    st.write("Your recent activity during this session.")

    if not st.session_state.history:
        st.info("No activity yet.")
    else:
        # category filter
        cats = ["All"] + sorted({item["category"] for item in st.session_state.history})
        h_filter = st.radio(
            "Filter",
            cats,
            horizontal=True,
            label_visibility="collapsed",
            key="history_filter",
        )

        items = st.session_state.history if h_filter == "All" else [
            i for i in st.session_state.history if i["category"] == h_filter
        ]

        # pick icon/theme by category
        theme_map = {
            "Judgment Analysis": ("📄", "bg-indigo"),
            "Legal Q&A": ("🧠", "bg-amber"),
            "Case Search": ("🔍", "bg-emerald"),
        }

        for item in reversed(items):
            icon, theme = theme_map.get(item["category"], ("📌", "bg-slate"))
            image_card(
                icon,
                item["category"],
                f'{item["text"]}<br><br><span style="color:#98a2b3;font-size:12px;">{item["time"]}</span>',
                theme=theme,
                tag="SESSION",
            )

        st.divider()
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.history = []
            st.success("History cleared.")
            st.rerun()


# ============================================================
# ABOUT
# ============================================================

elif st.session_state.page == "About":

    st.title("⚖️ About My Lawyer Friend")

    image_card(
        "🇮🇳",
        "What is My Lawyer Friend?",
        "A student-built Indian legal-information platform designed to make "
        "legal concepts, judgments and legal terminology easier to understand.",
        theme="bg-indigo",
        tag="MISSION",
    )

    st.markdown('<div class="section-title">🎯 Vision</div>', unsafe_allow_html=True)
    st.write("Make useful legal information easier to discover and understand.")

    st.markdown('<div class="section-title">🚀 Roadmap</div>', unsafe_allow_html=True)

    roadmap = [
        ("v1.0", "Premium UI and navigation", "bg-slate"),
        ("v1.1", "Judgment upload and Q&A", "bg-sky"),
        ("v1.2", "Gemini AI document analysis", "bg-indigo"),
        ("v1.3", "Responsive mobile-first redesign", "bg-violet"),
        ("v1.4", "Image-card system + live filters", "bg-emerald"),
        ("v1.5", "Official Indian case-data integration", "bg-amber"),
        ("v1.6", "User accounts and saved research", "bg-rose"),
        ("v2.0", "Advanced legal research assistant", "bg-fuchsia"),
    ]

    cols = st.columns(4)
    for i, (ver, feat, theme) in enumerate(roadmap):
        with cols[i % 4]:
            image_card("🚀", ver, feat, theme=theme, tag="ROADMAP")

    st.divider()
    st.subheader("👨‍💻 Project")
    st.code(
        f"My Lawyer Friend\n"
        f"Indian Legal Information Platform\n"
        f"Version {APP_VERSION}\n"
        f"Built as a CSE student portfolio project."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        ⚖️ <strong>My Lawyer Friend</strong><br>
        Legal information made simple · 🇮🇳 India<br><br>
        Built as an open-source CSE project.<br>
        General information only · Not legal advice
    </div>
    """,
    unsafe_allow_html=True,
)
