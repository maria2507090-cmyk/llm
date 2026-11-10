"""TutorIA: tutor virtual educativo con Streamlit y OpenAI Responses API."""
import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, RateLimitError, APIConnectionError, BadRequestError

load_dotenv()
st.set_page_config(page_title="TutorIA | Tutor virtual", page_icon="🎓", layout="centered")

st.markdown("""<style>
.stApp {background: #f9fafb;}
h1, h2, h3 {color: #1f2937;}
[data-testid='stSidebar'] {background: #fff7ed;}
</style>""", unsafe_allow_html=True)

MATERIAS = ["Matemáticas", "Programación", "Física", "Inteligencia Artificial", "Historia", "Otra materia"]
NIVELES = ["Básico", "Intermedio", "Avanzado"]
MODOS = ["Explicación", "Ejemplo paso a paso", "Pistas para resolver", "Practicar con preguntas"]

st.title("🎓 TutorIA")
st.caption("Aprende a tu ritmo con ayuda de inteligencia artificial.")

with st.sidebar:
    st.header("📚 Personaliza tu aprendizaje")
    materia = st.selectbox("Materia", MATERIAS)
    nivel = st.selectbox("Nivel", NIVELES)
    modo = st.selectbox("Modo de aprendizaje", MODOS)
    st.divider()
    st.caption("Las respuestas pueden contener errores. Verifica la información importante.")
    if st.button("🧹 Nueva conversación", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

api_key = os.getenv("OPENAI_API_KEY", "").strip()
if not api_key:
    st.warning("Para activar la IA, configura OPENAI_API_KEY en un archivo .env local. Consulta README.md.")
    st.stop()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Escribe tu duda o el tema que quieres estudiar...")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    instructions = f"""Eres TutorIA, tutor virtual educativo y paciente. Responde siempre en español.
Materia: {materia}. Nivel: {nivel}. Modo: {modo}.
Ajusta la complejidad a ese nivel y explica con claridad. No inventes hechos; admite incertidumbre.
En modo 'Ejemplo paso a paso', enseña el procedimiento con un ejemplo breve.
En modo 'Pistas para resolver', guía mediante pistas sin dar inmediatamente la respuesta final.
En modo 'Practicar con preguntas', plantea una pregunta o ejercicio breve, espera la respuesta del alumno y después ofrécele retroalimentación.
En modo 'Explicación', define y explica con un ejemplo accesible.
No incluyas información privada del alumno en la respuesta ni afirmes haber evaluado tareas externas.
"""
    # Limitar historial enviado para contener el costo de llamadas API.
    history = st.session_state.messages[-12:]
    with st.chat_message("assistant"):
        with st.spinner("TutorIA está preparando una explicación..."):
            try:
                response = OpenAI(api_key=api_key, timeout=40.0).responses.create(
                    model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                    instructions=instructions,
                    input=history,
                    max_output_tokens=550,
                    store=False,
                )
                answer = response.output_text or "No se recibió una respuesta de texto. Intenta reformular tu pregunta."
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except AuthenticationError:
                st.error("La clave API no es válida. Revisa OPENAI_API_KEY en tu archivo .env.")
            except RateLimitError:
                st.error("La API rechazó la solicitud por límite de uso o falta de cuota. Revisa tu facturación y límites.")
            except APIConnectionError:
                st.error("No fue posible conectar con la API. Revisa tu conexión a internet.")
            except BadRequestError:
                st.error("La solicitud fue rechazada. Verifica el modelo configurado y los parámetros.")
            except Exception:
                st.error("Ocurrió un error al consultar la API. Revisa los ajustes e inténtalo de nuevo.")
