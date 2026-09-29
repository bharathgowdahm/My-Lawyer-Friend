import streamlit as st
from datetime import datetime
import tempfile
import os
import requests

# ---------- PDF ----------
try:
    from pypdf import PdfReader
    PYPDF_AVAILABLE = True
except ImportError:
    PYPDF_AVAILABLE = False

# ---------- Gemini ----------
try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

# ---------- RAG ----------
try:
    from langchain_community.document_loaders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
    from langchain_community.vectorstores import FAISS
    from langchain.chains import RetrievalQA
    RAG_AVAILABLE = True
except ImportError:
    RAG_AVAILABLE = False


# ============================================================
# MY LAWYER FRIEND — V2.0
# Integrated: Gemini 3.8 Flash + Indian Kanoon + RAG
# ============================================================

st.set_page_config(
    page_title="My Lawyer Friend",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

APP_NAME = "My Lawyer Friend"
APP_VERSION = "2.0"
GEMINI_MODEL = "gemini-3.8-flash"

PAGES = [
    "Home",
    "Explain a Judgment",
    "Document Q&A",
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
INDIAN_KANOON_API_KEY = get_secret("INDIAN_KANOON_API_KEY", "")

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
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None
if "qa_file" not in st.session_state:
    st.session_state.qa_file = None
if "qa_history" not in st.session_state:
    st.session_state.qa_history = []

if st.session_state.page not in PAGES:
    st.session_state.page = "Home"


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
        radial-gradient(circle at 5% 0%, rgba(99,102,241,.08), transparent 28%),
        radial-gradient(circle at 100% 100%, rgba(245,158,11,.06), transparent 30%),
        #f6f7fb;
}

.block-container {
    max-width: 1280px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #08111f 0%, #0b1220 100%);
    border-right: 1px solid rgba(255,255,255,.05);
}
section[data-testid="stSidebar"] * { color: #e5e7eb; }
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

/* HERO */
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

/* SECTION */
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

/* IMAGE CARDS */
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

/* BUTTONS */
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

/* INPUTS */
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

/* ALERT BOXES */
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

/* FOOTER */
.footer {
    text-align: center;
    color: #667085 !important;
    padding-top: 40px;
    margin-top: 60px;
    border-top: 1px solid #e4e7ec;
    line-height: 1.8;
    font-size: 13px;
}

@media (max-width: 700px) {
    .block-container { padding: 1rem .85rem 3rem .85rem; }
    .hero { padding: 32px 22px; border-radius: 22px; }
    .hero-title { font-size: 34px; letter-spacing: -1px; }
    .hero-description { font-size: 14px; line-height: 1.65; }
    .section-title { font-size: 22px; margin-top: 28px; }
    .img-card-banner { height: 100px; }
    .img-card-icon { font-size: 42px; }
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================

def image_card(icon, title, text, theme="bg-indigo", tag=None):
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
        return False
    if not GEMINI_API_KEY:
        st.error("Gemini API key is not configured.")
        st.info("Add `GEMINI_API_KEY` in Streamlit Cloud → Settings → Secrets.")
        return False
    if client is None:
        st.error("Gemini client could not be initialized.")
        return False
    return True


def generate_ai(prompt, thinking_level="medium"):
    """Send prompt to Gemini 3.8 Flash with thinking level control."""
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_level=thinking_level
            )
        )
    )
    return getattr(response, "text", None) or "No response was returned."


def extract_pdf_text(uploaded_file):
    if not PYPDF_AVAILABLE:
        raise ImportError("pypdf is not installed.")
    reader = PdfReader(uploaded_file)
    parts = []
    for i, page in enumerate(reader.pages):
        if i >= 200:
            break
        try:
            t = page.extract_text() or ""
        except Exception:
            t = ""
        if t.strip():
            parts.append(t)
    return "\n\n".join(parts)


# ============================================================
# INDIAN KANOON SEARCH
# ============================================================

def search_indian_kanoon(query, page=0):
    """Search Indian Kanoon case database."""
    if not INDIAN_KANOON_API_KEY:
        return None, "Indian Kanoon API key not configured."

    url = "https://api.indiankanoon.org/search/"
    headers = {
        "Authorization": f"Token {INDIAN_KANOON_API_KEY}",
        "Accept": "application/json",
    }
    params = {
        "formInput": query,
        "pagenum": str(page),
    }

    try:
        response = requests.post(url, headers=headers, params=params, timeout=15)
        if response.status_code == 200:
            return response.json(), None
        elif response.status_code == 403:
            return None, "Invalid API key or insufficient credits."
        else:
            return None, f"API returned status {response.status_code}"
    except requests.exceptions.Timeout:
        return None, "Search request timed out. Please try again."
    except Exception as e:
        return None, f"Search failed: {str(e)}"


