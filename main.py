import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

# 1. Configuración de la Llave
llave = "AIzaSyA9PrK0oxK4W0UoPBPpmsVcwr4rGNq-EI3k"
genai.configure(api_key=llave)

# 2. Configuración del Modelo (Cambiamos el nombre al más estable)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="PsicoVisión AI", layout="wide")

st.title("🧠 PsicoVisión AI")
st.write("Cargá tu material de la UNLP y empezá la clase.")

archivo = st.file_uploader("Subí tu PDF", type=["pdf"])

if archivo:
    st.success("✅ Material recibido.")
    pregunta = st.text_input("¿Qué tema querés que explique el profesor?")

    if st.button("🎙️ INICIAR EXPLICACIÓN"):
        try:
            # Leemos el PDF
            lector = PdfReader(archivo)
            texto_pdf = ""
            for pagina in lector.pages[:3]: # Leemos solo 3 páginas para que sea rápido
                texto_pdf += pagina.extract_text()
            
            # El pedido a la IA
            with st.spinner("El profesor está analizando el texto..."):
                consigna = f"Actuá como un profesor de psicología. Basándote en este texto: {texto_pdf}, explicá de forma clara: {pregunta}"
                respuesta = model.generate_content(consigna)
                
                # Mostramos el resultado
                st.markdown("---")
                st.subheader("👨‍🏫 Clase Magistral:")
                st.write(respuesta.text)
                
        except Exception as e:
            st.error(f"Hubo un error técnico: {e}")
            
