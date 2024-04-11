# *Despliegue de Servicios de Amazon Web Services*

*En el marco de este proyecto, se emplean los servicios de AWS para establecer un Data Warehouse dedicado al almacenamiento y procesamiento de datos relacionados con los viajes en taxi en la ciudad de Nueva York. El objetivo principal es facilitar consultas SQL que permitan extraer información relevante del Data Warehouse, para luego llevar a cabo un análisis y visualización de los datos que se presentarán al cliente. La siguiente figura ilustra el ciclo de los datos y los servicios específicos de AWS utilizados en este proyecto:

![F](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/Data%20Lake%20(1).png)


*AWS Lambda* es un servicio de computación sin servidor que permite ejecutar código sin necesidad de administrar servidores. Con Lambda, podemos ejecutar código para una amplia variedad de aplicaciones o servicios backend, con tolerancia a errores y gestión automática de recursos de computación. Basta con cargar el código y Lambda se encargará de todo, desde la ejecución hasta el escalado, garantizando una alta disponibilidad. Además, podemos configurar la función para que se active automáticamente desde diversas fuentes, como S3, SNS, DynamoDB o Kinesis, sin necesidad de crear un punto de entrada. Lambda también nos permite crear nuevos servicios que se activen de forma directa o periódica.

En esta primera etapa del proyecto, hemos creado una función Lambda específicamente diseñada para realizar web scraping en la página de la Comisión de Taxis y Limusinas, con el objetivo de extraer los datos de los viajes realizados en la ciudad de Nueva York durante el año 2023. Estos datos son posteriormente almacenados de manera automatizada en un bucket de AWS S3.

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/taxis%20scrap.png)

Para automatizar el proceso, se empleó AWS EventBridge para programar la ejecución de la función Lambda el primer día de cada mes a las 00:00 horas.

![]()
