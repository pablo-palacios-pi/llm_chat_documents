# import os
# from uuid import uuid4
# from openai import AzureOpenAI
# from dotenv import load_dotenv
# import time
# #from doc_int import client

# load_dotenv()
# # current_dir = os.path.dirname(os.path.abspath(__file__))


# # def open_prompt(file_path: str):
# #     doc_dir = os.path.normpath(os.path.join(current_dir,file_path))
# #     with open(file=doc_dir, mode="r", encoding="utf-8") as file:
# #         prompt = file.read()
# #         return prompt
    

# # client = AzureOpenAI(
# #     api_version=os.getenv("API_VERSION_4_1"),
# #     azure_endpoint=os.getenv("ENDPOINT_DANI"),
# #     api_key=os.getenv("API_KEY_DANI"),
# # )

# # assistant = client.beta.assistants.create(  
# #     instructions=open_prompt("promptSystem_3.md"),  
# #     model="gpt-4.1" 
# # )  
# # print("Assistant ID:", assistant.id)



# assistant_ID = os.getenv("ASSISTANT_ID")

# async def get_answer(system):
#     response = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "system",
#                 "content": f"{system}",
#             },
#             {
#                 "role": "user",
#                 "content": "arranca la comparación",
#             }
#         ],
#         max_tokens=4096,
#         temperature=0.5,
#         tools=[],
#         top_p=1.0,
#         model="gpt-4.1"
#     )

#     #print(response)
#     respuesta = response.choices[0].message.content
#     return {
#         "respuesta": respuesta,
#     }



# async def rag(file1,file2,system_prompt):
#     try:
#         file_doc1 = client.files.create(
#                 file=file1,
#                 purpose='assistants'
#             )
#         file_doc2 = client.files.create(
#                 file=file2,
#                 purpose='assistants'
#             )
        
#         print("Archivos subidos con éxito.")
#         print(f"ID Doc 1: {file_doc1.id}")
#         print(f"ID Doc 2: {file_doc2.id}")
        
#         response = client.chat.completions.create(
#             model="gpt-4.1",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": system_prompt
#                 },
#                 {
#                     "role": "user",
#                     "content": "Hace la comparacion",

#                     "attachments": [
#                         {"file_id": file_doc1.id, "tools": [{"type": "file_search"}]},
#                         {"file_id": file_doc2.id, "tools": [{"type": "file_search"}]}
#                     ]
#                 }
#             ]
#         )
    
#         return response.choices[0].message.content
#     except Exception as e:
#         raise Exception(e)
    

# #print(client.models.retrieve("gpt-4.1"))


# import asyncio  
# import time  
  
# async def comparar_documentos(file1, file2,poll_interval=2):  
#     """  
#     Compara dos documentos utilizando un asistente IA y devuelve un informe de diferencias.  
  
#     Args:  
#         file1: Archivo preliminar.  
#         file2: Archivo corregido.  
#         prompt_summary: Instrucciones/resumen para el asistente.  
#         client: Instancia del cliente de la API.  
#         assistant_id: ID del asistente.  
#         poll_interval: Tiempo (segundos) entre revisiones de estado.  
  
#     Returns:  
#         Informe de diferencias generado por el asistente o mensaje de error.  
#     """  
#     try:  
#         # 1. Subir ambos archivos  
#         file_doc1 = await asyncio.to_thread(client.files.create, file=file1, purpose='assistants')  
#         file_doc2 = await asyncio.to_thread(client.files.create, file=file2, purpose='assistants')  
  
#         # 2. Crear un nuevo hilo ("thread")  
#         thread = await asyncio.to_thread(client.beta.threads.create)  
  
#         # 3. Agregar un mensaje al hilo  
#         await asyncio.to_thread(  
#             client.beta.threads.messages.create,  
#             thread_id=thread.id,  
#             role="user",  
#             content=(  
#                 "Hola. Acabo de subir dos documentos: uno es la versión preliminar y el otro es la corregida. "  
#                 "Por favor, compáralos y genera un informe de diferencias siguiendo las instrucciones del asistente."
#                 f"Archivo 1: {file_doc1.filename}, Archivo 2: {file_doc2.filename}"  
#             )
            
#         )  
          
#         # 4. Ejecutar el asistente  
#         run = await asyncio.to_thread(  
#             client.beta.threads.runs.create,  
#             thread_id=thread.id,  
#             assistant_id=assistant_ID
#             #instructions=""  
           
#         )  
  
