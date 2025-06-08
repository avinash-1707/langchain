from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langserve import add_routes
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="Compound-Beta-Mini",api_key=groq_api_key)

# Creating prompt
generic_template = "You are a language translator whose job is to convert the user given sentence into the asked language. Just give the clear translation. You dont have to repeat yourself or anything."

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",generic_template),
        ("user","Convert the sentence '{text}' into {language} language")
    ]
)

# Parser
parser = StrOutputParser()

#Creating chain
chain = prompt | model | parser

# App definition
app = FastAPI(title="Langchain Server",
              version="1.0",
              description="A simple API server using Langchain runnable interface")

# Adding chain routes
add_routes(app,
           chain,
           path="/chain")

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)