import streamlit as st
import requests

# st.title("Hola, Streamlit 👋")
# st.write("Esta es tu primera aplicación con Streamlit.")


st.set_page_config(page_title="Comparador", layout="centered")

st.title("📄 Comparar Documentos ")

file1 = st.file_uploader("📁 Subí el primer documento", type=["pdf", "docx", "txt"])
file2 = st.file_uploader("📁 Subí el segundo documento", type=["pdf", "docx", "txt"])

if st.button("Comparar Documentos"):
    if not file1 or not file2:
        st.error("Ambos archivos deben estar cargados.")
    else:
        with st.spinner("Procesando..."):
             
            files = {
                "file_1": (file1),
                "file_2": (file2),
            }

            #requests.get(url="http://backend:8081/api_test/")
            try:
                response = requests.post(
                    url="http://backend:8081/api_test/mini_rag", files=files
                )

                if response.status_code == 200:
                    result = response.json()
                    st.success("Comparación completada ✅")
                    st.write(result)
                else:
                    st.error(f"Error {response.status_code}: {response.text}")

            except requests.exceptions.ConnectionError:
                st.error("No se pudo conectar al backend. ¿Está corriendo en localhost:8081?")