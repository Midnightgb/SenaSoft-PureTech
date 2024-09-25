# Decisiones Técnicas del Proyecto SENASoft 2024

## Stack Tecnológico

### Backend: Python con FastAPI

- **Justificación**: 
  - Python es un lenguaje de alto nivel, fácil de aprender y versátil, ideal para el desarrollo rápido requerido en una competencia.
  - FastAPI ofrece alto rendimiento y facilita el desarrollo rápido de APIs RESTful.
  - Proporciona documentación automática de la API, cumpliendo con los requisitos de evaluación.

### Frontend: Vue.js

- **Justificación**:
  - Vue.js tiene una curva de aprendizaje suave, permitiendo crear interfaces de usuario interactivas rápidamente.
  - Se integra bien con el backend de FastAPI, facilitando el desarrollo full-stack.

### Base de Datos: Supabase con PostgreSQL

- **Justificación**:
  - PostgreSQL es un sistema de gestión de bases de datos relacional robusto y de código abierto, cumpliendo con los requisitos del concurso.
  - Supabase añade funcionalidades que aceleran el desarrollo, como autenticación y suscripciones en tiempo real.

### Despliegue: Render

- **Justificación**:
  - Ofrece un despliegue sencillo y rápido, crucial para demostrar la solución en un entorno de producción.
  - Facilita la implementación de despliegue continuo, demostrando buenas prácticas de DevOps.

## Arquitectura

- **Enfoque**: Diseño API-First con Arquitectura en Capas
- **Justificación**: 
  - Permite una separación clara de responsabilidades, facilitando el desarrollo paralelo y el mantenimiento.
  - Demuestra un enfoque profesional en el diseño de software.

## Control de Versiones y Flujo de Trabajo

- **Tecnología**: Git con flujo de trabajo Gitflow modificado
- **Justificación**:
  - Demuestra buenas prácticas de desarrollo colaborativo.
  - La integración de GitHub Actions para auto-merge muestra un enfoque en la automatización y la eficiencia del desarrollo.

## Metodología: Scrumban

- **Justificación**:
  - Combina elementos de Scrum y Kanban, adaptándose perfectamente al contexto de una competencia de corta duración.
  - Permite flexibilidad y visibilidad del progreso, aspectos cruciales en un entorno de competencia.

## Consideraciones Adicionales

### Seguridad

- Implementación de autenticación JWT y manejo seguro de contraseñas.
- **Justificación**: Demuestra preocupación por la seguridad, un aspecto crítico en aplicaciones web modernas.

### Documentación y Pruebas

- Énfasis en la documentación del código y de la API.
- Implementación de pruebas unitarias y de integración.
- **Justificación**: Demuestra un enfoque en la calidad del software y la mantenibilidad.

### Escalabilidad y Mantenibilidad

- **Justificación**: La elección de tecnologías modernas y la arquitectura adoptada permiten que la solución sea escalable y fácil de mantener, aspectos importantes para proyectos de software reales.

## Conclusión

El marco de trabajo y las tecnologías elegidas para SENASoft 2024 permiten un desarrollo rápido, eficiente y de alta calidad, alineándose con los objetivos y criterios de evaluación del concurso. Demuestran un equilibrio entre la velocidad de desarrollo necesaria para una competencia y las mejores prácticas de la industria del software.