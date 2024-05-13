from src.utils.load import load_pdf_text
from src.utils.split import split_book
from src.utils.vectordb import create_vector_db
from src.models.openai_model import OpenAIModel

TEXT_PATH = "data/Protocolos_clínicos_em_endocrinologia_e_diabetes_4ed_2021_Bandeira_221204_132239.pdf"

text = load_pdf_text(TEXT_PATH)
splits = split_book(text)
retriever = create_vector_db(splits)
chat = OpenAIModel(retriever)

async def main():
    while True:
        question = input("Ask a question: ")
        if question == "exit":
            break
        answer = await chat.answer(question)
        print(answer)

main()