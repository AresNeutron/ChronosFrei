# CronosFrei: El Calendario del Futuro (Prototipo)

## Introducción

**CronosFrei** es un proyecto ambicioso para crear una aplicación de calendario de escritorio que pone la privacidad del usuario en primer lugar. A diferencia de las soluciones actuales, CronosFrei funcionará completamente sin conexión y sin telemetría. Su característica principal es un asistente de voz basado en inteligencia artificial que permite a los usuarios gestionar sus horarios con lenguaje natural.

## Estado del Proyecto: Prototipo

Este repositorio contiene la arquitectura inicial del prototipo de CronosFrei. Hemos sentado las bases para la comunicación entre el frontend y el backend, así como la estructura fundamental de la base de datos y la interacción por voz.

## Arquitectura

La arquitectura del proyecto sigue un modelo cliente-servidor, pero ambos componentes se ejecutan localmente en la máquina del usuario.

* **Frontend (UI):** Desarrollado con **React** (JavaScript/TypeScript).
* **Backend (API):** Un servidor de **FastAPI** desarrollado en Python.
* **Base de datos:** **SQLite**, una base de datos basada en archivos, ideal para el uso sin conexión y la privacidad.
* **Speech-to-Text:** Se utiliza la **Web Speech API** del navegador para transcribir la voz del usuario a texto de forma local.
* **IA de Procesamiento de Lenguaje:** Se utiliza la librería de **spaCy** para entrenar un modelo personalizado que clasifica las intenciones del usuario y extrae entidades clave de sus peticiones en lenguaje natural.

## Cómo ejecutar el prototipo

### 1. Requisitos

Asegúrate de tener instalado Python 3.x y Node.js en tu sistema.

### 2. Backend

1.  Navega hasta la carpeta del backend.
2.  Instala las dependencias de Python:
    ```bash
    pip install "fastapi[all]"
    pip install "spacy"
    python -m spacy download es_core_news_sm
    ```
3.  Inicia el servidor:
    ```bash
    uvicorn main:app --reload
    ```
El servidor se ejecutará en `http://127.0.0.1:8000`.

### 3. Frontend

1.  Navega hasta la carpeta del frontend.
2.  Instala las dependencias de Node.js:
    ```bash
    npm install
    ```
3.  Inicia la aplicación de React:
    ```bash
    npm start
    ```
El frontend se ejecutará en `http://localhost:3000`.

## Características actuales (CRUD)

El prototipo actual permite las siguientes operaciones básicas en el calendario a través de los endpoints de la API:

* **Crear eventos:** `POST /events/`
* **Leer eventos:** `GET /events/`
* **Actualizar eventos:** `PUT /events/{event_id}`
* **Eliminar eventos:** `DELETE /events/{event_id}`

## Próximos pasos

La siguiente fase del desarrollo se centrará en:

1.  **Entrenamiento del modelo de spaCy:** Crear un conjunto de datos de entrenamiento robusto y entrenar el modelo para que entienda las intenciones del usuario de forma precisa.
2.  **Integración de la IA:** Implementar la lógica que toma la salida del modelo de spaCy y la traduce en llamadas a los métodos CRUD existentes en el backend.

---
