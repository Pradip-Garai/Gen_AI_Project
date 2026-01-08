from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

# Initialize LLM lazily to avoid errors when API key is missing
_llm = None

def get_llm():
    global _llm
    if _llm is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        _llm = ChatGroq(
            groq_api_key=api_key,
            model="llama-3.1-8b-instant",  
            temperature=0.7
        )
    return _llm

# For backward compatibility
llm = property(lambda self: get_llm())

if __name__ == "__main__":
    llm = get_llm()
    response = llm.invoke("What are the two main things to make Panipuri")
    print(response.content)
