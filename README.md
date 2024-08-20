# Proyecto Indiviual 1: Sistema de recomendacion de peliculas

![image](https://github.com/user-attachments/assets/de28fa21-e50b-4749-abfc-04273505e982)


# Introducción

El objetivo del presente proyecto es simular un ambiente de trabajo donde cumplimos el rol de **Data Scientist** dentro de una start-up que provee servicios de agregación de plataformas de streaming.
La misma nos solicita construir un modelo de Machine Learning(ML) que ponga en marcha un sistema de recomendacion de peliculas totalmente nuevo.
Para lograr este objetivo debemos combinar un trabajo de **Data Engineer** que posteriormente nos permita construir un **Producto Viable Minimo(MVP)** de un sistema de recomendacion de peliculas.

*Recordemos que el **MVP** es una metodología de desarrollo de productos o servicios que se centra en crear un producto con el mínimo conjunto de características necesarias para validar 
su viabilidad en el mercado y obtener retroalimentación de los usuarios lo antes posible. 
La idea detrás de este procedimiento es lanzar algo lo suficientemente funcional como para que los usuarios puedan interactuar con él y proporcionar comentarios y datos de uso, pero sin gastar recursos excesivos en el desarrollo de características complejas que pueden no ser necesarias o relevantes para los usuarios.*

Para llevar adelante esta tarea utilizaremos las siguientes herramientas:
* **Visual Studio Code(VS Code):** es un editor de código fuente ligero, multiplataforma y altamente personalizable, desarrollado por Microsoft. Es popular entre desarrolladores debido a sus características avanzadas, como la depuración integrada, el control de versiones (Git), la finalización de código inteligente, y su amplia gama de extensiones que permiten soporte para múltiples lenguajes de programación y herramientas de desarrollo. Además, es gratuito y de código abierto.

* **Fast Api:** es un framework web moderno y de alto rendimiento para construir APIs en Python. Es conocido por su rapidez y eficiencia, tanto en términos de tiempo de desarrollo como en rendimiento. FastAPI utiliza tipado basado en anotaciones de Python para generar automáticamente la documentación de la API (como OpenAPI y Swagger UI), lo que facilita el desarrollo y la comprensión del código. También es compatible con la asincronía, lo que lo hace ideal para aplicaciones que requieren manejar múltiples solicitudes simultáneamente de manera eficiente. Es ampliamente utilizado para crear APIs RESTful y microservicios.

* **Render:** es una plataforma de alojamiento en la nube que permite desplegar aplicaciones web, APIs, bases de datos y otros servicios de manera sencilla y escalable.

## Tabla de contenidos
- [Introducción](#introducción)
- [FastAPI](#fastapi)
- [ETL](#etl)
- [EDA](#eda)
- [Deployment](#deployment)


## ETL

(Extract, Transform, Load) es un proceso en la gestión de datos que implica tres etapas clave:
-*Extract (Extracción)*: Se extraen datos de diferentes fuentes, como bases de datos, archivos, APIs, etc.
En este caso trabajamos con documentos CSV que se pueden descargar aqui:
- + [Dataset](https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5?usp=drive_link)

-*Transform (Transformación)*: Los datos extraídos se limpian, se transforman y se estructuran para cumplir con los requisitos de negocio o de almacenamiento.
Para esto utilizaremos principalmente la biblioteca [Pandas](https://pandas.pydata.org/docs/user_guide/10min.html) que nos facilita el trabajo con CSVs.

-*Load (Carga)*: Los datos transformados se cargan en un sistema de destino, como un data warehouse, base de datos, o cualquier sistema de almacenamiento de datos.
En este caso, ambos datasets fueron unificados y llevados al archivo **'2.base_de_datos'**

El proceso ETL es fundamental para integrar datos de múltiples fuentes en un repositorio central, facilitando análisis, reportes y toma de decisiones basadas en datos.

## FastAPI
Ahora, utilizando *Fast Api*, vamos a disponibilizar los datos de la empresa a los usuarios para que puedan ser testeadas las operaciones deseadas.
Para ello desarrollamos seis funciones que demuestren ser eficaces junto con el sistema de recomendacion:

Se pueden observar en el apartado de **funciones.py:**
+ def **cantidad_filmaciones_mes(*`Mes*`)**: Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.

+ def **cantidad_filmaciones_dia( *`Dia`* )**: Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.

+ def **score_titulo( *`titulo_de_la_filmación`* )**: Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.

+ def **votos_titulo( *`titulo_de_la_filmación`* )**: Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.

+ def **get_actor( *`nombre_actor`* )**: Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno. **La definición no deberá considerar directores.**

+ def **get_director( *`nombre_director`* )**: Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

+ def **recomendacion( *`titulo`* )**: Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.

## EDA
(Exploratory Data Analysis) Es un proceso en el análisis de datos que implica explorar y analizar datasets para descubrir patrones, detectar anomalías, probar hipótesis y resumir las principales características. Se utilizan estadísticas descriptivas y visualizaciones para entender mejor los datos antes de aplicar modelos más avanzados o tomar decisiones.

En este caso la idea principal fue identificar las posibles relaciones entre variables y la deteccion de outliers.
Algunos ejemplos:

**Matriz de correlacion**

*Es una tabla que muestra los coeficientes de correlación entre varias variables en un dataset. Estos coeficientes indican la fuerza y dirección de la relación entre dos variables, con valores que van de -1 (correlación negativa perfecta) a 1 (correlación positiva perfecta), y 0 indicando ninguna correlación. Es útil para identificar relaciones entre variables.*

![image](https://github.com/user-attachments/assets/6a0994d9-8538-43a3-a8a8-2d892fb9d647)

La relacion entre **budget** (presupuesto),**revenue**(ganancia) y **return** la vamos a obviar porque la ultima variable fue creada por nosotros en el proceso de transformación.

Lo que si resulta interesante de esta matriz es que hay un relacion fuerte entre las variables **revenue** y **vote_count** (0.81)
Esto nos podria demostrar una estrecha relacion entre la cantidad de votos que tiene una pelicula y las ganancias que genera una pelicula. Tanto para bien o para mal, mientras mas votos/opiniones haya sobre una pelicula, mayor o menor sera su ganancia.

Lo mismo sucede con la relacion entre **budget** y **vote_count** (0.68), mostrando tambien que los proyectos que mas opiniones han recibido son los que mas cantidad de presupuesto recibiran para una proxima saga, por ejemplo. 

**Nube de palabras**

*Es una representación visual de la frecuencia de palabras en un texto. Las palabras que aparecen con mayor frecuencia se muestran más grandes y en negrita, mientras que las menos comunes se muestran más pequeñas. Es útil para identificar rápidamente los términos más importantes o recurrentes en un conjunto de datos textuales.*

![image](https://github.com/user-attachments/assets/38cb6af3-a05c-465b-bea6-adc05163c702)

La nube de la palabras nos ayudara para poder recomendar peliculas de acuerdo a las palabras mas frecuentes que aparecen en los titulos.

**Grafico de barras**

![image](https://github.com/user-attachments/assets/22dda823-2656-4189-af90-650a26f48bee)

Un grafico de barras nos mostrara más especificamente la cantidad de veces que aparece cada palabra. 

Esta información nos permite entender mejor cuales son los titulos mas consumidos popularmente.

+ Ambos analisis nos pueden ser de utilidad ya que basandonos en la popularidad **popularity** podriamos encontrarnos con varios inconvenientes al ser una categoria que cuenta con muchos outliers.

![image](https://github.com/user-attachments/assets/c22c89bd-fe74-4b75-9b02-a7f81579be20)

Para crear un sistema de recomendacion mas sofisticado habria que trabajar con datos mas certeros.

## Deployment

*Deployment (o despliegue) es el proceso de poner una aplicación o servicio en un entorno de producción, donde está accesible para los usuarios finales. Esto implica mover el código desde un entorno de desarrollo o pruebas a un servidor o plataforma donde puede ser utilizado en vivo.*

Para realizar esta tarea utilizaremos [Render](https://render.com/).Una plataforma que simplifica el proceso de deployment al automatizar tareas como la configuración del servidor, el manejo de certificados SSL y el despliegue continuo. Con Render, puedes desplegar fácilmente tu aplicación web, API o servicio con unos pocos clics o comandos, haciendo que esté disponible en la web sin necesidad de gestionar manualmente la infraestructura subyacente.

Aqui algunos ejemplos para que el usuario pueda testear:

Ingresamos la siguiente URL:
```
https://proyecto-individual-1-epb0.onrender.com
```

Y ejecutamos uno de los siguientes ejemplos:


+ /filmaciones_mes?mes=Enero

+ /filmaciones_dia?dia=Sabado

+ /score_titulo?titulo=Forrest Gump

+ /votos_titulo?titulo=Toy Story

+ /actor?actor=Tom Hanks

+ /director?director=Christopher Nolan

+ /recomendacion?titulo=Iron Man

*Nota: se pueden explorar distintos valores: en vez de Sabado, ingresar Lunes por ejemplo. Lo anterior es a modo de ejemplo*

Un ejemplo de como se deberia ver:

![image](https://github.com/user-attachments/assets/07d383c7-8e16-4eeb-a69b-492957db452a)


![image](https://github.com/user-attachments/assets/f940972d-46f7-4c1a-b560-e12ba841cbb6)

**¡Espero te haya sido de utilidad!**







