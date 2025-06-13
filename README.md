# README 

Repositorio para comparacion entre dos documentos mediante API. 

- Crear un entorno virtual
- Descargar las dependencias requirements.txt: pip install -r requirements.txt

- Crear un .env para las variables de entorno


Para iniciar frontend:
    - Abrir terminal 
    - Posicionarse en la carpeta ./llm_chat_documents 
    - Correr el comando: streamlit run .\stream_file.py
    - El front corre en Local URL: http://localhost:8501

Para iniciar backend: 
    - Abrir otra terminal aparte
    - Posicionarse en la carperta ./llm_chat_documents/chat_test
    - Correr el comando: uvicorn main:app --reload --port 8001 
    - El back corre en: running on http://127.0.0.1:8001 


