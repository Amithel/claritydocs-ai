import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize OpenAI client pointed to NVIDIA Build serverless endpoint
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

# Exact model string for Nemotron 3.5 Lightning
MODEL_NAME = "nvidia/nemotron-3.5-lightning-30b-a3b"

def analyze_document(doc_text: str) -> str:
    system_prompt = """You are an expert Legal, Medical, and Technical Document Simplifier. 
Your job is to translate complex jargon, legal contracts, medical reports, or official terms into clear, plain English suitable for anyone to understand.

Structure your response cleanly using markdown with these exact headings:
1. 💡 **Plain English Summary**: What does this document actually mean in 2-3 sentences?
2. ⚠️ **Red Flags & Hidden Traps**: Highlight any non-standard clauses, hidden fees, unusual liabilities, or critical warnings.
3. ✅ **Action Items & Checklist**: What specific steps, signatures, or deadlines does the reader need to follow?

Keep your tone objective, helpful, and crystal clear."""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Please analyze and simplify the following document:\n\n{doc_text}"}
            ],
            temperature=0.2,
            max_tokens=4096
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to NVIDIA Build API: {str(e)}"