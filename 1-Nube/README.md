# *Despliegue de Servicios de Amazon Web Services*

*En el marco de este proyecto, se emplean los servicios de AWS para establecer un Data Warehouse dedicado al almacenamiento y procesamiento de datos relacionados con los viajes en taxi en la ciudad de Nueva York. El objetivo principal es facilitar consultas SQL que permitan extraer información relevante del Data Warehouse, para luego llevar a cabo un análisis y visualización de los datos que se presentarán al cliente. La siguiente figura ilustra el ciclo de los datos y los servicios específicos de AWS utilizados en este proyecto:*

![F](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/Data%20Lake%20(1).png)


*AWS Lambda* *es un servicio de computación sin servidor que permite ejecutar código sin necesidad de administrar servidores. Con Lambda, podemos ejecutar código para una amplia variedad de aplicaciones o servicios backend, con tolerancia a errores y gestión automática de recursos de computación. Basta con cargar el código y Lambda se encargará de todo, desde la ejecución hasta el escalado, garantizando una alta disponibilidad. Además, podemos configurar la función para que se active automáticamente desde diversas fuentes, como S3, SNS, DynamoDB o Kinesis, sin necesidad de crear un punto de entrada. Lambda también nos permite crear nuevos servicios que se activen de forma directa o periódica.*

*En esta primera etapa del proyecto, hemos creado una función Lambda específicamente diseñada para realizar web scraping en la página de la Comisión de Taxis y Limusinas, con el objetivo de extraer los datos de los viajes realizados en la ciudad de Nueva York durante el año 2023. Estos datos son posteriormente almacenados de manera automatizada en un bucket de AWS S3.*

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/taxis%20scrap.png)

*Para automatizar el proceso, se empleó AWS EventBridge para programar la ejecución de la función Lambda el primer día de cada mes a las 00:00 horas.*

*Una vez obtenidos los archivos parquet, recurrimos al uso de AWS Glue para automatizar el proceso de normalización de los datos. AWS Glue es un servicio de extracción, transformación y carga (ETL) totalmente administrado que facilita la preparación y la carga de los datos para su análisis. Con AWS Glue, podemos crear y ejecutar trabajos de ETL con unos pocos clics en la consola de AWS o ejecutar el código directamente en Apache Spark para aprovechar los beneficios de escala, seguridad y administración que ofrece.*

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/ETL%20TAXIS.png)

*Para automatizar la normalización de los datos, se implementó AWS EventBridge para programar la ejecución de la tarea de AWS Glue en el primer día de cada mes, a la 01:00 horas.*



*Una vez completada la normalización de los datos, el archivo resultante en formato Parquet se guarda en un bucket de AWS S3. Sin embargo, el archivo se almacena con un nombre predeterminado generado automáticamente al guardar un archivo Parquet mediante Apache Spark con el formato de compresión Snappy.*

*Para abordar este problema, implementamos otra función Lambda que se encarga de renombrar el archivo y luego lo almacena en un bucket que alimenta a nuestro Data Warehouse.*

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/lambda%20renombrar.png)

*La automatización de este proceso se lleva a cabo mediante otro evento de AWS EventBridge que se ejecuta el primer día de cada mes a las 02:00 horas.*

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/aws%20s3.png)

*Para la validación de datos, utilizamos un desencadenador de SNS de AWS que envía un correo electrónico al administrador de la cuenta para informar si se ha realizado exitosamente la validación de datos.*


![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/WhatsApp%20Image%202024-04-17%20at%2009.02.20.jpeg)

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/WhatsApp%20Image%202024-04-17%20at%2009.02.20.jpeg)



*Una vez que el archivo se encuentra en el bucket que alimenta a AWS Athena, podemos ejecutar consultas SQL para obtener información de los datos almacenados en el Data Warehouse.*

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/crawler.png)
![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/crawler2.png)

*Conforme la base de datos de la Comisión de Taxis y Limusinas (TLC) se renueve, nuestro Data Warehouse y todos los servicios de AWS que dependan de él se actualizarán automáticamente mediante nuestra función Lambda. Esta función tomará los nuevos registros de viajes y los almacenará en el bucket del Data Warehouse, garantizando así la actualización continua de los datos y la coherencia del sistema.*

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/Athenas.png)



*Con las tablas que hemos creado, podemos plasmar la estructura del Diagrama Entidad-Relación (DER), lo cual facilita el análisis de datos. A continuación, se muestra el DER del estudio, el cual exhibe una estructura similar a un copo de nieve, donde cada tabla establece relaciones con otras, generando una red interconectada:*

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/Dise%C3%B1o%20sin%20t%C3%ADtulo.png)


*Para visualizar los datos almacenados en el Data Warehouse, empleamos Power BI, un servicio de inteligencia de negocios (BI) que nos permite crear y publicar paneles interactivos con visualizaciones de datos en tiempo real. Estos paneles son accesibles desde cualquier dispositivo y pueden compartirse fácilmente con otros miembros de la organización.*
*Conectamos Power BI utilizando el conector certificado Simba Athena, permitiéndonos acceder directamente a los datos almacenados en AWS Athena y crear visualizaciones dinámicas y personalizadas con facilidad. Este conector garantiza una integración segura y eficiente entre Power BI y AWS Athena, facilitando el análisis de datos en tiempo real y la toma de decisiones informadas.*

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/Dise%C3%B1o%20sin%20t%C3%ADtulo%20(1).png)


#### *Entrenamiento de Modelo en AWS SageMaker*

*Para el entrenamiento de nuestros modelos de Machine Learning, empleamos AWS Sagemaker, un servicio completamente administrado que agiliza la creación, entrenamiento e implementación de modelos de Machine Learning a cualquier escala. Con Sagemaker, podemos desarrollar modelos personalizados utilizando una amplia gama de algoritmos de aprendizaje, y llevarlos a producción en solo unos pocos clics. Esto incluye algoritmos para tareas como clasificación, regresión, agrupación, detección de anomalías, recomendación y aprendizaje profundo, proporcionándonos flexibilidad y potencia para abordar diversas necesidades de análisis y predicción.*


![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/SageMaker1.jpeg)

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/SageMaker2.jpeg)














