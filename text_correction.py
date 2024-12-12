import streamlit as st
import requests

def text_corrector_chatbot():
    st.header("Chatbot Corrector de Textos")
    user_input = st.text_area("Ingresa el texto que deseas corregir:")
    
    if st.button("Corregir"):
        response = requests.post(
            "https://api.x.ai/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer YOUR_API_KEY"
            },
            json={
                "messages": [
                    {"role": "system", "content": "You are a text correction assistant."},
                    {"role": "user", "content": user_input}
                ],
                "model": "grok-beta",
                "stream": False,
                "temperature": 0.7
            }
        )
        
        if response.status_code == 200:
            corrections = response.json().get("choices")[0].get("message").get("content")
            st.write(corrections)
        else:
            st.write("Error en la comunicación con el chatbot.")