def render_case_cards(docs):
    """Render Indian Kanoon search results as image cards."""
    if not docs:
        st.info("No cases found. Try different keywords.")
        return

    cols = st.columns(3)
    for i, doc in enumerate(docs[:9]):
        with cols[i % 3]:
            title = doc.get("title", "Unknown Case")
            if len(title) > 70:
                title = title[:70] + "..."

            court = doc.get("docsource", "Court not specified")
            doc_id = doc.get("tid")

            image_card(
                icon="📜",
                title=title,
                text=f"<strong>Court:</strong> {court}",
                theme="bg-indigo",
                tag="CASE LAW"
            )

            if doc_id:
                url = f"https://indiankanoon.org/doc/{doc_id}/"
                st.link_button("View Full Judgment →", url, use_container_width=True)


# ============================================================
# RAG: PDF DOCUMENT Q&A
# ============================================================

def build_qa_chain(uploaded_file):
    """Build RAG chain for uploaded PDF."""
    if not RAG_AVAILABLE:
        raise ImportError("RAG dependencies not installed.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    try:
        loader = PyPDFLoader(tmp_path)
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = splitter.split_documents(docs)

        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=GEMINI_API_KEY
        )
        vectorstore = FAISS.from_documents(chunks, embeddings)

        llm = ChatGoogleGenerativeAI(
            model=GEMINI_MODEL,
            google_api_key=GEMINI_API_KEY
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
            return_source_documents=True
        )

        return qa_chain
    finally:
        os.unlink(tmp_path)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div style="display:flex;align-items:center;gap:12px;padding:5px 0 10px 0;">
            <div style="width:44px;height:44px;border-radius:13px;
                        background:linear-gradient(135deg,#6366f1,#f59e0b);
                        display:flex;align-items:center;justify-content:center;
                        font-size:22px;">⚖️</div>
            <div>
                <div style="font-size:17px;font-weight:800;">My Lawyer Friend</div>
                <div style="color:#98a2b3;font-size:12px;margin-top:2px;">
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
        <div style="background:rgba(255,255,255,.04);
                    border:1px solid rgba(255,255,255,.08);
                    border-radius:14px;padding:15px;
                    font-size:12px;line-height:1.65;color:#cbd5e1;">
            🇮🇳 <strong style="color:#fbbf24;">Built for India</strong>
            <br><br>
            General legal information for educational
            and informational purposes.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(f"{APP_NAME} · v{APP_VERSION}")


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-badge">🇮🇳 &nbsp; Indian Legal Information Platform</div>
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
        if st.button("💬 Document Q&A", key="quick_docqa", type="primary"):
            go_to("Document Q&A")
            st.rerun()
    with q3:
        if st.button("🔍 Search Cases", key="quick_cases", type="primary"):
            go_to("Search Cases")
            st.rerun()

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
            "Upload a court judgment PDF and get a structured, plain-language explanation.",
            theme="bg-indigo",
            tag="AI POWERED",
        )
        if st.button("Open tool →", key="feature_judgment"):
            go_to("Explain a Judgment")
            st.rerun()
    with c2:
        image_card(
            "💬",
            "Document Q&A",
            "Ask questions about any uploaded PDF document and get answers with source citations.",
            theme="bg-amber",
            tag="RAG",
        )
        if st.button("Ask questions →", key="feature_docqa"):
            go_to("Document Q&A")
            st.rerun()
    with c3:
        image_card(
            "🔍",
            "Search Cases",
            "Search real Indian court judgments from the Indian Kanoon database.",
            theme="bg-emerald",
            tag="LIVE",
        )
        if st.button("Search cases →", key="feature_cases"):
            go_to("Search Cases")
            st.rerun()

    # ---- Trending topics ----
    st.markdown('<div class="section-title">🔥 Popular topics</div>', unsafe_allow_html=True)

    topics = [
        ("🛍️", "Consumer Rights", "bg-orange",
         "Complaints, refunds, defective products and consumer protection."),
        ("🏠", "Property", "bg-sky",
         "Ownership, rent, tenancy, and property-related legal concepts."),
        ("🚔", "FIR & Police", "bg-slate",
         "How FIRs work, police procedures and complaint filing."),
        ("💻", "Cyber Crime", "bg-violet",
         "Online fraud, identity theft, and how to report cybercrime."),
        ("👨‍👩‍👧", "Family Law", "bg-rose",
         "Marriage, divorce, maintenance, custody and succession basics."),
        ("💼", "Employment", "bg-teal",
         "Workplace rights, contracts, salary disputes and termination."),
    ]

    cols = st.columns(3)
    for i, (icon, title, theme, desc) in enumerate(topics):
        with cols[i % 3]:
            image_card(icon, title, desc, theme=theme, tag="TOPIC")

    # ---- Disclaimer ----
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
    st.write("Upload an Indian court judgment PDF and get a plain-language explanation.")

    st.info("💡 Text-based PDFs work best. Scanned PDFs may require OCR.")

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
                    st.error("No readable text found in this PDF.")
                    st.info("This appears to be a scanned PDF. OCR support can be added later.")
                    st.stop()

                document_text = document_text[:60000]

                prompt = f"""
You are "My Lawyer Friend", an Indian legal-information assistant.

Analyze the court judgment below and explain it in simple language.

IMPORTANT RULES:
- Only use information contained in the document.
- Do not invent facts, sections or laws.
- If something is unavailable, write: "Not stated in the document."
- Clearly distinguish the court's decision from your explanation.
- Preserve important legal terminology.
- Do not claim to be a lawyer.
- Do not provide personalized legal advice.

Use these sections:

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

                with st.spinner("🧠 Analyzing the judgment..."):
                    analysis = generate_ai(prompt, thinking_level="high")

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
                    "and consult a qualified lawyer for specific matters."
                )

            except Exception as error:
                st.error("Something went wrong while analyzing the judgment.")
                st.caption(f"Technical details: {error}")


# ============================================================
# DOCUMENT Q&A (RAG)
# ============================================================

elif st.session_state.page == "Document Q&A":

    st.title("💬 Document Q&A")
    st.write("Upload a PDF and ask questions about its contents. Answers are grounded in the document.")

    if not RAG_AVAILABLE:
        st.error("RAG dependencies are not installed.")
        st.info("Add the LangChain and FAISS packages to `requirements.txt`.")
        st.stop()

    uploaded_file = st.file_uploader(
        "Upload PDF document",
        type=["pdf"],
        help="Upload any legal document, contract, or judgment.",
    )

    if uploaded_file:
        # Build chain once per file
        if st.session_state.qa_file != uploaded_file.name:
            with st.spinner("📚 Processing document..."):
                try:
                    st.session_state.qa_chain = build_qa_chain(uploaded_file)
                    st.session_state.qa_file = uploaded_file.name
                    st.session_state.qa_history = []
                except Exception as e:
                    st.error(f"Failed to process document: {e}")
                    st.stop()

        st.success(f"✅ {uploaded_file.name} ready for questions")

        # Chat history
        for q, a in st.session_state.qa_history:
            with st.chat_message("user"):
                st.write(q)
            with st.chat_message("assistant"):
                st.write(a)

        # Input
        question = st.chat_input("Ask a question about this document...")

        if question:
            with st.spinner("🔍 Searching document..."):
                try:
                    result = st.session_state.qa_chain({"query": question})
                    answer = result["result"]
                    sources = result.get("source_documents", [])
                except Exception as e:
                    st.error(f"Error: {e}")
                    st.stop()

            st.session_state.qa_history.append((question, answer))

            with st.chat_message("user"):
                st.write(question)

            with st.chat_message("assistant"):
                st.write(answer)
                if sources:
                    with st.expander("📎 Source snippets"):
                        st.code(sources[0].page_content[:500])

            add_history("Document Q&A", question[:80])

    else:
        st.info("📌 Upload a PDF to begin asking questions.")
        st.markdown("### What you can ask")
        examples = [
            "What are the key obligations in this contract?",
            "Summarize the main arguments in this judgment.",
            "What sections of law are cited?",
            "What is the timeline of events?",
        ]
        for ex in examples:
            st.markdown(f"- {ex}")


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
- Do not invent laws or facts.
- Explain complicated concepts simply.
- Mention that laws can change.
- Encourage checking official sources for important matters.
"""

                with st.spinner("🧠 Preparing explanation..."):
                    answer = generate_ai(prompt, thinking_level="medium")

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


