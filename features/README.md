# Variables predictorias

Tras leer biblografía, se recopilan una serie de variables que se consideran determinantes a la hora de determinar el tiempo de supervivencia tras el alta de la admisión hospitalaria: 

Las variables recopiladas se extraen a partir de consultas a la base de datos y en algunos casos al preprocesamiento de estas. 

## Información demográfica

Se recopilan cinco variables de índole demográfica: Edad, sexo, estado civil, religión y etnicidad. Estas variables se extraen directamente de la tabla ADMISSIONS, excepto la edad, que se calcula a partir de la diferencia de tiempo entre la fecha de nacimiento, almacenada en la tabla PATIENTS, y la fecha de admisión hospitalaria, procedente de la tabla ADMISSIONS. 

### Edad

La edad de los pacientes mayores a 91 años se encuentra desplazada en el tiempo con la finalidad de proteger su identidad y dificultar su identificación, en cumplimiento con la ley estadounidense de privacidad, la HIPPA. De esta manera, encontramos con pacientes ancianos con edades superiores a 300 años. Mediante una función de preprocesado substituimos la edad de estos pacientes por 91 años. Posteriormente descartaremos estos registros del conjunto de datos que servirá para entrenar la red neuronal, por considerarlos poco fiables y propensos a inducir errores. Así mismo, se descartaran igualmente los neonatos, por presentar un comportamiento médico muy distinto al de la población adulta.  

```sql
SELECT hadm_id, 
EXTRACT(epoch FROM (admittime dob))/(3600*24*365)
AS age
FROM admissions a
INNER JOIN patients p
ON a.subject_id = p.subject_id
```

Se distribuye estadisticamente de la siguiente manera

<img src="C:\mimic-iii-project\plots\Demographic_data\age_histogram.png">


| Descriptor estadístico  | Valor (años) |
| :---------------------: | :----------: |
|        Recuento         |    58976     |
|  Media aritmética (μ)   |     55.2     |
| Desviación estándar (σ) |     27.3     |
|      Valor mínimo       |      0       |
|      Percentil 25%      |     43.5     |
|      Percentil 50%      |     61.8     |
|      Percentil 75%      |     75.9     |
|      Valor máximo       |     91.4     |

### Sexo ###

Extraemos esta variable para cada admisión hospitalaria directamente de la base de datos, sin ningún tipo de preprocesado, mediante la siguiente consulta simple. 

```sql
SELECT hadm_id, gender
FROM admissions a
INNER JOIN patients p
ON a.subject_id = p.subject_id

```

Se distribuye de la siguiente manera:

|         | Recuento | Proporción |
| :-----: | :------: | :--------: |
| Hombres |  32950   |   55.8 %   |
| Mujeres |  26026   |   44.2 %   |

### Estado civil

Lo obtenemos mediante la siguiente consulta, de forma análoga al sexo del paciente.

```sql
SELECT hadm_id, marital_status
FROM admissions a
INNER JOIN patients p
ON a.subject_id = p.subject_id
```

Observamos clases claramente descompensadas y poco significativas que es conveniente tratar. 

| Estado civil      | Cantidad |
| ----------------- | -------- |
| DIVORCED          | 3213     |
| LIFE PARTNER      | 15       |
| MARRIED           | 24239    |
| SEPARATED         | 571      |
| SINGLE            | 13254    |
| UNKNOWN (DEFAULT) | 345      |
| WIDOWED           | 7211     |

Para el preprocesado de esta variable, unificamos aquellos grupos de características similares. En concreto, se juntan los grupos DIVORCED y SEPARATED en uno solo, y se incluye LIFE PARTNER dentro de MARRIED. Para realizar este agrupamiento se tienen en cuenta los hábitos de vida y alimentación que pueden caracterizar a cada grupo. Tras realizar esta agrupación, llegamos a las siguientes clases: 

| Estado civil       | Cantidad |
| ------------------ | -------- |
| DIVORCED/SEPARATED | 3784     |
| MARRIED            | 24254    |
| SINGLE             | 13254    |
| UNKNOWN            | 10473    |
| WIDOWED            | 7211     |

### Religion

Realizamos un procedimiento análogo al llevado a cabo en la variable MARITAL_STATUS, teniendo en cuenta las mismas consideraciones en el momento de unificar grupos. Extraemos la variable de la base de datos con la siguiente consulta 

