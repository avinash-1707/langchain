import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import time

load_dotenv()

# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Respond to the questions asked in a professional yet friendly manner"),
        ("user","Question:{question}")
    ]
)

# Streamlit framework
st.title("Langchain demo with Llama3.2 model")
input_text = st.text_input("What question do you have in mind?")

# Calling LLM model
llm = OllamaLLM(model="llama3.2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

response = chain.invoke({
        "question": input_text
    })

def stream_data():
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.05)

if input_text:
    st.write_stream(stream_data)