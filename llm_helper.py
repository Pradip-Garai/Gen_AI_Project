from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",  
    temperature=0.7
)

if __name__ == "__main__":
    response = llm.invoke("What are the two main things to make Panipuri")
    print(response.content)
