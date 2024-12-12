import streamlit as st

# Función para la aplicación de pensamiento crítico
def critical_thinking_app():
    st.title("Desarrollo del Pensamiento Crítico")
    
    # Inicializar el estado de la sesión
    if 'chat_started' not in st.session_state:
        st.session_state.chat_started = False
    if 'current_exercise' not in st.session_state:
        st.session_state.current_exercise = 0
    if 'user_responses' not in st.session_state:
        st.session_state.user_responses = []
    
    exercises = [
        {
            "intro": "**Ejercicio 1: Análisis de Argumentos**\n\nLee el siguiente argumento y analízalo:\n\n"
                    '"La universidad debería prohibir el uso de teléfonos móviles en las aulas para mejorar la '
                    'concentración y el rendimiento académico de los estudiantes."\n\n'
                    "- ¿Cuáles son las premisas del argumento?\n"
                    "- ¿Es válido el razonamiento?\n"
                    "- ¿Qué suposiciones subyacentes hace el argumento?\n"
                    "- ¿Puedes pensar en posibles contraargumentos?",
            "feedback": {
                "premisas": "Deberías identificar: 1) El uso de móviles afecta la concentración, "
                           "2) La concentración afecta el rendimiento académico",
                "razonamiento": "Considera si la relación causa-efecto está bien establecida",
                "suposiciones": "Piensa en: ¿Todos los usos del móvil son perjudiciales? "
                               "¿No hay usos educativos beneficiosos?",
                "contraargumentos": "Podrías mencionar: uso educativo de apps, responsabilidad personal, "
                                  "preparación para el mundo real"
            }
        },
        {
            "intro": "**Ejercicio 2: Evaluación de Evidencias**\n\n"
                    "Analiza la siguiente afirmación:\n\n"
                    '"Los videojuegos violentos son la principal causa del aumento de la violencia juvenil, '
                    'ya que las estadísticas muestran que la violencia juvenil ha aumentado desde que los '
                    'videojuegos se hicieron populares."\n\n'
                    "- ¿Qué tipo de evidencia se presenta?\n"
                    "- ¿Es suficiente esta evidencia?\n"
                    "- ¿Qué otras variables deberían considerarse?\n"
                    "- ¿Puedes identificar alguna falacia en el razonamiento?",
            "feedback": {
                "evidencia": "La evidencia es correlacional, no causal",
                "suficiencia": "Una correlación temporal no prueba causalidad",
                "variables": "Factores socioeconómicos, entorno familiar, influencia de pares, etc.",
                "falacias": "Post hoc ergo propter hoc (después de esto, luego a causa de esto)"
            }
       },
        {
            "intro": "**Ejercicio 3: Resolución de Dilemas**\n\n"
                    "Considera el siguiente dilema ético:\n\n"
                    '"Una inteligencia artificial desarrollada para diagnóstico médico comete un error que '
                    'resulta en un diagnóstico incorrecto. ¿Quién es responsable: los desarrolladores, '
                    'el hospital que la implementó, o el médico que confió en ella?"\n\n'
                    "- ¿Cuáles son los diferentes aspectos éticos a considerar?\n"
                    "- ¿Cómo se distribuye la responsabilidad?\n"
                    "- ¿Qué medidas preventivas deberían existir?\n"
                    "- ¿Cómo equilibrar innovación tecnológica y seguridad del paciente?",
            "feedback": {
                "aspectos_eticos": "Autonomía médica, responsabilidad profesional, confianza en la tecnología",
                "responsabilidad": "Considerar la cadena de responsabilidades y el papel de cada actor",
                "prevencion": "Sistemas de verificación, capacitación, protocolos de seguridad",
                "equilibrio": "Balance entre avance tecnológico y principio de precaución"
            }
        }
    ]
    
    # Mensaje inicial
    if not st.session_state.chat_started:
        st.markdown("¡Hola! Soy tu asistente para desarrollar el pensamiento crítico. "
                   "Te presentaré una actividad a la vez para que puedas concentrarte mejor en cada ejercicio. "
                   "¿Estás listo para comenzar?")
        
        if st.button("¡Sí, comencemos!"):
            st.session_state.chat_started = True
            try:
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error al reiniciar la aplicación: {e}")
    
    # Mostrar ejercicios
    elif st.session_state.current_exercise < len(exercises):
        exercise = exercises[st.session_state.current_exercise]
        st.markdown(exercise["intro"])
        
        # Área para la respuesta del usuario
        user_response = st.text_area("Escribe tu análisis aquí:", height=200)
        
        # Botones para enviar respuesta o ver retroalimentación
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Enviar Análisis"):
                if user_response:
                    st.session_state.user_responses.append(user_response)
                    st.success("¡Gracias por tu análisis! Ahora puedes ver la retroalimentación.")
                    
                    try:
                        st.experimental_rerun()
                    except Exception as e:
                        st.error(f"Error al reiniciar la aplicación: {e}")
        
        with col2:
            if st.button("Ver Retroalimentación"):
                if len(st.session_state.user_responses) > st.session_state.current_exercise:
                    st.write("### Aspectos clave a considerar:")
                    for key, value in exercise["feedback"].items():
                        st.write(f"**{key.replace('_', ' ').title()}:**")
                        st.write(value)
                    
                    if st.button("Siguiente Ejercicio"):
                        st.session_state.current_exercise += 1
                        try:
                            st.experimental_rerun()
                        except Exception as e:
                            st.error(f"Error al reiniciar la aplicación: {e}")
                else:
                    st.warning("Por favor, envía tu análisis primero.")
    
    else:
        st.success("¡Felicitaciones! Has completado todos los ejercicios de pensamiento crítico.")
        if st.button("Comenzar de Nuevo"):
            st.session_state.chat_started = False
            st.session_state.current_exercise = 0
            st.session_state.user_responses = []
            try:
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error al reiniciar la aplicación: {e}")

critical_thinking_app()
