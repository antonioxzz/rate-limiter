# Proyecto: API con Rate Limiting y Frontend Moderno

Este es un proyecto Full-Stack diseñado para demostrar conceptos de arquitectura de software de nivel senior. La aplicación implementa una API de backend con autenticación y límites de peticiones por rol de usuario (Rate Limiting), y un frontend moderno para interactuar con ella.

El proyecto está completamente containerizado con Docker para facilitar su despliegue y ejecución en cualquier entorno.

## ✨ Características Principales

* **Backend Robusto:** API construida con FastAPI, siguiendo una arquitectura por capas (API, Servicios, CRUD).
* **Autenticación JWT:** Login de usuarios y protección de rutas mediante JSON Web Tokens.
* **Rate Limiting por Rol:** Un middleware personalizado que limita el número de peticiones a la API según el rol del usuario (`premium`, `free`, `anonymous`), usando Redis para un rendimiento óptimo.
* **Frontend Interactivo:** Interfaz construida con React y TypeScript, siguiendo una arquitectura de componentes y con una capa de servicios para la comunicación con el backend.
* **Containerización Completa:** Todo el stack (Backend, Frontend, PostgreSQL, Redis) está orquestado con Docker Compose.

---

## 🚀 Stack Tecnológico

<div style="display: flex; gap: 50px;">
<div>
  <h3>Backend</h3>
  <ul>
    <li>Python 3.11</li>
    <li>FastAPI</li>
    <li>SQLAlchemy (ORM)</li>
    <li>Redis (Rate Limiting)</li>
    <li>Passlib & Python-jose (Seguridad)</li>
  </ul>
</div>
<div>
  <h3>Frontend</h3>
  <ul>
    <li>React 18</li>
    <li>TypeScript</li>
    <li>CSS Modules</li>
    <li>React Testing Library</li>
  </ul>
</div>
<div>
    <h3>DevOps</h3>
    <ul>
        <li>Docker</li>
        <li>Docker Compose</li>
        <li>Makefile</li>
    </ul>
</div>
</div>

---

## 🏁 Cómo Empezar

### Prerrequisitos

Asegúrate de tener instalados en tu sistema:
* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Instalación y Ejecución

1.  **Clona el repositorio:**
    ```bash
    git clone <https://github.com/antonioxzz/rate-limiter.git>
    cd rate-limiter
    ```

2.  **Construye y levanta los contenedores:**
    Este comando construirá las imágenes de Docker, aplicará las migraciones de la base de datos, creará los usuarios iniciales y iniciará todos los servicios.
    ```bash
    docker-compose up --build
    ```
    *También puedes usar el atajo del Makefile:* `make up`

3.  **¡Listo! La aplicación está en marcha:**
    * **Frontend:** Accede a [http://localhost:3000](http://localhost:3000)
    * **Backend API Docs (Swagger):** Accede a [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🛠️ Uso y Pruebas

### Credenciales de Usuario

Puedes usar los siguientes usuarios para probar los diferentes límites de peticiones:
* **Usuario Gratuito:**
    * **Username:** `free_user`
    * **Password:** `password`
    * **Límite:** 10 peticiones por minuto.
* **Usuario Premium:**
    * **Username:** `premium_user`
    * **Password:** `password`
    * **Límite:** 100 peticiones por minuto.
* **Anónimo:**
    * Simplemente usa la aplicación sin iniciar sesión.
    * **Límite:** 5 peticiones por minuto (basado en IP).


## 🏛️ Conceptos de Arquitectura Demostrados

Este proyecto sirve como un portafolio de patrones de diseño y buenas prácticas, incluyendo:

* **Arquitectura por Capas:** Clara separación entre la capa de API (rutas), la capa de negocio (servicios) y la capa de acceso a datos (CRUD).
* **Inyección de Dependencias:** Usada extensivamente en FastAPI para gestionar las sesiones de base de datos y la autenticación.
* **Middleware Personalizado:** Implementación de un middleware para una funcionalidad transversal como el Rate Limiting.
* **Seguridad:** Autenticación con JWT, manejo de CORS y almacenamiento seguro de contraseñas con hashing.
* **Infraestructura como Código:** Uso de `docker-compose.yml` para definir todo el stack de la aplicación de forma declarativa.
