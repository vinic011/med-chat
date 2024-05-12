from .base_model import BaseModel

class OpenAIModel(BaseModel):
    def __init__(self):
        pass

    def ask(self, question: str) -> str:
        return f"OpenAI says: {question}"