import streamlit as st
from datetime import datetime

# PDF library
try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None


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

if "uploaded_name" not in st.session_state:
    st.session_state.uploaded_name = None

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "document_pages" not in st.session_state:
    st.session_state.document_pages = 0

if "qa_history" not in st.session_state:
    st.session_state.qa_history = []


# ============================================================
# CUSTOM CSS - PREMIUM THEME
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .stApp {
        background: #f7f8fc;
        background-image:
            radial-gradient(
                circle at 15% 10%,
                rgba(99, 102, 241, 0.06) 0%,
                transparent 40%
            ),
            radial-gradient(
                circle at 85% 90%,
                rgba(245, 158, 11, 0.05) 0%,
                transparent 40%
            );
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
            #0a0f1e 0%,
            #101828 100%
        );
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    section[data-testid="stSidebar"] * {
        color: #e4e7ec;
    }

    section[data-testid="stSidebar"] .stRadio label {
        padding: 10px 12px;
        border-radius: 10px;
        transition: background 0.2s ease;
        font-weight: 500;
        font-size: 14.5px;
    }

    section[data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255,255,255,0.06);
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
                circle at 90% 20%,
                rgba(245, 158, 11, 0.18) 0%,
                transparent 45%
            ),
            radial-gradient(
                circle at 10% 90%,
                rgba(99, 102, 241, 0.20) 0%,
                transparent 45%
            ),
            linear-gradient(
                135deg,
                #0a0f1e 0%,
                #18263d 55%,
                #263f63 100%
            );

        padding: 60px 55px;
        border-radius: 28px;
        color: white;
        margin-bottom: 35px;
        box-shadow: 0 20px 50px rgba(16, 24, 40, 0.25);
        position: relative;
        overflow: hidden;
        animation: fadeUp 0.7s ease;
    }

    .hero::after {
        content: "";
        position: absolute;
        top: -50%;
        right: -20%;
        width: 500px;
        height: 500px;
        background: radial-gradient(
            circle,
            rgba(245,158,11,0.15) 0%,
            transparent 70%
        );
        border-radius: 50%;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.20);
        backdrop-filter: blur(8px);
        padding: 8px 16px;
        border-radius: 30px;
        font-size: 13.5px;
        font-weight: 500;
        margin-bottom: 22px;
        letter-spacing: 0.3px;
    }

    .hero-title {
        font-size: 50px;
        font-weight: 800;
        line-height: 1.08;
        margin-bottom: 18px;
        letter-spacing: -1px;
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
        background-clip: text;
    }

    .hero-text {
        font-size: 17.5px;
        color: #cbd5e1;
        max-width: 680px;
        line-height: 1.65;
        position: relative;
        z-index: 2;
        margin-bottom: 28px;
    }

    .hero-stats {
        display: flex;
        gap: 40px;
        margin-top: 30px;
        position: relative;
        z-index: 2;
        flex-wrap: wrap;
    }

    .hero-stat-num {
        font-size: 26px;
        font-weight: 800;
        color: #fbbf24;
    }

    .hero-stat-label {
        font-size: 13px;
        color: #94a3b8;
        margin-top: 2px;
    }


    /* ========================================================
       CARDS
       ======================================================== */

    .card {
        background: white;
        border: 1px solid #eaecf0;
        border-radius: 20px;
        padding: 28px;
        min-height: 210px;
        box-shadow: 0 4px 20px rgba(16,24,40,0.05);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .card:hover {
        transform: translateY(-6px);
        box-shadow: 0 20px 40px rgba(16,24,40,0.12);
        border-color: #d0d5dd;
    }

    .card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(
            90deg,
            #6366f1,
            #f59e0b
        );
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .card:hover::before {
        opacity: 1;
    }

    .icon-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 52px;
        height: 52px;
        font-size: 26px;
        background: linear-gradient(
            135deg,
            #eef2ff,
            #e0e7ff
        );
        border-radius: 14px;
        margin-bottom: 18px;
    }

    .card-title {
        font-size: 18px;
        font-weight: 700;
        color: #101828;
        margin-bottom: 8px;
        letter-spacing: -0.2px;
    }

    .card-text {
        color: #667085;
        line-height: 1.55;
        font-size: 14px;
    }


    /* ========================================================
       SECTION TITLES
       ======================================================== */

    .section-title {
        font-size: 26px;
        font-weight: 750;
        color: #101828;
        margin-top: 40px;
        margin-bottom: 22px;
        letter-spacing: -0.5px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .section-subtitle {
        font-size: 15px;
        color: #667085;
        margin-top: -14px;
        margin-bottom: 22px;
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
        font-size: 14.5px;
        line-height: 1.6;
    }


    /* ========================================================
       PAGE HEADER
       ======================================================== */

    .page-header {
        background: linear-gradient(
            135deg,
            #ffffff,
            #f9fafb
        );
        border: 1px solid #eaecf0;
        border-radius: 20px;
        padding: 32px 36px;
        margin-bottom: 28px;
        box-shadow: 0 4px 20px rgba(16,24,40,0.04);
    }

    .page-header h1 {
        font-size: 30px;
        font-weight: 800;
        color: #101828;
        margin: 0 0 8px 0;
        letter-spacing: -0.6px;
    }

    .page-header p {
        color: #667085;
        font-size: 15.5px;
        margin: 0;
        line-height: 1.55;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {
        background: linear-gradient(
            135deg,
            #101828,
            #263f63
        );
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 26px;
        font-weight: 600;
        font-size: 14.5px;
        transition: all 0.25s ease;
        box-shadow: 0 4px 14px rgba(16,24,40,0.15);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 22px rgba(16,24,40,0.25);
        background: linear-gradient(
            135deg,
            #18263d,
            #2d4a75
        );
    }


    /* ========================================================
       FILE UPLOADER
       ======================================================== */

    div[data-testid="stFileUploader"] {
        background: white;
        border-radius: 16px;
        padding: 10px;
        border: 1px dashed #d0d5dd;
    }


    /* ========================================================
       INPUTS
       ======================================================== */

    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 12px !important;
        border: 1.5px solid #eaecf0 !important;
        padding: 12px 14px !important;
        font-size: 14.5px !important;
        transition: border 0.2s ease;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #6366f1 !important;
        box-shadow:
            0 0 0 3px rgba(99,102,241,0.10)
            !important;
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
        border-radius: 14px;
        padding: 20px 24px;
        color: #312e81;
        font-size: 14.5px;
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
        border-radius: 14px;
        padding: 18px 22px;
        color: #065f46;
        font-size: 14.5px;
    }


    /* ========================================================
       DOCUMENT PREVIEW
       ======================================================== */

    .document-card {
        background: white;
        border: 1px solid #eaecf0;
        border-radius: 18px;
        padding: 22px;
        box-shadow: 0 4px 18px rgba(16,24,40,0.05);
        margin-bottom: 18px;
    }

    .document-label {
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #667085;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .document-value {
        font-size: 16px;
        font-weight: 700;
        color: #101828;
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
        font-size: 13.5px;
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

    .fade-in {
        animation: fadeUp 0.6s ease;
    }


    /* ========================================================
       CHIP
       ======================================================== */

    .chip {
        display: inline-block;
        background: #f2f4f7;
        color: #344054;
        padding: 7px 14px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 500;
        margin: 4px 6px 4px 0;
        border: 1px solid #eaecf0;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


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
            padding:6px 0 4px 0;
        ">

            <div style="
                width:44px;
                height:44px;
                border-radius:12px;
                background:linear-gradient(
                    135deg,
                    #6366f1,
                    #f59e0b
                );
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
                    letter-spacing:-0.3px;
                ">
                    My Lawyer Friend
                </div>

                <div style="
                    color:#98a2b3;
                    font-size:12.5px;
                    margin-top:1px;
                ">
                    Legal info, made simple
                </div>
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown(
        """
        <div style="
            color:#98a2b3;
            font-size:11.5px;
            font-weight:600;
            letter-spacing:1.2px;
            text-transform:uppercase;
            margin-bottom:8px;
        ">
            Navigation
        </div>
        """,
        unsafe_allow_html=True,
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

    st.markdown(
        """
        <div style="
            background:rgba(255,255,255,0.04);
            border:1px solid rgba(255,255,255,0.08);
            border-radius:12px;
            padding:14px;
            font-size:12.5px;
            line-height:1.6;
            color:#cbd5e1;
        ">
            💡
            <strong style="color:#fbbf24;">
                Tip:
            </strong>
            Upload a judgment PDF to get a plain-language
            document preview.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div style='height:14px;'></div>",
        unsafe_allow_html=True,
    )

    st.caption(
        "🇮🇳 Designed for users in India · v1.1"
    )


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-badge">
                🇮🇳 &nbsp; Indian Legal Information Platform
            </div>

            <div class="hero-title">
                Your legal questions,<br>
                <span>explained simply.</span>
            </div>

            <div class="hero-text">
                My Lawyer Friend helps you understand court judgments,
                legal documents and everyday legal concepts using clear,
                jargon-free language — so you can make informed decisions
                with confidence.
            </div>

            <div class="hero-stats">

                <div>
                    <div class="hero-stat-num">
                        Simple
                    </div>

                    <div class="hero-stat-label">
                        Plain-language explanations
                    </div>
                </div>

                <div>
                    <div class="hero-stat-num">
                        On demand
                    </div>

                    <div class="hero-stat-label">
                        Use when you need it
                    </div>
                </div>

                <div>
                    <div class="hero-stat-num">
                        Free
                    </div>

                    <div class="hero-stat-label">
                        Core information
                    </div>
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    # ========================================================
    # QUICK ACTIONS
    # ========================================================

    st.markdown(
        '<div class="section-title">🚀 &nbsp;Quick actions</div>',
        unsafe_allow_html=True,
    )

    qa1, qa2, qa3 = st.columns(3)

    with qa1:
        if st.button(
            "📄 Explain a Judgment",
            use_container_width=True,
        ):
            st.session_state.page = "📄 Explain a Judgment"
            st.rerun()

    with qa2:
        if st.button(
            "🧠 Ask a Legal Question",
            use_container_width=True,
        ):
            st.session_state.page = "🧠 Legal Q&A"
            st.rerun()

    with qa3:
        if st.button(
            "🔍 Search Cases",
            use_container_width=True,
        ):
            st.session_state.page = "🔍 Search Cases"
            st.rerun()


    # ========================================================
    # FEATURE CARDS
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        '✨ &nbsp;What do you need help with?'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Choose a tool below to get started — no legal background needed.'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="card">

                <div class="icon-badge">
                    📄
                </div>

                <div class="card-title">
                    Explain a Judgment
                </div>

                <div class="card-text">
                    Upload a court judgment PDF and get a clear,
                    structured summary of the document.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
            <div class="card">

                <div class="icon-badge">
                    🔍
                </div>

                <div class="card-title">
                    Search Cases
                </div>

                <div class="card-text">
                    Find relevant Indian court cases and judgments
                    by keyword, topic, or case name.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:

        st.markdown(
            """
            <div class="card">

                <div class="icon-badge">
                    🧠
                </div>

                <div class="card-title">
                    Ask a Legal Question
                </div>

                <div class="card-text">
                    Ask about legal concepts and receive an
                    easy-to-understand explanation.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    # ========================================================
    # POPULAR TOPICS
    # ========================================================

    st.markdown(
        '<div class="section-title">🔥 &nbsp;Popular topics</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div>

            <span class="chip">
                Consumer Rights
            </span>

            <span class="chip">
                Property Disputes
            </span>

            <span class="chip">
                Fundamental Rights
            </span>

            <span class="chip">
                FIR &amp; Police Procedure
            </span>

            <span class="chip">
                Divorce &amp; Family Law
            </span>

            <span class="chip">
                Cyber Crime
            </span>

            <span class="chip">
                Employment Rights
            </span>

            <span class="chip">
                RTI
            </span>

            <span class="chip">
                Cheque Bounce
            </span>

        </div>
        """,
        unsafe_allow_html=True,
    )


    # ========================================================
    # BUILT FOR EVERYONE
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        '👥 &nbsp;Built for everyone'
        '</div>',
        unsafe_allow_html=True,
    )

    col4, col5, col6 = st.columns(3)

    with col4:

        st.markdown(
            """
            <div class="card">

                <div class="icon-badge">
                    👨‍👩‍👧
                </div>

                <div class="card-title">
                    Common People
                </div>

                <div class="card-text">
                    Understand legal documents without struggling
                    through complicated legal terminology.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col5:

        st.markdown(
            """
            <div class="card">

                <div class="icon-badge">
                    🎓
                </div>

                <div class="card-title">
                    Students
                </div>

                <div class="card-text">
                    Learn how real court decisions work through
                    simplified and structured explanations.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col6:

        st.markdown(
            """
            <div class="card">

                <div class="icon-badge">
                    💼
                </div>

                <div class="card-title">
                    Professionals
                </div>

                <div class="card-text">
                    Quickly identify key information inside
                    lengthy legal documents.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    # ========================================================
    # DISCLAIMER
    # ========================================================

    st.markdown(
        """
        <div class="disclaimer">

            <strong>
                ⚠️ Important Disclaimer
            </strong>

            <br><br>

            My Lawyer Friend provides general legal information
            for educational purposes only. It does not offer legal
            representation and is not a substitute for advice from
            a qualified lawyer.

            Always verify important information using the original
            legal source and consult a qualified professional for
            your specific situation.

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# EXPLAIN A JUDGMENT
# ============================================================

elif page == "📄 Explain a Judgment":

    st.markdown(
        """
        <div class="page-header">

            <h1>
                📄 Explain a Judgment
            </h1>

            <p>
                Upload an Indian court judgment PDF and get a
                structured document preview. AI explanation will
                be connected in the next development stage.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # PDF LIBRARY CHECK
    # --------------------------------------------------------

    if fitz is None:

        st.error(
            "PyMuPDF is not installed. Add 'PyMuPDF' "
            "to requirements.txt and redeploy."
        )

    else:

        uploaded_file = st.file_uploader(
            "Upload judgment PDF",
            type=["pdf"],
            help="Supported format: PDF",
        )


        if uploaded_file:

            file_size_mb = (
                uploaded_file.size / (1024 * 1024)
            )

            # ------------------------------------------------
            # READ PDF
            # ------------------------------------------------

            try:

                pdf_bytes = uploaded_file.getvalue()

                document = fitz.open(
                    stream=pdf_bytes,
                    filetype="pdf",
                )

                page_count = len(document)

                full_text = ""

                for pdf_page in document:

                    page_text = pdf_page.get_text(
                        "text"
                    )

                    full_text += (
                        page_text
                        + "\n"
                    )

                document.close()


                # ------------------------------------------------
                # SAVE DOCUMENT STATE
                # ------------------------------------------------

                st.session_state.uploaded_name = (
                    uploaded_file.name
                )

                st.session_state.document_text = (
                    full_text
                )

                st.session_state.document_pages = (
                    page_count
                )


                # ------------------------------------------------
                # FILE INFORMATION
                # ------------------------------------------------

                st.markdown(
                    '<div class="section-title">'
                    '📊 &nbsp;Document information'
                    '</div>',
                    unsafe_allow_html=True,
                )

                info1, info2, info3 = st.columns(3)

                with info1:

                    st.markdown(
                        f"""
                        <div class="document-card">

                            <div class="document-label">
                                File
                            </div>

                            <div class="document-value">
                                📄 {uploaded_file.name}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                with info2:

                    st.markdown(
                        f"""
                        <div class="document-card">

                            <div class="document-label">
                                Pages
                            </div>

                            <div class="document-value">
                                📑 {page_count}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                with info3:

                    st.markdown(
                        f"""
                        <div class="document-card">

                            <div class="document-label">
                                File size
                            </div>

                            <div class="document-value">
                                💾 {file_size_mb:.2f} MB
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )


                # ------------------------------------------------
                # EXTRACTION RESULT
                # ------------------------------------------------

                if full_text.strip():

                    st.markdown(
                        '<div class="success-box">'
                        '✅ PDF text extracted successfully. '
                        'The document is ready for AI analysis.'
                        '</div>',
                        unsafe_allow_html=True,
                    )

                    # Add history only once per uploaded file
                    existing = any(
                        item.get("name")
                        == uploaded_file.name
                        for item in st.session_state.history
                    )

                    if not existing:

                        st.session_state.history.append(
                            {
                                "type": "PDF",
                                "name": uploaded_file.name,
                                "time": datetime.now().strftime(
                                    "%d %b %Y, %I:%M %p"
                                ),
                            }
                        )


                    # ------------------------------------------------
                    # PREVIEW
                    # ------------------------------------------------

                    st.markdown(
                        '<div class="section-title">'
                        '📖 &nbsp;Document preview'
                        '</div>',
                        unsafe_allow_html=True,
                    )

                    preview_text = full_text.strip()

                    if len(preview_text) > 5000:

                        preview_text = (
                            preview_text[:5000]
                            + "\n\n… Preview shortened."
                        )

                    st.text_area(
                        "Extracted text",
                        value=preview_text,
                        height=350,
                    )


                    # ------------------------------------------------
                    # NEXT STEP MESSAGE
                    # ------------------------------------------------

                    st.markdown(
                        """
                        <div class="info-box">

                            🤖 <strong>AI analysis is next.</strong>

                            <br><br>

                            In the next version, My Lawyer Friend
                            will use the extracted judgment to identify:

                            <br><br>

                            • Case title<br>
                            • Court<br>
                            • Important dates<br>
                            • Facts of the case<br>
                            • Legal issues<br>
                            • Arguments<br>
                            • Decision / order<br>
                            • Important legal provisions<br>
                            • Plain-language explanation

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                else:

                    st.warning(
                        "The PDF does not contain readable text. "
                        "It may be a scanned/image-only document. "
                        "OCR support can be added later."
                    )

            except Exception as error:

                st.error(
                    "We could not read this PDF."
                )

                st.caption(
                    f"Technical details: {error}"
                )


# ============================================================
# SEARCH CASES
# ============================================================

elif page == "🔍 Search Cases":

    st.markdown(
        """
        <div class="page-header">

            <h1>
                🔍 Search Cases
            </h1>

            <p>
                Search for Indian court cases by case name,
                topic, keyword, or legal issue.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


    search_query = st.text_input(
        "Search",
        placeholder=(
            "Example: property dispute, consumer rights..."
        ),
    )


    search_button = st.button(
        "🔎 Search",
        use_container_width=False,
    )


    if search_button:

        if not search_query.strip():

            st.warning(
                "Enter a search term first."
            )

        else:

            st.info(
                f"Case search for "
                f"**{search_query.strip()}** "
                "will be connected to reliable legal sources "
                "in a future version."
            )

            st.markdown(
                """
                <div class="info-box">

                    📚 <strong>Source-first approach</strong>

                    <br><br>

                    The production version will prioritize
                    authoritative or clearly identified sources
                    instead of generating fictional case results.

                </div>
                """,
                unsafe_allow_html=True,
            )


# ============================================================
# KNOW YOUR RIGHTS
# ============================================================

elif page == "⚖️ Know Your Rights":

    st.markdown(
        """
        <div class="page-header">

            <h1>
                ⚖️ Know Your Rights
            </h1>

            <p>
                Explore common legal topics explained in
                simple language.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


    rights = [
        (
            "🛒",
            "Consumer Rights",
            "Understand basic consumer protection concepts."
        ),
        (
            "🚔",
            "Police & FIR",
            "Learn general information about FIRs and police procedures."
        ),
        (
            "💻",
            "Cyber Crime",
            "Learn about common cyber-related legal issues."
        ),
        (
            "🏠",
            "Property",
            "Understand common property-law concepts."
        ),
        (
            "💼",
            "Employment",
            "Explore general workplace legal information."
        ),
        (
            "📜",
            "RTI",
            "Learn the basics of the Right to Information framework."
        ),
    ]


    for index in range(0, len(rights), 3):

        columns = st.columns(3)

        for column_index, column in enumerate(columns):

            item_index = index + column_index

            if item_index < len(rights):

                icon, title, description = rights[item_index]

                with column:

                    st.markdown(
                        f"""
                        <div class="card">

                            <div class="icon-badge">
                                {icon}
                            </div>

                            <div class="card-title">
                                {title}
                            </div>

                            <div class="card-text">
                                {description}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )


    st.markdown(
        """
        <div class="disclaimer">

            <strong>
                ⚠️ Legal information notice
            </strong>

            <br><br>

            These topics provide general educational information.
            Laws and procedures can depend on the facts,
            jurisdiction, and current legislation.

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# LEGAL Q&A
# ============================================================

elif page == "🧠 Legal Q&A":

    st.markdown(
        """
        <div class="page-header">

            <h1>
                🧠 Legal Q&A
            </h1>

            <p>
                Ask a legal-information question and get a
                plain-language explanation.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown(
        """
        <div class="info-box">

            💡 <strong>How this will work</strong>

            <br><br>

            The production AI system will answer using
            trusted legal sources and will clearly distinguish
            factual information from general explanation.

        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown(
        '<div class="section-title">'
        '💬 &nbsp;Ask your question'
        '</div>',
        unsafe_allow_html=True,
    )


    question = st.text_area(
        "Your question",
        placeholder=(
            "Example: What is the general process for filing an FIR?"
        ),
        height=150,
    )


    if st.button(
        "✨ Get Explanation",
        key="legal_question_button",
    ):

        if not question.strip():

            st.warning(
                "Please enter a question first."
            )

        else:

            clean_question = question.strip()

            st.session_state.qa_history.append(
                {
                    "question": clean_question,
                    "time": datetime.now().strftime(
                        "%d %b %Y, %I:%M %p"
                    ),
                }
            )

            st.session_state.history.append(
                {
                    "type": "Q&A",
                    "name": clean_question[:80]
                    + (
                        "…"
                        if len(clean_question) > 80
                        else ""
                    ),
                    "time": datetime.now().strftime(
                        "%d %b %Y, %I:%M %p"
                    ),
                }
            )

            st.success(
                "Question saved. AI legal explanation "
                "will be connected in the next stage."
            )

            st.markdown(
                f"""
                <div class="card"
                     style="min-height:auto;margin-top:20px;">

                    <div class="card-title">
                        Your question
                    </div>

                    <div class="card-text">
                        {clean_question}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


    # --------------------------------------------------------
    # EXAMPLE QUESTIONS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        '💡 &nbsp;Example questions'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div>

            <span class="chip">
                How do I file an FIR?
            </span>

            <span class="chip">
                What is a legal notice?
            </span>

            <span class="chip">
                What are my rights as a tenant?
            </span>

            <span class="chip">
                How does a consumer complaint work?
            </span>

            <span class="chip">
                What is RTI?
            </span>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HISTORY
# ============================================================

elif page == "📚 History":

    st.markdown(
        """
        <div class="page-header">

            <h1>
                📚 My History
            </h1>

            <p>
                Your recent document uploads and legal questions.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


    if not st.session_state.history:

        st.markdown(
            """
            <div class="info-box">

                🗂️ <strong>No history yet.</strong>

                <br><br>

                Your uploaded documents and questions
                will appear here.

            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        for item in reversed(
            st.session_state.history
        ):

            st.markdown(
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
                        gap:14px;
                        flex-wrap:wrap;
                    ">

                        <div>

                            <div style="
                                font-size:12px;
                                color:#6366f1;
                                font-weight:600;
                                letter-spacing:0.5px;
                                text-transform:uppercase;
                            ">
                                {item["type"]}
                            </div>

                            <div style="
                                font-size:15px;
                                color:#101828;
                                font-weight:600;
                                margin-top:3px;
                            ">
                                {item["name"]}
                            </div>

                        </div>

                        <div style="
                            color:#98a2b3;
                            font-size:13px;
                        ">
                            {item["time"]}
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


        st.markdown(
            "<div style='height:14px;'></div>",
            unsafe_allow_html=True,
        )


        if st.button(
            "🗑️ Clear History",
            key="clear_history",
        ):

            st.session_state.history = []

            st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        ⚖️
        <strong style="color:#344054;">
            My Lawyer Friend
        </strong>

        · Legal information made simple

        <br>

        Built as an open-source CSE project ·
        Made with care for users in 🇮🇳 India

    </div>
    """,
    unsafe_allow_html=True,
)