```sql
SELECT hadm_id, religion 
FROM admissions a
INNER JOIN patients p
ON a.subject_id = p.subject_id
```

De la misma manera que con el estado civil, obtenemos grupos descompensados y poco significativos. En concreto, obtenemos 20 grupos, 14 de los cuales cuentan con menos de mil registros, de un total de ~ 59k. Tras agruparlos según características culturales similares, llegamos a los siguientes grupos:

| Religion       | Valores |
| :------------- | :-----: |
| BUDDHIST/HINDU |   380   |
| CHRISTIAN      |  29323  |
| JEWISH/HEBREW  |  5330   |
| MUSLIM         |   225   |
| NONE           |  23176  |
| ORTHODOX       |   542   |

### Etnicidad

Realizando el mismo proceso que para las variables anteriores, extraemos y unificamos la etnicidad del paciente para cada admisión hospitalaria. 

```sql
SELECT hadm_id, ethnicity
FROM admissions a
INNER JOIN patients p
ON a.subject_id = p.subject_id
```

Se recopilan 41 orígenes étnicos distintos, algunos muy similares entre si. Por ejemplo, se hace distinción de hispanos según el país, dando lugar a numerosas categorías con menos de diez entradas. Sucede lo mismo con pacientes de origen asiático y caucásico. También hay presentes registros de pacientes con origen nativo de norteamérica (72 registros) o nativo del caribe (9 registros). Estos registros poco significativos se agrupan bajo la categoria OTHER. La agrupación realizada se puede consultar en el archivo 'mappings.py' ubicado en la carpeta resources. El resultado de preprocesar la variable es el siguiente:

| Etnicidad | Cantidad |
| --------- | -------- |
| ASIAN     | 2007     |
| BLACK     | 5785     |
| HISPANIC  | 2136     |
| NONE      | 5896     |
| OTHER     | 1766     |
| WHITE     | 41386    |

## Pruebas de laboratorio

Se extraen diez pruebas de laboratorio comunes, realizadas rutinariamente tras el ingreso de un paciente, para emplearlas como variables predictorias.

Para cada una de ellas, obtenemos su valor medio y su desviación estándar, dando lugar a un total de veinte variables. 

Cada uno de los resultados de las pruebas se almacena en la tabla LABEVENTS mediante un identificador, ITEMID.

La relación de ITEMIDs para las pruebas de laboratorio es la siguiente:

| Prueba de laboratorio      | ITEMID       |
| -------------------------- | ------------ |
| Nitrógeno ureico en sangre | 51066        |
| Recuento de plaquetas      | 51265        |
| Hematocrito                | 51221        |
| Potasio en sangre          | 50971        |
| Sodio en sangre            | 50983        |
| Creatinina en sangre       | 50912        |
| Bicarbonato en sangre      | 50882        |
| Recuento de leucocitos     | 51301        |
| Glucosa en sangre          | 50809, 50931 |
| Albúmina en sangre         | 50862        |

Para obtener el promedio y la desviación estándar de cada una de estas variables, por ejemplo para el sodio en sangre, realizamos la siguiente consulta: 

```sql
SELECT hadm_id,
avg(valuenum) AS AVG_SODIUM,
stddev(valuenum) AS STD_SODIUM,
FROM labevents
WHERE itemid = 50983
GROUP BY hadm_id
```

Esta función se ejecuta en bucle para todas las pruebas de laboratorio.

En cuanto al preprocesado, descartamos aquellos valores por debajo del percentil 1% y por encima del percentil 99%, al considerarlos errores aberrantes o fallos de medicion, además de ser poco significativos. Se realiza mediante una función creada para ello, disponible en 'preprocessing service'.

Tras extraer las variables y tratarlas, obtenemos el siguiente resultado:

