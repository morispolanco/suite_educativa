import streamlit as st
import requests

def philosophical_inquiry_chatbot():
    st.header("Chatbot de Indagación Filosófica")
    user_input = st.text_input("Plantea una pregunta filosófica:")
    
    if st.button("Enviar"):
        response = requests.post(
            "https://api.x.ai/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer YOUR_API_KEY"
            },
            json={
                "messages": [
                    {"role": "system", "content": "You are a philosophical inquiry assistant."},
                    {"role": "user", "content": user_input}
                ],
                "model": "grok-beta",
                "stream": False,
                "temperature": 0.7
            }
        )
        
        if response.status_code == 200:
            answer = response.json().get("choices")[0].get("message").get("content")
            st.write(answer)
        else:
            st.write("Error en la comunicación con el chatbot.")
