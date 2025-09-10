# 📂 Portafolio Nivel 3  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-DB-lightgrey?logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Flask-API-black?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/Estado-Completado-brightgreen" alt="Estado">
  <img src="https://img.shields.io/badge/Licencia-MIT-yellow" alt="Licencia">
</p>

Este repositorio contiene proyectos de Python de **nivel intermedio**, enfocados en integrar **bases de datos**, **análisis de datos**, **visualización** y **desarrollo de APIs**.  
Cada proyecto está diseñado para practicar habilidades esenciales en el desarrollo backend y análisis de datos.


---

## 🧾 Tabla de Contenidos

1. [📇 Gestor de Contactos (CRUD con SQLite)](#-1-gestor-de-contactos-crud-con-sqlite)
2. [📊 Dashboard de Ventas - Versión 1 (CLI)](#-2-dashboard-de-ventas---versión-1-cli)
3. [📊 Dashboard de Ventas - Versión 2 (GUI con Tkinter)](#-3-dashboard-de-ventas---versión-2-gui-con-tkinter)
4. [🌐 Mini API con Flask](#-4-mini-api-con-flask)
5. [📡 Cliente para la Mini API](#-5-cliente-para-la-mini-api)
6. [🚀 Instalación y Uso](#-instalación-y-uso)

---

### 📇 1. Gestor de Contactos (CRUD con SQLite)

Una aplicación con interfaz gráfica en **Tkinter** que permite:  
✅ Agregar, editar y eliminar contactos  
✅ Guardar los datos en **SQLite**  
✅ Interfaz oscura, moderna y fácil de usar  

📸 **Captura de pantalla:**  
![Gestor de Contactos](assets/gestor_contactos.png)

---

### 📊 2. Dashboard de Ventas - Versión 1 (CLI)

Un script en **Python + Pandas** que:  
- Lee datos desde `ventas.csv`  
- Agrupa por categoría y muestra **gráficas de barras** con Matplotlib  
- Ideal para análisis rápido en terminal  

📸 **Captura de salida:**  
![Dashboard CLI](assets/dashboard_basico.png)

---

### 📊 3. Dashboard de Ventas - Versión 2 (GUI con Tkinter)

Versión con interfaz gráfica para mostrar métricas de ventas en tiempo real.  
✅ Gráfica de ventas por categoría  
✅ Interfaz amigable y en modo oscuro  
✅ Posibilidad de filtrar datos y actualizar  

📸 **Captura de pantalla:**  
![Dashboard GUI](assets/dashboard_interactivo.png)

---

### 🌐 4. Mini API con Flask

Un microservidor en **Flask** que expone datos en formato JSON.  
- Permite consultar datos de ejemplo  
- Endpoint principal: `http://127.0.0.1:5000/data`  

📸 **Captura ejecutando la API:**  
![Mini API](assets/mini_api.png)

---

### 📡 5. Cliente para la Mini API

Un script que consume los datos de la API y los imprime en consola.  
✅ Ejemplo práctico de **requests**  
✅ Manejo de respuestas JSON  

📸 **Captura de salida:**  
![Cliente API](assets/cliente_api.png)

---

## 🚀 Instalación y Uso

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/iparra-sys/Portafolio-Nivel-3.git
cd Portafolio-Nivel-3
```

### 2️⃣ Instalar dependencias necesarias
```bash
pip install pandas flask matplotlib
```

### 3️⃣ Ejecutar cada proyecto
```bash
python crud_contactos.py           # Gestor de contactos (GUI)
python dashboard_ventas.py         # Dashboard de ventas versión CLI
python dashboard_ventas_gui.py     # Dashboard de ventas versión GUI
python mini_api.py                 # Iniciar API con Flask
python cliente_mini_api.py         # Cliente para consumir la API
```

---

### 🛠️ Tecnologías Usadas
- 🐍 **Python 3.13**
- 🗄 **SQLite** – Base de datos local
- 🖥 **Tkinter** – Interfaces gráficas
- 📊 **Pandas & Matplotlib** – Análisis y visualización de datos
- 🌐 **Flask** – Creación de API REST
- 🔗 **Requests** – Consumo de APIs

---

## 🛠️ Habilidades Desarrolladas  

- 🐍 **Programación en Python** (estructuras, módulos, librerías externas)  
- 🗄️ **Gestión de bases de datos con SQLite** (CRUD completo)  
- 🎨 **Diseño de interfaces gráficas con Tkinter** en modo oscuro  
- 📊 **Análisis y visualización de datos** con Pandas y Matplotlib  
- 🌐 **Desarrollo de APIs REST con Flask**  
- 🔗 **Consumo de APIs con Requests**  
- 🛠️ **Uso de Git y GitHub** para control de versiones y portafolio  

---

## 🚀 Próximos Pasos  

- 🏗️ Implementar **autenticación de usuarios** para el gestor de contactos  
- 📈 Agregar **dashboards interactivos** con filtros avanzados (Plotly o Dash)  
- 🌍 Desplegar la **Mini API** en un servicio gratuito (Render, Railway o HuggingFace Spaces)  
- 🧪 Incluir **pruebas automatizadas** (pytest) para mejorar la calidad del código  
- 🖥️ Migrar el proyecto a una arquitectura **MVC** para mayor escalabilidad  

---
