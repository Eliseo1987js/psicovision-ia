import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

# --- CONFIGURACIÓN SEGURA ---
try:
    # Buscamos la llave en el 'escondite' de Streamlit
    llave = st.secrets["llave_google"]
    genai.configure(api_key=llave)
    model = # Cambiamos el nombre del modelo a la versión base estable
model = genai.GenerativeModel('gemini-1.5-flash')

except Exception:
    st.error("Falta configurar la llave_google en los Secrets de Streamlit.")

# --- DISEÑO ---
st.set_page_config(page_title="PsicoVisión AI", layout="wide")
st.title("🧠 PsicoVisión AI: Tu Profesor de Psicología")

# --- LÓGICA ---
archivo = st.file_uploader("Subí tu PDF de estudio", type=["pdf"])

if archivo:
    st.success("✅ Material recibido.")
    tema = st.text_input("Escribí el concepto a explicar:")

    if st.button("🎙️ EXPLICAR CLASE"):
        try:
            lector = PdfReader(archivo)
            texto_pdf = ""
            for pagina in lector.pages[:3]:
                texto_pdf += pagina.extract_text()
            
            with st.spinner("El profesor está escribiendo en el pizarrón..."):
                consigna = f"Actuá como profesor de psicología. Basándote en: {texto_pdf}, explicá: {tema}"
                resultado = model.generate_content(consigna)
                
                # Resultado con estilo de pizarrón
                st.markdown(f"""
                <div style="background-color: #1c2e26; color: white; padding: 20px; border-radius: 15px; border: 5px solid #3e2723;">
                    <h3>👨‍🏫 CLASE:</h3>
                    <p>{resultado.text}</p>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error técnico: {e}")
            
