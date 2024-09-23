# Proyecto SENASoft 2024 - Configuración para Desarrollo Local
[View in English](./README.md)

Este README proporciona instrucciones para configurar el entorno de desarrollo del proyecto SENASoft 2024. Sigue estos pasos para poner en marcha el proyecto en tu máquina local.

## Prerrequisitos

Antes de comenzar, asegúrate de tener instalado el siguiente software en tu sistema:

1. **Python**: Versión 3.12 o superior
   - Descarga desde: https://www.python.org/downloads/
   - Verifica la instalación: `python --version`

2. **Node.js**: Última versión LTS (18.x o superior)
   - Descarga desde: https://nodejs.org/
   - Verifica la instalación: `node --version`

3. **npm**: Viene con la instalación de Node.js
   - Verifica la instalación: `npm --version`

4. **Git**: Última versión
   - Descarga desde: https://git-scm.com/downloads
   - Verifica la instalación: `git --version`

5. **Visual Studio Code**: Última versión
   - Descarga desde: https://code.visualstudio.com/
   - Extensiones recomendadas:
     - Python
     - Pylance
     - Vue.js Extension Pack
     - ESLint
     - Prettier

## Configuración del Proyecto

1. **Clonar el Repositorio**
   ```
   git clone https://github.com/tu-repo/senasoft-2024.git
   cd senasoft-2024
   ```

2. **Configuración del Backend (Python/FastAPI)**
   ```
   cd backend
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configuración del Frontend (Vue.js)**
   ```
   cd frontend
   npm install
   ```

4. **Variables de Entorno**
   - Copia `.env.example` a `.env` en el directorio que vas a trabajar `backend` o `frontend`
   - Completa las variables de entorno necesarias

## Ejecutar la Aplicación

1. **Iniciar el Servidor Backend**
   ```
   cd backend
   uvicorn main:app --reload
   ```
   La API estará disponible en `http://localhost:8000`

2. **Iniciar el Servidor de Desarrollo Frontend**
   ```
   cd frontend
   npm run serve
   ```
   El frontend estará disponible en `http://localhost:8080`

3. **Acceder a la Aplicación**
   Abre tu navegador web y navega a `http://localhost:8080`

## Flujo de Trabajo de Desarrollo

1. Realiza cambios en tu entorno local
2. Prueba los cambios localmente
3. Haz commit de los cambios en Git
4. Sube los cambios al repositorio remoto
5. El pipeline de CI/CD se encargará del despliegue en Render

## Solución de Problemas

Si encuentras algún problema durante la configuración o el desarrollo, consulta la documentación del proyecto o crea un issue en el repositorio de GitHub.

## Recursos Adicionales

- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de Vue.js](https://vuejs.org/guide/introduction.html)
- [Documentación de SQLAlchemy](https://docs.sqlalchemy.org/)

¡Feliz codificación!