import streamlit as st
import textwrap
from datetime import datetime

# ============================================================
# MY LAWYER FRIEND — v1.1
# Indian Legal Information Platform
# ============================================================

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="My Lawyer Friend · Legal Information Made Simple",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# SESSION STATE
# ============================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"


# ============================================================
# HELPER — SAFE HTML RENDERING
# IMPORTANT:
# textwrap.dedent prevents Streamlit from treating HTML
# as a Markdown code block.
# ============================================================

def html(content):
    st.markdown(
        textwrap.dedent(content).strip(),
        unsafe_allow_html=True
    )


def add_history(item_type, name):
    st.session_state.history.append(
        {
            "type": item_type,
            "name": name[:100],
            "time": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        }
    )


# ============================================================
# PREMIUM CSS
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
            radial-gradient(
                circle at 10% 10%,
                rgba(99,102,241,0.06),
                transparent 35%
            ),
            radial-gradient(
                circle at 90% 90%,
                rgba(245,158,11,0.05),
                transparent 35%
            ),
            #f7f8fc;
    }

    .block-container {
        max-width: 1280px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    /* ========================================================
       SIDEBAR
    ======================================================== */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #090d18 0%,
            #101828 100%
        );
        border-right: 1px solid rgba(255,255,255,0.06);
    }

    section[data-testid="stSidebar"] * {
        color: #e4e7ec;
    }

    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.08) !important;
    }

    /* ========================================================
       HERO
    ======================================================== */

    .hero {
        background:
            radial-gradient(
                circle at 90% 15%,
                rgba(245,158,11,0.18),
                transparent 40%
            ),
            radial-gradient(
                circle at 10% 90%,
                rgba(99,102,241,0.20),
                transparent 45%
            ),
            linear-gradient(
                135deg,
                #090d18 0%,
                #18263d 55%,
                #29466f 100%
            );

        padding: 60px 55px;
        border-radius: 28px;
        color: white;
        margin-bottom: 35px;
        box-shadow: 0 20px 50px rgba(16,24,40,0.22);
        position: relative;
        overflow: hidden;
        animation: fadeUp 0.6s ease;
    }

    .hero-title {
        font-size: 50px;
        font-weight: 800;
        line-height: 1.08;
        letter-spacing: -1.5px;
        margin-bottom: 18px;
        position: relative;
        z-index: 2;
    }

    .hero-title span {
        background: linear-gradient(
            135deg,
            #fbbf24,
            #f59e0b
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-badge {
        display: inline-block;
        padding: 8px 16px;
        border-radius: 30px;
        background: rgba(255,255,255,0.09);
        border: 1px solid rgba(255,255,255,0.18);
        font-size: 13px;
        margin-bottom: 22px;
    }

    .hero-text {
        max-width: 700px;
        color: #cbd5e1;
        font-size: 17px;
        line-height: 1.7;
        position: relative;
        z-index: 2;
    }

    .hero-stats {
        display: flex;
        gap: 45px;
        margin-top: 32px;
        flex-wrap: wrap;
        position: relative;
        z-index: 2;
    }

    .hero-stat-num {
        font-size: 26px;
        font-weight: 800;
        color: #fbbf24;
    }

    .hero-stat-label {
        font-size: 12.5px;
        color: #94a3b8;
    }

    /* ========================================================
       CARDS
    ======================================================== */

    .card {
        background: white;
        border: 1px solid #eaecf0;
        border-radius: 20px;
        padding: 26px;
        min-height: 210px;
        box-shadow: 0 4px 20px rgba(16,24,40,0.05);
        transition: all 0.25s ease;
        position: relative;
        overflow: hidden;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 18px 38px rgba(16,24,40,0.11);
        border-color: #d0d5dd;
    }

    .card::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(
            90deg,
            #6366f1,
            #f59e0b
        );
        opacity: 0;
        transition: opacity 0.25s ease;
    }

    .card:hover::before {
        opacity: 1;
    }

    .icon-badge {
        width: 52px;
        height: 52px;
        border-radius: 14px;
        background: linear-gradient(
            135deg,
            #eef2ff,
            #e0e7ff
        );
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 25px;
        margin-bottom: 17px;
    }

    .card-title {
        font-size: 18px;
        font-weight: 700;
        color: #101828;
        margin-bottom: 8px;
    }

    .card-text {
        color: #667085;
        font-size: 14px;
        line-height: 1.6;
    }

    /* ========================================================
       SECTION
    ======================================================== */

    .section-title {
        font-size: 26px;
        font-weight: 800;
        color: #101828;
        margin-top: 40px;
        margin-bottom: 20px;
        letter-spacing: -0.5px;
    }

    .section-subtitle {
        color: #667085;
        font-size: 15px;
        margin-top: -10px;
        margin-bottom: 22px;
    }

    /* ========================================================
       PAGE HEADER
    ======================================================== */

    .page-header {
        background: white;
        border: 1px solid #eaecf0;
        border-radius: 20px;
        padding: 30px 34px;
        margin-bottom: 28px;
        box-shadow: 0 4px 18px rgba(16,24,40,0.04);
    }

    .page-header h1 {
        color: #101828;
        font-size: 30px;
        font-weight: 800;
        margin: 0 0 8px 0;
    }

    .page-header p {
        color: #667085;
        margin: 0;
        line-height: 1.6;
    }

    /* ========================================================
       CHIPS
    ======================================================== */

    .chip {
        display: inline-block;
        background: #f2f4f7;
        border: 1px solid #eaecf0;
        color: #344054;
        padding: 7px 13px;
        border-radius: 20px;
        font-size: 13px;
        margin: 4px;
    }

    /* ========================================================
       INFO BOXES
    ======================================================== */

    .info-box {
        background: linear-gradient(
            135deg,
            #eef2ff,
            #e0e7ff
        );
        border: 1px solid #c7d2fe;
        border-left: 5px solid #6366f1;
        border-radius: 15px;
        padding: 19px 22px;
        color: #312e81;
        font-size: 14px;
        line-height: 1.6;
    }

    .success-box {
        background: linear-gradient(
            135deg,
            #ecfdf5,
            #d1fae5
        );
        border: 1px solid #a7f3d0;
        border-left: 5px solid #10b981;
        border-radius: 15px;
        padding: 19px 22px;
        color: #065f46;
        font-size: 14px;
        line-height: 1.6;
    }

    .warning-box {
        background: linear-gradient(
            135deg,
            #fffbeb,
            #fef3c7
        );
        border: 1px solid #fde68a;
        border-left: 5px solid #f59e0b;
        border-radius: 15px;
        padding: 19px 22px;
        color: #78350f;
        font-size: 14px;
        line-height: 1.6;
    }

    /* ========================================================
       DISCLAIMER
    ======================================================== */

    .disclaimer {
        background: linear-gradient(
            135deg,
            #fffbeb,
            #fef3c7
        );
        border: 1px solid #fde68a;
        border-left: 5px solid #f59e0b;
        border-radius: 16px;
        padding: 22px 26px;
        margin-top: 40px;
        color: #78350f;
        font-size: 14px;
        line-height: 1.65;
    }

    /* ========================================================
       BUTTONS
    ======================================================== */

    .stButton > button {
        border-radius: 12px;
        border: none;
        padding: 11px 20px;
        font-weight: 600;
        background: linear-gradient(
            135deg,
            #101828,
            #263f63
        );
        color: white;
        box-shadow: 0 4px 14px rgba(16,24,40,0.15);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 22px rgba(16,24,40,0.20);
    }

    /* ========================================================
       INPUTS
    ======================================================== */

    .stTextInput input,
    .stTextArea textarea {
        border-radius: 12px !important;
        border: 1.5px solid #eaecf0 !important;
    }

    /* ========================================================
       FOOTER
    ======================================================== */

    .footer {
        text-align: center;
        color: #98a2b3;
        margin-top: 70px;
        padding-top: 30px;
        border-top: 1px solid #eaecf0;
        font-size: 13px;
        line-height: 1.7;
    }

    /* ========================================================
       ANIMATION
    ======================================================== */

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(15px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* ========================================================
       MOBILE
    ======================================================== */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero {
            padding: 35px 25px;
            border-radius: 22px;
        }

        .hero-title {
            font-size: 34px;
        }

        .hero-text {
            font-size: 15px;
        }

        .hero-stats {
            gap: 22px;
        }

        .page-header {
            padding: 24px;
        }

        .page-header h1 {
            font-size: 25px;
        }

        .section-title {
            font-size: 22px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    html(
        """
        <div style="
            display:flex;
            align-items:center;
            gap:12px;
            padding:6px 0 5px 0;
        ">

            <div style="
                width:44px;
                height:44px;
                border-radius:12px;
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
                ">
                    Legal information, made simple
                </div>
            </div>

        </div>
        """
    )

    st.divider()

    st.markdown(
        "### Navigation"
    )

    page = st.radio(
        "Go to",
        [
            "🏠 Home",
            "📄 Explain a Judgment",
            "🔍 Search Cases",
            "⚖️ Know Your Rights",
            "🧠 Legal Q&A",
            "📚 History",
        ],
        label_visibility="collapsed",
        key="page",
    )

    st.divider()

    html(
        """
        <div style="
            background:rgba(255,255,255,0.04);
            border:1px solid rgba(255,255,255,0.08);
            border-radius:12px;
            padding:14px;
            font-size:12px;
            line-height:1.6;
            color:#cbd5e1;
        ">
            💡 <strong style="color:#fbbf24;">Tip</strong><br>
            Upload a judgment PDF or ask a legal question
            to explore the platform.
        </div>
        """
    )

    st.markdown("")

    st.caption("🇮🇳 Designed for users in India · v1.1")


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    html(
        """
        <div class="hero">

            <div class="hero-badge">
                🇮🇳 Indian Legal Information Platform
            </div>

            <div class="hero-title">
                Your legal questions,
                <br>
                <span>explained simply.</span>
            </div>

            <div class="hero-text">
                My Lawyer Friend helps people understand legal
                concepts, court judgments, rights and procedures
                using simple language — without unnecessary legal jargon.
            </div>

            <div class="hero-stats">

                <div>
                    <div class="hero-stat-num">24/7</div>
                    <div class="hero-stat-label">
                        Information access
                    </div>
                </div>

                <div>
                    <div class="hero-stat-num">India</div>
                    <div class="hero-stat-label">
                        Designed for Indian users
                    </div>
                </div>

                <div>
                    <div class="hero-stat-num">Simple</div>
                    <div class="hero-stat-label">
                        Plain-language explanations
                    </div>
                </div>

            </div>

        </div>
        """
    )

    html(
        """
        <div class="section-title">
            🚀 Quick actions
        </div>
        """
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button(
            "📄 Explain a Judgment",
            use_container_width=True
        ):
            st.session_state.page = "📄 Explain a Judgment"
            st.rerun()

    with c2:
        if st.button(
            "🧠 Ask Legal Question",
            use_container_width=True
        ):
            st.session_state.page = "🧠 Legal Q&A"
            st.rerun()

    with c3:
        if st.button(
            "🔍 Search Cases",
            use_container_width=True
        ):
            st.session_state.page = "🔍 Search Cases"
            st.rerun()

    html(
        """
        <div class="section-title">
            ✨ What can you do here?
        </div>

        <div class="section-subtitle">
            Explore legal information through simple,
            user-friendly tools.
        </div>
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        html(
            """
            <div class="card">
                <div class="icon-badge">📄</div>

                <div class="card-title">
                    Explain a Judgment
                </div>

                <div class="card-text">
                    Upload a judgment PDF and understand
                    its important points in simple language.
                </div>
            </div>
            """
        )

    with col2:
        html(
            """
            <div class="card">
                <div class="icon-badge">🔍</div>

                <div class="card-title">
                    Search Cases
                </div>

                <div class="card-text">
                    Search Indian legal resources and
                    explore relevant cases and judgments.
                </div>
            </div>
            """
        )

    with col3:
        html(
            """
            <div class="card">
                <div class="icon-badge">🧠</div>

                <div class="card-title">
                    Legal Q&A
                </div>

                <div class="card-text">
                    Ask general legal questions and
                    receive easy-to-understand explanations.
                </div>
            </div>
            """
        )

    html(
        """
        <div class="section-title">
            🔥 Popular topics
        </div>

        <div>
            <span class="chip">Consumer Rights</span>
            <span class="chip">Property</span>
            <span class="chip">Fundamental Rights</span>
            <span class="chip">FIR & Police</span>
            <span class="chip">Family Law</span>
            <span class="chip">Cyber Crime</span>
            <span class="chip">Employment</span>
            <span class="chip">RTI</span>
            <span class="chip">Cheque Bounce</span>
        </div>
        """
    )

    html(
        """
        <div class="section-title">
            👥 Built for everyone
        </div>
        """
    )

    a, b, c = st.columns(3)

    with a:
        html(
            """
            <div class="card">
                <div class="icon-badge">👨‍👩‍👧</div>

                <div class="card-title">
                    Common People
                </div>

                <div class="card-text">
                    Understand everyday legal concepts
                    without complicated terminology.
                </div>
            </div>
            """
        )

    with b:
        html(
            """
            <div class="card">
                <div class="icon-badge">🎓</div>

                <div class="card-title">
                    Students
                </div>

                <div class="card-text">
                    Learn about real legal concepts,
                    cases and judicial decisions.
                </div>
            </div>
            """
        )

    with c:
        html(
            """
            <div class="card">
                <div class="icon-badge">💼</div>

                <div class="card-title">
                    Professionals
                </div>

                <div class="card-text">
                    Quickly explore general legal
                    information and resources.
                </div>
            </div>
            """
        )

    html(
        """
        <div class="disclaimer">

            <strong>⚠️ Important Disclaimer</strong>

            <br><br>

            My Lawyer Friend provides general legal information
            for educational and informational purposes only.

            It does not provide legal representation or create
            a lawyer-client relationship.

            <br><br>

            For important legal matters, verify information
            against official sources and consult a qualified
            legal professional.

        </div>
        """
    )


# ============================================================
# EXPLAIN JUDGMENT
# ============================================================

elif page == "📄 Explain a Judgment":

    html(
        """
        <div class="page-header">

            <h1>
                📄 Explain a Judgment
            </h1>

            <p>
                Upload an Indian court judgment PDF and
                organize the document for easy understanding.
            </p>

        </div>
        """
    )

    uploaded_file = st.file_uploader(
        "Upload judgment PDF",
        type=["pdf"],
        help="Upload a PDF judgment."
    )

    if uploaded_file:

        size_mb = uploaded_file.size / (1024 * 1024)

        html(
            f"""
            <div class="success-box">

                <strong>✓ Document uploaded</strong>

                <br><br>

                <strong>File:</strong>
                {uploaded_file.name}

                <br>

                <strong>Size:</strong>
                {size_mb:.2f} MB

                <br><br>

                The document is ready for the next
                processing stage.

            </div>
            """
        )

        if st.button(
            "📚 Add to History",
            use_container_width=False
        ):
            add_history(
                "Judgment",
                uploaded_file.name
            )

            st.success(
                "Judgment added to your history."
            )

    html(
        """
        <div class="section-title">
            🧩 What the future AI analyzer will identify
        </div>
        """
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        html(
            """
            <div class="card">
                <div class="icon-badge">📌</div>
                <div class="card-title">Facts</div>
                <div class="card-text">
                    Important background facts and
                    events in the case.
                </div>
            </div>
            """
        )

    with c2:
        html(
            """
            <div class="card">
                <div class="icon-badge">⚖️</div>
                <div class="card-title">Legal Issues</div>
                <div class="card-text">
                    The legal questions considered
                    by the court.
                </div>
            </div>
            """
        )

    with c3:
        html(
            """
            <div class="card">
                <div class="icon-badge">🏛️</div>
                <div class="card-title">Decision</div>
                <div class="card-text">
                    The court's decision and important
                    reasoning in simple language.
                </div>
            </div>
            """
        )

    html(
        """
        <div class="warning-box">

            <strong>⚠️ Development note</strong>

            <br><br>

            v1.1 focuses on the professional interface
            and document workflow. AI-powered judgment
            analysis will be connected in the next stage.

        </div>
        """
    )


# ============================================================
# SEARCH CASES
# ============================================================

elif page == "🔍 Search Cases":

    html(
        """
        <div class="page-header">

            <h1>
                🔍 Search Cases
            </h1>

            <p>
                Search for Indian legal information using
                keywords, case names or legal topics.
            </p>

        </div>
        """
    )

    query = st.text_input(
        "Search",
        placeholder="Example: consumer protection, property dispute..."
    )

    if st.button(
        "🔎 Search",
        use_container_width=True
    ):

        if query.strip():

            add_history(
                "Case Search",
                query
            )

            html(
                f"""
                <div class="info-box">

                    <strong>Search prepared</strong>

                    <br><br>

                    Query:
                    <strong>{query}</strong>

                    <br><br>

                    The next version can connect this
                    search box to official legal datasets
                    and court-search services.

                </div>
                """
            )

        else:
            st.warning(
                "Enter a search term first."
            )

    html(
        """
        <div class="section-title">
            🏛️ Legal resources
        </div>
        """
    )

    r1, r2, r3 = st.columns(3)

    with r1:
        html(
            """
            <div class="card">

                <div class="icon-badge">
                    🏛️
                </div>

                <div class="card-title">
                    Supreme Court
                </div>

                <div class="card-text">
                    Use official Supreme Court resources
                    when verifying important judgments.
                </div>

            </div>
            """
        )

    with r2:
        html(
            """
            <div class="card">

                <div class="icon-badge">
                    ⚖️
                </div>

                <div class="card-title">
                    High Courts
                </div>

                <div class="card-text">
                    Explore information relating to
                    High Court decisions and proceedings.
                </div>

            </div>
            """
        )

    with r3:
        html(
            """
            <div class="card">

                <div class="icon-badge">
                    📚
                </div>

                <div class="card-title">
                    Legal Research
                </div>

                <div class="card-text">
                    Search by topic, legal issue,
                    case name or keyword.
                </div>

            </div>
            """
        )


# ============================================================
# KNOW YOUR RIGHTS
# ============================================================

elif page == "⚖️ Know Your Rights":

    html(
        """
        <div class="page-header">

            <h1>
                ⚖️ Know Your Rights
            </h1>

            <p>
                Explore general information about
                everyday legal rights and procedures.
            </p>

        </div>
        """
    )

    topics = {
        "🚔 Police & FIR": [
            "What is an FIR?",
            "What happens after an FIR?",
            "General information about police complaints."
        ],

        "🛒 Consumer Rights": [
            "Consumer complaints",
            "Defective products",
            "Service-related disputes"
        ],

        "💼 Employment": [
            "Salary-related issues",
            "Employment documents",
            "Workplace legal information"
        ],

        "🏠 Property": [
            "Property documentation",
            "Rental disputes",
            "General property-law concepts"
        ],

        "💻 Cyber Crime": [
            "Online fraud",
            "Cyber complaints",
            "Digital safety"
        ],

        "👨‍👩‍👧 Family Law": [
            "Marriage-related legal information",
            "Family disputes",
            "General family-law concepts"
        ],
    }

    for index, (title, items) in enumerate(topics.items()):

        if index % 2 == 0:
            c1, c2 = st.columns(2)

        with c1 if index % 2 == 0 else c2:

            html(
                f"""
                <div class="card"
                     style="min-height:180px;margin-bottom:18px;">

                    <div class="card-title">
                        {title}
                    </div>

                    <div class="card-text">

                        <ul>
                            <li>{items[0]}</li>
                            <li>{items[1]}</li>
                            <li>{items[2]}</li>
                        </ul>

                    </div>

                </div>
                """
            )


# ============================================================
# LEGAL Q&A
# ============================================================

elif page == "🧠 Legal Q&A":

    html(
        """
        <div class="page-header">

            <h1>
                🧠 Legal Q&A
            </h1>

            <p>
                Ask a general legal-information question
                in your own words.
            </p>

        </div>
        """
    )

    question = st.text_area(
        "Your question",
        placeholder=(
            "Example: What is the general process for filing "
            "a consumer complaint in India?"
        ),
        height=150,
    )

    if st.button(
        "💬 Submit Question",
        use_container_width=True
    ):

        if question.strip():

            add_history(
                "Q&A",
                question
            )

            html(
                """
                <div class="info-box">

                    <strong>✓ Question received</strong>

                    <br><br>

                    Your question has been added to your
                    session history.

                    <br><br>

                    <strong>Next development:</strong>
                    connect this interface to a carefully
                    sourced legal-information AI system.

                </div>
                """
            )

        else:

            st.warning(
                "Please enter a question."
            )

    html(
        """
        <div class="section-title">
            💡 Example questions
        </div>

        <div>

            <span class="chip">
                How do I file an FIR?
            </span>

            <span class="chip">
                What is a legal notice?
            </span>

            <span class="chip">
                What are consumer rights?
            </span>

            <span class="chip">
                What is RTI?
            </span>

            <span class="chip">
                What is a cheque bounce case?
            </span>

        </div>
        """
    )

    html(
        """
        <div class="warning-box" style="margin-top:25px;">

            <strong>⚠️ Important</strong>

            <br><br>

            This tool is for general legal information.
            It is not a substitute for advice from a
            qualified lawyer for your particular situation.

        </div>
        """
    )


# ============================================================
# HISTORY
# ============================================================

elif page == "📚 History":

    html(
        """
        <div class="page-header">

            <h1>
                📚 My History
            </h1>

            <p>
                Your recent searches, questions and
                document activity in this session.
            </p>

        </div>
        """
    )

    if not st.session_state.history:

        html(
            """
            <div class="info-box">

                🗂️ <strong>No history yet.</strong>

                <br><br>

                Your searches, questions and uploaded
                judgments will appear here.

            </div>
            """
        )

    else:

        for item in reversed(
            st.session_state.history
        ):

            html(
                f"""
                <div class="card"
                     style="
                        min-height:auto;
                        padding:18px 22px;
                        margin-bottom:12px;
                     ">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        align-items:center;
                        gap:15px;
                        flex-wrap:wrap;
                    ">

                        <div>

                            <div style="
                                font-size:11px;
                                color:#6366f1;
                                font-weight:700;
                                text-transform:uppercase;
                                letter-spacing:0.7px;
                            ">
                                {item["type"]}
                            </div>

                            <div style="
                                font-size:15px;
                                color:#101828;
                                font-weight:600;
                                margin-top:4px;
                            ">
                                {item["name"]}
                            </div>

                        </div>

                        <div style="
                            color:#98a2b3;
                            font-size:12px;
                        ">
                            {item["time"]}
                        </div>

                    </div>

                </div>
                """
            )

        st.markdown("")

        if st.button(
            "🗑️ Clear History",
            use_container_width=False
        ):

            st.session_state.history = []

            st.rerun()


# ============================================================
# FOOTER
# ============================================================

html(
    """
    <div class="footer">

        ⚖️
        <strong style="color:#344054;">
            My Lawyer Friend
        </strong>

        · Legal information made simple

        <br>

        Built as an open-source CSE project
        · Made for users in 🇮🇳 India

        <br>

        <span style="font-size:12px;">
            v1.1 · Educational & informational use
        </span>

    </div>
    """
)