# ============================================================
# SEARCH CASES (Indian Kanoon)
# ============================================================

elif st.session_state.page == "Search Cases":

    st.title("🔍 Search Cases")
    st.write("Search real Indian court judgments from the Indian Kanoon database.")

    if not INDIAN_KANOON_API_KEY:
        st.warning(
            "Indian Kanoon API key not configured. "
            "Add `INDIAN_KANOON_API_KEY` in Streamlit Cloud → Settings → Secrets."
        )
        st.info(
            "Indian Kanoon offers ₹500 free trial credit on signup. "
            "Visit https://api.indiankanoon.org/signup/ to get a key."
        )
        st.stop()

    search_term = st.text_input(
        "Search by case name, keyword, or topic",
        placeholder="Example: right to privacy, consumer protection, Article 21",
    )

    if st.button("🔍 Search", type="primary", use_container_width=True):
        if not search_term.strip():
            st.warning("Please enter a search term.")
        else:
            with st.spinner("Searching Indian Kanoon..."):
                data, error = search_indian_kanoon(search_term)

            if error:
                st.error(error)
                st.info("If the API is unavailable, you can search directly at indiankanoon.org")
                st.link_button("Search on Indian Kanoon →", f"https://indiankanoon.org/search/?formInput={search_term}")
            else:
                docs = data.get("docs", [])
                st.success(f"Found {len(docs)} results")
                add_history("Case Search", search_term)
                render_case_cards(docs)

    # Official links fallback
    st.divider()
    st.markdown('<div class="section-title">🇮🇳 Official legal resources</div>', unsafe_allow_html=True)

    resources = [
        ("⚖️", "Supreme Court of India", "https://www.sci.gov.in/", "bg-indigo"),
        ("🏛️", "eCourts Services", "https://ecourts.gov.in/", "bg-emerald"),
        ("📚", "India Code", "https://www.indiacode.nic.in/", "bg-amber"),
        ("📜", "Indian Kanoon", "https://indiankanoon.org/", "bg-slate"),
    ]

    cols = st.columns(4)
    for i, (icon, name, url, theme) in enumerate(resources):
        with cols[i % 4]:
            image_card(icon, name, "Official government resource", theme=theme, tag="LINK")
            st.link_button("Visit →", url, use_container_width=True)


