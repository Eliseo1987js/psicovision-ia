import streamlit as st
import time

# CONFIGURACIÓN
st.set_page_config(page_title="PsicoVisión AI", page_icon="🧠", layout="wide")

# ESTILO DE PIZARRÓN
st.markdown("""
    <style>
    .pizarro-box {
        background-color: #1e2d24;
        color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border: 8px solid #4e342e;
        font-family: 'Courier New', Courier, monospace;
        font-size: 20px;
        min-height: 400px;
        box-shadow: inset 0 0 10px #000;
    }
    </style>
    """, unsafe_allow_html=True)

# FUNCIÓN DE VOZ
def hablar(texto):
    js_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance('{texto}');
    msg.lang = 'es-AR';
    msg.rate = 0.9; 
    window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js_code, height=0)

# ENCABEZADO
st.title("🧠 PsicoVisión AI")
st.subheader("Tu Pizarrón Inteligente de Psicología")

# IDENTIDAD LEGAL
st.sidebar.markdown(f"**Autor:** Jonatan Eliseo Segura")
st.sidebar.markdown(f"**Registro DNDA:** EX-2026-41927493")

file = st.file_uploader("Subí tu PDF de estudio", type=["pdf"])

if file:
    if st.button("🎙️ Iniciar Explicación en Pizarrón"):
        texto_clase = "Analizando el texto... El autor plantea que el aparato psíquico se organiza mediante procesos complejos. En el pizarrón veremos los puntos clave."
        
        hablar(texto_clase)
        
        # Efecto de escritura
        placeholder = st.empty()
        pizarron_contenido = "### 📝 CLASE: Análisis de Conceptos\n\n"
        
        for palabra in texto_clase.split():
            pizarron_contenido += palabra + " "
            placeholder.markdown(f'<div class="pizarro-box">{pizarron_contenido}</div>', unsafe_allow_html=True)
            time.sleep(0.3) # Esto hace que parezca que escribe a mano
