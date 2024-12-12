import streamlit as st
import requests

# Función para llamar a la API de X.AI
def call_xai_api(user_message):
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + st.secrets["general"]["api_key"]
    }
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        "model": "grok-beta",
        "stream": False,
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Función para el asistente de corrección de textos
def text_correction_app():
    st.title("Asistente de Corrección de Textos")
    st.subheader("Mejora de Gramática y Estilo con Explicaciones")
    
    user_text = st.text_area("Ingresa tu texto para corrección:", height=200)
    
    if st.button("Analizar Texto"):
        if user_text:
            st.write("### Correcciones y Explicaciones:")
            
            # Llamar a la API de X.AI para obtener correcciones
            api_response = call_xai_api(user_text)
            st.write(api_response)  # Mostrar la respuesta de la API
