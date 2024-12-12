import streamlit as st

# Función para el simulador de decisiones históricas
def historical_decisions_app():
    st.title("Simulador de Decisiones Históricas")
    st.subheader("Toma decisiones y observa sus consecuencias")
    
    # Situaciones históricas con personajes y decisiones
    scenarios = [
        {
            "character": "Napoleón Bonaparte",
            "situation": "Estás en la Batalla de Waterloo. Tu ejército se enfrenta a las fuerzas combinadas de Gran Bretaña y Prusia.",
            "decisions": [
                "Atacar de inmediato",
                "Retirarse y reagruparse",
                "Buscar alianzas con otros países"
            ]
        },
        {
            "character": "John F. Kennedy",
            "situation": "Durante la Crisis de los Misiles en Cuba, debes decidir cómo responder a la amenaza de los misiles soviéticos.",
            "decisions": [
                "Imponer un bloqueo naval",
                "Atacar los sitios de misiles",
                "Negociar con la URSS"
            ]
        },
        {
            "character": "Abraham Lincoln",
            "situation": "Eres el presidente durante la Guerra Civil. Debes decidir si emitir la Proclamación de Emancipación.",
            "decisions": [
                "Emitir la proclamación",
                "Esperar a ganar más batallas",
                "Buscar una solución pacífica"
            ]
        },
        {
            "character": "Cleopatra",
            "situation": "Eres la reina de Egipto y debes decidir cómo manejar la invasión romana.",
            "decisions": [
                "Aliarte con Marco Antonio",
                "Rendirte y negociar",
                "Luchar hasta el final"
            ]
        },
        {
            "character": "Winston Churchill",
            "situation": "Eres el primer ministro durante la Segunda Guerra Mundial. Debes decidir cómo enfrentar la amenaza nazi.",
            "decisions": [
                "Declarar la guerra a Alemania",
                "Buscar alianzas con otros países",
                "Negociar una paz"
            ]
        },
        {
            "character": "Mahatma Gandhi",
            "situation": "Estás liderando la lucha por la independencia de la India. Debes decidir entre la resistencia pacífica y la violencia.",
            "decisions": [
                "Promover la resistencia pacífica",
                "Utilizar la violencia si es necesario",
                "Negociar con los británicos"
            ]
        },
        {
            "character": "Marie Curie",
            "situation": "Eres una científica pionera y debes decidir si compartir tus descubrimientos sobre la radiactividad con el mundo.",
            "decisions": [
                "Publicar tus hallazgos",
                "Mantenerlos en secreto",
                "Colaborar con otros científicos"
            ]
        },
        {
            "character": "Nelson Mandela",
            "situation": "Eres un líder anti-apartheid en Sudáfrica. Debes decidir cómo abordar la reconciliación después de años de opresión.",
            "decisions": [
                "Promover la paz y la reconciliación",
                "Buscar justicia a través de juicios",
                "Mantener la presión sobre el gobierno"
            ]
        },
        {
            "character": "Alexander el Grande",
            "situation": "Estás en medio de una campaña militar y debes decidir si invadir Persia.",
            "decisions": [
                "Invadir inmediatamente",
                "Esperar refuerzos",
                "Negociar una paz"
            ]
        },
        {
            "character": "Martin Luther King Jr.",
            "situation": "Eres un líder del movimiento por los derechos civiles en EE.UU. Debes decidir cómo responder a la violencia en las protestas.",
            "decisions": [
                "Promover la no violencia",
                "Organizar una marcha masiva",
                "Utilizar la violencia en defensa"
            ]
        },
        {
            "character": "Julius Caesar",
            "situation": "Eres el dictador de Roma y debes decidir cómo manejar la conspiración en tu contra.",
            "decisions": [
                "Ignorar las advertencias",
                "Tomar medidas preventivas",
                "Buscar aliados entre los conspiradores"
            ]
        },
        {
            "character": "Galileo Galilei",
            "situation": "Eres un astrónomo y debes decidir si defender tus descubrimientos sobre el heliocentrismo.",
            "decisions": [
                "Defender tus hallazgos",
                "Retirarte y mantener un perfil bajo",
                "Colaborar con la Iglesia"
            ]
        },
        {
            "character": "Rosa Parks",
            "situation": "Eres una activista de derechos civiles y decides no ceder tu asiento en el autobús. ¿Cuál es tu siguiente paso?",
            "decisions": [
                "Organizar una boicot",
                "Aceptar las consecuencias",
                "Buscar apoyo de otros activistas"
            ]
        },
        {
            "character": "Vikingo Anónimo",
            "situation": "Eres un explorador vikingo y decides si atacar una aldea costera o comerciar con ella.",
            "decisions": [
                "Atacar y saquear",
                "Establecer comercio",
                "Retirarte y buscar otra aldea"
            ]
        },
        {
            "character": "Emperador Qin Shi Huang",
            "situation": "Eres el primer emperador de China y debes decidir cómo unificar el país.",
            "decisions": [
                "Imponer un gobierno centralizado",
                "Permitir autonomía a las regiones",
                "Fomentar la guerra entre los estados"
            ]
        },
        {
            "character": "Florence Nightingale",
            "situation": "Eres una pionera en enfermería y debes decidir cómo mejorar las condiciones en los hospitales durante la guerra.",
            "decisions": [
                "Implementar reformas de higiene",
                "Protestar contra el gobierno",
                "Buscar apoyo de otros médicos"
            ]
        },
        {
            "character": "Simón Bolívar",
            "situation": "Eres un líder revolucionario en América del Sur y debes decidir cómo liberar a los países del dominio español.",
            "decisions": [
                "Luchar en batallas",
                "Buscar alianzas con otros países",
                "Negociar la independencia"
            ]
        },
        {
            "character": "Leonardo da Vinci",
            "situation": "Eres un genio del Renacimiento y debes decidir cómo utilizar tus talentos para el bien de la humanidad.",
            "decisions": [
                "Crear obras de arte",
                "Inventar nuevas tecnologías",
                "Enseñar a otros artistas"
            ]
        },
        {
            "character": "Malala Yousafzai",
            "situation": "Eres una activista por la educación y debes decidir cómo continuar tu lucha después de un ataque.",
            "decisions": [
                "Seguir hablando en público",
                "Retirarte para protegerte",
                "Buscar apoyo internacional"
            ]
        }
    ]
    
    # Inicializar el estado de la sesión
    if 'current_scenario' not in st.session_state:
        st.session_state.current_scenario = 0
        st.session_state.consequences = []

    # Mostrar la situación actual
    if st.session_state.current_scenario < len(scenarios):
        scenario = scenarios[st.session_state.current_scenario]
        st.markdown(f"### Personaje: {scenario['character']}")
        st.markdown(f"### Situación: {scenario['situation']}")
        decision = st.selectbox("¿Qué decisión tomarás?", scenario['decisions'])
        if st.button("Enviar Decisión", key=f'decision_{st.session_state.current_scenario}'):  
            st.session_state.consequences.append(f"Decidiste: {decision}")
            st.session_state.current_scenario += 1
            st.experimental_rerun()
    else:
        st.success("¡Has completado el simulador de decisiones históricas!")
        st.write("### Consecuencias de tus decisiones:")
        for consequence in st.session_state.consequences:
            st.write(consequence)

historical_decisions_app()
