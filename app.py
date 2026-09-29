import streamlit as st
from datetime import datetime
from pypdf import PdfReader

try:
    from google import genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False


# ============================================================
# MY LAWYER FRIEND — V1.2
# Premium Indian Legal Information Platform
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
# AI CONFIG  (safe for local dev — no secrets.toml required)
# ============================================================

def _get_secret(key, default=""):
    try:
        return st.secrets.get(key, default)
    except Exception:
        return default


GEMINI_API_KEY = _get_secret("GEMINI_API_KEY", "")

client = None
if GEMINI_API_KEY and GENAI_AVAILABLE:
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
    except Exception:
        client = None


# ============================================================
# SESSION STATE
# ============================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "page" not in st.session_state:
    st.session_state.page = "Home"

# Guard: if page was set to an invalid value, reset
PAGES = [
    "Home",
    "Explain a Judgment",
    "Legal Q&A",
    "Search Cases",
    "Know Your Rights",
    "History",
    "About",
]
if st.session_state.page not in PAGES:
    st.session_state.page = "Home"


# ============================================================
# PREMIUM CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 0%, rgba(99,102,241,.07), transparent 30%),
        radial-gradient(circle at 100% 100%, rgba(245,158,11,.06), transparent 30%),
        #f7f8fc;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
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
    padding: 8px 12px;
    border-radius: 10px;
    transition: background .2s ease;
    font-weight: 500;
    font-size: 14.5px;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,.06);
}

section[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,.08) !important;
}


/* ============================================================
   HERO
   ============================================================ */

.hero-box {
    background: linear-gradient(135deg, #0b1220 0%, #162544 55%, #254b7a 100%);
    border-radius: 28px;
    padding: 48px;
    color: white;
    box-shadow: 0 25px 60px rgba(15,23,42,.20);
    margin-bottom: 32px;
}

.hero-small {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 30px;
    background: rgba(255,255,255,.10);
    border: 1px solid rgba(255,255,255,.15);
    font-size: 13px;
    margin-bottom: 18px;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -1.5px;
    margin: 0;
}

.hero-highlight {
    color: #fbbf24;
}

.hero-description {
    max-width: 700px;
    color: #cbd5e1;
    font-size: 17px;
    line-height: 1.7;
    margin-top: 18px;
}


/* ============================================================
   SECTION HEADERS
   ============================================================ */

.section-title {
    font-size: 27px;
    font-weight: 800;
    color: #101828;
    margin-top: 35px;
    margin-bottom: 7px;
    letter-spacing: -0.5px;
}

.section-subtitle {
    color: #667085;
    margin-bottom: 20px;
    font-size: 15px;
}


/* ============================================================
   CARDS
   ============================================================ */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border: 1px solid #eaecf0;
    border-radius: 20px;
    box-shadow: 0 5px 20px rgba(16,24,40,.05);
    transition: transform .2s ease, box-shadow .2s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 35px rgba(16,24,40,.10);
}


/* ============================================================
   BUTTONS
   ============================================================ */

.stButton > button {
    border-radius: 12px;
    min-height: 45px;
    font-weight: 600;
    border: 1px solid #d0d5dd;
    transition: all .2s ease;
}

.stButton > button:hover {
    border-color: #6366f1;
    color: #4338ca;
    transform: translateY(-1px);
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #101828, #263f63);
    color: white;
    border: none;
    box-shadow: 0 6px 18px rgba(16,24,40,.18);
}

.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #18263d, #2d4a75);
    transform: translateY(-2px);
    box-shadow: 0 10px 24px rgba(16,24,40,.28);
}


/* ============================================================
   INPUTS
   ============================================================ */

.stTextInput input,
.stTextArea textarea {
    border-radius: 12px !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,.12) !important;
}


/* ============================================================
   ALERT BOXES
   ============================================================ */

.warning-box {
    background: #fffbeb;
    border: 1px solid #fcd34d;
    border-left: 5px solid #f59e0b;
    padding: 20px 24px;
    border-radius: 14px;
    color: #78350f;
    line-height: 1.65;
    margin-top: 20px;
}

