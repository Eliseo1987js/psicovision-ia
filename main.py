import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# CONFIGURACIÓN DEFINITIVA
# Forzamos la versión estable 'v1' para que no dé error 404
try:
    if "llave_google" in st.secrets:
        genai.configure(api_key=st.secrets["llave_google"], transport='rest')
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("Falta la llave en los Secrets de Streamlit.")
except Exception as e:
    st.error(f"Error de conexión: {e}")

st.set_page_config(page_title="PsicoVisión AI", layout="wide")
st.title("🧠 PsicoVisión AI")

archivo = st.file_uploader("Subí tu PDF de estudio", type=["pdf"])

if archivo:
    st.success("✅ Material recibido.")
    tema = st.text_input("¿Qué tema querés que explique el profesor?")

    if st.button("🎙️ INICIAR EXPLICACIÓN"):
        try:
            lector = PdfReader(archivo)
            texto_pdf = ""
            # Leemos las primeras páginas para procesar rápido
            for pagina in lector.pages[:5]:
                texto_pdf += pagina.extract_text()
            
            with st.spinner("El profesor está analizando el material..."):
                consigna = f"Actuá como un profesor de psicología pedagógico. Basándote en este texto: {texto_pdf}, explicá de forma clara: {tema}"
                resultado = model.generate_content(consigna)
                
                st.markdown("---")
                st.subheader("👨‍🏫 Clase Magistral:")
                st.info(resultado.text)
        except Exception as e:
            st.error(f"Hubo un problema técnico: {e}")
            
