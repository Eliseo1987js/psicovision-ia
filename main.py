import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

# --- 🔑 ESTA ES LA PARTE QUE VAMOS A COMPLETAR DESPUÉS ---
# Por ahora lo dejamos vacío para que no tire error
API_KEY = "AIzaSyA9PnK0oK4MOUaPBPpmsVcwr4rGMq-EI3k" 

if API_KEY != "PONER_ACA_LA_CLAVE_DESPUES":
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

# --- 🎨 DISEÑO DEL PIZARRÓN ---
st.set_page_config(page_title="PsicoVisión AI", layout="wide")

st.markdown("""
    <style>
    .pizarron {
        background-color: #1c2e26; color: white; padding: 30px;
        border: 10px solid #3e2723; border-radius: 20px;
        font-family: 'Courier New', monospace; box-shadow: inset 0 0 50px black;
    }
    .tiza { color: #FFEB3B; font-weight: bold; border-bottom: 2px solid #FFEB3B; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 PsicoVisión AI: Tu Profesor de Psicología")

# --- 📚 LÓGICA DE CARGA ---
archivo = st.file_uploader("Subí tu PDF de estudio", type=["pdf"])

if archivo:
    st.success("👨‍🏫 Profesor: 'Ya tengo el material en la mano. ¿Qué querés aprender?'")
    tema = st.text_input("Escribí el concepto o tema:")

    if st.button("🎙️ EXPLICAR CLASE"):
        if API_KEY == "PONER_ACA_LA_CLAVE_DESPUES":
            st.warning("⚠️ Jonatan, falta pegar la API KEY en GitHub para que el profesor pueda hablar.")
        else:
            # Aquí el profesor lee y explica de verdad
            lector = PdfReader(archivo)
            texto_pdf = ""
            for pagina in lector.pages[:5]:
                texto_pdf += pagina.extract_text()
            
            consigna = f"Basándote en este texto: {texto_pdf}, explicá de forma clara: {tema}"
            with st.spinner("Escribiendo en el pizarrón..."):
                resultado = model.generate_content(consigna)
                st.markdown(f"<div class='pizarron'><h2 class='tiza'>CLASE:</h2><p>{resultado.text}</p></div>", unsafe_allow_html=True)
                
