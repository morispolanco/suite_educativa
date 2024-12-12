# Suite de Aplicaciones Educativas

Un conjunto completo de aplicaciones educativas construidas con Streamlit, diseñadas para mejorar el pensamiento crítico, las habilidades de escritura, la comprensión filosófica y la perspectiva histórica.

## Aplicaciones Incluidas

1. **Desarrollo del Pensamiento Crítico**
   - Tareas interactivas para estudiantes de primer año universitario
   - Niveles de dificultad progresiva
   - Retroalimentación y orientación inmediata

2. **Asistente de Corrección de Textos**
   - Corrección de gramática y ortografía
   - Explicaciones detalladas para cada corrección
   - Sugerencias de mejora de estilo

3. **Indagación Filosófica**
   - Preguntas filosóficas profundas
   - Diálogo interactivo
   - Verificación de coherencia en las respuestas

4. **Simulador de Decisiones Históricas**
   - Juego de roles en escenarios históricos
   - Generación dinámica de resultados
   - Aprendizaje a través de la toma de decisiones interactiva

## Instrucciones de Configuración

1. Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Crear un archivo .env con tu clave API de X.AI:
   ```
   XAI_API_KEY=tu_clave_api_aquí
   ```

4. Ejecutar la aplicación:
   ```bash
   streamlit run app.py
   ```

## Requisitos
- Python 3.8+
- Streamlit
- Requests
- python-dotenv

## Uso
1. Selecciona una aplicación desde la barra lateral
2. Sigue las instrucciones en pantalla
3. Interactúa con las indicaciones y preguntas
4. Recibe retroalimentación y orientación basada en tus entradas

## Nota
Asegúrate de mantener tu clave API segura y nunca la subas al control de versiones.
