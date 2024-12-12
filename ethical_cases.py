import streamlit as st
import requests

def ethical_dilemma_chatbot():
    st.header("Chatbot de Dilemas Éticos")
    user_input = st.text_input("Describe un dilema ético:")
    
    if st.button("Enviar"):
        response = requests.post(
            "https://api.x.ai/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer YOUR_API_KEY"
            },
            json={
                "messages": [
                    {"role": "system", "content": "You are an ethical dilemma assistant."},
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
