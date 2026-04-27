import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# --- CONFIGURACIÓN DE SEGURIDAD TOTAL ---
# Esta parte soluciona el error de la llave y el error 404 de versión
if "llave_google" in st.secrets:
    # Usamos transport='rest' para que no busque versiones viejas de Google
    genai.configure(api_key=st.secrets["llave_google"], transport='rest')
    # Usamos el nombre base del modelo que es el más estable
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ Error: No pegaste la llave en el cuadro de Secrets de Streamlit.")

st.set_page_config(page_title="PsicoVisión AI", layout="wide")
st.title("🧠 PsicoVisión AI: Tu Profesor de Psicología")

# --- INTERFAZ ---
archivo = st.file_uploader("Subí tu PDF de estudio", type=["pdf"])

if archivo:
    st.success("✅ Material recibido. El profesor está listo.")
    tema = st.text_input("¿Qué tema específico querés que te explique?")

    if st.button("🎙️ INICIAR CLASE"):
        try:
            # Lectura del PDF
            lector = PdfReader(archivo)
            texto_pdf = ""
            for pagina in lector.pages[:3]: # Lee las primeras 3 páginas para ir rápido
                texto_pdf += pagina.extract_text()
            
            with st.spinner("El profesor está escribiendo en el pizarrón..."):
                # Pedido directo a la IA
                consigna = f"Actuá como profesor de psicología pedagógico. Basándote en este texto: {texto_pdf}, explicá: {tema}"
                resultado = model.generate_content(consigna)
                
                # Cuadro de respuesta
                st.markdown("---")
                st.subheader("👨‍🏫 Explicación del Profesor:")
                st.info(resultado.text)
                
        except Exception as e:
            # Si hay un error, lo mostramos para saber qué pasó
            st.error(f"Hubo un problema técnico: {e}")
            
