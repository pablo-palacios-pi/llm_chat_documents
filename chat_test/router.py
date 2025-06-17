from fastapi import APIRouter, HTTPException, status, UploadFile,File,Form
from pydantic import BaseModel
from .views import get_answer,rag
#from PyPDF2 import PdfReader
#from langchain.prompts import PromptTemplate


router_ = APIRouter()

class Questions(BaseModel):
    ask: str


import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def open_prompt(file_path: str):
    doc_dir = os.path.normpath(os.path.join(current_dir,file_path))
    with open(file=doc_dir, mode="r", encoding="utf-8") as file:
        prompt = file.read()
        return prompt
    
    
@router_.get("/")
async def root():
    return {"message":"Bienvenido al Backend"}
    


@router_.post("/mini_rag")
async def comparar_docus(file_1: UploadFile = File(...), file_2: UploadFile = File(...)):
    if not file_1:
        raise HTTPException(status_code=403, detail="Los campos no pueden estar vacíos")
    elif not file_2:
        raise HTTPException(status_code=403, detail="Los campos no pueden estar vacíos")
    
    prompt_summary = open_prompt("promptSystem_2.md")

    answer_chat = await rag(file1=file_1.file, file2=file_2.file, system_prompt=prompt_summary)
    return answer_chat

# @router_.post("/chat_llm",status_code=status.HTTP_201_CREATED)
# async def conversacion_llm(question: Questions):
#     ask = question.ask
#     answer_chat = await get_answer(ask)
#     return{"respuesta":answer_chat}



# @router_.post("/chat_agentes",status_code=status.HTTP_201_CREATED)
# async def conversacion_llm(question: Questions):
#     ask = question.ask
#     answer_chat = await get_message(ask)
#     return{"respuesta":answer_chat}




# @router_.post("/upload_file")
# async def add_document(title_1: str = Form(...), file_1: UploadFile = File(...),title_2: str = Form(...), file_2: UploadFile = File(...)):
    
#     if not title_1 or not file_1:
#         raise HTTPException(status_code=403, detail="Los campos no pueden estar vacíos")
#     elif not title_2 or not file_2:
#         raise HTTPException(status_code=403, detail="Los campos no pueden estar vacíos")
    

#     reader = PdfReader(file_1.file)

#     text_1 = ""
#     for page in reader.pages:
#         text_1 += page.extract_text()


#     reader_2 = PdfReader(file_2.file)

#     text_2 = ""
#     for page_2 in reader_2.pages:
#         text_2 += page_2.extract_text()

#     prompt_summary = open_prompt("promptSystem.md")

#     prompt = PromptTemplate(
#         input_variables=["document_a", "document_b"],
#         template=prompt_summary,
#     )


#     final_prompt = prompt.format(document_a=text_1,document_b=text_2)

#     print(final_prompt)

#     answer_chat = await get_answer(system=final_prompt)
#     return answer_chat


