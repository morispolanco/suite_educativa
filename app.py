import streamlit as st
import requests

st.set_page_config(page_title="Suite de Chatbots Educativos", layout="wide")

# Lista de chatbots
chatbots = [
    "Chatbot de Pensamiento Crítico",
    "Chatbot de Indagación Filosófica",
    "Chatbot de Dilemas Éticos",
    "Chatbot de Personajes Históricos",
    "Chatbot Corrector de Textos"
]

# Selección del chatbot
selected_chatbot = st.sidebar.selectbox("Seleccione el Chatbot:", chatbots)

# Función para llamar a la API externa
def llamar_api(mensaje_usuario, instrucciones_sistema="You are a helpful assistant."):
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
        try:
            return data["choices"][0]["message"]["content"]
        except:
            return "No se pudo obtener la respuesta del asistente."
    else:
        return f"Error en la petición: {response.status_code} - {response.text}"

# --- Chatbot de Pensamiento Crítico ---
def init_critical_thinking_state():
    if "critical_thinking_interactions" not in st.session_state:
        st.session_state.critical_thinking_interactions = 0
    if "critical_thinking_messages" not in st.session_state:
        st.session_state.critical_thinking_messages = []
    if "critical_thinking_current_problem" not in st.session_state:
        st.session_state.critical_thinking_current_problem = 0

def chatbot_pensamiento_critico():
    st.markdown("### Chatbot de Pensamiento Crítico")
    st.write("Este chatbot te presentará un problema y a lo largo de 20 interacciones te guiará en el pensamiento crítico.")
    st.write(f"Interacción actual: {st.session_state.critical_thinking_interactions} / 20")

    if st.session_state.critical_thinking_interactions == 0:
        st.session_state.critical_thinking_current_problem += 1
        new_problem = f"Problema {st.session_state.critical_thinking_current_problem}: Imagina un escenario... ¿Qué harías si...?"
        st.session_state.critical_thinking_messages.append(new_problem)
        st.write(new_problem)
    else:
        st.write(st.session_state.critical_thinking_messages[-1])

    user_input = st.text_input("Tu respuesta:", key="critical_thinking_user_input")
    if st.button("Enviar", key="critical_thinking_send"):
        if user_input:
            respuesta = llamar_api(
                user_input,
                instrucciones_sistema="Eres un asistente que promueve el pensamiento crítico."
            )
            st.session_state.critical_thinking_messages.append("Usuario: " + user_input)
            st.session_state.critical_thinking_messages.append("Asistente: " + respuesta)
            st.session_state.critical_thinking_interactions += 1

            if st.session_state.critical_thinking_interactions >= 20:
                st.write("Se han completado 20 interacciones, proponiendo un nuevo problema...")
                st.session_state.critical_thinking_interactions = 0

    # Mostrar el historial breve
    for msg in st.session_state.critical_thinking_messages[-6:]:
        st.write(msg)


# --- Chatbot de Indagación Filosófica ---
def init_filosofia_state():
    if "filosofia_interactions" not in st.session_state:
        st.session_state.filosofia_interactions = 0
    if "filosofia_messages" not in st.session_state:
        st.session_state.filosofia_messages = []

def chatbot_indagacion_filosofica():
    st.markdown("### Chatbot de Indagación Filosófica")
    st.write("Este chatbot comienza con una pregunta filosófica y durante 20 interacciones profundiza en tu razonamiento.")
    st.write(f"Interacción actual: {st.session_state.filosofia_interactions} / 20")

    if st.session_state.filosofia_interactions == 0 and not st.session_state.filosofia_messages:
        pregunta_inicial = "¿Qué es una persona?"
        st.session_state.filosofia_messages.append(pregunta_inicial)
        st.write(pregunta_inicial)
    else:
        st.write(st.session_state.filosofia_messages[-1])

    user_input = st.text_input("Tu respuesta filosófica:", key="filosofia_user_input")
    if st.button("Enviar", key="filosofia_send"):
        if user_input:
            respuesta = llamar_api(
                user_input,
                instrucciones_sistema="Eres un asistente que desafía la coherencia del razonamiento filosófico del usuario."
            )
            st.session_state.filosofia_messages.append("Usuario: " + user_input)
            st.session_state.filosofia_messages.append("Asistente: " + respuesta)
            st.session_state.filosofia_interactions += 1

            if st.session_state.filosofia_interactions >= 20:
                # Al finalizar las 20 interacciones, generar una síntesis
                sintesis = "Basado en tus respuestas, tu visión del ser humano y la vida se resume en..."
                st.session_state.filosofia_messages.append("Asistente (Síntesis): " + sintesis)
                st.write(sintesis)
                st.session_state.filosofia_interactions = 0

    for msg in st.session_state.filosofia_messages[-6:]:
        st.write(msg)


# --- Chatbot de Dilemas Éticos ---
def init_dilemas_state():
    if "dilemas_interactions" not in st.session_state:
        st.session_state.dilemas_interactions = 0
    if "dilemas_messages" not in st.session_state:
        st.session_state.dilemas_messages = []

