from .base_model import BaseModel

class LLAMAModel(BaseModel):
    def __init__(self):
        pass

    def answer(self, question: str) -> str:
        return f"OpenAI says: {question}"