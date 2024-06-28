# Challenger N5 - Dev Python Senior
## Consideraciones generales
De acuerdo a lo solicitado en los [requerimientos técnicos](docs/challenger.md) diseñé un sistema basado en los siguientes supuestos:
- El sistema solicitado es parte de un sistema que seguirá creciendo en el futuro, incorporando nuevas funcionalidades.
- El sistema debe poder escalar en un futuro.
- Puede requerirse un cambio de alguna de las tecnologías usadas actualmente.

Por estas razones elegí un diseño basado en [arquitectura hexagonal](docs/arquitectura_hexagonal.md). 
Esta arquitectura es una de las más usadas dentro de las Arquitecturas Limpias. 
Utiliza los conceptos de Código Limpio, Principios SOLID y patrones de diseño, como por ejemplo el patrón repositorio entre otros.
Consiste en aislar toda la lógica de negocios propia, de todo agente externo como ser framework, bases de datos, ORMs, etc.
Dicha característica permite general código, escalable, reutilizable y fácilmente testeable.

En el caso en particular solicitado, soy consciente que puede ser considerado como una sobre-ingeniería del proyecto, al ser este un CRUD muy básico. 
Dado que el objetivo de esta prueba es que se hagan una idea de mi forma de trabajo, me parece pertinente este diseño.
Considero que Django REST Framework (DRF), es la herramienta que permite resolver los requerimientos, de la manera más rápida y eficiente posible.

## Consideraciones de diseño
Como normas generales de desarrollo tengo los siguientes criterios:
- **Nombres de variables, clases, funciones o métodos**: se nombran en inglés de acuerdo a las buenas prácticas a nivel mundial. Con excepción de lo expresamente indicado en español. La interfaz administrativa está en español, así como los nombre de las bases de datos que ve el usuario.
- **Implementación de la API de DRF**: uso tres capas (directorios) para concretar la arquitectura elegida, con el uso del patrón Vertical Slice dentro de estos:
  - **Infrastructure**: Capa donde están todos los elementos externos del sistema, como el DRF, la implementación de los adaptadores y la implementación de las inyecciones de dependencia. (Directorio Wirings). Es la capa externa del sistema.
  - **Application**: Capa donde se gestionan los casos de uso del sistema. Es la capa intermedia del sistema.
  - **Domain**: Capa donde se gestiona la logica de negocios de sistema. En ella están los servicios, que son los que implementan la lógica de negocios, los puestos o repositorios (Clases Abstractas) y las entidades que manejan los datos. Es la capa interna del sistema.
- **Archivos**: Toda clase o función independiente debe ir en un archivo propio. El único lugar donde no se sigue esta regla es con las familias de excepciones.
- **Manejo de errores propio**. Definición de una excepción base, de la cual heredan todas las demás excepciones. A su vez se definen varios tipos de excepciones básicas, a partir de las cuales se generan familias de excepciones de acuerdo a un tipo de error en particular. Este diseño permite definir un decorador que maneja los errores en los distintos métodos implementados, evitando la repetición de código. En el caso particular de DRF se usa un decorador en las vistas que estandariza el mensaje de respuesta de estas y a su vez de acuerdo a la familia de excepciones que llegue genera una respuesta de status HTTP.
- **Cobertura de test**. El código debe tener la mayor cobertura de test posible. En este caso en particular, no se hicieron test unitarios, ya que no había logica de negocios a probar. Es por eso que se implementaron test E2E.

## Instalación, ejecución y pruebas automáticas
- [Usando docker](docs/docker_install.md)
- [Usando entorno virtual](docs/virtual_env_install.md)


## Uso del sistema
Una vez generado el primer usuario se podrá acceder a la interfaz administrativa mediante el link http://127.0.0.1:8000/admin/, mediante las credenciales generadas previamente.

Mediante el link http://127.0.0.1:8000/api/docs/ se podrá acceder a la documentación interactiva de la aplicación (Swagger) y probar los endpoints.

### Procedimiento para cargar multas
1. Mediante la interface administrativa completar los datos de las personas, vehículos y Oficiales que puedan acceder al sistema.
2. El sistema que use el oficial, deberá requerir un token mediante una instrucción POST al endpoint **/api/officer_token/**.
3. Una vez obtenido el mismo, se enviará una petición POST al endpoint **/api/cargar_infraccion/** para cargar la infracción.

### Procedimiento para ver las multas
1. El sistema que use el usuario, enviará una petición POST al endpoint **/api/generar_informe/** para recibir el listado de las infracciones que tenga.

La información que se envia en el cuerpo de las peticiones está documentada en el link de swagger mencionado previamente.