def chatbot_dilemas_eticos():
    st.markdown("### Chatbot de Dilemas Éticos")
    st.write("Este chatbot presenta un dilema ético y analiza tu postura durante 20 interacciones.")
    st.write(f"Interacción actual: {st.session_state.dilemas_interactions} / 20")

    if st.session_state.dilemas_interactions == 0 and not st.session_state.dilemas_messages:
        dilema_inicial = "Estás en un puente y puedes salvar 5 vidas empujando a una persona. ¿Qué harías?"
        st.session_state.dilemas_messages.append(dilema_inicial)
        st.write(dilema_inicial)
    else:
        st.write(st.session_state.dilemas_messages[-1])

    user_input = st.text_input("Tu respuesta ética:", key="dilemas_user_input")
    if st.button("Enviar", key="dilemas_send"):
        if user_input:
            respuesta = llamar_api(
                user_input,
                instrucciones_sistema="Eres un asistente que analiza posturas éticas y morales."
            )
            st.session_state.dilemas_messages.append("Usuario: " + user_input)
            st.session_state.dilemas_messages.append("Asistente: " + respuesta)
            st.session_state.dilemas_interactions += 1

            if st.session_state.dilemas_interactions >= 20:
                evaluacion = "Tu postura ética parece inclinarse hacia el utilitarismo/deontologismo/etc."
                st.session_state.dilemas_messages.append("Asistente (Evaluación): " + evaluacion)
                st.write(evaluacion)
                st.session_state.dilemas_interactions = 0

    for msg in st.session_state.dilemas_messages[-6:]:
        st.write(msg)


# --- Chatbot de Personajes Históricos ---
def init_personajes_state():
    if "personajes_interactions" not in st.session_state:
        st.session_state.personajes_interactions = 0
    if "personajes_messages" not in st.session_state:
        st.session_state.personajes_messages = []

def chatbot_personajes_historicos():
    st.markdown("### Chatbot de Personajes Históricos")
    st.write("Este chatbot te sitúa en el lugar de un personaje histórico y analiza tus decisiones durante 20 interacciones.")
    st.write(f"Interacción actual: {st.session_state.personajes_interactions} / 20")

    if st.session_state.personajes_interactions == 0 and not st.session_state.personajes_messages:
        contexto = "Eres Napoleón en la batalla de Waterloo. ¿Qué decisión tomarás a continuación?"
        st.session_state.personajes_messages.append(contexto)
        st.write(contexto)
    else:
        st.write(st.session_state.personajes_messages[-1])

    user_input = st.text_input("Tu decisión histórica:", key="personajes_user_input")
    if st.button("Enviar", key="personajes_send"):
        if user_input:
            respuesta = llamar_api(
                user_input,
                instrucciones_sistema="Eres un asistente que simula un contexto histórico y analiza las decisiones del usuario."
            )
            st.session_state.personajes_messages.append("Usuario: " + user_input)
            st.session_state.personajes_messages.append("Asistente: " + respuesta)
            st.session_state.personajes_interactions += 1

            if st.session_state.personajes_interactions >= 20:
                evaluacion = "Tus decisiones se asemejan a las estrategias reales de Napoleón en ciertos aspectos..."
                st.session_state.personajes_messages.append("Asistente (Evaluación): " + evaluacion)
                st.write(evaluacion)
                st.session_state.personajes_interactions = 0

    for msg in st.session_state.personajes_messages[-6:]:
        st.write(msg)


# --- Chatbot Corrector de Textos ---
def init_corrector_state():
    if "corrector_messages" not in st.session_state:
        st.session_state.corrector_messages = []

def chatbot_corrector_textos():
    st.markdown("### Chatbot Corrector de Textos")
    st.write("Ingresa un texto y el chatbot lo corregirá, destacando errores y ofreciendo sugerencias.")
    texto_usuario = st.text_area("Escribe tu texto aquí:", key="corrector_user_text")
    if st.button("Corregir", key="corrector_send"):
        if texto_usuario.strip():
            prompt = f"Corrige el siguiente texto, destacando errores y explicando las correcciones:\n\n{texto_usuario}"
            respuesta = llamar_api(prompt, instrucciones_sistema="Eres un corrector experto de textos.")
            st.session_state.corrector_messages.append("Texto del usuario: " + texto_usuario)
            st.session_state.corrector_messages.append("Corrección: " + respuesta)
            st.write("Correcciones:")
            st.write(respuesta)
        else:
            st.warning("Por favor, ingresa un texto antes de corregir.")

    for msg in st.session_state.corrector_messages[-6:]:
        st.write(msg)


# Inicializar estados del chatbot seleccionado
if selected_chatbot == "Chatbot de Pensamiento Crítico":
    init_critical_thinking_state()
    chatbot_pensamiento_critico()
elif selected_chatbot == "Chatbot de Indagación Filosófica":
    init_filosofia_state()
    chatbot_indagacion_filosofica()
elif selected_chatbot == "Chatbot de Dilemas Éticos":
    init_dilemas_state()
    chatbot_dilemas_eticos()
elif selected_chatbot == "Chatbot de Personajes Históricos":
    init_personajes_state()
    chatbot_personajes_historicos()
elif selected_chatbot == "Chatbot Corrector de Textos":
    init_corrector_state()
    chatbot_corrector_textos()
