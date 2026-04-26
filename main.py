import streamlit as st

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="PsicoVisión AI", page_icon="🧠")

# ENCABEZADO PROFESIONAL
st.title("🧠 PsicoVisión AI")
st.subheader("Análisis Inteligente para Estudiantes de Psicología")
st.markdown("---")

# INFORMACIÓN LEGAL Y AUTOR
st.sidebar.info(f"""
**Autor:** Jonatan Eliseo Segura  
**Registro DNDA:** EX-2026-41927493  
**Versión:** 1.0 (Estable)
""")

# CUERPO DE LA APP
st.write("### 🚀 Bienvenido")
st.write("Subí tus apuntes o textos de la facultad para generar guiones de estudio y análisis de conceptos.")

# CARGA DE ARCHIVOS
uploaded_file = st.file_uploader("Subí tu PDF de la facultad", type=["pdf"])

if uploaded_file is not None:
    st.success("¡Archivo cargado con éxito!")
    
    st.write("### 📝 Opciones de Generación")
    opcion = st.selectbox("¿Qué querés generar?", [
        "Guion para TikTok/Reels (Resumen viral)",
        "Análisis de conceptos clave",
        "Preguntas de examen",
        "Resumen ejecutivo"
    ])
    
    if st.button("Generar Contenido"):
        st.info(f"Procesando análisis para: {opcion}...")
        # Aquí irá la lógica de IA en la siguiente fase
        st.write("---")
        st.write("#### Resultado Sugerido:")
        st.write("Estamos conectando con el motor de IA para procesar tu texto. ¡Ya casi está listo!")
else:
    st.warning("Esperando que subas un archivo para empezar...")

# PIE DE PÁGINA
st.markdown("---")
st.caption("Desarrollado para facilitar el estudio en la UNLP y facultades de Psicología.")
