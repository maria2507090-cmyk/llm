# TutorIA 🎓 — Tutor virtual inteligente

Proyecto académico de un **tutor educativo** desarrollado en Python con **Streamlit** y la **API de OpenAI (Responses API)**. Permite hacer preguntas, seleccionar materias y niveles, obtener explicaciones paso a paso y practicar con ejercicios.

## Funcionalidades

- Chat educativo con contexto durante la sesión.
- Materias: Matemáticas, Programación, Física, Inteligencia Artificial, Historia y Otra materia.
- Niveles: básico, intermedio y avanzado.
- Cuatro modos: explicación, ejemplo paso a paso, pistas y práctica.
- Botón para iniciar una conversación nueva.
- Mensajes de error claros cuando la clave API, cuota o conexión presentan problemas.

> **Alcance:** es un prototipo educativo. Las respuestas del modelo pueden contener errores y deben verificarse. El historial se conserva solo en la sesión de Streamlit. No se requiere una base de datos real.

## Requisitos

- Python **3.11**.
- Internet.
- Una clave de OpenAI API con acceso y saldo/cuota disponible. La API puede generar cargos de acuerdo con su uso; **no está incluida automáticamente en una suscripción de ChatGPT**.

## Instalación desde cero

1. Clona el repositorio:

   ```bash
   git clone https://github.com/maria2507090-cmyk/llm.git
   cd llm
   ```

2. Crea y activa el entorno virtual:

   **macOS / Linux**

   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows (PowerShell)**

   ```powershell
   py -3.11 -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Instala las librerías:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r tutoria/requirements.txt
   ```

4. Configura la clave API (nunca la publiques):

   **macOS / Linux**

   ```bash
   cp tutoria/.env.example tutoria/.env
   ```

   **Windows (PowerShell)**

   ```powershell
   Copy-Item tutoria/.env.example tutoria/.env
   ```

   Si aún no existe `tutoria/.env.example`, créalo con el texto `OPENAI_API_KEY=pon_aqui_tu_clave` y `OPENAI_MODEL=gpt-4.1-mini`, sin incluir claves reales. Después, edita `tutoria/.env` e introduce tu clave real en `OPENAI_API_KEY`. Puedes crear una desde https://platform.openai.com/api-keys y consultar costos/cuotas en https://platform.openai.com/ .

5. Ejecuta el tutor:

   ```bash
   python -m streamlit run tutoria/app.py
   ```

   Abre la dirección que muestra Streamlit, normalmente http://localhost:8501 .

## Demostración para calificación

1. Selecciona **Matemáticas**, nivel **Básico**, modo **Explicación**; pregunta: «¿Qué es una derivada?».
2. Cambia el modo a **Ejemplo paso a paso**; pregunta: «Enséñame a calcular una derivada sencilla».
3. Cambia a **Pistas para resolver**; pregunta: «Ayúdame a resolver 2x + 3 = 11».
4. Cambia a **Practicar con preguntas**; solicita un ejercicio corto y contesta la pregunta de TutorIA.
5. Presiona **Nueva conversación** para reiniciar el historial.

Sin una clave válida y cuota disponible, la interfaz puede abrir, pero no puede generar respuestas reales con OpenAI. La integración con OpenAI está implementada, aunque debe verificarse con una solicitud real. Una demostración simulada, si se incorpora, no sustituye el uso obligatorio de la API.

## Estructura

```text
llm/
├── .gitignore                 # Excluye claves y archivos locales
├── README.md                  # Instrucciones del proyecto
├── tutoria/
│   ├── app.py                 # Interfaz y conexión con OpenAI
│   ├── requirements.txt       # Dependencias
│   └── .env.example           # Plantilla pública, sin secretos
└── .venv/                     # Entorno local; no se sube a Git
```

## Seguridad y limitaciones

- `tutoria/.env` y `.venv/` se ignoran en Git; nunca subas una clave real a GitHub.
- Se usa el modelo configurado mediante `OPENAI_MODEL`, por defecto `gpt-4.1-mini`; debe estar disponible en la cuenta de API usada.
- El tutor no sustituye a un docente. Se limita el historial enviado a los últimos 12 mensajes para controlar costos.
- Las conversaciones se envían al servicio de OpenAI para producir respuestas; no ingreses información sensible.
- La aplicación no guarda perfiles permanentes, no califica automáticamente ni se integra con plataformas escolares.

## Detener la aplicación

Presiona `Ctrl + C` en la terminal donde se está ejecutando Streamlit. Para salir del entorno: `deactivate`.
