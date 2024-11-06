# Willinn-ia-api - Prueba Técnica Willinn

Willinn IA es una API para la prueba técnica de Trainee de Willinn, implementa un sistema de preguntas y respuestas basado en documentos PDF utilizando el modelo Llama2 para obtener la respuesta.

## Componentes principales

1. **Aplicación Streamlit (streamlit_app.py)**: Interfaz de usuario web para cargar PDFs y hacer preguntas.
2. **Servidor Flask (app.py)**: Backend que procesa las consultas y genera respuestas al PDF cargado por defecto.

## Características

- Carga y procesamiento de documentos PDF
- Vectorización de texto utilizando embeddings de HuggingFace
- Búsqueda de similitud semántica usando FAISS
- Generación de respuestas con el modelo de lenguaje Llama 2
- Interfaz de usuario con Streamlit

## Requisitos

- Python 3.7+
- Streamlit
- Flask
- Langchain
- PyPDF2
- FAISS
- HuggingFace Transformers
- Ollama (con el modelo Llama 2 instalado)

## Requisitos de Hardware

**RAM:** RAM > 4 GB

**CPU:** RTX 1660, 2060, AMD 5700xt, RTX 3050, RTX 3060, TX 3070

## Instalar Ollama

En Linux usa el siguiente comando.

```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ollama run llama2
```

Ahora puedes probar el modelo Llama2.

```bash
  >>> Send a message (/? for help)
```
Para cerrar la interacción con el modelo usa /bye

```bash
  >>> /bye
```

## Instalación

Clona este repositorio y dependencias
```bash
git clone https://github.com/GaboAfk/willinn-ia-api
```

```bash
cd willinn-ia-api
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

Asegúrate de tener Ollama instalado y el modelo Llama 2 descargado

## Uso

1. Inicia el servidor Flask (`http://localhost:5555/llama2` queda disponible para hacer preguntas en el formato POST {"question": "tu pregunta"}): 

```bash
python app.py
```

2. Ejecuta la aplicación Streamlit (en otra terminal):

```bash
streamlit run streamlit_app.py
```

3. Abre tu navegador y ve a `http://localhost:8501`
4. Carga un PDF o utiliza el PDF por defecto (Mi CV)
5. Haz preguntas sobre el contenido del documento

## Estructura del proyecto

- `streamlit_app.py`: Aplicación frontend de Streamlit
- `app.py`: Servidor backend de Flask
- `documents/`: Directorio para almacenar PDFs (incluye un CV por defecto)

## Autor
Gabriel - [GaboAfk](https://github.com/GaboAfk)