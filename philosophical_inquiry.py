import streamlit as st

# Función para la aplicación de exploración filosófica
def philosophical_inquiry_app():
    st.title("Exploración Filosófica")
    
    # Inicializar el estado de la sesión
    if 'chat_started' not in st.session_state:
        st.session_state.chat_started = False
    if 'current_topic' not in st.session_state:
        st.session_state.current_topic = 0
    if 'user_responses' not in st.session_state:
        st.session_state.user_responses = []
    
    topics = [
        "¿Qué es la verdad?",
        "¿Es el libre albedrío una ilusión?",
        "¿Qué significa vivir una buena vida?",
        "¿Existen los universales?",
        "¿Qué es la justicia?",
        "¿Es la moralidad objetiva o subjetiva?",
        "¿Qué es la felicidad?",
        "¿Es la naturaleza humana inherentemente buena o mala?",
        "¿Qué es el conocimiento?",
        "¿Es el sufrimiento necesario para el crecimiento personal?",
        "¿Qué papel juega la razón en la vida humana?",
        "¿Es la religión necesaria para la moralidad?",
        "¿Qué es la identidad?",
        "¿Es el arte una forma de conocimiento?",
        "¿Qué significa ser auténtico?",
        "¿Es el tiempo una ilusión?",
        "¿Qué es la belleza?",
        "¿Es el egoísmo natural en los seres humanos?",
        "¿Qué es la libertad?",
        "¿Es la vida un sueño?"
    ]
    
    # Mensaje inicial
    if not st.session_state.chat_started:
        st.markdown("¡Bienvenido a la Exploración Filosófica! Aquí discutiremos temas profundos y reflexivos. "
                   "Te presentaré un tema a la vez. ¿Estás listo para comenzar?")
        
        if st.button("¡Sí, comencemos!", key='start_button'):
            st.session_state.chat_started = True
            st.experimental_rerun()
    
    # Mostrar temas
    elif st.session_state.current_topic < len(topics):
        topic = topics[st.session_state.current_topic]
        st.markdown(f"### Tema {st.session_state.current_topic + 1}: {topic}")
        
        # Área para la respuesta del usuario
        user_response = st.text_area("Escribe tus pensamientos aquí:", height=200)
        
        # Botones para enviar respuesta o ver retroalimentación
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Enviar Pensamientos", key=f'enviar_pensamientos_{st.session_state.current_topic}'):
                if user_response:
                    st.session_state.user_responses.append(user_response)
                    st.success("¡Gracias por compartir tus pensamientos! Ahora puedes ver la retroalimentación.")
        
        with col2:
            if st.button("Ver Retroalimentación", key=f'ver_retroalimentacion_{st.session_state.current_topic}'):
                if len(st.session_state.user_responses) > st.session_state.current_topic:
                    st.write("### Reflexiones sobre el tema:")
                    # Aquí se puede agregar un sistema de retroalimentación
                    st.write("**Reflexiona sobre tus pensamientos y considera:**")
                    st.write("- ¿Has considerado otros puntos de vista?\n- ¿Cómo se relacionan tus pensamientos con el tema?\n- ¿Qué preguntas adicionales surgen de tu reflexión?")
                    
                    if st.button("Siguiente Tema", key=f'siguiente_tema_{st.session_state.current_topic}'):
                        st.session_state.current_topic += 1
                        st.experimental_rerun()
                else:
                    st.warning("Por favor, envía tus pensamientos primero.")
    
    else:
        st.success("¡Felicitaciones! Has completado todos los temas de exploración filosófica.")
        if st.button("Comenzar de Nuevo", key='start_again_button'):
            st.session_state.chat_started = False
            st.session_state.current_topic = 0
            st.session_state.user_responses = []
            st.experimental_rerun()

philosophical_inquiry_app()
