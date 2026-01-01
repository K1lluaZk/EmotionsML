<p align="center">Emotion Detection IA</p>
<p align="center">Un sistema profesional de visión artificial en tiempo real para el reconocimiento de emociones humanas, construido con OpenCV y DeepFace.</p>

<p align="center"> <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white" alt="OpenCV"> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white" alt="FastAPI"> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white" alt="TensorFlow"> </p>

---

### 🎮 Sobre el Proyecto

Este proyecto es una implementación profesional de un sistema de Reconocimiento de Emociones. Está diseñado con una **Arquitectura Modular por Capas**, separando la lógica central de IA de la interfaz de distribución. Proporciona una experiencia en tiempo real optimizando los cuadros de la cámara y utilizando Deep Learning para identificar las emociones humanas dominantes.

### ✨ Características Clave

* **🧠 Inferencia con DeepFace:** Utiliza modelos de aprendizaje profundo pre-entrenados para analizar expresiones faciales y detectar emociones dominantes (felicidad, tristeza, neutralidad, etc.).
* **⚡ Rendimiento Optimizado (Frame Skip):** Para garantizar una transmisión de video fluida a 30 FPS, la IA realiza la inferencia solo en 1 de cada 5 cuadros, reduciendo significativamente la carga del CPU.
* **🏗️ Arquitectura Modular:** Separación estricta entre la lógica de Machine Learning (`Src/`) y la capa de distribución web (`App/`) para un alto mantenimiento.
* **🌐 Hub de Distribución Web:** Construido con **FastAPI**, presenta una página de aterrizaje dedicada para explicar el proyecto y un punto de acceso seguro para descargar el código fuente en un archivo ZIP.
* **🛠️ Manejo de Errores Robusto:** Incluye verificaciones de disponibilidad de la cámara y lógica de detección ("enforce_detection") para evitar fallos del sistema cuando no hay un rostro presente.

### 🛠️ Tecnologías Utilizadas

* **Machine Learning:** DeepFace (Wrapper para Keras/TensorFlow).
* **Visión Artificial:** OpenCV (cv2) para la manipulación de flujo de video en tiempo real.
* **Backend Web:** FastAPI con servidor Uvicorn y plantillas Jinja2.
* **Frontend:** CSS3 moderno con Flexbox y HTML5 semántico.

### 🚀 Cómo Ejecutar Localmente

1. **Clonar el repositorio:**

```bash
git clone https://github.com/K1lluaZk/EmotionsML.git

```

2. **Configurar el Entorno Virtual:**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

```

3. **Instalar Dependencias:**

```bash
pip install -r Src/requirements.txt

```

4. **Lanzar la Aplicación:**

* **Para ejecutar el Detector:** `python Src/main.py`.
* **Para ejecutar la Web App:** `cd App && uvicorn server:app --reload`.

### 📁 Estructura del Proyecto

```text
├── App/                # Capa de Distribución Web
│   ├── downloads/      # Almacenamiento del ZIP del proyecto
│   ├── static/         # Estilos CSS y activos
│   ├── templates/      # Plantillas HTML (Jinja2)
│   └── server.py       # Lógica del servidor FastAPI
├── Src/                # Lógica Central de ML
│   ├── config.py       # Parámetros globales (FPS, colores)
│   ├── detectemotions.py # Clase EmotionDetector
│   └── main.py         # Orquestador de OpenCV
└── venv/               # Entorno virtual

```

### ✍️ Autor

**K1lluaZk** - [Perfil de GitHub](https://www.google.com/search?q=https://github.com/K1lluaZk)

### 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la **Licencia MIT**.
