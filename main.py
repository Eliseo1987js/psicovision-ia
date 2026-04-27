import streamlit as st

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
        box-shadow: inset 0 0 15px #000;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# FUNCIÓN DE VOZ FLUIDA (Lee todo de corrido)
def hablar_fluido(texto):
    js_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance("{texto}");
    msg.lang = 'es-AR';
    msg.rate = 1.0; 
    msg.pitch = 1.0;
    window.speechSynthesis.cancel(); // Limpia voces anteriores
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
    # Aquí simulamos la respuesta del análisis para la demo
    texto_para_explicar = "Hola. Soy tu asistente de PsicoVisión A. I. He analizado el texto y estos son los puntos clave que el autor desarrolla sobre el aparato psíquico y la conducta humana."
    
    if st.button("🎙️ Iniciar Clase en Pizarrón"):
        # Dispara la voz de corrido
        hablar_fluido(texto_para_explicar)
        
        # Muestra el pizarrón directamente con el texto
        st.markdown(f"""
        <div class="pizarro-box">
            <h3>📝 NOTAS DEL DOCENTE:</h3>
            <p>{texto_para_explicar}</p>
            <hr>
            <p>✍️ <i>Análisis profundo completado.</i></p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.warning("Cargá un libro para empezar la clase.")
    
