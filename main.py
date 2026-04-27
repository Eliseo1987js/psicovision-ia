import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

# --- 🔑 CONFIGURACIÓN ---
API_KEY = "AIzaSyA9PrK0oxK4W0UoPBPpmsVcwr4rGNq-EI3k" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 🎨 DISEÑO ---
st.set_page_config(page_title="PsicoVisión AI", layout="wide")
st.markdown("""
    <style>
    .pizarron {
        background-color: #1c2e26; color: white; padding: 30px;
        border: 10px solid #3e2723; border-radius: 20px;
        font-family: 'Courier New', monospace; box-shadow: inset 0 0 50px black;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 PsicoVisión AI")

# --- 📚 LÓGICA ---
archivo = st.file_uploader("Subí tu PDF de estudio", type=["pdf"])

if archivo:
    st.success("👨‍🏫 Profesor: 'Material listo. ¿Qué quieres aprender?'")
    tema = st.text_input("Escribí el concepto:")

    if st.button("🎙️ EXPLICAR CLASE"):
        lector = PdfReader(archivo)
        texto_pdf = ""
        for pagina in lector.pages[:5]:
            texto_pdf += pagina.extract_text()
        
        consigna = f"Basándote en este texto: {texto_pdf}, explicá de forma clara: {tema}"
        
        with st.spinner("El profesor está escribiendo..."):
            resultado = model.generate_content(consigna)
            st.markdown(f"<div class='pizarron'><h2>👨‍🏫 CLASE:</h2><p>{resultado.text}</p></div>", unsafe_allow_html=True)
            
