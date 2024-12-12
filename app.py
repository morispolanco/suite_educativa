import streamlit as st
from chatbots.critical_thinking_bot import critical_thinking_chatbot
from chatbots.philosophical_inquiry_bot import philosophical_inquiry_chatbot
from chatbots.ethical_dilemma_bot import ethical_dilemma_chatbot
from chatbots.historical_figures_bot import historical_figures_chatbot
from chatbots.text_corrector_bot import text_corrector_chatbot

def main():
    st.title("Suite de Chatbots Educativos")

    chatbot_option = st.selectbox("Selecciona un Chatbot", 
                                    ["Pensamiento Crítico", 
                                     "Indagación Filosófica", 
                                     "Dilemas Éticos", 
                                     "Personajes Históricos", 
                                     "Corrector de Textos"])

    if chatbot_option == "Pensamiento Crítico":
        critical_thinking_chatbot()
    elif chatbot_option == "Indagación Filosófica":
        philosophical_inquiry_chatbot()
    elif chatbot_option == "Dilemas Éticos":
        ethical_dilemma_chatbot()
    elif chatbot_option == "Personajes Históricos":
        historical_figures_chatbot()
    elif chatbot_option == "Corrector de Textos":
        text_corrector_chatbot()

if __name__ == "__main__":
    main()
