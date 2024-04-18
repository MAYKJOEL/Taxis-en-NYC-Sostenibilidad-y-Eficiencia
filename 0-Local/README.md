# *Proyecto Taxis-en-NYC-Sostenibilidad-y-Eficiencia*

*Primera etapa del proyecto: Trabajamos en local*

*Como primera fase del proyecto, elaboramos un diagrama de Gantt para establecer objetivos y fechas de entrega con mayor claridad y precisión.*

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/WhatsApp%20Image%202024-04-11%20at%2011.16.37.jpeg)


#### *Extraccion, Transformacion y Carga (ETL) y Análisis Exploracion de datos (EDA)*

*Luego de establecer los objetivos concretos del proyecto, se realizó una exhaustiva exploración a nivel local para identificar la plataforma en la nube más adecuada para la implementación posterior. Esta etapa inicial fue fundamental para analizar las diversas opciones disponibles y evaluar sus capacidades en relación con los requisitos del proyecto. Es crucial destacar que durante este proceso se llevó a cabo el Análisis Exploratorio de Datos [notebook EDA](https://github.com/MAYKJOEL/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/0-Local/2-EDA/EDA.ipynb) y la Transformación de Datos (ETL) inicial en el [notebook ETL](https://github.com/MAYKJOEL/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/tree/main/0-Local/1-ETL). En este notebook, se exploró el contenido de los datasets proporcionados para realizar una selección precisa de las columnas a utilizar y definir el tipo de datos de las mismas, con el objetivo de evitar sesgos en el análisis posterior.*


#### *Web Scraping*

*Como siguiente paso, se procedió a aplicar web scraping en la página de la Comisión de taxis y limusinas de Nueva York para obtener los enlaces de descarga de los conjuntos de datos de viajes en taxi correspondientes al año 2023 y enero del año 2024. Tambien realizamos Transformacion de datos (ETL) y Análisis expliratorio de datos(EDA). [Notebook ETL Y EDA](https://github.com/MAYKJOEL/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/tree/main/0-Local/0-DataSets/2-DatosProporcionadosConETL)*

#### *Realizamos un segundo Análisis Exploratorio de Datos (EDA)*

*Una vez que hemos normalizado y preparado todos los archivos, hemos llevado a cabo un segundo análisis exploratorio de datos para mejorar la claridad de la visualización y permitir un análisis más exhaustivo. El código necesario para este proceso se encuentra detallado en el notebook adjunto.*

#### *Dashboard PowerBi*


**KPI´S**:  :white_circle:

*A través del análisis de KPIs fundamentales, hemos evaluado si la inversión en esta tecnología representa una verdadera contribución a la reducción de la contaminación ambiental.*

**KPI nro 1**
*En primer lugar, el KPI 1, relativo a las emisiones de CO2 por milla recorrida, nos ofrece resultados altamente satisfactorios. La meta establecida era reducir las emisiones en un 30%, y con gran satisfacción podemos informar que se logró una reducción del 100%. Esto significa que los taxis eléctricos están generando un 30% menos de CO2 que los taxis tradicionales por cada milla recorrida, lo que representa un avance significativo en la lucha contra la contaminación atmosférica.*

**KPI nro 2**
*En cuanto al KPI 2, que mide la reducción anual de emisiones, si bien no se alcanzó la meta del 15% establecida para el período 2022-2023, sí se logró una reducción considerable del 12%. Esta desviación de la meta nos impulsa a realizar una investigación profunda para identificar las causas subyacentes y desarrollar estrategias efectivas para optimizar el rendimiento en el futuro. No obstante, cabe destacar que la reducción del 12% sigue siendo un resultado positivo que demuestra el potencial de los taxis eléctricos para disminuir el impacto ambiental del sector transporte.*

**KPI nro 3**
*En lo que respecta al KPI 3, que evalúa el impacto ambiental total en un período de 6 años, los resultados son mixtos. La meta era reducir las emisiones en un 15% durante este período, sin embargo, solo se logró una reducción del 7%. Si bien no se superó la meta inicial, este resultado evidencia un avance positivo en la dirección correcta.*

**En definitiva, los tres KPIs ambientales nos permiten concluir:**
*Que los taxis eléctricos están teniendo un impacto positivo en el medio ambiente. La reducción de las emisiones de CO2 por milla recorrida, la disminución anual de emisiones y el impacto ambiental total positivo, aunque no alcance la meta esperada, confirman que la inversión en taxis eléctricos es una decisión acertada que contribuye a la mitigación del cambio climático y la mejora de la calidad del aire.*

<br><br>

**Preguntas claves**:  :white_circle:

**¿Cómo se comparan las emisiones de CO2 de los taxis eléctricos con las de otros tipos de transporte?**

*Los taxis eléctricos presentan emisiones de CO2 significativamente más bajas en comparación con los taxis tradicionales. Un taxi eléctrico emite un promedio de 0 gramos de CO2 por milla, mientras que un taxi tradicional emite un promedio de 150 gramos de CO2 por milla. Esta diferencia sustancial posiciona a los taxis eléctricos como una alternativa más ecoamigable dentro del sector transporte.*

**¿Qué tan accesibles son los taxis eléctricos para los consumidores?**

*En los últimos años, el costo de los taxis eléctricos ha experimentado una reducción considerable, haciéndolos más accesibles para los consumidores. El precio promedio de un nuevo taxi eléctrico en los Estados Unidos ronda los $35,000, y además, existen diversos incentivos gubernamentales que facilitan la adquisición de estos vehículos.* 

**¿Qué infraestructura se necesita para apoyar la adopción generalizada de taxis eléctricos?**

*Para fomentar la adopción masiva de taxis eléctricos, es fundamental desarrollar una infraestructura adecuada que incluya estaciones de carga públicas. Afortunadamente, la infraestructura de carga se encuentra en constante expansión.*

<br><br>

**En CONCLUSIÓN, este estudio nos permite afirmar que**:  :white_circle:
*los taxis eléctricos representan una alternativa viable y sostenible para el servicio de taxi, contribuyendo de manera significativa a la reducción de la contaminación ambiental y promoviendo un futuro más verde. La inversión en esta tecnología no solo beneficia al medio ambiente, sino que también abre nuevas oportunidades para el desarrollo económico y la creación de empleos.*

#### *Eleccion del Modelo de Machine Learning*


Modelo: RandomForest Regressor

*Motivación:*

*1. Capacidad para manejar relaciones no lineales:*
*El RandomForest Regressor es un modelo de ensamble basado en árboles que puede capturar relaciones no lineales y patrones complejos en los datos. Esta capacidad es fundamental para nuestro problema, ya que la demanda de taxis puede estar influenciada por una variedad de factores no lineales, como eventos especiales o condiciones climáticas.*

*2. Regularización incorporada mediante GridSearchCV:*
*Al utilizar GridSearchCV de sklearn, hemos mejorado el modelo RandomForest Regressor incorporando técnicas de regularización para prevenir el sobreajuste. Esto garantiza que nuestro modelo generalice bien a nuevos datos y no se ajuste excesivamente a las particularidades del conjunto de entrenamiento.*

*3. Manejo eficiente de datos faltantes:*
*El RandomForest Regressor puede manejar eficientemente los valores perdidos en los datos, lo que es beneficioso para lidiar con posibles valores faltantes en nuestros datos de entrada.*

*4. Escalabilidad y rendimiento:*
*Aunque RandomForest Regressor puede ser menos escalable que otros modelos, como XGBoost, su rendimiento sigue siendo sólido y es adecuado para manejar conjuntos de datos de tamaño moderado. Dado que estamos trabajando con datos de distritos de Nueva York, la capacidad de manejar eficientemente estos datos es esencial para garantizar un entrenamiento y predicciones eficaces.*

*Fórmula Matemática del RandomForest Regressor:*
*El modelo RandomForest Regressor realiza predicciones mediante la combinación de las predicciones de múltiples árboles de decisión, tomando el promedio de las predicciones individuales. La fórmula general se expresa como:*

![](https://github.com/titolup/Taxis-en-NYC-Sostenibilidad-y-Eficiencia/blob/main/1-Nube/Imagenes%20AWS/Captura%20de%20pantalla%20(108).png)

*Lógica de Uso:*
*1. Entrenamiento:*
*Utilizaremos datos históricos de demanda de taxis en Nueva York para entrenar nuestro modelo RandomForest Regressor, ajustando los hiperparámetros mediante GridSearchCV para optimizar su rendimiento.*

*2. Predicción:*
*Una vez entrenado, el modelo será capaz de realizar predicciones sobre la demanda de taxis en diferentes distritos. Utilizaremos características relevantes, como la hora del día, el día de la semana, eventos especiales para hacer predicciones precisas.*

*3. Evaluación:*
*Evaluaremos el rendimiento del modelo utilizando métricas como el error cuadrático medio (MSE) y coeficiente de determinación (R^2) para garantizar la precisión y la capacidad de generalización del modelo a datos no vistos.*

*4. Ajuste Fino mediante GridSearchCV:*

*a. Exploración sistemática del espacio de hiperparámetros.*
*b. Optimización del rendimiento del modelo.*
*c. Evaluación cruzada incorporada.*
*d. Automatización del proceso de ajuste de hiperparámetros.*

*Funcionamiento del GridSearchCV:*
*El modelo GridSearchCV realiza una búsqueda exhaustiva en el espacio de hiperparámetros especificado y evalúa el rendimiento del estimador para cada combinación de hiperparámetros utilizando validación cruzada. Luego, selecciona la combinación de hiperparámetros que maximiza la métrica de evaluación especificada.*

*Endpoints:*
*Con el modelo entrenado y los datasets normalizados, se han creado funciones para el despliegue de los mismos, trabajando tanto con archivos locales (Notebook Local Endpoints) como en la plataforma de AWS (Notebook AWS Endpoints). El despliegue se realizó utilizando la libreria fastAPI y el servidor Render* 


#### *Entrenamiento de Modelo en AWS SageMaker*

*Para el entrenamiento de nuestros modelos de Machine Learning, empleamos AWS Sagemaker, un servicio completamente administrado que agiliza la creación, entrenamiento e implementación de modelos de Machine Learning a cualquier escala. Con Sagemaker, podemos desarrollar modelos personalizados utilizando una amplia gama de algoritmos de aprendizaje, y llevarlos a producción en solo unos pocos clics. Esto incluye algoritmos para tareas como clasificación, regresión, agrupación, detección de anomalías, recomendación y aprendizaje profundo, proporcionándonos flexibilidad y potencia para abordar diversas necesidades de análisis y predicción.*


![]()







