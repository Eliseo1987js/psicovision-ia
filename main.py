import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

# CONFIGURACIÓN SEGURA
# El programa busca la llave en el 'escondite' que configuraste en Streamlit
try:
    llave = st.secrets["llave_google"]
    genai.configure(api_key=llave)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Falta configurar la llave en los Secrets de Streamlit.")

st.set_page_config(page_title="PsicoVisión AI", layout="wide")

st.title("🧠 PsicoVisión AI")
st.write("Cargá tu material de la UNLP y empezá la clase.")

archivo = st.file_uploader("Subí tu PDF de estudio", type=["pdf"])

if archivo:
    st.success("✅ Material recibido.")
    tema = st.text_input("¿Qué tema querés que explique el profesor?")

    if st.button("🎙️ INICIAR EXPLICACIÓN"):
        try:
            lector = PdfReader(archivo)
            texto_pdf = ""
            # Leemos las primeras páginas para la explicación
            for pagina in lector.pages[:3]:
                texto_pdf += pagina.extract_text()
            
            with st.spinner("El profesor está analizando el texto..."):
                consigna = f"Actuá como un profesor de psicología. Basándote en este texto: {texto_pdf}, explicá de forma clara y pedagógica: {tema}"
                resultado = model.generate_content(consigna)
                
                st.markdown("---")
                st.subheader("👨‍🏫 Clase Magistral:")
                st.write(resultado.text)
        except Exception as e:
            st.error(f"Hubo un error: {e}")
            
