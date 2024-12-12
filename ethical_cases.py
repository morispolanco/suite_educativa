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

# Función para el módulo de casos éticos
def ethical_cases_app():
    st.title("Casos Éticos")
    st.subheader("Reflexiona sobre dilemas éticos y comparte tu análisis")
    
    # Casos éticos
    cases = [
        {
            "case": "Un amigo te pide que lo ayudes a hacer trampa en un examen. ¿Qué harías?",
            "feedback": "Ayudar a un amigo a hacer trampa puede parecer leal, pero es deshonesto y puede tener consecuencias negativas para ambos."
        },
        {
            "case": "Encuentras una billetera en la calle con dinero en efectivo. ¿La devuelves o la quedas?",
            "feedback": "Devolver la billetera es lo correcto, ya que el dinero no te pertenece y podría ser muy importante para su dueño."
        },
        {
            "case": "Tu jefe te pide que ocultes información negativa sobre un proyecto. ¿Qué harías?",
            "feedback": "Ocultar información puede ser perjudicial para la empresa y para tus colegas. La transparencia es fundamental."
        },
        {
            "case": "Un compañero de trabajo está siendo acosado, pero no quieres involucrarte. ¿Qué harías?",
            "feedback": "Es importante actuar y ayudar a tu compañero. Ignorar el acoso perpetúa el problema."
        },
        {
            "case": "Descubres que un producto que vendes tiene defectos peligrosos. ¿Qué haces?",
            "feedback": "Es tu responsabilidad informar a los clientes y retirar el producto del mercado para proteger su seguridad."
        },
        {
            "case": "Un familiar te pide que mientas en un asunto legal. ¿Qué harías?",
            "feedback": "Mentir es ilegal y poco ético. Es mejor ser honesto, incluso si es difícil."
        },
        {
            "case": "Tienes la oportunidad de obtener un ascenso, pero implica tomar decisiones poco éticas. ¿Qué harías?",
            "feedback": "El éxito no vale la pena si se logra a costa de la ética. Es mejor buscar oportunidades que se alineen con tus valores."
        },
        {
            "case": "Un amigo te pide que le des una respuesta a un examen. ¿Qué harías?",
            "feedback": "Ayudar a un amigo a hacer trampa no solo es deshonesto, sino que también puede perjudicar su aprendizaje."
        },
        {
            "case": "Te ofrecen un soborno para asegurar un contrato. ¿Qué harías?",
            "feedback": "Aceptar un soborno es ilegal y poco ético. Es mejor rechazarlo y actuar con integridad."
        },
        {
            "case": "Alguien te pide que hables mal de un colega. ¿Qué harías?",
            "feedback": "Hablar mal de otros es poco profesional y puede dañar relaciones. Es mejor mantener una actitud positiva."
        },
        {
            "case": "Un cliente te pide que le des un trato preferencial. ¿Qué harías?",
            "feedback": "Tratar a todos los clientes de manera justa es fundamental. No debes favorecer a uno sobre otro."
        },
        {
            "case": "Tu equipo está bajo presión para cumplir con un plazo, pero sabes que el trabajo no está a la altura. ¿Qué harías?",
            "feedback": "Es mejor comunicar la situación y buscar una solución que comprometer la calidad."
        },
        {
            "case": "Ves a un compañero robando suministros de la oficina. ¿Qué harías?",
            "feedback": "Es importante informar sobre el robo, ya que afecta a todos en la empresa."
        },
        {
            "case": "Tu mejor amigo ha cometido un error grave y no quiere que nadie lo sepa. ¿Qué harías?",
            "feedback": "Apoyar a tu amigo es importante, pero también lo es la honestidad. Considera la mejor manera de ayudarlo."
        },
        {
            "case": "Un estudiante está siendo acosado en la escuela. ¿Qué harías?",
            "feedback": "Es fundamental intervenir y ayudar a la víctima. Ignorar el acoso solo lo perpetúa."
        },
        {
            "case": "Te das cuenta de que un compañero está siendo discriminado. ¿Qué harías?",
            "feedback": "Es importante defender a quienes son discriminados y crear un ambiente inclusivo."
        },
        {
            "case": "Un colega te pide que lo cubras en un error que cometió. ¿Qué harías?",
            "feedback": "Cubrir a alguien puede parecer leal, pero es mejor ser honesto y ayudar a la persona a asumir la responsabilidad."
        },
        {
            "case": "Te ofrecen una beca, pero debes comprometerte a trabajar para la empresa durante varios años. ¿Qué harías?",
            "feedback": "Considera si el compromiso es lo que deseas y si la empresa se alinea con tus valores."
        },
        {
            "case": "Un amigo está en una relación tóxica. ¿Qué harías?",
            "feedback": "Es importante hablar con tu amigo y ofrecerle apoyo, pero también respetar su decisión."
        },
        {
            "case": "Te das cuenta de que un producto que vendes está causando daño a los consumidores. ¿Qué harías?",
            "feedback": "Es tu responsabilidad retirar el producto y garantizar la seguridad de los consumidores."
        }
    ]
    
    # Inicializar el estado de la sesión
    if 'current_case' not in st.session_state:
        st.session_state.current_case = 0
        st.session_state.user_responses = []

    # Mostrar el caso actual
    if st.session_state.current_case < len(cases):
        ethical_case = cases[st.session_state.current_case]
        st.markdown(f"### Caso Ético {st.session_state.current_case + 1}:")
        st.markdown(ethical_case['case'])
        user_response = st.text_area("¿Qué harías tú?", height=150)
        if st.button("Enviar Análisis", key=f'enviar_analisis_{st.session_state.current_case}'):  
            st.session_state.user_responses.append(user_response)
            st.success("¡Gracias por compartir tu análisis! Ahora puedes ver la retroalimentación.")
            st.write("### Retroalimentación:")
            st.write(ethical_case['feedback'])
            xai_response = call_xai_api(user_response)
            st.write("### Respuesta de X.AI:")
            st.write(xai_response['choices'][0]['message']['content'])
            st.session_state.current_case += 1
            st.experimental_rerun()
    else:
        st.success("¡Has completado el módulo de casos éticos!")
        st.write("### Análisis de tus respuestas:")
        for response in st.session_state.user_responses:
            st.write(response)

ethical_cases_app()