|   Prueba de laboratorio    | Medidas (x 1000) | Media aritmética (μ) | Desviación estándar (σ) | Valor mínimo | Percentil 25 % | Percentil 50% | Percentil 75% | Valor máximo | Unidad de medida |
| :------------------------: | :--------------: | :------------------: | :---------------------: | :----------: | :------------: | :-----------: | :-----------: | :----------: | :--------------: |
| Nitrógeno ureico en sangre |       49.9       |         24.5         |          16.1           |     5.6      |      13.4      |     19.2      |     30.3      |      93      |     mg/24hr      |
|   Recuento de plaquetas    |       55.8       |        241.1         |          97.9           |     44.9     |     172.3      |      229      |     297.1     |    595.6     |       K/uL       |
|        Hematocrito         |       55.9       |         33.9         |           6.9           |     23.8     |      29.1      |     31.9      |     36.7      |     58.9     |        %         |
|     Potasio en sangre      |       51.8       |         4.2          |           0.4           |     3.3      |      3.9       |      4.1      |      4.4      |     5.8      |      mEq/L       |
|      Sodio en sangre       |       51.8       |        138.7         |           3.1           |    128.7     |     136.9      |     138.9     |     140.8     |    147.8     |      mEq/L       |
|    Creatinina en sangre    |       49.9       |         1.3          |           1.1           |     0.35     |      0.72      |     0.93      |     1.34      |     7.9      |      mg/dL       |
|   Bicarbonato en sangre    |       51.8       |        138.7         |           3.1           |    128.7     |     136.9      |     138.9     |     140.8     |    147.8     |      mEq/L       |
|   Recuento de leucocitos   |       55.8       |         241          |          97.9           |     44.9     |     172.3      |      229      |     297.1     |    595.6     |       K/uL       |
|     Glucosa en sangre      |       49.6       |        131.7         |          32.9           |     78.2     |      110       |     124.2     |     124.3     |    144.3     |      mg/dL       |
|     Albúmina en sangre     |       30.5       |         3.2          |           0.6           |     1.7      |      2.7       |      3.2      |      3.7      |     4.7      |       g/dL       |

## Señales fisológicas

De la misma forma que obtenemos los resultado de las pruebas de laboratorio, extraemos de la base de datos el promedio y la desviación estándar de seis señales fisiológicas para emplearlas como variables predictorias. 

Las medidas han sido tomadas con dos sistemas de monitorización distintos, Philips CareVue y Metavision. Así mismo, la base de datos distingue entre medidas tomadas automáticamente y medidas tomadas expresamente por el personal médico, entre otros factores. Es por ello que una misma medida presenta múltiples identificadores.

| Señal fisiológica       | ITEMID                            |
| ----------------------- | --------------------------------- |
| Frecuencia cardíaca     | 220045, 211                       |
| Frecuencia respiratoria | 8113, 3603, 220210, 618           |
| Presión sistólica       | 51,442,455,6701,220179,220050     |
| Presión diastólica      | 8368,8440,8441,8555,220180,220051 |
| Temperatura             | 223761,678                        |
| Saturación de oxígeno   | 646, 220277                       |

Las señales fisiológicas se registran en la tabla CHARTEVENTS. Empleamos la siguiente consulta, muy similar a la empleada para obtener los resultados de las pruebas de laboratorio, para extraer los valores deseados en el caso de la saturación de oxígeno.

```sql
SELECT hadm_id,
avg(valuenum) AS AVG_SPO2,
stddev(valuenum) AS STD_SPO2,
FROM chartevents
WHERE itemid IN (646, 220277)
GROUP BY hadm_id
```

Aplicamos el mismo procesamiento usado anteriormente, es decir, descartamos aquellos valores por debajo del percentil 1% y aquellos por encima del 99%. La estadísticas descriptivas del promedio de estas variables se muestra en la siguiente tabla.

| Prueba de laboratorio   | Medidas (x 1000) | Media aritmética (μ) | Desviación estándar (σ) | Valor mínimo | Percentil 25 % | Percentil 50% | Percentil 75% | Valor máximo | Unidad de medida |
| ----------------------- | ---------------- | -------------------- | ----------------------- | ------------ | -------------- | ------------- | ------------- | ------------ | ---------------- |
| Frecuencia cardíaca     | 55.6             | 92.2                 | 22.9                    | 55.5         | 78.9           | 86.8          | 99.8          | 162          | BPM              |
| Frecuencia respiratoria | 55.6             | 22.7                 | 10.1                    | 12.4         | 16.9           | 19.4          | 23            | 60           | BPM              |
| Presión sistólica       | 48               | 120.5                | 15.2                    | 86.8         | 109.2          | 118.8         | 130.6         | 163.8        | mmHg             |
| Presión diastólica      | 48               | 61                   | 9.7                     | 39.2         | 54             | 60.1          | 67.1          | 91.8         | mmHg             |
| Temperatura             | 47.2             | 98.2                 | 0.9                     | 94.7         | 97.7           | 98.2          | 98.8          | 100.6        | ºF               |
| Saturación de oxígeno   | 48               | 96.9                 | 1.64                    | 89.3         | 96.1           | 97.2          | 98.8          | 99.8         | %                |

