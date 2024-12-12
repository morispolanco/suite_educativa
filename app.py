import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Suite de Aplicaciones Educativas",
    page_icon="🎓",
    layout="wide"
)

from critical_thinking import critical_thinking_app
from philosophical_inquiry import philosophical_inquiry_app
from historical_decisions import historical_decisions_app
from ethical_cases import ethical_cases_app
from text_correction import text_correction_app
import os
from dotenv import load_dotenv
import requests
import json

# Cargar variables de entorno
load_dotenv()

# Lógica de enrutamiento para la aplicación
if __name__ == '__main__':
    st.sidebar.title("Menú")
    app_mode = st.sidebar.selectbox("Selecciona el modo de la aplicación:", ("Pensamiento Crítico", "Indagación Filosófica", "Corrección de Textos", "Decisiones Históricas", "Casos Éticos"))
    
    if app_mode == "Pensamiento Crítico":
        critical_thinking_app()
    elif app_mode == "Indagación Filosófica":
        philosophical_inquiry_app()
    elif app_mode == "Corrección de Textos":
        text_correction_app()
    elif app_mode == "Decisiones Históricas":
        historical_decisions_app()
    elif app_mode == "Casos Éticos":
        ethical_cases_app()
