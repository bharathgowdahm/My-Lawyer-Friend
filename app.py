import streamlit as st
from datetime import datetime

# PDF support
from pypdf import PdfReader

# Gemini support
try:
    from google import genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False


# ============================================================
# MY LAWYER FRIEND
# V1.3 — Premium Indian Legal Information Platform
# ============================================================


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="My Lawyer Friend",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CONSTANTS
# ============================================================

APP_NAME = "My Lawyer Friend"
APP_VERSION = "1.3"
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
# PREMIUM CSS
# ============================================================

st.markdown(
    """
<style>

/* ============================================================
   GLOBAL
   ============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html,
body,
[class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 5% 0%,
            rgba(99,102,241,.08),
            transparent 28%
        ),
        radial-gradient(
            circle at 100% 100%,
            rgba(245,158,11,.06),
            transparent 30%
        ),
        #f6f7fb;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background: #0b1220;
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb;
}

section[data-testid="stSidebar"] .stRadio label {
    color: #e5e7eb !important;
    font-size: 14px !important;
    font-weight: 600 !important;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,.07);
    border-radius: 10px;
}

section[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,.10) !important;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    background:
        radial-gradient(
            circle at 90% 20%,
            rgba(99,102,241,.35),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #08111f 0%,
            #12223e 55%,
            #214b78 100%
        );

    border-radius: 28px;
    padding: 48px;
    color: white;
    box-shadow:
        0 25px 70px rgba(15,23,42,.22);

    margin-bottom: 32px;
}

.hero-badge {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 999px;

    background: rgba(255,255,255,.09);
    border: 1px solid rgba(255,255,255,.15);

    color: #e5e7eb;
    font-size: 13px;
    font-weight: 600;

    margin-bottom: 18px;
}

.hero-title {
    font-size: 50px;
    line-height: 1.05;
    font-weight: 800;
    letter-spacing: -2px;

    margin: 0;
    color: #ffffff !important;
}

.hero-highlight {
    color: #fbbf24 !important;
}

.hero-description {
    max-width: 720px;
    margin-top: 18px;

    color: #dbe4f0 !important;

    font-size: 17px;
    line-height: 1.75;
}


/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {
    color: #101828 !important;

    font-size: 27px;
    font-weight: 800;

    margin-top: 35px;
    margin-bottom: 6px;
}

.section-subtitle {
    color: #667085 !important;

    font-size: 15px;

    margin-bottom: 20px;
}


/* ============================================================
   CUSTOM CARDS
   ============================================================ */

.mlf-card {
    background: #ffffff;

    border: 1px solid #e4e7ec;

    border-radius: 20px;

    padding: 24px;

    min-height: 150px;

    box-shadow:
        0 7px 25px rgba(16,24,40,.055);

    margin-bottom: 14px;
}

.mlf-card:hover {
    border-color: #c7d2fe;

    box-shadow:
        0 14px 35px rgba(16,24,40,.10);
}

.mlf-card h3 {
    color: #101828 !important;

    font-size: 19px;
    font-weight: 800;

    margin-top: 0;
    margin-bottom: 10px;
}

.mlf-card p {
    color: #475467 !important;

    font-size: 14px;
    line-height: 1.65;

    margin-bottom: 0;
}

.mlf-card-small {
    min-height: 100px;
}

.mlf-card-small strong {
    color: #101828 !important;
}

.mlf-card-small span {
    color: #667085 !important;
}


/* ============================================================
   TOPIC CARDS
   ============================================================ */

.topic-card {
    background: #ffffff;

    border: 1px solid #e4e7ec;

    border-radius: 16px;

    padding: 18px;

    margin-bottom: 12px;

    min-height: 75px;

    box-shadow: 0 4px 16px rgba(16,24,40,.04);
}

.topic-title {
    color: #101828 !important;

    font-weight: 700;

    font-size: 15px;
}

.topic-description {
    color: #667085 !important;

    font-size: 12px;

    margin-top: 5px;
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
    background:
        linear-gradient(
            135deg,
            #101828,
            #263f63
        );

    color: #ffffff !important;

    border: none;

    box-shadow:
        0 7px 20px rgba(16,24,40,.18);
}

.stButton > button[kind="primary"]:hover {
    color: #ffffff !important;

    background:
        linear-gradient(
            135deg,
            #17243a,
            #31527f
        );
}


/* ============================================================
   INPUTS
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

    box-shadow:
        0 0 0 3px rgba(99,102,241,.12) !important;
}


/* ============================================================
   SELECTBOX
   ============================================================ */

div[data-baseweb="select"] > div {
    background: #ffffff !important;

    border-radius: 12px !important;

    color: #101828 !important;
}


/* ============================================================
   FILE UPLOADER
   ============================================================ */

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

    .block-container {
        padding: 1rem 0.85rem 3rem 0.85rem;
    }

    .hero {
        padding: 30px 23px;

        border-radius: 22px;
    }

    .hero-title {
        font-size: 34px;

        letter-spacing: -1px;
    }

    .hero-description {
        font-size: 14px;

        line-height: 1.65;
    }

    .section-title {
        font-size: 22px;

        margin-top: 28px;
    }

    .section-subtitle {
        font-size: 13px;
    }

    .mlf-card {
        padding: 19px;

        border-radius: 17px;
    }

    .topic-card {
        padding: 15px;
    }

    .stButton > button {
        min-height: 46px;
    }
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================

def add_history(category, text):
    """Save activity for the current session."""

    st.session_state.history.append(
        {
            "category": category,
            "text": text,
            "time": datetime.now().strftime(
                "%d %b %Y · %I:%M %p"
            ),
        }
    )


def go_to(page):
    """Navigate safely."""

    if page in PAGES:
        st.session_state.page = page


def require_ai():
    """Check Gemini availability."""

    if not GENAI_AVAILABLE:
        st.error(
            "Google Gemini package is not installed."
        )

        st.code(
            "pip install google-genai"
        )

        return False

    if not GEMINI_API_KEY:
        st.error(
            "Gemini API key is not configured."
        )

        st.info(
            "Go to Streamlit Cloud → Manage app → "
            "Settings → Secrets and add GEMINI_API_KEY."
        )

        return False

    if client is None:
        st.error(
            "Gemini client could not be initialized."
        )

        return False

    return True


def generate_ai(prompt):
    """Send a prompt to Gemini."""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    text = getattr(response, "text", None)

    if text:
        return text

    return "No response was returned by the AI."


def extract_pdf_text(uploaded_file):
    """Extract text from PDF."""

    reader = PdfReader(uploaded_file)

    text_parts = []

    max_pages = 200

    for index, page in enumerate(reader.pages):

        if index >= max_pages:
            break

        try:
            page_text = page.extract_text() or ""
        except Exception:
            page_text = ""

        if page_text.strip():
            text_parts.append(page_text)

    return "\n\n".join(text_parts)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            display:flex;
            align-items:center;
            gap:12px;
            padding:5px 0 10px 0;
        ">

            <div style="
                width:44px;
                height:44px;
                border-radius:13px;
                background:linear-gradient(135deg,#6366f1,#f59e0b);
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:22px;
            ">
                ⚖️
            </div>

            <div>

                <div style="
                    font-size:17px;
                    font-weight:800;
                ">
                    My Lawyer Friend
                </div>

                <div style="
                    color:#98a2b3;
                    font-size:12px;
                    margin-top:2px;
                ">
                    Legal information, made simple
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    selected_page = st.radio(
        "Navigation",
        PAGES,
        index=PAGES.index(st.session_state.page),
        label_visibility="collapsed",
    )

    if selected_page != st.session_state.page:
        st.session_state.page = selected_page

    st.divider()

    st.markdown(
        """
        <div style="
            background:rgba(255,255,255,.04);
            border:1px solid rgba(255,255,255,.08);
            border-radius:14px;
            padding:15px;
            font-size:12px;
            line-height:1.65;
            color:#cbd5e1;
        ">

        🇮🇳 <strong style="color:#fbbf24;">
        Built for India
        </strong>

        <br><br>

        General legal information for educational
        and informational purposes.

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        f"{APP_NAME} · v{APP_VERSION}"
    )


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    # HERO
    st.markdown(
        """
        <div class="hero">

            <div class="hero-badge">
                🇮🇳 Indian Legal Information Platform
            </div>

            <div class="hero-title">
                Your legal questions.<br>
                <span class="hero-highlight">
                    Made simple.
                </span>
            </div>

            <div class="hero-description">
                My Lawyer Friend helps ordinary people
                understand legal information, court judgments
                and everyday legal concepts without complicated
                terminology.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    # QUICK ACTIONS
    st.markdown(
        '<div class="section-title">🚀 Quick actions</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Start with one of the tools below.'
        '</div>',
        unsafe_allow_html=True,
    )

    q1, q2, q3 = st.columns(3)

    with q1:
        if st.button(
            "📄 Explain Judgment",
            key="quick_judgment",
            type="primary",
        ):
            go_to("Explain a Judgment")
            st.rerun()

    with q2:
        if st.button(
            "🧠 Ask Legal Question",
            key="quick_qa",
            type="primary",
        ):
            go_to("Legal Q&A")
            st.rerun()

    with q3:
        if st.button(
            "🔍 Search Cases",
            key="quick_cases",
            type="primary",
        ):
            go_to("Search Cases")
            st.rerun()


    # FEATURES
    st.markdown(
        '<div class="section-title">✨ What can you do here?</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Simple tools designed for common legal-information needs.'
        '</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class="mlf-card">

                <h3>📄 Explain a Judgment</h3>

                <p>
                Upload a court judgment PDF and get
                a structured plain-language explanation.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Open tool →",
            key="feature_judgment",
        ):
            go_to("Explain a Judgment")
            st.rerun()


    with c2:

        st.markdown(
            """
            <div class="mlf-card">

                <h3>🧠 Legal Q&A</h3>

                <p>
                Ask general legal-information questions
                and receive simple explanations.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Ask a question →",
            key="feature_qa",
        ):
            go_to("Legal Q&A")
            st.rerun()


    with c3:

        st.markdown(
            """
            <div class="mlf-card">

                <h3>🔍 Search Cases</h3>

                <p>
                Search Indian legal resources by
                case name, topic or keyword.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Search cases →",
            key="feature_cases",
        ):
            go_to("Search Cases")
            st.rerun()


    # POPULAR TOPICS
    st.markdown(
        '<div class="section-title">🔥 Popular topics</div>',
        unsafe_allow_html=True,
    )

    topics = [
        ("🛍️", "Consumer Rights"),
        ("🏠", "Property"),
        ("🚔", "FIR & Police"),
        ("💻", "Cyber Crime"),
        ("👨‍👩‍👧", "Family Law"),
        ("💼", "Employment"),
        ("📄", "RTI"),
        ("⚖️", "Fundamental Rights"),
        ("💳", "Cheque Bounce"),
    ]

    topic_columns = st.columns(3)

    for index, (icon, topic) in enumerate(topics):

        with topic_columns[index % 3]:

            st.markdown(
                f"""
                <div class="topic-card">

                    <div class="topic-title">
                        {icon} {topic}
                    </div>

                    <div class="topic-description">
                        Explore general legal information
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


    # AUDIENCE
    st.markdown(
        '<div class="section-title">👥 Built for everyone</div>',
        unsafe_allow_html=True,
    )

    a, b, c = st.columns(3)

    with a:

        st.markdown(
            """
            <div class="mlf-card">

                <h3>👨‍👩‍👧 Common People</h3>

                <p>
                Understand legal terminology and
                everyday legal concepts more easily.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with b:

        st.markdown(
            """
            <div class="mlf-card">

                <h3>🎓 Students</h3>

                <p>
                Learn legal concepts through
                simplified explanations.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with c:

        st.markdown(
            """
            <div class="mlf-card">

                <h3>💼 Professionals</h3>

                <p>
                Quickly explore general information
                before consulting a professional.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )


    # DISCLAIMER
    st.markdown(
        """
        <div class="warning-box">

            <strong>⚠️ Important</strong>

            <br><br>

            My Lawyer Friend provides general legal
            information for educational and informational
            purposes.

            <br><br>

            It does not provide legal representation,
            create a lawyer-client relationship, or
            replace advice from a qualified legal
            professional.

            <br><br>

            Always verify important information against
            official legal sources.

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# EXPLAIN JUDGMENT
# ============================================================

elif st.session_state.page == "Explain a Judgment":

    st.title("📄 Explain a Judgment")

    st.write(
        "Upload an Indian court judgment PDF and "
        "understand it in simpler language."
    )

    st.info(
        "💡 Text-based PDFs work best. "
        "Scanned/image-only PDFs may require OCR."
    )

    uploaded_file = st.file_uploader(
        "Upload judgment PDF",
        type=["pdf"],
        help="Upload a court judgment PDF.",
    )

    if uploaded_file:

        file_size = uploaded_file.size / 1024

        st.success(
            f"✅ {uploaded_file.name} uploaded"
        )

        st.caption(
            f"File size: {file_size:,.1f} KB"
        )

        st.divider()

        if st.button(
            "⚖️ Analyze Judgment",
            type="primary",
            use_container_width=True,
        ):

            if not require_ai():
                st.stop()

            try:

                # READ PDF
                with st.spinner(
                    "📖 Reading the judgment..."
                ):

                    document_text = extract_pdf_text(
                        uploaded_file
                    )

                if not document_text.strip():

                    st.error(
                        "No readable text was found "
                        "inside this PDF."
                    )

                    st.info(
                        "This appears to be a scanned or "
                        "image-only PDF. OCR support can "
                        "be added later."
                    )

                    st.stop()


                # TOKEN SAFETY
                document_text = document_text[:60000]


                # PROMPT
                prompt = f"""
You are "My Lawyer Friend", an Indian
legal-information assistant.

Analyze the court judgment provided below.

The user wants a simple explanation,
not personalized legal advice.

IMPORTANT RULES:

1. Only use information contained in the document.
2. Do not invent facts.
3. Do not invent sections or laws.
4. If something is not available, write:
   "Not stated in the document."
5. Clearly distinguish the court's decision
   from your explanation.
6. Preserve important legal terminology.
7. Do not claim to be a lawyer.
8. Do not provide personalized legal advice.

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


                # AI
                with st.spinner(
                    "🧠 AI is analyzing the judgment..."
                ):

                    analysis = generate_ai(
                        prompt
                    )


                st.success(
                    "✅ Judgment analysis completed"
                )

                st.divider()

                st.subheader(
                    "⚖️ Judgment Explanation"
                )

                st.markdown(
                    analysis
                )


                # DOWNLOAD
                st.download_button(
                    label="⬇️ Download Explanation",
                    data=analysis,
                    file_name=(
                        "my_lawyer_friend_analysis.txt"
                    ),
                    mime="text/plain",
                    use_container_width=True,
                )


                # HISTORY
                add_history(
                    "Judgment Analysis",
                    uploaded_file.name,
                )


                st.divider()

                st.warning(
                    "⚠️ AI-generated legal information "
                    "may contain errors. Verify important "
                    "details against the original judgment "
                    "and consult a qualified lawyer for "
                    "specific legal matters."
                )


            except Exception as error:

                st.error(
                    "Something went wrong while "
                    "analyzing the judgment."
                )

                st.caption(
                    f"Technical details: {error}"
                )


    else:

        st.markdown(
            '<div class="section-title">'
            'What you will get'
            '</div>',
            unsafe_allow_html=True,
        )

        features = [
            "📌 Case title and court",
            "📅 Judgment date",
            "👥 Parties involved",
            "📖 Background and facts",
            "⚖️ Legal issues",
            "🗣️ Arguments",
            "📚 Important laws and sections",
            "🧠 Court reasoning",
            "🏛️ Final decision",
            "💡 Simple explanation",
            "📝 Important takeaways",
        ]

        for feature in features:
            st.markdown(
                f"""
                <div class="topic-card">
                    <div class="topic-title">
                        {feature}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ============================================================
# LEGAL Q&A
# ============================================================

elif st.session_state.page == "Legal Q&A":

    st.title("🧠 Legal Q&A")

    st.write(
        "Ask a general legal-information question "
        "in simple language."
    )

    question = st.text_area(
        "Your question",
        placeholder=(
            "Example: What is an FIR and "
            "when can a person file one?"
        ),
        height=150,
    )

    if st.button(
        "🤖 Get Explanation",
        type="primary",
        use_container_width=True,
    ):

        if not question.strip():

            st.warning(
                "Please enter your question first."
            )

        elif not require_ai():

            st.stop()

        else:

            try:

                prompt = f"""
You are "My Lawyer Friend",
an Indian legal-information assistant.

Answer the following question for
an ordinary person in India.

QUESTION:

{question}

RULES:

- Provide general legal information only.
- Do not claim to be the user's lawyer.
- Do not provide personalized legal advice.
- Do not create a lawyer-client relationship.
- Do not invent laws.
- Do not invent facts.
- Explain complicated concepts simply.
- Mention relevant legal provisions only
  when reasonably supported.
- State when information may depend on facts.
- Laws can change, so recommend checking
  official sources for important matters.
"""

                with st.spinner(
                    "🧠 Preparing explanation..."
                ):

                    answer = generate_ai(
                        prompt
                    )

                st.success(
                    "Explanation generated"
                )

                st.divider()

                st.markdown(
                    answer
                )

                add_history(
                    "Legal Q&A",
                    question,
                )

                st.warning(
                    "⚠️ General legal information only. "
                    "For a specific legal matter, consult "
                    "a qualified legal professional."
                )

            except Exception as error:

                st.error(
                    "Unable to generate the explanation."
                )

                st.caption(
                    f"Technical details: {error}"
                )


# ============================================================
# SEARCH CASES
# ============================================================

elif st.session_state.page == "Search Cases":

    st.title("🔍 Search Cases")

    st.write(
        "Find Indian legal resources by case name, "
        "keyword or court."
    )

    st.info(
        "🚧 Live case-data integration is currently "
        "under development. This screen is the "
        "foundation for the v1.4 case-search system."
    )

    search_term = st.text_input(
        "Case name or keyword",
        placeholder=(
            "Example: consumer protection"
        ),
    )

    court = st.selectbox(
        "Court",
        [
            "All Courts",
            "Supreme Court of India",
            "High Courts",
            "District Courts",
        ],
    )

    if st.button(
        "🔍 Search",
        type="primary",
        use_container_width=True,
    ):

        if not search_term.strip():

            st.warning(
                "Please enter a search term."
            )

        else:

            add_history(
                "Case Search",
                search_term,
            )

            st.success(
                "Search request prepared."
            )

            st.write(
                f"**Keyword:** {search_term}"
            )

            st.write(
                f"**Court:** {court}"
            )

            st.divider()

            st.subheader(
                "🇮🇳 Official legal resources"
            )

            st.markdown(
                """
                ### ⚖️ Supreme Court of India

                Use the official Supreme Court
                website to access court information.

                **https://www.sci.gov.in/**


                ### 🏛️ eCourts

                Use the Indian eCourts system for
                court-related services.

                **https://ecourts.gov.in/**


                ### 📚 India Code

                Search central laws and legislation.

                **https://www.indiacode.nic.in/**
                """
            )


# ============================================================
# KNOW YOUR RIGHTS
# ============================================================

elif st.session_state.page == "Know Your Rights":

    st.title("⚖️ Know Your Rights")

    st.write(
        "Explore general legal-information topics."
    )

    rights = [

        (
            "🚔",
            "Police & FIR",
            "General information about complaints, "
            "FIRs and police procedures."
        ),

        (
            "🛍️",
            "Consumer Rights",
            "General information about consumer "
            "complaints and consumer protection."
        ),

        (
            "💻",
            "Cyber Crime",
            "General information about online fraud, "
            "cybercrime and reporting."
        ),

        (
            "🏠",
            "Property",
            "General information about property-related "
            "legal concepts."
        ),

        (
            "💼",
            "Employment",
            "General information about workplace "
            "and employment-related legal concepts."
        ),

        (
            "📄",
            "RTI",
            "General information about the "
            "Right to Information framework."
        ),

        (
            "👨‍👩‍👧",
            "Family Law",
            "General information about common "
            "family-law concepts."
        ),

        (
            "🛡️",
            "Fundamental Rights",
            "General educational information about "
            "fundamental rights under the Constitution."
        ),

    ]

    for icon, title, description in rights:

        st.markdown(
            f"""
            <div class="mlf-card">

                <h3>
                    {icon} {title}
                </h3>

                <p>
                    {description}
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )


    st.markdown(
        """
        <div class="info-box">

            <strong>📌 Important</strong>

            <br><br>

            The information on this page is
            educational and general in nature.
            Specific legal rights and procedures
            can depend on the facts and applicable law.

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HISTORY
# ============================================================

elif st.session_state.page == "History":

    st.title("📚 History")

    st.write(
        "Your recent activity during this session."
    )

    if not st.session_state.history:

        st.info(
            "No activity yet."
        )

    else:

        for item in reversed(
            st.session_state.history
        ):

            st.markdown(
                f"""
                <div class="mlf-card mlf-card-small">

                    <strong>
                        {item["category"]}
                    </strong>

                    <div style="
                        color:#667085;
                        font-size:12px;
                        margin-top:5px;
                    ">
                        {item["time"]}
                    </div>

                    <div style="
                        color:#344054;
                        font-size:14px;
                        margin-top:10px;
                    ">
                        {item["text"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


        st.divider()

        if st.button(
            "🗑️ Clear History",
            use_container_width=True,
        ):

            st.session_state.history = []

            st.success(
                "History cleared."
            )

            st.rerun()


# ============================================================
# ABOUT
# ============================================================

elif st.session_state.page == "About":

    st.title("⚖️ About My Lawyer Friend")

    st.markdown(
        """
        <div class="mlf-card">

            <h3>
                🇮🇳 What is My Lawyer Friend?
            </h3>

            <p>
                My Lawyer Friend is a student-built
                Indian legal-information platform
                designed to make legal concepts,
                judgments and legal terminology
                easier to understand.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown(
        '<div class="section-title">🎯 Vision</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "Make useful legal information easier "
        "to discover and understand."
    )


    st.markdown(
        '<div class="section-title">🚀 Roadmap</div>',
        unsafe_allow_html=True,
    )

    roadmap = [
        (
            "v1.0",
            "Premium UI and navigation"
        ),
        (
            "v1.1",
            "Judgment upload and Q&A"
        ),
        (
            "v1.2",
            "Gemini AI document analysis"
        ),
        (
            "v1.3",
            "Responsive mobile-first redesign"
        ),
        (
            "v1.4",
            "Official Indian case-data integration"
        ),
        (
            "v1.5",
            "Official legal-source updates"
        ),
        (
            "v1.6",
            "User accounts and saved research"
        ),
        (
            "v2.0",
            "Advanced legal research assistant"
        ),
    ]

    for version, feature in roadmap:

        st.markdown(
            f"""
            <div class="topic-card">

                <div class="topic-title">
                    {version}
                </div>

                <div class="topic-description">
                    {feature}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    st.divider()

    st.subheader("👨‍💻 Project")

    st.code(
        "My Lawyer Friend\n"
        "Indian Legal Information Platform\n"
        f"Version {APP_VERSION}\n"
        "Built as a CSE student portfolio project."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        ⚖️ <strong>My Lawyer Friend</strong>

        <br>

        Legal information made simple · 🇮🇳 India

        <br><br>

        Built as an open-source CSE project.

        <br>

        General information only · Not legal advice

    </div>
    """,
    unsafe_allow_html=True,
)
