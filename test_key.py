from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

"""print("=" * 50)
print("Current Working Directory:")
print(os.getcwd())

print("\nGEMINI_API_KEY:")
print(os.getenv("GEMINI_API_KEY"))

print("\nTAVILY_API_KEY:")
print(os.getenv("TAVILY_API_KEY"))

print("=" * 50)"""


from langchain_google_genai import GoogleGenerativeAIEmbeddings

emb =  GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

vector = emb.embed_query("hello")

print(len(vector))