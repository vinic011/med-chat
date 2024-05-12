from abc import ABC, abstractmethod
from langchain_core.prompts import ChatPromptTemplate


template = """Answer the question based only on the following context:

{context}

Question: {question}
"""

class Model(ABC):
    def __init__(self) -> None:
        self.template = template
        self.prompt = ChatPromptTemplate.from_template(template)

    @abstractmethod
    def answer(self, question: str) -> str:
        pass