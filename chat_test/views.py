import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()


client = AzureOpenAI(
    api_version="2025-01-01-preview",
    azure_endpoint="https://ai-danielvallejosai0530531063088720.openai.azure.com/",
    api_key="EARAfege87W1E3y9jdxiIxopGCUJkXclbIe3AgF55j4K8u6SW77eJQQJ99BDACHYHv6XJ3w3AAAAACOGYMCD",
)

def armar_documento_docx():
    pass

aviable_fuctions = {
        "armar_documento_docx":armar_documento_docx}
    
tools = [
        {
            "type":"function",
            "function":{
                "name":"top_10",
                "description":"""Funcion que devuelve el nombre y el volumen total las 10 monedas que tienen más actividad comercia en las ultimas 24 horas, 
                basado en la confianza o interés en el mercado en negociar puediendo ofrecer mejores oportunidades de trading debido a su alta liquidez.""",
                "parameters": { 
                    "type": "object",
                    "properties": {},  
                    "required": [] 
                }
            }
        },
]

async def get_answer(system):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"{system}",
            },
            {
                "role": "user",
                "content": "arranca la comparación",
            }
        ],
        max_tokens=4096,
        temperature=0.5,
        tools=[],
        top_p=1.0,
        model="gpt-4.1"
    )

    print(response)
    respuesta = response.choices[0].message.content
    return {
        "respuesta": respuesta,
    }



async def rag(file1,file2,system_prompt):
    try:
        file_doc1 = client.files.create(
                file=file1,
                purpose='assistants'
            )
        file_doc2 = client.files.create(
                file=file2,
                purpose='assistants'
            )
        print("Archivos subidos con éxito.")
        print(f"ID Doc 1: {file_doc1.id}")
        print(f"ID Doc 2: {file_doc2.id}")
        # 4. Creación de la llamada a la API
        print("\nEnviando solicitud al modelo...")

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": "Hace la comparacion",
                    # La sección de adjuntos está perfecta
                    "attachments": [
                        {"file_id": file_doc1.id, "tools": [{"type": "file_search"}]},
                        {"file_id": file_doc2.id, "tools": [{"type": "file_search"}]}
                    ]
                }
            ]
        )
    
        return response.choices[0].message.content


    except Exception as e:
        raise Exception(e)