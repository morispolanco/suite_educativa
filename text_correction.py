import streamlit as st

# Función para el asistente de corrección de textos
def text_correction_app():
    st.title("Asistente de Corrección de Textos")
    st.subheader("Mejora de Gramática y Estilo con Explicaciones")
    
    user_text = st.text_area("Ingresa tu texto para corrección:", height=200)
    
    if st.button("Analizar Texto"):
        if user_text:
            st.write("### Correcciones y Explicaciones:")
            
            # Ejemplo de correcciones (en una app real, esto usaría un servicio NLP apropiado)
            corrections = [
                {
                    "original": "haber",
                    "correction": "a ver",
                    "explanation": "Se usa 'a ver' cuando queremos expresar el acto de mirar o examinar algo."
                },
                {
                    "original": "hay",
                    "correction": "ahí",
                    "explanation": "Se usa 'ahí' para indicar lugar, mientras que 'hay' es una forma del verbo haber."
                }
            ]
            
            for corr in corrections:
                st.write(f"**Original:** {corr['original']}")
                st.write(f"**Corrección:** {corr['correction']}")
                st.write(f"_Explicación:_ {corr['explanation']}")
                st.write("---")

