import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# Configuración de la IA usando el secreto guardado
try:
    genai.configure(api_key=st.secrets["llave_google"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Error con la llave. Revisá los Secrets de Streamlit.")

st.set_page_config(page_title="PsicoVisión AI", layout="wide")
st.title("🧠 PsicoVisión AI")

archivo = st.file_uploader("Subí tu PDF de estudio", type=["pdf"])

if archivo:
    st.success("✅ Material cargado.")
    tema = st.text_input("¿Qué tema querés que explique el profesor?")

    if st.button("🎙️ INICIAR CLASE"):
        try:
            # Lectura del PDF
            lector = PdfReader(archivo)
            texto_completo = ""
            for pagina in lector.pages[:5]: # Lee las primeras 5 páginas
                texto_completo += pagina.extract_text()
            
            # Pedido al profesor
            with st.spinner("El profesor está preparando la clase..."):
                consigna = f"Actuá como un profesor experto. Basándote en este texto: {texto_completo}, explicá de forma clara: {tema}"
                respuesta = model.generate_content(consigna)
                
                # Pizarrón de resultados
                st.markdown("---")
                st.subheader("👨‍🏫 Clase Magistral:")
                st.info(respuesta.text)
        except Exception as e:
            st.error(f"Hubo un problema: {e}")
            