A continuación se muestra la distribución de densidad de estas variables.

<img src="C:\mimic-iii-project\plots\Physio_data\subplot.png">

## Información hospitalaria

Se extraen once variables relacionadas con cada estáncia hospitalaria. 

| Variables hospitalarias               | Tipo                    |
| ------------------------------------- | ----------------------- |
| Servicio médico                       | Categórica (20 valores) |
| Grupo de diagnóstico ICD9             | Categórica              |
| Realización de cirugía                | Binaria                 |
| Duración de estáncia en UCI           | Numérica continua       |
| Duración de estáncia total            | Numérica continua       |
| Indicador de severidad OASIS          | Numérica entera         |
| Indicador de severidad SAPS           | Numérica entera         |
| Indicador de severidad SOFA           | Numérica entera         |
| Tiempo en ventilación mecánica        | Numérica continua       |
| Fallecimiento en hospital             | Binaria                 |
| Cantidad de procedimientos realizados | Numéria entera          |

### Servicio médico

Se trata de una variable categórica que indica el servicio médico más relevante por el cual es atendido el paciente en la estáncia hospitalaria. Debido a que en numerosas ocasiones un paciente permanece en más de un servicio durante su estáncia, es necesario una función de preprocesado que extraiga el servicio de mayor importancia en función de un criterio. 

En concreto, se ha diseñado una función que utiliza la siguiente prioridad para extraer un único servicio para cada estáncia hospitalaria.

* Servicios de cirugía especializada 
* Servicio de cirugía general
* Servicio especializado
* Servicio de medicina general

De esta forma, un paciente admitido en el servicio de medicina general y posteriormente trasladado al servicio de cirugía cardíaca, constará como un paciente tratado bajo el servicio de cirugía cardíaca únicamente, por ejemplo. Esto permite reducir la complejidad de la variable y obtener la información de mayor relevancia. Tras aplicar este preprocesado, se obtienen las siguientes categorías y recuentos.  

| Servicio médico | Significado                  | Cantidad |
| --------------- | ---------------------------- | -------- |
| MED             | Medicina general             | 17260    |
| NB              | Neonatos                     | 7806     |
| CSURG           | Cirugía cardíaca             | 7697     |
| CMED            | Cardiología                  | 5860     |
| SURG            | Cirugía general              | 5034     |
| NSURG           | Cirugía neurológica          | 4024     |
| TRAUM           | Traumatología                | 2699     |
| NMED            | Neurología                   | 2324     |
| OMED            | Obstetricia                  | 1475     |
| VSURG           | Cirugía vascular no cardíaca | 1371     |
| TSURG           | Cirugía torácia              | 1281     |
| ORTHO           | Ortopédia                    | 739      |
| GU              | Urología                     | 334      |
| PSURG           | Cirugía plástica             | 269      |
| GYN             | Ginecología                  | 206      |

### Grupo de diagnóstico ICD9

ICD-9 és el acrónimo de "International Statistical Classification of Diseases and Related Health Problems 9th Revision", publicado por la Organización Mundial de la Salud en 1977. 

Se emplean para clasificar y codificar las patólogias, lesiones, síntomas, circustancias sociales y causas externas de enfermedades, con el fin de recopilar información sanitaria útil relacionada con defunciones, enfermedades y traumatismos. 

Estos códigos se dividen en capítulos, secciones, categorías, subcategorías y subclasificaciones, por ejemplo:

- Códigos 390 – 459: Enfermededades del sistema circulatorio

- - Enfermedades cerebrovasculadres (430-438)

  - - Oclusión  de arterias cerebrales (434)

    - - Embolia cerebral (434.1)

      - - Embolia cerebral con infarto cerebral (434.1.1)

La versión mas actual es la ICD-10, que se desarrolló en 1992, aunque en la base de datos MIMIC III v1.4 se recoge la versión anterior, la ICD-9. Actualmente, se esta realizando la transición generalizada a nivel mundial del estándar ICD – 9 a ICD – 10. 

