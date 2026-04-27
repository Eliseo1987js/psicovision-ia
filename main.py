import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# Conexión directa con el secreto de Streamlit
try:
    genai.configure(api_key=st.secrets["llave_google"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Falta la llave en Secrets.")

st.title("🧠 PsicoVisión AI")

archivo = st.file_uploader("Subí tu PDF", type=["pdf"])

if archivo:
    st.success("✅ PDF cargado.")
    tema = st.text_input("¿Qué tema explicamos?")

    if st.button("INICIAR CLASE"):
        try:
            # Lectura básica
            lector = PdfReader(archivo)
            texto = ""
            for p in lector.pages[:3]:
                texto += p.extract_text()
            
            # Respuesta del profesor
            res = model.generate_content(f"Explicá esto como profesor: {tema}. Contexto: {texto}")
            st.write(res.text)
        except Exception as e:
            st.error(f"Error: {e}")
            