# ============================================================
# KNOW YOUR RIGHTS
# ============================================================

elif st.session_state.page == "Know Your Rights":

    st.title("⚖️ Know Your Rights")
    st.write("Explore general legal-information topics.")

    rights = [
        ("🚔", "Police & FIR", "bg-slate",
         "General information about complaints, FIRs and police procedures."),
        ("🛍️", "Consumer Rights", "bg-orange",
         "Consumer complaints, refunds, and consumer protection."),
        ("💻", "Cyber Crime", "bg-violet",
         "Online fraud, cybercrime and how to report incidents."),
        ("🏠", "Property", "bg-sky",
         "Property-related legal concepts and disputes."),
        ("💼", "Employment", "bg-teal",
         "Workplace rights, salaries, and employment-related concepts."),
        ("📄", "RTI", "bg-cyan",
         "Right to Information — filing, appeals and transparency."),
        ("👨‍👩‍👧", "Family Law", "bg-rose",
         "Common family-law concepts."),
        ("🛡️", "Fundamental Rights", "bg-indigo",
         "Fundamental rights under the Indian Constitution."),
    ]

    cols = st.columns(3)
    for i, (icon, title, theme, desc) in enumerate(rights):
        with cols[i % 3]:
            image_card(icon, title, desc, theme=theme, tag="RIGHTS")


# ============================================================
# HISTORY
# ============================================================

elif st.session_state.page == "History":

    st.title("📚 History")
    st.write("Your recent activity during this session.")

    if not st.session_state.history:
        st.info("No activity yet.")
    else:
        theme_map = {
            "Judgment Analysis": ("📄", "bg-indigo"),
            "Document Q&A": ("💬", "bg-amber"),
            "Legal Q&A": ("🧠", "bg-violet"),
            "Case Search": ("🔍", "bg-emerald"),
        }

        for item in reversed(st.session_state.history):
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

    st.markdown('<div class="section-title">🚀 Roadmap</div>', unsafe_allow_html=True)

    roadmap = [
        ("v1.0", "Premium UI and navigation", "bg-slate"),
        ("v1.2", "AI document analysis", "bg-indigo"),
        ("v1.4", "Image-card system + filters", "bg-emerald"),
        ("v2.0", "Indian Kanoon + RAG integration", "bg-amber"),
        ("v2.1", "Voice input + regional languages", "bg-violet"),
        ("v2.2", "Legal notice generator", "bg-rose"),
        ("v3.0", "Advanced legal research assistant", "bg-fuchsia"),
    ]

    cols = st.columns(4)
    for i, (ver, feat, theme) in enumerate(roadmap):
        with cols[i % 4]:
            image_card("🚀", ver, feat, theme=theme, tag="ROADMAP")

    st.divider()
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