Debido a la gran variedad de códigos y al desbalance de clases de cada código específico, se emplea únicamente el código primario ICD – 9, tal y como se recogen en el siguiente listado:

- Codigos 001 – 139: Enfermedades infecciosas y parasitarias
- Códigos 140 – 239: Neoplasias
- Códigos 240 - 279 : Enfermedades endocrinas, de la nutricion y metabolicas y      trastornos de la inmunidad
- Códigos 280 – 289: Enfermedades de la sangre y de los órganos hematopoyéticos
- Códigos 290 – 319: Trastornos mentales
- Códigos 320 – 389: Enfermedades del sistema nervioso y de los órganos de los sentidos
- Códigos 390 – 459: Enfermedades del sistema circulatorio
- Códigos 460 – 519: Enfermedades del aparato respiratorio
- Códigos 520 – 579: Enfermedades del aparato digestivo
- Códigos 580 – 629: Enfermedades del aparato genitourinario
- Códigos 630 – 679: Complicaciones del embarazo, parto y puerperio
- Códigos 680 – 709: Enfermedades de la piel y del tejido subcutáneo
- Códigos 710 – 739:  Enfermedades del sistema      osteo-mioarticular y tejido conjuntivo
- Códigos 740 – 759: Anomalías congénitas
- Códigos 760 – 779: Ciertas enfermedades con origen en el periodo perinatal
- Códigos 780 – 799: Síntomas, signos y estados mal definidos
- Códigos 800 – 999: Lesiones y envenenamientos
- Códigos E y V: Causas externas de lesiones y clasificación suplementaria. 

Mediante la siguiente consulta obtenemos el código ICD-9 de mayor prioridad para cada admisión, indicado por seq_num = 1. 

```sql
SELECT hadm_id, diagnoses_icd.icd9_code
FROM diagnoses_icd  
INNER JOIN d_icd_diagnoses 
ON diagnoses_icd.icd9_code = d_icd_diagnoses.icd9_code 
WHERE seq_num = 1
```

Es necesaria una función de filtrado que convierta el código ICD-9 específico a su clasificación mayor en función de su número de código, lo cual se realizará en la etapa de preprocesado.

### Grupo de código ICD-9-CM de Procedimiento

De forma análoga a los códigos ICD-9 de diagnóstico, se presenta un subconjunto de códigos ICD-9 de procedimiento, los cuales permiten clasificar los procedimientos médicos realizados sobre cada paciente durante su estancia hospitalaria. Se emplean principalmente en la facturación de los servicios médicos. De la misma forma que con los códigos de diagnóstico, recopilaremos el código ICD-9 de procedimiento más relevante para cada admisión.

* Procedimientos e intervenciones no clasificados bajo otros conceptos (00-00)
* Operaciones sobre el sistema nervioso (01-05)
* Operaciones sobre el sistema endocrino (06-07)
* Operaciones sobre el ojo (08-16)
* Otros procedimientos diagnósticos y terapéuticos diversos (17-17)
* Operaciones sobre el oído (18-20)
* Operaciones sobre la nariz, boca y faringe (21-29)
* Operaciones sobre el aparato respiratorio (30-34)
* Operaciones sobre el aparato cardiovascular (35-39)
* Operaciones sobre el sistema hemático y linfático (40-41)
* Operaciones sobre el aparato digestivo (42-54)
* Operaciones sobre el aparato urinario (55-59)
* Operaciones sobre órganos genitales masculinos (60-64)
* Operaciones sobre órganos genitales femeninos (65-71)
* Procedimientos obstétricos (72-75)
* Operaciones sobre el aparato musculoesquelético (76-84)
* Operaciones sobre el aparato tegumentario (85-86)
* Procedimientos diagnósticos y terapéuticos misceláneos (87-99)

Utilizaremos una consulta a base de datos similar a la empleada para los  códigos ICD-9 de diagnóstico y posteriormente preprocesaremos los códigos para transformarlos a su apartado principal. 

```sql
SELECT hadm_id, procedures_icd.icd9_code 
FROM procedures_icd 
INNER JOIN d_icd_procedures 
ON procedures_icd.icd9_code = d_icd_procedures.icd9_code 
AND seq_num = 1
```

