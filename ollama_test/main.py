from fastapi import FastAPI
from langchain_ollama import ChatOllama
from pydantic import BaseModel


    
app = FastAPI()
llm = ChatOllama(
    temperature=0,
    model="gemma3:270m"
)

class Message(BaseModel):
    content:str

@app.post("/chat_ollama")
def chat_ollama(requet_body: Message):  
    response = llm.invoke(requet_body.content)
    return response.content
    