.info-box {
    background: #eef2ff;
    border: 1px solid #c7d2fe;
    border-left: 5px solid #6366f1;
    padding: 20px 24px;
    border-radius: 14px;
    color: #312e81;
    line-height: 1.65;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    color: #98a2b3;
    padding-top: 40px;
    margin-top: 60px;
    border-top: 1px solid #eaecf0;
    line-height: 1.8;
    font-size: 13.5px;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px) {
    .block-container { padding: 1rem; }
    .hero-box { padding: 30px 24px; border-radius: 22px; }
    .hero-title { font-size: 34px; }
    .hero-description { font-size: 15px; }
    .section-title { font-size: 23px; }
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================

def add_history(category: str, text: str) -> None:
    st.session_state.history.append(
        {
            "category": category,
            "text": text,
            "time": datetime.now().strftime("%d %b %Y · %I:%M %p"),
        }
    )


def go_to(page_name: str) -> None:
    """Safe navigation helper — call BEFORE st.rerun()."""
    if page_name in PAGES:
        st.session_state.page = page_name


def require_ai() -> bool:
    """Returns True if AI client is available; else shows an error."""
    if not GENAI_AVAILABLE:
        st.error("Missing dependency: `google-genai`. Run `pip install google-genai`.")
        return False
    if not GEMINI_API_KEY:
        st.error("Gemini API key is not configured.")
        st.info(
            "Add `GEMINI_API_KEY` under **Streamlit Cloud → Manage app → "
            "Settings → Secrets**, or in a local `.streamlit/secrets.toml` file."
        )
        return False
    if client is None:
        st.error("AI client could not be initialised. Please check the API key.")
        return False
    return True


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="display:flex;align-items:center;gap:12px;padding:4px 0 8px 0;">
            <div style="width:44px;height:44px;border-radius:12px;
                        background:linear-gradient(135deg,#6366f1,#f59e0b);
                        display:flex;align-items:center;justify-content:center;
                        font-size:22px;">⚖️</div>
            <div>
                <div style="font-size:17px;font-weight:800;letter-spacing:-0.3px;">
                    My Lawyer Friend
                </div>
                <div style="color:#98a2b3;font-size:12.5px;margin-top:1px;">
                    Legal info, made simple
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # --- Navigation (fully synced with session_state) ---
    selected = st.radio(
        "Navigation",
        PAGES,
        index=PAGES.index(st.session_state.page),
        label_visibility="collapsed",
        key="nav_radio",
    )

    # Sync session_state when user clicks a radio option
    if selected != st.session_state.page:
        st.session_state.page = selected

    st.divider()

    st.markdown(
        """
        <div style="background:rgba(255,255,255,.04);
                    border:1px solid rgba(255,255,255,.08);
                    border-radius:12px;padding:14px;
                    font-size:12.5px;line-height:1.6;color:#cbd5e1;">
            🇮🇳 <strong style="color:#fbbf24;">Built for users in India.</strong><br>
            Provides general legal information — not a substitute
            for a qualified lawyer.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption("My Lawyer Friend · v1.2")


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    st.markdown(
        """
        <div class="hero-box">
            <div class="hero-small">🇮🇳 &nbsp; Indian Legal Information Platform</div>
            <div class="hero-title">
                Your legal questions.<br>
                <span class="hero-highlight">Made simple.</span>
            </div>
            <div class="hero-description">
                My Lawyer Friend helps ordinary people understand legal
                information, court judgments and everyday legal concepts
                without complicated terminology.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---------- Quick actions ----------
    st.markdown('<div class="section-title">🚀 Quick actions</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Start with one of the tools below.</div>',
        unsafe_allow_html=True,
    )

    q1, q2, q3 = st.columns(3)

    with q1:
        if st.button("📄 Explain Judgment", use_container_width=True, type="primary"):
            go_to("Explain a Judgment")
            st.rerun()

    with q2:
        if st.button("🧠 Ask Legal Question", use_container_width=True, type="primary"):
            go_to("Legal Q&A")
            st.rerun()

    with q3:
        if st.button("🔍 Search Cases", use_container_width=True, type="primary"):
            go_to("Search Cases")
            st.rerun()

    # ---------- Features ----------
    st.markdown('<div class="section-title">✨ What can you do here?</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Simple tools designed for common legal-information needs.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.markdown("### 📄 Explain a Judgment")
            st.write(
                "Upload a court judgment and understand its important "
                "points in simpler language."
            )
            if st.button("Open tool →", key="home_judgment", use_container_width=True):
                go_to("Explain a Judgment")
                st.rerun()

    with c2:
        with st.container(border=True):
            st.markdown("### 🧠 Legal Q&A")
            st.write(
                "Ask general legal-information questions and explore "
                "clear, plain-language explanations."
            )
            if st.button("Ask a question →", key="home_qa", use_container_width=True):
                go_to("Legal Q&A")
                st.rerun()

    with c3:
        with st.container(border=True):
            st.markdown("### 🔍 Search Cases")
            st.write(
                "Search for Indian court cases by topic, keyword or case name."
            )
            if st.button("Search cases →", key="home_search", use_container_width=True):
                go_to("Search Cases")
                st.rerun()

    # ---------- Topics ----------
    st.markdown('<div class="section-title">🔥 Popular topics</div>', unsafe_allow_html=True)

    topics = [
        "Consumer Rights",
        "Property",
        "FIR & Police",
        "Cyber Crime",
        "Family Law",
        "Employment",
        "RTI",
        "Fundamental Rights",
        "Cheque Bounce",
    ]

    cols = st.columns(3)
    for i, topic in enumerate(topics):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"**{topic}**")
                st.caption("Explore general legal information")

    # ---------- Audience ----------
    st.markdown('<div class="section-title">👥 Built for everyone</div>', unsafe_allow_html=True)

    a, b, c = st.columns(3)
    with a:
        with st.container(border=True):
            st.markdown("### 👨‍👩‍👧 Common People")
            st.write("Understand legal terminology and everyday legal concepts more easily.")
    with b:
        with st.container(border=True):
            st.markdown("### 🎓 Students")
            st.write("Learn from simplified explanations of legal concepts and judgments.")
    with c:
        with st.container(border=True):
            st.markdown("### 💼 Professionals")
            st.write("Quickly explore general information before consulting a professional.")

    # ---------- Disclaimer ----------
    st.markdown(
        """
        <div class="warning-box">
            <strong>⚠️ Important</strong><br><br>
            My Lawyer Friend provides general legal information for
            educational and informational purposes.<br><br>
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
    st.write("Upload an Indian court judgment and get a plain-language explanation.")

    uploaded = st.file_uploader(
        "Choose a judgment PDF",
        type=["pdf"],
        help="Upload a court judgment PDF (max ~200 MB).",
    )

    if uploaded:

        size_kb = uploaded.size / 1024
        st.success(f"✅ {uploaded.name} uploaded successfully")
        st.caption(f"File size: {size_kb:,.1f} KB")
        st.divider()

        if st.button("🔎 Analyze Judgment", use_container_width=True, type="primary"):

            if not require_ai():
                st.stop()

            try:
                # ---------- PDF extraction ----------
                with st.spinner("📖 Reading the judgment..."):
                    reader = PdfReader(uploaded)
                    pages_text = []
                    # Cap pages to avoid memory blow-ups
                    MAX_PAGES = 200
                    for i, pdf_page in enumerate(reader.pages):
                        if i >= MAX_PAGES:
                            break
                        try:
                            text = pdf_page.extract_text() or ""
                        except Exception:
                            text = ""
                        if text.strip():
                            pages_text.append(text)

                    document_text = "\n".join(pages_text)

                if not document_text.strip():
                    st.error("I couldn't extract readable text from this PDF.")
                    st.info(
                        "This may be a scanned/image-only PDF. "
                        "OCR support can be added in a later version."
                    )
                    st.stop()

                # ---------- Trim for token safety ----------
                MAX_CHARS = 60000
                document_text = document_text[:MAX_CHARS]

                prompt = f"""
You are "My Lawyer Friend", an Indian legal-information assistant.

Analyze the court judgment below and explain it in simple language
for an ordinary person.

IMPORTANT RULES:
- Do not claim to be the user's lawyer.
- Do not provide personalized legal advice.
- Do not invent facts.
- Only use information contained in the document.
- If something is unavailable, say: "Not stated in the document."
- Preserve important legal terms, sections and case names.
- Clearly distinguish the court's decision from general explanation.

Use these sections:

# 1. CASE TITLE
# 2. COURT
# 3. DATE
# 4. PARTIES
# 5. CASE BACKGROUND
# 6. IMPORTANT FACTS
# 7. LEGAL ISSUES
# 8. ARGUMENTS
# 9. IMPORTANT LAWS / SECTIONS
# 10. COURT'S REASONING
# 11. FINAL DECISION
# 12. SIMPLE EXPLANATION
# 13. IMPORTANT TAKEAWAYS

COURT JUDGMENT:

{document_text}
"""

                with st.spinner("⚖️ Analyzing the judgment..."):
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt,
                    )

                analysis = response.text if getattr(response, "text", None) else "No analysis was returned."

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

                add_history("Judgment Analysis", uploaded.name)

                st.divider()
                st.warning(
                    "⚠️ This AI-generated explanation is for general "
                    "educational/informational purposes. Verify important "
                    "information against the original judgment and consult "
                    "a qualified lawyer for advice about a specific matter."
                )

            except Exception as error:
                st.error("Something went wrong while analyzing the judgment.")
                st.caption(f"Technical details: {error}")

    else:
        st.info("📌 Upload a court judgment PDF to begin.")
        st.markdown("### What you'll get")

        features = [
            "📌 Case title and court",
            "👥 Parties involved",
            "📖 Background and facts",
            "⚖️ Legal issues",
            "🗣️ Arguments",
            "📚 Important laws and sections",
            "🧠 Court's reasoning",
            "🏛️ Final decision",
            "💡 Simple-language explanation",
            "📝 Key takeaways",
        ]
        for feature in features:
            st.write(feature)


# ============================================================
# LEGAL Q&A
# ============================================================

elif st.session_state.page == "Legal Q&A":

    st.title("🧠 Legal Q&A")
    st.write("Ask a general legal-information question in simple language.")

    question = st.text_area(
        "Your question",
        placeholder="Example: What is an FIR and when can a person file one?",
        height=140,
    )

    if st.button("🤖 Get Explanation", use_container_width=True, type="primary"):

        if not question.strip():
            st.warning("Please enter a question first.")

        elif not require_ai():
            st.stop()

        else:
            try:
                prompt = f"""
You are My Lawyer Friend, an Indian legal-information assistant.

Answer this question for an ordinary person.

Question:
{question}

Rules:
- Provide general legal information only.
- Do not claim to be the user's lawyer.
- Do not create a lawyer-client relationship.
- Do not give personalized legal advice.
- Do not invent laws or facts.
- Explain important legal concepts simply.
- Mention that laws can change.
- Encourage checking official sources for important matters.
"""

                with st.spinner("🧠 Preparing an explanation..."):
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt,
                    )

                answer = response.text if getattr(response, "text", None) else "No answer was returned."

                st.success("Explanation generated")
                st.markdown(answer)

                add_history("Legal Q&A", question)

                st.warning(
                    "⚠️ General legal information only. For a specific legal "
                    "matter, consult a qualified legal professional."
                )

            except Exception as error:
                st.error("Unable to generate the explanation.")
                st.caption(f"Technical details: {error}")


# ============================================================
# SEARCH CASES
# ============================================================

elif st.session_state.page == "Search Cases":

    st.title("🔍 Search Cases")
    st.write(
        "Search tools will connect to public/official legal sources "
        "in a future version."
    )

    search = st.text_input(
        "Case name or keyword",
        placeholder="Example: consumer protection",
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

    if st.button("🔍 Search", use_container_width=True, type="primary"):
        if not search.strip():
            st.warning("Enter a search term.")
        else:
            add_history("Case Search", search)
            st.info("🔧 Live Indian case-data integration will be added in v1.3.")
            st.write(f"Search term: **{search}**")
            st.write(f"Court filter: **{court}**")


# ============================================================
# KNOW YOUR RIGHTS
# ============================================================

elif st.session_state.page == "Know Your Rights":

    st.title("⚖️ Know Your Rights")
    st.write("Explore general legal-information topics.")

    rights = {
        "🚔 Police & FIR":
            "General information about complaints, FIRs and police procedures.",
        "🛍️ Consumer Rights":
            "General information about consumer complaints and consumer protection.",
        "💻 Cyber Crime":
            "General information about online fraud, cybercrime and reporting.",
        "🏠 Property":
            "General information about property-related legal concepts.",
        "💼 Employment":
            "General information about workplace and employment-related legal concepts.",
        "📄 RTI":
            "General information about the Right to Information framework.",
    }

    for title, description in rights.items():
        with st.container(border=True):
            st.markdown(f"### {title}")
            st.write(description)
            st.caption("General information only — verify with official sources.")


# ============================================================
# HISTORY
# ============================================================

elif st.session_state.page == "History":

    st.title("📚 History")
    st.write("Your recent activity in this session.")

    if not st.session_state.history:
        st.info("No activity yet.")
    else:
        for item in reversed(st.session_state.history):
            with st.container(border=True):
                st.caption(f"{item['category']} · {item['time']}")
                st.write(item["text"])

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
    st.write(
        """
        **My Lawyer Friend** is a student-built legal-information platform
        designed to make legal concepts easier to understand.
        """
    )

    st.divider()
    st.subheader("🎯 Vision")
    st.write(
        "Make useful legal information easier to discover and understand "
        "for ordinary users."
    )

    st.subheader("🚀 Project roadmap")

    roadmap = [
        ("v1.0", "Premium UI and navigation"),
        ("v1.1", "Judgment upload + Q&A interface"),
        ("v1.2", "AI document analysis"),
        ("v1.3", "Indian case-data integration"),
        ("v1.4", "Official legal-source updates"),
        ("v1.5", "User accounts and saved cases"),
        ("v2.0", "Advanced legal research assistant"),
    ]

    for version, feature in roadmap:
        with st.container(border=True):
            st.markdown(f"**{version}** — {feature}")

    st.divider()
    st.subheader("👨‍💻 Project")
    st.write("Built as a CSE student portfolio project.")
    st.code(
        "My Lawyer Friend\n"
        "Indian Legal Information Platform\n"
        "Version 1.2"
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
