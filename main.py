import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# --- CONFIGURACIÓN DE SEGURIDAD Y CONEXIÓN ---
# Forzamos la versión 'v1' para evitar el error 404 que aparecía antes
try:
    if "llave_google" in st.secrets:
        genai.configure(api_key=st.secrets["llave_google"], transport='rest')
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("⚠️ Error: No se encontró la llave en los Secrets de Streamlit.")
except Exception as e:
    st.error(f"❌ Error de configuración: {e}")

# --- DISEÑO DE LA APLICACIÓN ---
st.set_page_config(page_title="PsicoVisión AI", layout="wide")

st.markdown("""
    <style>
    .pizarron {
        background-color: #1c2e26; 
        color: white; 
        padding: 25px;
        border: 8px solid #3e2723; 
        border-radius: 15px;
        font-family: 'Courier New', monospace;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 PsicoVisión AI: Tu Profesor de Psicología")
st.write("Cargá tus textos de la UNLP para que el profesor te los explique.")

# --- LÓGICA DE FUNCIONAMIENTO ---
archivo = st.file_uploader("Subí tu archivo PDF", type=["pdf"])

if archivo:
    st.success("✅ Material recibido. El profesor está listo para explicar.")
    tema = st.text_input("¿Qué tema específico querés que explique el profesor?")

    if st.button("🎙️ INICIAR EXPLICACIÓN"):
        if not tema:
            st.warning("Por favor, escribí un tema para que el profesor pueda empezar.")
        else:
            try:
                # Leemos el contenido del PDF
                lector = PdfReader(archivo)
                texto_pdf = ""
                # Procesamos las primeras páginas para mayor rapidez
                for pagina in lector.pages[:5]:
                    texto_pdf += pagina.extract_text()
                
                with st.spinner("El profesor está preparando el pizarrón..."):
                    # Pedido pedagógico a la IA
                    consigna = (
                        f"Actuá como un profesor de psicología pedagógico y claro. "
                        f"Basándote en este material: {texto_pdf}. "
                        f"Explicá profundamente el siguiente tema: {tema}"
                    )
                    
                    resultado = model.generate_content(consigna)
                    
                    # Mostramos el resultado con estilo de pizarrón
                    st.markdown(f"""
                        <div class='pizarron'>
                            <h2>👨‍🏫 CLASE MAGISTRAL:</h2>
                            <p>{resultado.text}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    
            except Exception as e:
                st.error(f"Hubo un problema al procesar el pedido: {e}")
                
