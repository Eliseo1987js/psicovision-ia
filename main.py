import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

# CONFIGURACIÓN SEGURA
try:
    # El programa busca la llave en el 'escondite' secreto
    llave = st.secrets["llave_google"]
    genai.configure(api_key=llave)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception:
    st.error("Error: Configurá 'llave_google' en los Secrets de Streamlit.")

st.set_page_config(page_title="PsicoVisión AI", layout="wide")
st.title("🧠 PsicoVisión AI: Tu Profesor de Psicología")

archivo = st.file_uploader("Subí tu PDF de estudio", type=["pdf"])

if archivo:
    st.success("✅ Material recibido.")
    tema = st.text_input("¿Qué tema querés que explique el profesor?")

    if st.button("🎙️ EXPLICAR CLASE"):
        try:
            lector = PdfReader(archivo)
            texto_pdf = ""
            # Leemos solo 3 páginas para evitar saturar la memoria
            for pagina in lector.pages[:3]:
                texto_pdf += pagina.extract_text()
            
            with st.spinner("El profesor está analizando el texto..."):
                consigna = f"Actuá como un profesor de psicología pedagógico. Basándote en este texto: {texto_pdf}, explicá de forma clara: {tema}"
                resultado = model.generate_content(consigna)
                
                # Resultado con estilo de pizarrón
                st.markdown(f"""
                <div style="background-color: #1c2e26; color: white; padding: 20px; border-radius: 15px; border: 5px solid #3e2723;">
                    <h3>👨‍🏫 CLASE:</h3>
                    <p>{resultado.text}</p>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Hubo un error técnico: {e}")
            
