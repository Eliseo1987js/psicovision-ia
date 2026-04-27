import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

# --- CONFIGURACIÓN DE SEGURIDAD ---
# Buscamos la llave en el "escondite" de Streamlit
try:
    llave = st.secrets["llave_google"]
    genai.configure(api_key=llave)
    # Usamos el modelo más estable y rápido
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Error: No se encontró la llave en Secrets. Revisá el paso 1.")

# --- DISEÑO DEL PIZARRÓN ---
st.set_page_config(page_title="PsicoVisión AI", layout="wide")
st.markdown("""
    <style>
    .pizarron {
        background-color: #1c2e26; color: white; padding: 30px;
        border: 10px solid #3e2723; border-radius: 20px;
        font-family: 'Courier New', monospace; box-shadow: inset 0 0 50px black;
    }
    .tiza { color: #FFE03D; font-weight: bold; border-bottom: 2px solid #FFE03D; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 PsicoVisión AI: Tu Profesor de Psicología")
st.write("Cargá tus apuntes de la UNLP y el profesor te explicará la clase.")

# --- LÓGICA DE CARGA Y PROCESAMIENTO ---
archivo = st.file_uploader("Subí tu PDF de estudio", type=["pdf"])

if archivo:
    st.success("✅ Profesor: 'Material recibido. ¿Qué quieres aprender?'")
    tema = st.text_input("Escribí el concepto o tema a explicar:")

    if st.button("🎙️ EXPLICAR CLASE"):
        try:
            # Leemos el PDF
            lector = PdfReader(archivo)
            texto_pdf = ""
            # Procesamos las primeras 5 páginas para no saturar la memoria
            for pagina in lector.pages[:5]:
                texto_pdf += pagina.extract_text()
            
            with st.spinner("Escribiendo en el pizarrón..."):
                # Armamos el pedido para la IA
                consigna = f"Actuá como un profesor de psicología pedagógico. Basándote en este texto: {texto_pdf}, explicá de forma clara y profunda el siguiente tema: {tema}"
                
                resultado = model.generate_content(consigna)
                
                # Mostramos el resultado con estilo de pizarrón
                st.markdown(f"""
                    <div class='pizarron'>
                        <h2 class='tiza'>👨‍🏫 CLASE MAGISTRAL:</h2>
                        <p>{resultado.text}</p>
                    </div>
                """, unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"Hubo un problema técnico: {e}")
            
