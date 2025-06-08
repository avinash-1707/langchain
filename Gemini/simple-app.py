import os 
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")
# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","Act as a senior web developer and answer the questions that are asked to you in a very efficient manner"),
        ("user","Question:{question}")
    ]
)

llm = GoogleGenerativeAI(model="gemini-2.0-flash")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

response = chain.invoke({
    "question": "What do you mean by server side rendering in nextjs"
})

print(response)