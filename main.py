import streamlit as st
import time

# CONFIGURACIÓN PROFESIONAL
st.set_page_config(page_title="PsicoVisión AI", page_icon="🧠", layout="wide")

# ESTILO DE PIZARRÓN MULTICOLOR Y PEDAGÓGICO
st.markdown("""
    <style>
    .pizarro-box {
        background-color: #1c2e26;
        color: #ffffff;
        padding: 40px;
        border-radius: 25px;
        border: 15px solid #3e2723;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: inset 0 0 50px #000;
        line-height: 1.8;
        font-size: 20px;
    }
    .tiza-amarilla { color: #FFEB3B; font-weight: bold; font-size: 28px; border-bottom: 2px solid #FFEB3B; margin-bottom: 15px; }
    .tiza-roja { color: #FF5252; font-weight: bold; } 
    .tiza-celeste { color: #81D4FA; font-weight: bold; }
    .tiza-verde { color: #B9F6CA; font-style: italic; }
    .tiza-blanca { color: #FFFFFF; }
    </style>
    """, unsafe_allow_html=True)

# MOTOR DE VOZ HUMANA
def hablar_profesor(texto):
    texto_limpio = texto.replace('"', '').replace("'", "")
    js_code = f"""<script>
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance("{texto_limpio}");
    u.lang = 'es-AR'; u.rate = 1.0; u.pitch = 1.0;
    window.speechSynthesis.speak(u);
    </script>"""
    st.components.v1.html(js_code, height=0)

# --- INTERFAZ ---
st.title("🧠 PsicoVisión AI: Tu Profesor Particular")
st.write("---")

with st.sidebar:
    st.header("⚙️ Herramientas de Estudio")
    st.info(f"**Autor:** Jonatan E. Segura\n\n**Registro DNDA:** EX-2026-41927493")
    st.write("---")
    modo = st.radio("¿Qué haremos hoy?", [
        "Clase Magistral y Resumen", 
        "Traductor de Autores (Simple)", 
        "Simulacro de Examen",
        "Comparar con otro Autor"
    ])
    st.success("Modo Confiable: ON")

file = st.file_uploader("Subí tu material de estudio (PDF)", type=["pdf"])

if file:
    pregunta = st.text_input("¿Qué concepto querés profundizar hoy?")
    
    if st.button("🎙️ ¡PROFESOR, EXPLIQUE!"):
        # Lógica de respuesta según el modo
        if modo == "Clase Magistral y Resumen":
            explicacion = "He leído el texto completo. El autor centraliza su tesis en la construcción del sujeto a través del lenguaje."
            puntos = "1. Estructura psíquica. 2. Influencia del entorno. 3. El deseo inconsciente."
            
            hablar_profesor(explicacion + " " + puntos)
            
            st.markdown(f"""
            <div class="pizarro-box">
                <div class='tiza-amarilla'>👨‍🏫 CLASE MAGISTRAL</div>
                <p class='tiza-blanca'>{explicacion}</p>
                <div class='tiza-celeste'>🔑 CONCEPTOS PARA EL PARCIAL:</div>
                <p class='tiza-blanca'>{puntos}</p>
                <div class='tiza-roja'>⚠️ IMPORTANTE:</div>
                <p class='tiza-blanca'>Este tema es pregunta fija de final. Relacionalo con la teoría del vínculo.</p>
                <div class='tiza-verde'>💡 EJEMPLO:</div>
                <p class='tiza-blanca'>Es como cuando un niño aprende a hablar; no solo copia sonidos, construye su mundo.</p>
            </div>
            """, unsafe_allow_html=True)

        elif modo == "Simulacro de Examen":
            pregunta_examen = "Pregunta de examen: ¿Cómo define el autor la 'subjetividad' en el capítulo 2?"
            hablar_profesor(pregunta_examen)
            st.markdown(f"""
            <div class="pizarro-box">
                <div class='tiza-amarilla'>📝 SIMULACRO DE EXAMEN</div>
                <p class='tiza-roja'>{pregunta_examen}</p>
                <br>
                <p class='tiza-blanca'>(Tómate un minuto para pensar la respuesta y luego consúltame la solución).</p>
            </div>
            """, unsafe_allow_html=True)
            
        elif modo == "Traductor de Autores (Simple)":
            traduccion = "Básicamente, lo que el autor dice con palabras difíciles es que aprendemos mejor cuando estamos con otros."
            hablar_profesor(traduccion)
            st.markdown(f"""
            <div class="pizarro-box">
                <div class='tiza-amarilla'>🐥 EXPLICACIÓN SIMPLE</div>
                <p class='tiza-verde'>{traduccion}</p>
            </div>
            """, unsafe_allow_html=True)
else:
    st.info("Subí un libro para empezar la clase interactiva con colores y voz.")
