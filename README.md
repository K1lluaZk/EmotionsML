<p align="center">EmotionsML - Web Distribution Hub</p>
<p align="center">Portal de aterrizaje y plataforma de distribución construida con FastAPI para el despliegue del software de detección de emociones.</p>

<p align="center"> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white" alt="FastAPI"> <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Uvicorn-202222?style=flat&logo=uvicorn&logoColor=white" alt="Uvicorn"> <img src="https://img.shields.io/badge/Jinja2-B41717?style=flat&logo=jinja&logoColor=white" alt="Jinja2"> </p>

---

### 🌐 Sobre la Web App

Este módulo constituye la **Capa de Distribución** del proyecto EmotionsML. A diferencia del motor de detección, esta es una aplicación web backend diseñada para presentar el proyecto a usuarios finales y permitir la descarga segura del paquete de software comprimido mediante una interfaz moderna y eficiente.

### ✨ Características de la Web

* **🚀 Backend de Alto Rendimiento:** Desarrollada íntegramente con **FastAPI**, aprovechando la programación asíncrona para gestionar las solicitudes de descarga de forma inmediata.
* **📂 Sistema de Entrega de Archivos:** Implementa un endpoint dinámico (`/download`) que utiliza `FileResponse` para servir el paquete `emotionsml.zip` almacenado en el servidor.
* **🎨 UI Profesional y Responsiva:** Interfaz de usuario limpia diseñada con **CSS3 personalizado**, enfocada en la conversión y la claridad de información.
* **🏗️ Servidor ASGI Robusto:** Utiliza **Uvicorn** como servidor de producción, garantizando estabilidad y una gestión eficiente de los recursos del sistema.
* **🧩 Renderizado Dinámico:** Implementación de plantillas **Jinja2** para separar la estructura HTML de la lógica del servidor, facilitando el mantenimiento y futuras actualizaciones del portal.

### 🛠️ Tecnologías Utilizadas

* **Framework Principal:** FastAPI (Python).
* **Servidor de Aplicaciones:** Uvicorn.
* **Motor de Plantillas:** Jinja2.
* **Frontend:** HTML5 semántico y CSS3 (Flexbox/Grid).

### 🚀 Cómo Ejecutar el Portal

1. **Configurar el Entorno:**
Asegúrate de que las dependencias de FastAPI estén instaladas en tu entorno virtual.
```bash
pip install fastapi uvicorn jinja2

```


2. **Lanzar el Servidor:**
Desde la raíz del proyecto, navega a la carpeta `App` y ejecuta:
```bash
cd App
uvicorn server:app --reload

```


3. **Acceso Local:**
Abre tu navegador en `http://127.0.0.1:8000`.

### 📁 Estructura del Portal Web

```text
├── downloads/          # Directorio raíz del archivo descargable (ZIP)
├── static/             # Archivos CSS, logos y estilos visuales
├── templates/          # Documentos HTML renderizados por el servidor
└── server.py           # Corazón de la Web App (Rutas y lógica FastAPI)

```

### ✍️ Autor

**K1lluaZk** - [Perfil de GitHub](https://www.google.com/search?q=https://github.com/K1lluaZk)

### 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la **Licencia MIT**.

### 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la **Licencia MIT**.
