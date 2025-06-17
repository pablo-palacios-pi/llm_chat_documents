import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()


client = AzureOpenAI(
    api_version=os.getenv("API_VERSION_4_1"),
    azure_endpoint=os.getenv("ENDPOINT_DANI"),
    api_key=os.getenv("API_KEY_DANI"),
)

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