import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from .base_model import BaseModel

OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

class OpenAIModel(BaseModel):
    def __init__(self, retriver):
        self.retriver = retriver
        self.LLM = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=OPEN_AI_KEY)

    def answer(self, question: str) -> str:
        context = self.retriver.search(question)
        chain = (
            {"context": context, "question": RunnablePassthrough()}
            | self.prompt
            | self.LLM
            | StrOutputParser()
        )

        chain.invoke(question)