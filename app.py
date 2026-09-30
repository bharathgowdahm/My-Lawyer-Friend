import streamlit as st
from datetime import datetime
import html

# Optional PDF support
try:
    from pypdf import PdfReader
    PYPDF_AVAILABLE = True
except ImportError:
    PYPDF_AVAILABLE = False

# Optional Gemini support
try:
    from google import genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False


# ============================================================
# CONFIG
# ============================================================

APP_NAME = "My Lawyer Friend"
APP_VERSION = "2.0"
GEMINI_MODEL = "gemini-2.5-flash"

st.set_page_config(
    page_title=APP_NAME,
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>
:root {
    --primary: #16324f;
    --secondary: #0f766e;
    --accent: #d4a017;
    --bg: #f5f7fb;
    --card: #ffffff;
    --text: #172033;
    --muted: #64748b;
}

.stApp {
    background: var(--bg);
    color: var(--text);
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.hero {
    background: linear-gradient(135deg, #102a43 0%, #16324f 55%, #0f766e 100%);
    padding: 42px;
    border-radius: 24px;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 14px 35px rgba(15, 23, 42, 0.14);
}

.hero h1 {
    font-size: 44px;
    margin: 0 0 10px 0;
    font-weight: 800;
}

.hero p {
    font-size: 18px;
    line-height: 1.6;
    max-width: 850px;
    color: #e2e8f0;
}

.badge {
    display: inline-block;
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 999px;
    padding: 7px 13px;
    margin-bottom: 14px;
    font-size: 13px;
}

.card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 16px;
    box-shadow: 0 6px 20px rgba(15, 23, 42, 0.05);
}

.card h3 {
    margin-top: 0;
    color: #16324f;
}

.small-muted {
    color: #64748b;
    font-size: 14px;
}

.stat {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(15, 23, 42, 0.05);
}

.stat-num {
    font-size: 30px;
    font-weight: 800;
    color: #16324f;
}

.stat-label {
    color: #64748b;
    font-size: 14px;
    margin-top: 5px;
}

.disclaimer {
    background: #fff7ed;
    border-left: 5px solid #d4a017;
    padding: 16px 18px;
    border-radius: 10px;
    color: #7c4a03;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    padding: 35px 0 10px 0;
}

.stButton > button {
    border-radius: 10px;
    font-weight: 650;
}

@media (max-width: 700px) {
    .hero {
        padding: 28px 22px;
    }
    .hero h1 {
        font-size: 32px;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================

def get_secret(key, default=""):
    try:
        return st.secrets.get(key, default)
    except Exception:
        return default


GEMINI_API_KEY = get_secret("GEMINI_API_KEY", "").strip()

client = None
if GEMINI_API_KEY and GENAI_AVAILABLE:
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
    except Exception:
        client = None


def require_ai():
    if not GENAI_AVAILABLE:
        st.error("Google Gemini package is not installed.")
        st.code("google-genai")
        return False

    if not GEMINI_API_KEY:
        st.error("Gemini API key is not configured.")
        st.info("Add GEMINI_API_KEY in Streamlit Cloud → Settings → Secrets.")
        return False

    if client is None:
        st.error("Gemini client could not be initialized.")
        return False

    return True


def generate_ai(prompt):
    """Generate an answer from Gemini and show the real error if it fails."""
    if not require_ai():
        return None

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        text = getattr(response, "text", None)

        if not text:
            st.error("Gemini returned an empty response.")
            return None

        return text.strip()

    except Exception as exc:
        st.error("Gemini API Error")
        st.code(str(exc))
        return None


def add_history(category, title, content):
    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.insert(
        0,
        {
            "category": category,
            "title": title,
            "content": content,
            "time": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        },
    )

    st.session_state.history = st.session_state.history[:30]


def extract_pdf_text(uploaded_file):
    if not PYPDF_AVAILABLE:
        st.error("PDF support is not installed. Add pypdf to requirements.txt.")
        return ""

    try:
        reader = PdfReader(uploaded_file)
        pages = reader.pages[:200]

        chunks = []
        for page in pages:
            try:
                chunks.append(page.extract_text() or "")
            except Exception:
                continue

        text = "\n".join(chunks).strip()

        if not text:
            st.warning(
                "No selectable text was found. This may be a scanned/image-only PDF."
            )
            return ""

        return text[:60000]

    except Exception as exc:
        st.error("Could not read the PDF.")
        st.code(str(exc))
        return ""


def safe_text(value):
    return html.escape(str(value))


def show_disclaimer():
    st.markdown(
        """
<div class="disclaimer">
<strong>Important:</strong> My Lawyer Friend provides general legal information
and educational explanations. It is not a substitute for advice from a qualified
lawyer or official legal authority. For urgent or case-specific matters, consult
a lawyer and verify information with official sources.
</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "history" not in st.session_state:
    st.session_state.history = []


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("## ⚖️ My Lawyer Friend")
    st.caption(f"Version {APP_VERSION}")

    pages = [
        "Home",
        "Explain a Judgment",
        "Legal Q&A",
        "Search Cases",
        "Know Your Rights",
        "History",
        "About",
    ]

    selected_page = st.radio(
        "Navigation",
        pages,
        index=pages.index(st.session_state.page),
    )

    st.session_state.page = selected_page

    st.divider()

    st.markdown("### Quick status")

    if client:
        st.success("AI connected")
    elif not GENAI_AVAILABLE:
        st.warning("Gemini package missing")
    else:
        st.warning("AI key not configured")

    if PYPDF_AVAILABLE:
        st.success("PDF support ready")
    else:
        st.warning("PDF package missing")


page = st.session_state.page


# ============================================================
# HOME
# ============================================================

if page == "Home":
    st.markdown(
        """
<div class="hero">
    <div class="badge">🇮🇳 Indian Legal Information Platform</div>
    <h1>My Lawyer Friend ⚖️</h1>
    <p>
        Understand Indian legal concepts, judgments and everyday rights in
        simple language — with AI assistance and links to useful legal resources.
    </p>
</div>
""",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
<div class="stat">
<div class="stat-num">AI</div>
<div class="stat-label">Legal explanations</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
<div class="stat">
<div class="stat-num">PDF</div>
<div class="stat-label">Judgment analysis</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
<div class="stat">
<div class="stat-num">IN</div>
<div class="stat-label">India-focused resources</div>
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown("## What can you do?")

    a, b = st.columns(2)

    with a:
        st.markdown(
            """
<div class="card">
<h3>📄 Explain a Judgment</h3>
<p>Upload a text-based PDF judgment and get a structured plain-language explanation.</p>
</div>
""",
            unsafe_allow_html=True,
        )

        if st.button("Open Judgment Analyzer", use_container_width=True):
            st.session_state.page = "Explain a Judgment"
            st.rerun()

    with b:
        st.markdown(
            """
<div class="card">
<h3>🧠 Legal Q&A</h3>
<p>Ask general questions about Indian law and receive an educational explanation.</p>
</div>
""",
            unsafe_allow_html=True,
        )

        if st.button("Ask a Legal Question", use_container_width=True):
            st.session_state.page = "Legal Q&A"
            st.rerun()

    st.markdown("## Popular topics")

    topics = [
        "FIR and police complaints",
        "Consumer rights",
        "Cybercrime",
        "Women and child rights",
        "Traffic and vehicle laws",
        "Online fraud",
    ]

    cols = st.columns(3)
    for index, topic in enumerate(topics):
        with cols[index % 3]:
            st.markdown(
                f"""
<div class="card">
<h3>{safe_text(topic)}</h3>
<p class="small-muted">Ask the AI for a general explanation.</p>
</div>
""",
                unsafe_allow_html=True,
            )

    show_disclaimer()


# ============================================================
# EXPLAIN JUDGMENT
# ============================================================

elif page == "Explain a Judgment":
    st.title("📄 Explain a Judgment")
    st.write(
        "Upload a text-based PDF judgment. The AI will organize the document into "
        "plain-language sections."
    )

    uploaded = st.file_uploader(
        "Upload judgment PDF",
        type=["pdf"],
        help="Text-based PDFs work best.",
    )

    if uploaded:
        st.success(f"Selected: {uploaded.name}")

        if st.button("🤖 Analyze Judgment", type="primary"):
            if not require_ai():
                st.stop()

            with st.spinner("Reading and analyzing the judgment..."):
                pdf_text = extract_pdf_text(uploaded)

                if pdf_text:
                    prompt = f"""
You are an Indian legal information assistant.

Analyze the following judgment for educational purposes.

IMPORTANT:
- Do not present this as personalized legal advice.
- Do not invent facts, citations, statutes, dates, judges, holdings, or case details.
- If something is unclear from the document, say so.
- Explain difficult legal terminology in simple English.
- Clearly distinguish what the judgment says from your explanation.

Use these sections:

1. Case name and citation
2. Court and date
3. Parties
4. Background facts
5. Legal questions/issues
6. Relevant laws and sections
7. Arguments/positions mentioned
8. Court's reasoning
9. Decision/holding
10. Important observations
11. Practical meaning
12. Key takeaways
13. Important limitations or uncertainties

Judgment text:
{pdf_text}
"""

                    answer = generate_ai(prompt)

                    if answer:
                        st.markdown("## Analysis")
                        st.markdown(answer)

                        add_history(
                            "Judgment",
                            uploaded.name,
                            answer,
                        )

                        st.download_button(
                            "⬇️ Download explanation",
                            data=answer,
                            file_name="judgment_explanation.txt",
                            mime="text/plain",
                        )

    show_disclaimer()


# ============================================================
# LEGAL Q&A
# ============================================================

elif page == "Legal Q&A":
    st.title("🧠 Legal Q&A")
    st.write("Ask a general legal-information question.")

    suggestions = [
        "What is an FIR in India?",
        "What are basic consumer rights?",
        "What should I do after an online fraud?",
        "What is a legal notice?",
        "What is the difference between civil and criminal cases?",
        "What are basic cybercrime reporting options?",
    ]

    selected_suggestion = st.selectbox(
        "Choose an example or write your own question",
        [""] + suggestions,
    )

    question = st.text_area(
        "Your question",
        value=selected_suggestion,
        height=130,
        placeholder="Example: What is an FIR in India?",
    )

    if st.button("🤖 Get Explanation", type="primary"):
        if not question.strip():
            st.warning("Please enter a question.")
        elif require_ai():
            prompt = f"""
You are My Lawyer Friend, an Indian legal information assistant.

Answer this question for educational purposes:

{question}

Rules:
- Focus on Indian law unless the user specifies another jurisdiction.
- Use simple language.
- Do not pretend to be the user's lawyer.
- Do not give personalized legal advice.
- Do not invent sections, cases, deadlines, procedures, or penalties.
- Where current law may matter, tell the user to verify with an official source or qualified lawyer.
- If the question is unclear, state the assumption you are making.
- Structure the answer with headings and bullet points when useful.
"""

            with st.spinner("Preparing explanation..."):
                answer = generate_ai(prompt)

            if answer:
                st.markdown("## Answer")
                st.markdown(answer)

                add_history(
                    "Legal Q&A",
                    question.strip(),
                    answer,
                )

    show_disclaimer()


# ============================================================
# SEARCH CASES
# ============================================================

elif page == "Search Cases":
    st.title("🔎 Search Legal Resources")

    st.info(
        "Live court-database integration is not enabled in this version. "
        "Use the trusted resources below for direct searching."
    )

    keyword = st.text_input(
        "What are you looking for?",
        placeholder="Example: consumer complaint, bail, cybercrime",
    )

    court = st.selectbox(
        "Court / source",
        [
            "All",
            "Supreme Court of India",
            "eCourts",
            "India Code",
            "Indian Kanoon",
            "NHRC",
            "NCW",
        ],
    )

    if keyword:
        st.markdown("### Suggested search")
        st.code(f"{keyword} {court if court != 'All' else ''}".strip())

    resources = [
        (
            "Supreme Court of India",
            "Official Supreme Court website and case-related information.",
            "https://www.sci.gov.in/",
        ),
        (
            "eCourts",
            "Indian judiciary services and case information.",
            "https://ecourts.gov.in/",
        ),
        (
            "India Code",
            "Central laws and legislation database.",
            "https://www.indiacode.nic.in/",
        ),
        (
            "Indian Kanoon",
            "Legal database for searching judgments and legal materials.",
            "https://indiankanoon.org/",
        ),
        (
            "National Human Rights Commission",
            "Human-rights information and complaint resources.",
            "https://nhrc.nic.in/",
        ),
        (
            "National Commission for Women",
            "Information and resources relating to women's rights.",
            "https://www.ncw.gov.in/",
        ),
    ]

    for name, description, url in resources:
        st.markdown(
            f"""
<div class="card">
<h3>{safe_text(name)}</h3>
<p>{safe_text(description)}</p>
<a href="{safe_text(url)}" target="_blank">Open resource →</a>
</div>
""",
            unsafe_allow_html=True,
        )


# ============================================================
# KNOW YOUR RIGHTS
# ============================================================

elif page == "Know Your Rights":
    st.title("🛡️ Know Your Rights")

    categories = [
        "All",
        "Police",
        "Consumers",
        "Cyber Safety",
        "Women",
        "General",
    ]

    category = st.selectbox("Filter by category", categories)

    rights = [
        (
            "Police",
            "FIR basics",
            "An FIR is a formal record of information relating to a cognizable offence. Procedures and circumstances can vary, so verify the current law and official police guidance.",
        ),
        (
            "Consumers",
            "Consumer complaints",
            "Consumers can use India's consumer-protection mechanisms for eligible disputes involving goods or services.",
        ),
        (
            "Cyber Safety",
            "Online fraud",
            "For suspected financial cyber fraud, act quickly and use official cybercrime reporting and banking channels.",
        ),
        (
            "Women",
            "Safety and support",
            "There are legal protections and government support mechanisms for women facing harassment, violence or other offences.",
        ),
        (
            "General",
            "Legal assistance",
            "People who cannot afford private legal representation may be eligible for legal-aid services depending on applicable rules.",
        ),
    ]

    filtered = rights if category == "All" else [
        item for item in rights if item[0] == category
    ]

    for item_category, title, description in filtered:
        st.markdown(
            f"""
<div class="card">
<div class="small-muted">{safe_text(item_category)}</div>
<h3>{safe_text(title)}</h3>
<p>{safe_text(description)}</p>
</div>
""",
            unsafe_allow_html=True,
        )

    show_disclaimer()


# ============================================================
# HISTORY
# ============================================================

elif page == "History":
    st.title("🕘 History")

    if not st.session_state.history:
        st.info("No activity in this session yet.")
    else:
        if st.button("Clear session history"):
            st.session_state.history = []
            st.rerun()

        for item in st.session_state.history:
            with st.expander(
                f"{item['category']} — {item['title']} — {item['time']}"
            ):
                st.markdown(item["content"])


# ============================================================
# ABOUT
# ============================================================

elif page == "About":
    st.title("ℹ️ About My Lawyer Friend")

    st.markdown(
        """
<div class="card">
<h3>Mission</h3>
<p>
Make Indian legal information easier to understand for students and ordinary
users through a simple, responsible interface.
</p>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
### Current features

- AI-powered general legal Q&A
- PDF judgment explanation
- Legal-resource directory
- Rights information
- Session history
- Mobile-friendly interface

### Planned improvements

- Verified case-search integration
- Better scanned-PDF/OCR support
- Source citations
- User accounts
- Saved documents
- Multilingual support
- Stronger privacy controls
- Official API integrations where permitted
"""
    )

    show_disclaimer()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">
    My Lawyer Friend · Educational legal-information project ·
    Not a substitute for professional legal advice
</div>
""",
    unsafe_allow_html=True,
)
