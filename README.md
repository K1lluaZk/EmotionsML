<p align="center">EmotionsML - Core Engine</p>
<p align="center">El núcleo de procesamiento de IA que gestiona la captura de video y la inferencia de emociones en tiempo real.</p>

<p align="center"> <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white" alt="OpenCV"> <img src="https://img.shields.io/badge/DeepFace-E34F26?style=flat&logo=scikitlearn&logoColor=white" alt="DeepFace"> </p>

---

### 🧠 Sobre el Módulo Src

Esta carpeta contiene la **Lógica de Negocio** y el **Motor de Inferencia**. Es el corazón del proyecto, donde se transforma el flujo de datos de la cámara en información analítica sobre el estado emocional del usuario. Se ha diseñado bajo un esquema de desacoplamiento para permitir que el modelo de detección sea independiente de la interfaz de visualización.

### ✨ Características del Motor (`main.py`)

* **🎮 Orquestación en Tiempo Real:** El script `main.py` actúa como el controlador principal, gestionando el ciclo de vida de la cámara (`VideoCapture`) y la liberación de recursos del sistema.
* **⚡ Optimización de Inferencia:** Implementa un sistema de **conteo de frames** para ejecutar la IA de forma intermitente, evitando el desfase (lag) entre la captura y el procesamiento.
* **🖼️ Superposición de UI (HUD):** Renderiza dinámicamente etiquetas de texto sobre el video utilizando las funciones de dibujo de OpenCV, mostrando la emoción detectada sin interrumpir el flujo visual.
* **⚙️ Configuración Centralizada:** Utiliza `config.py` para abstraer constantes como el `FRAME_SKIP`, escalas de fuente y colores, permitiendo ajustes rápidos sin tocar la lógica principal.
* **🛡️ Estabilidad del Proceso:** Incluye bloques `try-except` para manejar excepciones durante el análisis de DeepFace, garantizando que el programa no se cierre si la detección falla momentáneamente.

### 🛠️ Componentes Internos

* **`main.py`**: Punto de entrada del programa. Contiene el bucle principal de video y la lógica de visualización.
* **`detectemotions.py`**: Clase `EmotionDetector` que encapsula la librería **DeepFace**. Su único objetivo es procesar un frame y retornar el nombre de la emoción.
* **`config.py`**: Diccionario de parámetros técnicos para el ajuste fino del rendimiento.
* **`requirements.txt`**: Listado estricto de librerías necesarias para el funcionamiento del motor de IA.

### 🚀 Cómo Ejecutar el Motor

1. **Asegúrate de estar en el entorno virtual:**
```bash
# Windows
venv\Scripts\activate

```


2. **Ejecuta el script principal:**
```bash
python Src/main.py

```


3. **Controles de Usuario:**
* **'q'**: Finaliza la ejecución y cierra las ventanas.
* **Cerrar ventana**: El programa detecta el cierre manual de la ventana y libera la cámara automáticamente.



### 📁 Estructura del Módulo

```text
├── config.py           # Variables de entorno y ajustes técnicos
├── detectemotions.py   # Wrapper del modelo de Machine Learning
├── main.py             # Script principal (Orquestador)
└── requirements.txt    # Dependencias específicas de ML y Visión

```

### ✍️ Autor

**K1lluaZk** - [Perfil de GitHub](https://www.google.com/search?q=https://github.com/K1lluaZk)

### 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la **Licencia MIT**.

---

