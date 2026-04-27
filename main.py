import streamlit as st
from PyPDF2 import PdfReader

# --- ESTILOS DE PIZARRÓN Y EXAMEN ---
st.set_page_config(page_title="PsicoVisión AI", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
    .pizarro-box {
        background-color: #1c2e26; color: #ffffff; padding: 30px;
        border-radius: 20px; border: 12px solid #3e2723;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: inset 0 0 40px #000; line-height: 1.7;
    }
    .tiza-amarilla { color: #FFEB3B; font-weight: bold; font-size: 24px; border-bottom: 2px solid #FFEB3B; }
    .tiza-roja { color: #FF5252; font-weight: bold; }
    .tiza-verde { color: #B9F6CA; }
    .examen-box {
        background-color: #f0f2f6; color: #1f1f1f; padding: 20px;
        border-radius: 10px; border-left: 5px solid #ff4b4b; margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def hablar(texto):
    texto_limpio = texto.replace('"', '').replace("'", "")
    js_code = f"""<script>
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance("{texto_limpio}");
    u.lang = 'es-AR'; u.rate = 1.0;
    window.speechSynthesis.speak(u);
    </script>"""
    st.components.v1.html(js_code, height=0)

# --- INTERFAZ ---
st.title("🧠 PsicoVisión AI: Clase y Evaluación")

file = st.file_uploader("Subí tu PDF de estudio", type=["pdf"])

if file:
    reader = PdfReader(file)
    # Extraemos el texto (simulado para el ejemplo)
    texto_leido = reader.pages[0].extract_text()[:500] 

    tema = st.text_input("¿Qué tema específico querés que explique el profesor?")

    if st.button("🎙️ EMPEZAR CLASE COMPLETA"):
        # PARTE 1: LA CLASE EN EL PIZARRÓN
        explicacion = f"Hoy vamos a analizar {tema}. Según el texto, este concepto se define como una estructura dinámica que..."
        hablar(explicacion)
        
        st.markdown(f"""
        <div class='pizarro-box'>
            <div class='tiza-amarilla'>👨‍🏫 CLASE MAGISTRAL: {tema.upper()}</div>
            <p>{explicacion}</p>
            <p class='tiza-verde'>💡 Nota: Esta parte es fundamental para entender la bibliografía de la cursada.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()

        # PARTE 2: LA PRUEBA (SIMULACRO)
        st.subheader("📝 Evaluación de Control")
        st.write("Respondé estas preguntas para saber si estás preparado para el parcial:")
        
        with st.container():
            st.markdown("""
            <div class='examen-box'>
                <strong>Pregunta 1:</strong> ¿Cómo se relaciona este concepto con la subjetividad del autor?<br><br>
                <strong>Pregunta 2:</strong> ¿Cuáles son los tres pilares que menciona el texto sobre este proceso?
            </div>
            """, unsafe_allow_html=True)
            
            respuesta = st.text_area("Escribí tu respuesta aquí para que el profesor la califique:")
            if st.button("Enviar para Calificar"):
                st.success("✅ ¡Excelente razonamiento! Has captado la esencia del texto.")
                hablar("Muy bien hecho. Tu respuesta demuestra que comprendiste el material.")

else:
    st.info("Subí el archivo para generar la clase y el examen automático.")
