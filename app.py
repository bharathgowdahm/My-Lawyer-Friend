import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="My Lawyer Friend",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: #f7f8fc;
    }

    /* Remove Streamlit top spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem;
        max-width: 1250px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #101828;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Hero */
    .hero {
        background: linear-gradient(
            135deg,
            #101828 0%,
            #18263d 55%,
            #263f63 100%
        );
        padding: 55px 50px;
        border-radius: 28px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 15px 40px rgba(16, 24, 40, 0.18);
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.18);
        padding: 8px 15px;
        border-radius: 30px;
        font-size: 14px;
        margin-bottom: 20px;
    }

    .hero-title {
        font-size: 48px;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 15px;
    }

    .hero-text {
        font-size: 18px;
        color: #d0d5dd;
        max-width: 720px;
        line-height: 1.6;
    }

    /* Feature cards */
    .card {
        background: white;
        border: 1px solid #eaecf0;
        border-radius: 20px;
        padding: 25px;
        min-height: 190px;
        box-shadow: 0 8px 25px rgba(16,24,40,0.05);
        transition: 0.2s ease;
    }

    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 14px 35px rgba(16,24,40,0.10);
    }

    .icon {
        font-size: 30px;
        margin-bottom: 12px;
    }

    .card-title {
        font-size: 19px;
        font-weight: 700;
        color: #101828;
        margin-bottom: 8px;
    }

    .card-text {
        color: #667085;
        line-height: 1.5;
        font-size: 14px;
    }

    /* Section title */
    .section-title {
        font-size: 28px;
        font-weight: 750;
        color: #101828;
        margin-top: 35px;
        margin-bottom: 20px;
    }

    /* Disclaimer */
    .disclaimer {
        background: #fffaeb;
        border: 1px solid #fedf89;
        border-radius: 18px;
        padding: 20px;
        margin-top: 30px;
        color: #7a2e0b;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #98a2b3;
        margin-top: 60px;
        padding-top: 25px;
        border-top: 1px solid #eaecf0;
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div style="font-size:28px;font-weight:800;">
        ⚖️ My Lawyer Friend
        </div>
        <div style="color:#98a2b3;margin-top:5px;">
        Legal information made simple
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### Navigation")

    st.page_link(
        "app.py",
        label="🏠 Home",
    )

    st.markdown("📄 Explain a Judgment")
    st.markdown("🔍 Search Cases")
    st.markdown("⚖️ Know Your Rights")
    st.markdown("🧠 Ask Legal Questions")
    st.markdown("📚 My History")

    st.divider()

    st.caption("🇮🇳 Built for users in India")

# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------

st.markdown(
    """
    <div class="hero">

        <div class="hero-badge">
            🇮🇳 Indian Legal Information Platform
        </div>

        <div class="hero-title">
            Your legal questions,<br>
            explained simply.
        </div>

        <div class="hero-text">
            My Lawyer Friend helps you understand court judgments,
            legal documents and everyday legal concepts using
            clear and simple language.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# QUICK ACTIONS
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">What do you need help with?</div>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <div class="icon">📄</div>
            <div class="card-title">
                Explain a Judgment
            </div>
            <div class="card-text">
                Upload a court judgment and understand
                the important points in simpler language.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <div class="icon">🔍</div>
            <div class="card-title">
                Search Cases
            </div>
            <div class="card-text">
                Find useful information about Indian
                court cases and judgments.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <div class="icon">🧠</div>
            <div class="card-title">
                Ask a Legal Question
            </div>
            <div class="card-text">
                Ask questions about legal concepts
                and receive easy-to-understand explanations.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# SECOND SECTION
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">Built for everyone</div>',
    unsafe_allow_html=True,
)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown(
        """
        <div class="card">
            <div class="icon">👨‍👩‍👧</div>
            <div class="card-title">
                Common People
            </div>
            <div class="card-text">
                Understand legal documents without
                needing to know complicated legal terminology.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col5:
    st.markdown(
        """
        <div class="card">
            <div class="icon">🎓</div>
            <div class="card-title">
                Students
            </div>
            <div class="card-text">
                Learn how real court decisions work
                through simplified explanations.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col6:
    st.markdown(
        """
        <div class="card">
            <div class="icon">💼</div>
            <div class="card-title">
                Professionals
            </div>
            <div class="card-text">
                Quickly identify important information
                inside lengthy legal documents.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# DISCLAIMER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="disclaimer">
        <strong>⚠️ Important</strong><br><br>
        My Lawyer Friend provides general legal information
        for educational purposes. It does not provide legal
        representation or replace advice from a qualified lawyer.
        Always verify important information using the original
        legal source and seek professional advice when necessary.
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        ⚖️ My Lawyer Friend · Legal information made simple<br>
        Built as an open-source CSE project
    </div>
    """,
    unsafe_allow_html=True,
)
