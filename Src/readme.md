
# 🎭 Emotion Detection IA - Proyecto Profesional

Este es un sistema de visión artificial en tiempo real capaz de detectar emociones humanas utilizando la cámara web. El proyecto ha sido estructurado siguiendo una **Arquitectura Modular por Capas** para garantizar escalabilidad y limpieza de código.

## 🚀 Guía de Inicio Rápido

### 1. Requisitos Previos

* Python 3.9 o superior instalado.
* Cámara web funcional.

¡Entendido! Como no incluiremos los archivos .bat, el README tiene que ser muy claro para que el usuario sepa que debe usar la terminal.

Aquí tienes el contenido que debes poner en un archivo llamado instrucciones.txt (o README.txt) dentro de tu carpeta Src antes de comprimirla en el emotionsml.zip.

🚀 GUÍA DE INSTALACIÓN Y USO
Este proyecto utiliza Inteligencia Artificial para detectar emociones en tiempo real. Sigue estos pasos para configurarlo en tu computadora:

1. Requisitos Previos
Debes tener instalado Python 3.9 o una versión superior. Puedes descargarlo desde python.org.

2. Preparación del Entorno (Terminal)
Abre una terminal o CMD dentro de la carpeta del proyecto y ejecuta los siguientes comandos en orden:

Crear el entorno virtual (para no ensuciar tu PC):

Bash

python -m venv venv
Activar el entorno:

En Windows: venv\Scripts\activate

En Mac/Linux: source venv/bin/activate

3. Instalar las Librerías
Una vez activado el entorno (verás que dice (venv) al inicio de la línea), instala las dependencias:

Bash

pip install -r requirements.txt
Nota: Esto puede tardar unos minutos porque descargará TensorFlow y OpenCV.

4. Ejecutar el Proyecto
Con todo instalado, lanza la aplicación con:

Bash

python main.py
5. Cómo usarlo
La cámara se encenderá automáticamente.

El sistema analizará tu rostro cada pocos segundos para mantener la fluidez.

Para salir: Presiona la tecla 'q' en tu teclado o cierra la ventana del video.

---

## 🏗️ Arquitectura del Proyecto

El código está dividido de la siguiente manera para seguir las mejores prácticas de ingeniería de software:

* **`main.py`**: El orquestador. Maneja el flujo de video de OpenCV y coordina la lógica de detección.
* **`detectemotions.py`**: La capa de Inteligencia Artificial. Contiene la clase `EmotionDetector` que encapsula la lógica de **DeepFace**.
* **`config.py`**: Parámetros de configuración (FPS, colores, umbrales).
* **`requirements.txt`**: Lista de dependencias necesarias.

---

## ⚙️ Optimizaciones Implementadas

Para asegurar un rendimiento fluido, hemos aplicado las siguientes técnicas:

1. **Frame Skipping**: El modelo de IA procesa 1 de cada 5 cuadros (configurable en `config.py`). Esto permite que el video se mantenga a 30 FPS constantes sin retrasos.
2. **Inferencia desacoplada**: La lógica de detección es independiente de la captura, lo que facilita el intercambio del modelo en el futuro.
3. **Entorno Aislado**: Uso de entornos virtuales para evitar conflictos con otras librerías del sistema.

---

## 🛠️ Tecnologías Utilizadas

* **OpenCV**: Captura y procesamiento de imagen.
* **DeepFace**: Inferencia de emociones mediante redes neuronales.
* **FastAPI**: (En la capa de distribución) Para la entrega del software.

---

### Notas del Desarrollador

Si experimentas lentitud, puedes aumentar el valor de `FRAME_SKIP` en `config.py`. Para salir de la aplicación, presiona la tecla **'q'** o cierra la ventana de video.


