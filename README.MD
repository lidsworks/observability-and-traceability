

🎯 Objetivo del proyecto
------------------------

Este proyecto es una prueba de concepto para ilustrar la importancia de la observabilidad y trazabilidad en sistemas distribuidos.

La aplicación consta de una aplicación web desarrollada con Nuxt.js que se comunica con dos backends: una aplicación de enrutamiento y gestión de API desarrollada con PHP y otra aplicación de gestión de hitos desarrollada con Python y Flask.

El objetivo de la aplicación es visualizar una serie de hitos históricos almacenados en base de datos utilizando tecnologías como New Relic para la observación y monitoreo de la aplicación y Kubernetes para el despliegue en un cluster de contenedores.

La generación de los hitos se realiza de forma automática utilizando la API de generación de texto de OpenAI, por lo que los hitos no son creados manualmente por parte del usuario.

📝 Descripción de la aplicación
-----------------------------

La aplicación consta de tres capas de aplicación:

* La capa de frontal que se comunica con los dos backends y se encarga de renderizar la información de los hitos históricos.
* La capa de gateway que se encarga de enrutar las solicitudes entre los dos backends y realizar la gestión de tokens de autenticación JWT.
* La capa de backend que se encarga de la gestión de la base de datos y la gestión de los hitos históricos.

La comunicación entre las capas se realiza mediante APIs REST y la información se almacena en una base de datos MySQL.

La generación de los hitos se realiza de forma automática utilizando la API de generación de texto de OpenAI, específicamente con chatGPT (Chat from the future), una versión avanzada de la API de texto de OpenAI que permite generar texto de manera más natural y contextual.

La información de los hitos se genera utilizando la pregunta "Sabrías decirme un hecho histórico tecnológico que sucediera en una fecha específica?", por lo que los hitos son generados utilizando la información histórica de los acontecimientos tecnológicos ocurridos en diferentes fechas.

🔍 ¿Qué podemos aprender de este proyecto?
---------------------------------------

El proyecto nos permite ver cómo es fácil monitorear y observar la información de una aplicación distribuida utilizando New Relic y Kubernetes.

En el proyecto podemos ver cómo se puede utilizar New Relic para medir el rendimiento y la trazabilidad de la aplicación y cómo se puede utilizar Kubernetes para desplegar la aplicación en un cluster de contenedores.

🎯 ¿Qué se puede mejorar?
------------------------

Este proyecto es una POC y hay varias cosas que se podrían mejorar:

* Se podría mejorar la seguridad y la implementación de autenticación de usuarios.
* Se podría mejorar la experiencia de usuario al agregar validaciones y mensajes de error útiles en la capa de frontal.
* Añadir test funcionales para validar el código antes de subir
* Validar imágenes de Docker (y paquetes de sistemas)


🤝 Microservicios creados
---------------

* [app-milestone-frontend]: aplicación web desarrollada con Nuxt.js
* [app-milestone-gateway]: aplicación de enrutamiento y gestión de API desarrollada con PHP
* [app-milestone-backend]: aplicación de gestión de hitos desarrollada con Python y Flask

🤖 Despliegue en Kubernetes
-------------------------

Este proyecto se ha desplegado en un cluster de Kubernetes en un proveedor cloud.

🔍 Observabilidad con New Relic
-------------------------------

Se ha integrado New Relic para la observación y monitoreo de la aplicación.

🤖 Integración con GitHub Actions
----------------------------

Se ha configurado GitHub Actions para automatizar el despliegue en el cluster de Kubernetes.

💻 Tecnologías utilizadas
-------------------------

* Backend: Python, Flask y SQLAlchemy
* Gateway: PHP y Slim 
* Frontend: Nuxt y Vuetify 