*** FALTA HACER ESTO, que se me ha olvidado ***

### Realización de cirugía

Para detectar si se han realizado intervenciones quirúrgicas en un paciente durante su estancia hospitalaria emplearemos los indicadores de cirugía, (Surgery Flags), proporcionados por el HCUP, Healthcare Cost and Utilization Project, una iniciativa financiada por el gobierno estadounidense mediante la ‘Agency for Healthcare Research and Quality’ (AHRQ) dedicada a la gestión y análisis de datos médicos. 

Esta entidad proporciona herramientas para identificar intervenciones y eventos quirúrgicos  mediante códigos ICD-9 de procemiento o códigos CPT (Current Procedural Terminology) , ambos presentes en la base de datos MIMIC-III v.1.4. 

Permite la clasificación de procedimientos en tres grupos:

- NARROW: Procedimientos quirúrgicos terapéuticos invasivos requiriendo incisión, extirpación, manipulación o suturado de tejido que penetra o atraviesa la piel, típicamente se realiza  en quirófano y con anestesia local o general o sedación.
- BROAD: Procedimientos quirúrgicos que no se pueden clasificar como aquellos incluidos en el indicador NARROW,  pero se realizan bajo condiciones quirúrgicas. Este grupo incluye      procedimientos quirúrgicos de diagnóstico, como procedimientos endoscópicos o percutáneos, o aquellos realizados a través de orificios  naturales. Se trata de intervenciones menos invasivas.
- NEITHER: Procedimientos no registrado como NARROW o BROAD, es decir, procedimientos no quirúrgicos. 

Esta clasificación se distribuye en forma de archivo CSV y mediante Python se diseña una función para devolver la clasificación del procedimiento.

Debido a que unicamente se clasifican un 4% de registros como BROAD, se decide incluir estos dentro de NARROW con el fin de evitar clases desproporcionadas, dando lugar a una variable binaria con la siguiente distribución.

| Indicador de cirugía | Recuento | Porcentaje |
| :------------------: | :------: | :--------: |
|        Narrow        |  29867   |    56%     |
|      No Surgery      |  23043   |    44%     |

### Duración de estancia en UCI

De la base de datos es posible extraer directamente la duración de estancia en UCI en dias para cada paciente en una misma admisión hospitalaria. Esta información se haya en la tabla ICUSTAYS y la obtenemos mediante la siguiente consulta. 

```sql
SELECT hadm_id, 
sum(los) AS total_icu_time 
FROM icustays
GROUP BY hadm_id
```

Es necesario emplear la función agregada de suma en la consulta debido a que en ciertas ocasiones un paciente ingresa en la UCI, es transferido a otra sección y posteriormente regresa a la UCI, con lo cual se registran distintas duraciones para una misma estancia. De esta forma, obtenemos una variable continua, a la cual no aplicamos preprocesado.

### Duración de estáncia hospitalaria

Obtenemos la duración de estáncia hospitalaria, incluyendo la duración en UCI, como la diferencia entre el tiempo de admisión y de alta. Para ello empleamos la función EXTRACT y epoch, propias de PostgreSQL.

```sql
SELECT hadm_id, 
EXTRACT(epoch FROM(dischtime - admittime))/(3600*24) AS total_los_days
FROM admissions
```

Esta variable se mide también en dias y no requiere preprocesado. 

### Recuento de admisiones

Para cada admisión, indica la cantidad de estancias hospitalarias que ha realizado el mismo paciente, contando también la misma.

Esto permite identificar aquellas admisiones correspondientes a pacientes readmitidos en diversas ocasiones, lo cual puede ser indicador de sujetos con enfermedades crónicas, que requieren regularmente atención médica. 

Obtenemos esta variable mediante funciones de preprocesado sobre la tabla ADMISSIONS. 

### Recuento de procedimientos

Indica la cantidad de procedimientos, tanto quirúrgicos como no quirúrgicos, realizados a un paciente en una misma estancia hospitalaria. Se trata de una variable numérica discreta que obtenemos mediante la siguiente consulta.

```sql
SELECT hadm_id, count(*) AS procedure_count
FROM procedures_icd
GROUP BY hadm_id
```

Esta variable no requiere de preprocesado. 

### Indicadores de severidad

