import streamlit as st
from pypdf import PdfReader
from nvidia_client import analyze_document  # Or nebius_client if you kept the filename

st.set_page_config(
    page_title="ClarityDocs AI | Simplify Jargon Instantly",
    page_icon="📄",
    layout="wide"
)

st.title("📄 ClarityDocs AI")
st.caption("Translate complex legal contracts, medical reports, and official jargon into plain English instantly using NVIDIA Nemotron on NVIDIA Build API.")

with st.sidebar:
    st.header("About ClarityDocs")
    st.markdown("Bridge the gap between complex legal/technical writing and everyday understanding.")
    st.markdown("**Infrastructure:** NVIDIA Build Serverless")
    st.markdown("**Engine:** NVIDIA Nemotron-3.5")
    st.info("Upload a PDF or paste text to uncover hidden traps and action items.")

# Input choice
input_method = st.radio("Choose Input Method:", ["Upload PDF Document", "Paste Raw Text"])

doc_text = ""

if input_method == "Upload PDF Document":
    uploaded_file = st.file_uploader("Upload your document (PDF)", type=["pdf"])
    if uploaded_file is not None:
        try:
            reader = PdfReader(uploaded_file)
            extracted_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"
            doc_text = extracted_text
            st.success(f"Successfully extracted text from PDF ({len(doc_text)} characters).")
        except Exception as e:
            st.error(f"Error reading PDF: {e}")
else:
    doc_text = st.text_area("Paste complex document text here:", height=250, placeholder="Paste terms of service, rental agreement, or medical lab report...")

if st.button("🚀 Analyze & Simplify Document", type="primary"):
    if doc_text.strip():
        with st.spinner("Analyzing document structure, scanning for red flags, and drafting plain-English summary..."):
            result = analyze_document(doc_text)
            st.markdown("---")
            st.markdown(result)
    else:
        st.warning("Please upload a PDF or enter text before running analysis.")