import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

# --- 🔑 CONFIGURACIÓN SEGURA ---
# El programa busca la llave en el 'escondite' de Streamlit
try:
    llave = st.secrets["llave_google"]
    genai.configure(api_key=llave)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception:
    st.error("Falta configurar la llave en los Secrets de Streamlit.")

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

# --- 📚 LÓGICA DE CARGA ---
archivo = st.file_uploader("Subí tu PDF de estudio", type=["pdf"])

if archivo:
    st.success("✅ Material recibido. El profesor está listo.")
    tema = st.text_input("¿Qué tema específico querés que explique el profesor?")

    if st.button("🎙️ INICIAR EXPLICACIÓN"):
        try:
            lector = PdfReader(archivo)
            texto_pdf = ""
            # Leemos las primeras 3 páginas para que sea rápido
            for pagina in lector.pages[:3]:
                texto_pdf += pagina.extract_text()
            
            with st.spinner("El profesor está analizando el texto..."):
                consigna = f"Actuá como un profesor de psicología de la UNLP. Basándote en este texto: {texto_pdf}, explicá de forma clara: {tema}"
                resultado = model.generate_content(consigna)
                
                st.markdown(f"<div class='pizarron'><h2>👨‍🏫 CLASE:</h2><p>{resultado.text}</p></div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Hubo un error técnico: {e}")
            