Distintos indicadores de severidad han sido desarrollados con el objetivo y predecir la mortalidad hospitalaria a partir de la información de los pacientes, en particular de las medidas tomadas durante las primeras 24h horas de su ingreso. Sin embargo, presentan ciertas limitaciones, por ejemplo al depender de medidas subjetivas tomadas por el personal médico o al emplear relaciones lineales que no se adaptan a la realidad. 

Utilizaremos como variables predictoras los indicadores SOFA, SAPS y OASIS, los cuales obtendremos mediante la siguiente consulta:

```sql
SELECT o.hadm_id, 
AVG(o.oasis) AS oasis_avg, 
AVG(so.sofa) AS sofa_avg, 
AVG(sa.saps) as saps_avg
FROM oasis o
INNER JOIN sofa so
ON o.hadm_id = so.hadm_id
INNER JOIN saps sa
ON sa.hadm_id = so.hadm_id
GROUP BY o.hadm_id
```

Para obtener estos indicadores, utilizamos scripts del repositorio de código oficial de MIMIC-III. [https://github.com/MIT-LCP/mimic-code/tree/master/concepts/severityscores]. De esta manera, creamos vistas materializadas que contienen los indicadores de severidad precalculados para cada admision hospitalaria.

#### SOFA

“Sequential Organ Failure Assessment score”. Creado en 1994 por la European Society of Intensive Medicine (ESICM), este indicador fue desarrollado para evaluar la severidad de la enfermedad del paciente, basada en el grado de fallo orgánico de seis órganos. En concreto, se toman las siguientes medidas.

- Sistema respiratorio:

- - PaO2
  - Presencia de ventilación mecánica

- Sistema nervioso:

- - Glasgow Coma Scale. 

- Sistema cardiovascular:

- - Presión arterial media
  - Nivel de dopamina
  - Nvel de Epinefrina
  - Nivel de norepinefrina

- Hígado:

- - Nivel de bilirrubina

- Coagulación:

- - Nivel de plaquetas

- Renal:

- - Nivel de creatinina
  - Volumen de orina

Los resultados de estas pruebas otorgan puntuaciones entre 0 y 4, que posteriormente se suman para obtener la puntuación SOFA total. Permite obtener una idea aproximada de la mortalidad del paciente, de manera sencilla y directa de calcular a partir de solamente once variables básicas. 

#### SAPS

Simplified Acute Physiology Score. Creado en 1993 por Le Gall y Lemenshow Saulnier, se emplea para medir la severidad de la enfermedad de los paciente admitidos en unidad de cuidados intensivos de edad mayor a 15 años. Se completa 24h tras el ingreso y otorga una puntuación de entre 0 y 163, además de la mortalidad predecida en porcentaje. Se calcula a partir de 12 medidas fisiológicas básicas, la edad del paciente y el tipo de admisión. 

El resultado de SAPS es mejor empleado para contrastar la gravedad de grupos de pacientes con patologías distintas, más que a nivel individual, debido a que sus resultados pueden ser poco precisos a nivel de paciente. 

#### OASIS

OASIS, Oxford Acute Severity of Illness Score, se trata de un indicador de severidad diseñado en 2013 por Johnson AE1, Kramer AA, Clifford GD, de la Universidad de Oxford. Se caracteriza por emplear técnicas de aprendizaje automático, en concreto optimización por enjambre de partículas, y por no requerir un gran trabajo de recolección de información, ya que requiere unicamente diez características, excluyendo medidas de laboratorio, o informacion sobre diagnósticos y comorbilidades.

### Tiempo en ventilación mecánica

Empleando de nuevo una vista materializada disponible en el repositorio de código de MIMIC-III, obtenemos el tiempo que pasa cada paciente en ventilación mecánica durante su estáncia hospitalaria. Utilizamos la siguiente consulta sobre la vista VENTDURATIONS.

```sql
SELECT hadm_id, SUM(duration_hours) AS total_mech_vent_time
FROM ventdurations v
INNER JOIN icustays i
ON v.icustay_id = i.icustay_id
GROUP BY hadm_id
```

En ocasiones, un paciente pasa un tiempo conectado al ventilador mecánico, es desconectado, y conectado de nuevo posteriormente. Es por ello que la vista materializada registra en ocasiones diversas entradas para una misma estancia en UCI, con lo cual es conveniente calcular la suma de duraciones para una estancia.