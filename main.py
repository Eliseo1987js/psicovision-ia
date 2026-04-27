import streamlit as st

# CONFIGURACIÓN
st.set_page_config(page_title="PsicoVisión AI", page_icon="🧠", layout="wide")

# ESTILO DE PIZARRÓN AMPLIO Y CÓMODO
st.markdown("""
    <style>
    .pizarro-box {
        background-color: #1e2d24;
        color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        border: 10px solid #4e342e;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: inset 0 0 20px #000;
        line-height: 1.6;
    }
    .seccion-titulo {
        color: #FFD700;
        border-bottom: 2px solid #FFD700;
        margin-top: 20px;
        font-size: 24px;
    }
    </style>
    """, unsafe_allow_html=True)

# MOTOR DE VOZ
def hablar(texto):
    texto_limpio = texto.replace('"', '').replace("'", "")
    js_code = f"""<script>
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance("{texto_limpio}");
    u.lang = 'es-AR'; u.rate = 1.0;
    window.speechSynthesis.speak(u);
    </script>"""
    st.components.v1.html(js_code, height=0)

# INTERFAZ
st.title("🧠 PsicoVisión AI")
st.write("### El Asistente Completo para Estudiantes de Psicología")

with st.sidebar:
    st.markdown(f"**Desarrollador:**\nJonatan Eliseo Segura")
    st.markdown(f"**DNDA:** EX-2026-41927493")
    st.write("---")
    modo = st.selectbox("Elegí qué necesitas:", ["Clase Completa", "Resumen Rápido", "Solo Preguntas"])

file = st.file_uploader("Subí tu libro o apunte (PDF)", type=["pdf"])

if file:
    pregunta = st.text_input("¿Qué parte del texto querés que te explique hoy?")
    
    if st.button("🎙️ PROCESAR ANÁLISIS"):
        # Contenido generado (Esto luego se conecta con la IA real)
        explicacion = "El concepto que consultás es fundamental en la teoría del autor. Se refiere a la estructura dinámica que organiza la experiencia del sujeto."
        resumen = "En pocas palabras: el sujeto se constituye a través de su relación con el otro y el lenguaje."
        
        # Habla la explicación
        hablar(explicacion + " " + resumen)
        
        # Pizarrón organizado
        st.markdown(f"""
        <div class="pizarro-box">
            <div class='seccion-titulo'>👨‍🏫 Explicación Amplia</div>
            <p>{explicacion}</p>
            
            <div class='seccion-titulo'>📋 Resumen para Estudiar</div>
            <p>{resumen}</p>
            
            <div class='seccion-titulo'>🔑 Conceptos Clave</div>
            <ul>
                <li>Subjetividad</li>
                <li>Aparato Psíquico</li>
                <li>Vínculo Social</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("Cargá un archivo para empezar a usar las herramientas de análisis.")
    
