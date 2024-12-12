import streamlit as st
import requests

st.set_page_config(page_title="Suite de Chatbots Educativos", layout="wide")

# Definir la lista de chatbots
chatbots = [
    "Chatbot de Pensamiento Crítico",
    "Chatbot de Indagación Filosófica",
    "Chatbot de Dilemas Éticos",
    "Chatbot de Personajes Históricos",
    "Chatbot Corrector de Textos"
]

# Selección del chatbot
selected_chatbot = st.sidebar.selectbox("Seleccione el Chatbot:", chatbots)

# Inicializar estados en session_state
if "interactions" not in st.session_state:
    st.session_state.interactions = 0
    
if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_problem" not in st.session_state:
    st.session_state.current_problem = 0

# Función para llamar a la API externa (simulación)
def llamar_api(mensaje_usuario, instrucciones_sistema="You are a helpful assistant."):
    # Aquí adaptamos el ejemplo de curl a requests
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {st.secrets['API_KEY']}"
    }
    payload = {
        "messages": [
            {"role": "system", "content": instrucciones_sistema},
            {"role": "user", "content": mensaje_usuario}
        ],
        "model": "grok-beta",
        "stream": False,
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        # Dependiendo de la estructura de respuesta de la API, ajustar:
        # Suponiendo la respuesta del asistente esté en data["choices"][0]["message"]["content"]
        try:
            return data["choices"][0]["message"]["content"]
        except:
            return "No se pudo obtener la respuesta del asistente."
    else:
        return f"Error en la petición: {response.status_code} - {response.text}"

# Funciones de lógica para cada chatbot:
def chatbot_pensamiento_critico():
    st.markdown("### Chatbot de Pensamiento Crítico")
    st.write("Este chatbot te presentará un problema y a lo largo de 20 interacciones te guiará en el pensamiento crítico.")
    st.write(f"Interacción actual: {st.session_state.interactions} / 20")

    # Ejemplo: Cada 20 interacciones cambia el problema
    if st.session_state.interactions == 0:
        st.session_state.current_problem += 1
        st.session_state.messages.append(f"Problema {st.session_state.current_problem}: ¿Qué harías si...?")
        st.write(st.session_state.messages[-1])
    else:
        st.write(st.session_state.messages[-1])

    user_input = st.text_input("Tu respuesta:")
    if st.button("Enviar"):
        if user_input:
            # Llamamos a la API
            respuesta = llamar_api(user_input, instrucciones_sistema="Eres un asistente que promueve el pensamiento crítico.")
            st.session_state.messages.append("Usuario: " + user_input)
            st.session_state.messages.append("Asistente: " + respuesta)
            st.session_state.interactions += 1

            if st.session_state.interactions >= 20:
                st.write("Se han completado 20 interacciones, proponiendo un nuevo problema...")
                st.session_state.interactions = 0

    # Mostrar el historial
    for msg in st.session_state.messages[-6:]:  # Muestra los últimos 6 mensajes
        st.write(msg)

def chatbot_indagacion_filosofica():
    st.markdown("### Chatbot de Indagación Filosófica")
    st.write("Este chatbot comienza con una pregunta filosófica y durante 20 interacciones profundiza en tu razonamiento.")
    st.write(f"Interacción actual: {st.session_state.interactions} / 20")

    # Podrías definir una pregunta inicial:
    if st.session_state.interactions == 0:
        pregunta_inicial = "¿Qué es una persona?"
        st.session_state.messages.append(pregunta_inicial)
        st.write(pregunta_inicial)
    else:
        st.write(st.session_state.messages[-1])

    user_input = st.text_input("Tu respuesta filosófica:")
    if st.button("Enviar"):
        if user_input:
            respuesta = llamar_api(user_input, instrucciones_sistema="Eres un asistente que desafía la coherencia del razonamiento filosófico del usuario.")
            st.session_state.messages.append("Usuario: " + user_input)
            st.session_state.messages.append("Asistente: " + respuesta)
            st.session_state.interactions += 1

            if st.session_state.interactions >= 20:
                # Al finalizar, ofrecer una síntesis
                sintesis = "Basado en tus respuestas, tu visión del ser humano y la vida se resume en..."
                st.session_state.messages.append("Asistente (Síntesis): " + sintesis)
                st.write(sintesis)
                st.session_state.interactions = 0

    for msg in st.session_state.messages[-6:]:
        st.write(msg)

def chatbot_dilemas_eticos():
    st.markdown("### Chatbot de Dilemas Éticos")
    st.write("Este chatbot presenta un dilema ético y analiza tu postura durante 20 interacciones.")
    st.write(f"Interacción actual: {st.session_state.interactions} / 20")

    if st.session_state.interactions == 0:
        dilema_inicial = "Estás en un puente y puedes salvar 5 vidas empujando a una persona. ¿Qué harías?"
        st.session_state.messages.append(dilema_inicial)
        st.write(dilema_inicial)
    else:
        st.write(st.session_state.messages[-1])

    user_input = st.text_input("Tu respuesta ética:")
    if st.button("Enviar"):
        if user_input:
            respuesta = llamar_api(user_input, instrucciones_sistema="Eres un asistente que analiza posturas éticas y morales.")
            st.session_state.messages.append("Usuario: " + user_input)
            st.session_state.messages.append("Asistente: " + respuesta)
            st.session_state.interactions += 1

            if st.session_state.interactions >= 20:
                # Proporcionar evaluación de la postura ética
                evaluacion = "Tu postura ética parece inclinarse hacia el utilitarismo/deontologismo/etc."
                st.session_state.messages.append("Asistente (Evaluación): " + evaluacion)
                st.write(evaluacion)
                st.session_state.interactions = 0

    for msg in st.session_state.messages[-6:]:
        st.write(msg)

def chatbot_personajes_historicos():
    st.markdown("### Chatbot de Personajes Históricos")
    st.write("Este chatbot te sitúa en el lugar de un personaje histórico y analiza tus decisiones durante 20 interacciones.")
    st.write(f"Interacción actual: {st.session_state.interactions} / 20")

    if st.session_state.interactions == 0:
        contexto = "Eres Napoleón en la batalla de Waterloo. ¿Qué decisión tomarás a continuación?"
        st.session_state.messages.append(contexto)
        st.write(contexto)
    else:
        st.write(st.session_state.messages[-1])

    user_input = st.text_input("Tu decisión histórica:")
    if st.button("Enviar"):
        if user_input:
            respuesta = llamar_api(user_input, instrucciones_sistema="Eres un asistente que simula el contexto histórico y analiza las decisiones tomadas por el usuario como si fuera un personaje histórico.")
            st.session_state.messages.append("Usuario: " + user_input)
            st.session_state.messages.append("Asistente: " + respuesta)
            st.session_state.interactions += 1

            if st.session_state.interactions >= 20:
                # Evaluar las decisiones en relación al personaje histórico
                evaluacion = "Tus decisiones se asemejan a las estrategias reales de Napoleón en ciertos aspectos..."
                st.session_state.messages.append("Asistente (Evaluación): " + evaluacion)
                st.write(evaluacion)
                st.session_state.interactions = 0

    for msg in st.session_state.messages[-6:]:
        st.write(msg)

def chatbot_corrector_textos():
    st.markdown("### Chatbot Corrector de Textos")
    st.write("Ingresa un texto y el chatbot lo corregirá, destacando errores y ofreciendo sugerencias.")

    texto_usuario = st.text_area("Escribe tu texto aquí:")
    if st.button("Corregir"):
        if texto_usuario.strip():
            # Aquí podrías enviar el texto a la API con un prompt adecuado
            prompt = f"Corrige el siguiente texto, destacando errores y explicando las correcciones: {texto_usuario}"
            respuesta = llamar_api(prompt, instrucciones_sistema="Eres un corrector experto de textos.")
            st.write("Correcciones:")
            st.write(respuesta)
        else:
            st.warning("Por favor, ingresa un texto antes de corregir.")

# Mostrar el chatbot seleccionado
if selected_chatbot == "Chatbot de Pensamiento Crítico":
    chatbot_pensamiento_critico()
elif selected_chatbot == "Chatbot de Indagación Filosófica":
    chatbot_indagacion_filosofica()
elif selected_chatbot == "Chatbot de Dilemas Éticos":
    chatbot_dilemas_eticos()
elif selected_chatbot == "Chatbot de Personajes Históricos":
    chatbot_personajes_historicos()
elif selected_chatbot == "Chatbot Corrector de Textos":
    chatbot_corrector_textos()
