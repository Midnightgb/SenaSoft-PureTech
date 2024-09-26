# Marco de Trabajo del Proyecto SENASoft 2024

[View in English](./WORK_FRAMEWORK.md)

## 1. Stack Tecnológico
- Backend: Python con FastAPI
- Frontend: Vue.js
- Base de Datos: Supabase con PostgreSQL
- Despliegue: Render

## 2. Arquitectura
- Enfoque: Diseño API-First con Arquitectura en Capas
- Capas:
  1. Presentación: Vue.js (Frontend)
  2. Lógica de Negocio: FastAPI (Backend)
  3. Datos: Supabase/PostgreSQL

## 3. Estructura del Repositorio
```
/
├── backend/
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
├── docs/
├── .github/
│   └── workflows/
│       └── auto-merge.yml
├── .gitignore
├── README.md
├── README_ES.md
└── docker-compose.yml
```

## 4. Metodología: Scrumban
- Elementos de Scrum:
  - Sprints cortos
  - Daily stand-ups
  - Revisiones al final de cada sprint
- Elementos de Kanban:
  - Tablero visual (Trello) con columnas:
    - Por hacer
    - En progreso
    - Revisión
    - Hecho

## 5. Flujo de Trabajo
1. Diseño inicial de la API con FastAPI
2. Desarrollo iterativo en sprints cortos
3. Actualización constante del tablero Kanban
4. Revisiones diarias y al final de cada sprint
5. Integración continua entre frontend y backend
6. Despliegue continuo a Render

## 6. Control de Versiones (Git)
- Rama principal: `master`
- Rama de desarrollo: `develop`
- Ramas de feature: `feature/*`
- Ramas de bugfix: `bugfix/*`
- Uso de GitHub Actions para auto-merge de features completadas

## 7. Proceso de Desarrollo
1. Crear una nueva rama desde `develop` para cada feature/bugfix
2. Desarrollar y hacer commits frecuentes
3. Realizar pruebas locales
4. Crear un Pull Request a `develop`
5. Revisión de código por pares (si es posible en el contexto de la competencia)
6. Merge a `develop` (automático si se usa la palabra clave en el commit  "`[ready for deploy]`")
7. Despliegue automático a Render desde `develop`

## 8. Despliegue (Render)
- Frontend:
  1. Crear un nuevo Static Site en Render
  2. Conectar con el repositorio de GitHub
  3. Configurar:
     - Build Command: `cd frontend && npm install && npm run build`
     - Publish Directory: `frontend/dist`
- Backend:
  1. Crear un nuevo Web Service en Render
  2. Conectar con el repositorio de GitHub
  3. Configurar:
     - Root Directory: `backend`
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## 9. Entregables Clave
- Código fuente en GitHub (frontend y backend)
- Documentación de la API (generada por FastAPI)
- Base de datos funcional en Supabase
- Aplicación desplegada y accesible en Render
- Tablero Kanban con historial de progreso
- Presentación final del proyecto

## 10. Consideraciones Adicionales
- Enfoque en la calidad del código y las mejores prácticas
- Atención a la experiencia del usuario (UX/UI)
- Implementación de pruebas (unitarias, integración)
- Documentación clara del proceso y decisiones tomadas
- Configuración de variables de entorno en Render para las credenciales de Supabase

## 11. Generación de Requirements del Backend
Utilizamos `pip freeze` para generar el archivo `requirements.txt` para el backend. Para generar los requirements, ejecuta el siguiente comando en el directorio del backend:

Si estás en el directorio raíz del proyecto, puedes ejecutar el siguiente comando:
```
cd backend && pip freeze > requirements.txt && cd ..
```
o si ya estás en el directorio del backend, puedes ejecutar el siguiente comando:
```
pip freeze > requirements.txt
```

Este comando escaneará el código fuente del backend y generará un archivo `requirements.txt` con las dependencias necesarias para ejecutar el proyecto.