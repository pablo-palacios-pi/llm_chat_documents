<<<<<<< HEAD
# 📄 Comparador de Documentos – Instrucciones Manuales

Este proyecto permite **comparar dos documentos** y generar un informe detallado de las diferencias a través de una **interfaz web sencilla**.



**Crear archivo `.env`:**

   En la raíz del proyecto, creá un archivo llamado `.env` y agregá tus variables de entorno

---

# 🐳 Levantar Proyecto con Docker (Linux o Windows)

## Requisitos

- Tener [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado (funciona tanto en **Windows** como **Linux**).
- Tener este proyecto descargado o clonado en tu computadora.

---

##  Cómo levantar el proyecto

1. **Abrí una terminal** en la carpeta del proyecto.

2. Ejecutá los siguientes comandos **uno por uno**, en orden:

   ### (Opcional) Borrar contenedores anteriores
   ```bash
   docker compose down --volumes --remove-orphans
   ```

   > Esto limpia posibles versiones anteriores del proyecto.

   ### 🔧 Construir el proyecto
   ```bash
   docker compose build
   ```

   > Este comando prepara todo el entorno necesario.

   ### ▶️ Iniciar el proyecto
   ```bash
   docker compose up
   ```

   > Esperá unos segundos y el proyecto estará corriendo.

---

## 🌐 Acceso

Una vez que el proyecto esté corriendo, podés acceder desde tu navegador a:

```
http://localhost:8501
```



# Levantar Manualmente

1. **Crear un entorno virtual:**

   En tu terminal:
   ```bash
   python -m venv venv
   ```

2. **Activar el entorno virtual:**

   - En **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - En **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

### 🔷 1. Iniciar el Frontend (Interfaz Web)

1. Abrí una terminal nueva.
2. Navegá a la carpeta:
   ```bash
   cd ./llm_chat_documents
   ```
3. Ejecutá Streamlit:
   ```bash
   streamlit run stream_file.py
   ```
4. Accedé desde tu navegador:  
   👉 [http://localhost:8501](http://localhost:8501)

---

### 🔶 2. Iniciar el Backend (Servidor API)

1. Abrí otra terminal diferente.
2. Navegá a la carpeta del backend:
   ```bash
   cd ./llm_chat_documents/chat_test
   ```
3. Iniciá el servidor FastAPI:
   ```bash
   uvicorn main:app --reload --port 8001
   ```
4. El backend estará disponible en:  
   👉 [http://127.0.0.1:8001](http://127.0.0.1:8001)

---
=======
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


>>>>>>> 8c17240f2aee98267357cd8d54659806f11d9708