#         # 5. Esperar la finalización del asistente  
#         while run.status not in ["completed", "failed"]:  
#             await asyncio.sleep(poll_interval)  
#             run = await asyncio.to_thread(  
#                 client.beta.threads.runs.retrieve,  
#                 thread_id=thread.id,  
#                 run_id=run.id  
#             )  
  
#         # 6. Obtener respuesta del asistente  
#         messages = await asyncio.to_thread(  
#             client.beta.threads.messages.list,  
#             thread_id=thread.id  
#         )  
#         for msg in reversed(messages.data):  
#             if msg.role == "assistant":  
#                 return msg.content[0].text.value  
  
#         return "No se obtuvo respuesta del asistente."  
      
#     except Exception as e:  
#         # Mejor manejo de errores  
#         return f"Error al comparar documentos: {e}"  


  

# # from azure.ai.documentintelligence import DocumentIntelligenceClient  
# # from azure.core.credentials import AzureKeyCredential  

# # def doc_intelligence():
# #     endpoint = "https://docint-demo-adium.cognitiveservices.azure.com/"  
# #     key = "6VycicjSZOGX5jMomqRIXRCFgoiSs7v1f6Ua1uL9xXj0BaOqyUm9JQQJ99BFACYeBjFXJ3w3AAALACOGyOXC"  
# #     client = DocumentIntelligenceClient(endpoint, AzureKeyCredential(key))  
    
# #     with open(r"/mnt/c/Users/PabloPalacios/Desktop/pi_Train/llm_chat_documents/chat_test/1. ENTRADA - Folleto Paciente ILTUXAM 40-5-12.5 ISP 1.pdf", "rb") as f:  
# #         poller = client.begin_analyze_document(  
# #             "prebuilt-invoice",  # o "prebuilt-read", "prebuilt-document"  
# #             f  
# #         )  
# #         result = poller.result()  
    
# #     all_lines = []  
# #     for page in result.pages:  
# #         for line in page.lines:  
# #             all_lines.append(line.content)  
# #     return all_lines 


# # print(doc_intelligence())


#from traitlets import ClassBasedTraitType
from fastapi import UploadFile
from turtle import st
from click import File
import pymupdf4llm 
import tempfile
from docx2pdf import convert
import shutil
import os
import asyncio

class TempleFileHannder:
    
    @staticmethod
    async def create_templife_pdf(file: UploadFile) -> str:
        try: 
            contents = file.read()

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:  
                    temp.write(contents)  
                    temp.flush()            
                    temp_path = temp.name  

            return temp_path
        except ValueError as v:
            raise ValueError(f"El valor de ser obj File: {str(v)}", 'AD-001', 400)
        
    @staticmethod
    def delete_templife(temp_path_name: str):
        try:
            os.remove(temp_path_name)
        except FileNotFoundError as f:
            raise FileNotFoundError(f"Templefile no encotrado: {str(f)}", 'AD-001', 400)


    @staticmethod
    async def make_md_file(temp_path: str) -> str:  
        try:
             
            llama_reader = pymupdf4llm.LlamaMarkdownReader()
            llama_docs = llama_reader.load_data(file_path=temp_path)

            with tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8", suffix=".md", delete=False) as temp_md:  
                for doc in llama_docs:  
                    temp_md.write(doc.text)  
                    temp_md.write("\n\n---\n\n")  
                temp_md.flush()  
                temp_md_path = temp_md.name 

            return temp_md_path
        except Exception as e:
            raise Exception(f'Error inesperado al cargar archivos {str(e)}', 'AD-002', 500)
        
    @staticmethod
    async def create_temple_doc_to_pdf(file: UploadFile) -> str:

        with tempfile.TemporaryDirectory() as temp_dir:  
            temp_docx_path = os.path.join(temp_dir, "temp_file.docx")  

            contents = file.read()

            with open(temp_docx_path, "wb") as out_file:  
                out_file.write(contents)

            convert(temp_docx_path, temp_dir)  
            generated_pdf_path = os.path.join(temp_dir, "temp_file.pdf")  
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:  
                temp_pdf_path = temp_pdf.name  
            shutil.move(generated_pdf_path, temp_pdf_path)  
            return temp_pdf_path
        
        # with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:  
        #     temp_pdf_path = temp_pdf.name  # <--- Handler se cierra aquí (fin del with)  

        # shutil.move(generated_pdf_path, temp_pdf_path)

        # await asyncio.sleep(0.1) 
        # os.remove(path=generated_pdf_path)