# Resumen

Según la OMS, un destino médico es un cambio en el estado de salud de un invididuo, colectivo, o población, atribuible a intervenciones determinadas. La predicción de destinos médicos es una rama de la investigación médica que estudia el resultado final de la estructura y procesos del sistema médico en la salud y el bienestar de pacientes y poblaciones. Es un pilar importante en la toma de decisiones y en análisis de políticas y procedimientos, ya que permite la evaluación de la calidad del cuidado médico, su eficiencia y efectividad. Su objetivo es identificar fallos en la práctica médica que afectan a la salud del paciente y desarrollar estrategias que mejoren el cuidado. Para ello, mide eventos tangibles experimentados por el paciente, tales como la mortalidad, la readmisión o la morbilidad. El resultado de la investigación sobre destinos médicos se utiliza para informar a los cuerpos legistlativos que toman decisiones realacionadas con la sanidad, así como a órganos financieros, tales como el gobierno o compañias aseguradoras, que buscan minimizar costes médicos proporcionando un cuidado médico adecuado. La recolecta estandarizada de estadísticas y datos médicos acerca del cuidado médico que reciben los pacientes ha permitido que los registros médicos puedan ser empleados como una fuente fiable para la investigación.

Uno de los destinos médicos más relevantes es la mortalidad extrahospitalaria de los pacientes, es decir el tiempo hasta su defunción tras el alta hospitalaria. El objetivo de este estudio es la predicción de esta variables mediante redes neuronales artificiales. En concreto, se trata de una tarea de la predicción clasificatoria en tres franjas temporales (0 - 1 meses, 1 - 12 meses, 12+ meses). Para ello se emplean un total de 43 variables predictorias, incluyendo información demográfica, señales fisiológicas, resultados de pruebas de laboratorio y otras variables relacionadas con la estáncia hospitalaria de los pacientes. Obtenemos la información necesaria de la base de datos pública MIMIC-III v1.4, correspondiente a los ingresos hospitalarios en unidad de cuidados intensivos en el hospital Beth Israel Deaconess Medical Center, en Boston, Massachussets, EE.UU. Se trata de un conjunto de datos que contiene información médica deideintificada sobre más de 40.000 pacientes críticos entre los años 2001 y 2012. De esta forma, diseñaremos una red neuronal capaz de predecir satisfactoriamente la mortalidad extrahospitalaria de los pacientes en función de estas variables.

Palabras clave: *Redes Neuronales Artificiales*, *minería de datos*, *Inteligencia artificial* , *Predicción de mortalidad*, *aprendizaje profundo*, *Unidad de cuidados intensivos*

# Abstract

According to WHO, a medical outcome is a change in the health status of an individual, group, or population, attributable to certain causes. The prediction of medical outcomes is a branch of medical research that studies the final result of the structure and processes of the medical system in the health and well-being of patients and populations. It is an important factor in decision making and analysis of policies and procedures, since it allows the evaluation of the quality of medical care, its efficiency and effectiveness. Its objective is to identify faults in medical practice that affect the health of the patient and the development of strategies that improve care. To do this, it measures tangible events experienced by the patient, stories such as mortality, readmission or morbidity. The result of the research on medical destinations is used to inform the legal bodies that make decisions related to health, as well as financial entities, such as the government or insurance companies, that seek to minimize costs whilst providing adequate medical care. Routine collection statistics and medical data related to patient care that patients have allowed medical records to be used as a reliable source inresearch.

One of the most relevant medical outcomes is out-of-hospital mortality of patients, that is, the time until their death after hospital discharge. The objective of this study is the prediction of this outcome through artificial neural networks. Specifically, it is a classificatory prediction task in three time intervals (0 - 1 months, 1 - 12 months, 12+ months). For this, a total of 43 predictor variables are used, including demographic information, physiological signals, results of laboratory tests and other variables related to the hospital stay of patients. Data is obtained from the public database MIMIC-III v1.4, corresponding to hospital admissions in the intensive care unit at Beth Israel Deaconess Medical Center, in Boston, Massachusetts, USA. It is a set of data that contains medical information of more than 40,000 critical patients between 2001 and 2012. In this way, we will design an artificial neural network capable of satisfactorily predicting out-of-hospital mortality of patients based on these variables.

Key Words: *Artificial Neural Networks*, *Data mining*, *Artificial Intelligence* , *Mortality prediction*, *Deep Learning*, *Intensive Care Unit*

# Introducción

La inteligencia artificial es un campo relativamente reciente con múltiples aplicaciones en diversos ámbitos, entre ellos la medicina. Se trata de la habilidad de los algoritmos de computación de aproximar conclusiones sin itervención humana. El objetivo principal de la aplicación de la inteligencia artificial a la medicina es analizar las relaciones entre las técnicas de prevención o tratamientos y su resultado sobre los pacientes. Actualmente, se han desarrollado soluciones para diversos problemas en procesos de diagnóstico, desarrollo de medicamentos, medicina personalizada, tratamiento y  monitor de pacientes, etc. Grandes compañias como IBM y Google también han desarrollado algoritmos de inteligencia artificial para el sector de la sanidad. Es un campo en constante expansión, con investigación constante y grandes promesas de futuro. 

## Objetivos y alcance

El objetivo principal es el desarrollo y la implementación de un modelo predictivo clasificatorio basado en redes neuronales artificiales capaz de predecir la mortalidad extra-hospitalaria de pacientes críticos. Se desea que este modelo presente un AUROC superior al 0.80, indicando así buena capacidad diagnóstica. 

Para ello, se pretende emplear el lenguaje de programación Python, en su versión 3.6. Se ha decidido emplear este lenguaje por poseer experiencia anterior en su uso, además de existir una gran comunidad dedicada a su uso en análisis y minería de datos, junto con potentes librerías y amplio soporte. 

En cuanto a la estructura del código, se desea emplear una arquitectura basada en microservicios, con funciones compartimentalizadas y facilmente reutilizables. Se estructurará el código en clases y se emplearan archivos auxiliares que serán referidos por otros. 

Queda fuera del alcance de este documento la interpretación detallada de ciertos conceptos matemáticos altamente complejos, tales como ciertos algoritmos de optimización, o el análisis de patologías o situaciones médicas y sus efectos sobre la mortalidad de los pacientes. 

# Redes neuronales artificiales

## Descripción del conjunto de datos

MIMIC-III ("Medical information Mart for Intensive Care") es una base de datos correspondiente a los ingresos hospitalarios en unidad de cuidados intensivos en el hospital Beth Israel Deaconess Medical Center, en Boston, Massachussets, EE.UU. Incluye información relativa a los signos vitales de los pacientes, medicación, medidas de laboratorio, observaciones y notas tomadas por el personal médico, balance de fluidos, códigos de procedimientos, códigos de diagnósticos, reportes de imágenes médicas, duración de la estancia hospitalaria y datos de la supervivencia de los pacientes, entre otros. Estos datos se encuentran deidentificados y són de ámbito público para el uso académico.

Es la única base de datos libremente accesible de este tipo. Además, destaca por su gran cantidad de registros, obtenidos a lo largo de más de una década, concretamente entre los años 2001 y 2012 

Contiene datos asociados con 53423 admisiones hospitalarias para pacientes adultos mayores de 16 años en unidad de cuidados intensivos entre 2001 y 2012. Así mismo, contiene información sobre 7870 neonatos admitidos entre 2001 y 2008. La mediana de edad de los pacientes es de 65.8 años, el 55.9% de los pacientes son hombres y la mortalidad hospitalaria es del 11.5%. La duración mediana de una estáncia en la unidad de cuidados intensivos es de 2.1 dias y la mediana de duración en el hospital es de 6.9 dias. 

Contiene tipos variados de datos, desde medidas fisiológicas realizadas por el personal médico, hasta interpretaciones textuales de imágenes médicas provenientes del departamento de radiología. 

Como sistemas de monitorización y recogida de datos, se emplearon dos dispositivos: Philips CareVue Clinical Information System (M2331A y M1215A) y iMDsoft MetaVision ICU. Estos dispositivos fueron la fuente de diversos datos clínicos, tales como medidas fisiológicas como el ritmo cardíaco, la presión arterial o el ritmo respiratorio, notas acerca del progreso de los pacientes o suministro de medicamentos. MIMIC - III fusiona los datos provenientes de los dos dispositivos en los casos en que es posible. 

Informació adicional fue recopilada de los sistemas de registro hospitalarios, principalmente datos relativos a la demografia de los pacientes y la mortalidad hospitalaria, resultados de test de laboratorios, reportes sobre electrocardiogramas y imágenes médicas, y códigos de diagnóstico y de procedimientos. Así mismo, se recopila información acerca de la mortalidad extra-hospitalaria a partir de los archivos de la seguridad social estadounidense. 

### Deidentifación, privacidad y condiciones de acceso

Todos los ficheros fueron deidentifacos antes de ser introducidos en MIMIC-III, de acuerdo la normativa estadounidense vigente, "Health Insurance Portability and Accountability Act (HIPAA)". Para ello, se eliminó toda la información que permitia identificar los pacientes, tal cómo el número de teléfono, nombre, dirección, etc. 

En cuanto a las fechas, fueron desplazadas en el futuro de forma aleatoria de manera consistente para cada individuo, resultando en estancias que ocurren entre el año 2100 y 2200. Sin embargo, la hora, dia de la semana y estación fueron conservadas en este proceso de modifcación de fechas. 

Así mismo, la edad de los pacientes mayores a 89 años fue enmascarada para preservar su intimidad según la regulación vigente. Es por ello que aparecen con edades superiores a 300 años. 

Para acceder a la base de datos es necesario realizar un proceso consistente en completar un curso reconocido sobre la protección de datos de los participantes en el estudio, acorde con las regulaciones del HIPPA, y firmar un acuerdo de uso, el cual delimita un uso adecuado de la información y estándares de seguridad, además de prohibir expresamente la identifación de los usuarios. El proceso requiere alrededor de una semana y se realiza por internet. 

En concreto, se debe realizar el curso  ‘Data or Specimens Only Research’ proprcionado por el Massachusetts Institute of Technology  a través del Programa CITI, Collaborative Institutional Training Initiative.  

Una vez completado se recibe un certificado de finalización, el cual debe ser enviado a los administradores de MIMIC-III con tal de obtener las claves de acceso necesarias.

Una vez hecho este proceso, la información se obtiene como una colección de CSVs, junto con scripts para importarlos en bases de datos. En la web oficial de mimic (<https://mimic.physionet.org>) se encuentran los pasos y los scripts necesarios para cargar los archivos en una base de datos local en PostgreSQL, así como para la creación de índices de búsqueda. 

### Tablas

La base de datos comprende un total de 26, las cuales se detallan a continuación:

- ADMISSIONS: Define la admisión hospitalaria de cada paciente, identificando cada una con un ID, HADM_ID. Contiene **58976** registros.  La información proviene de la base de datos del hospital. Así mismo, contiene algunas entradas relativas a la donación de órganos de pacientes fallecidos en el hospital.

- CALLOUT: Esta tabla contiene información de pacientes listos para ser dados de alta de la UCI. Cuando esto ocure, se dice que un paciente está ‘Called out’. Esta información no está disponible para todos los pacientes, ya que se empezó a recolectar después del inicio de creación de la base de datos. Así mismo, por motivos no especificados, no se incluyen entradas relativas a neonatos. Contiene 34499 registros. 

  Cuando un paciente está listo para ser dado de alta de la UCI, el personal médico encargado crea una petición de ‘call out’, la cual es posteriormente admitida. Posteriormente es transferido fuera de la UCI.

- CAREGIVERS: Esta tabla proporciona información acerca del personal médico y sus intervenciones sobre los pacientes. Contiene 7567 registros y proviene de la base de datos de los dispositivos de monitorización CareVue y Metavision. 

- CHARTEVENTS: Esta tabla contiene información relativa a los pacientes durante su estancia en la unidad de cuidados intensivos, tal como sus signos vitales, e información relevante asociada a su cuidado, como los ajustes de ventilación mecánica, pruebas de laboratorio, estado mental, etc. Contiene ciertos valores repetidos con la tabla LABEVENTS, que fueron incluidos por el personal médico con el objetivo de unificar la información en una sola tabla. En caso de discrepancias entre los valores, se toman como correctos los de la tabla LABEVENTS. Contiene alrededor de 330.000 registros.

- CPTEVENTS: Esta tabla contiene CPT (Current Procedural Terminology), códigos que identifican los procedimientos llevados a cabo en cada paciente. Se emplean principalmente para facturación. 

- D_CPT: Contiene definiciones generales, poco detalladas, de códigos CPT empleados en la tabla CPTEVENTS. Se trata de una tabla auxiliar que no presenta una relación única con las entradas de CPT, cada entrada de D_CPT se corresponde con un rango de códigos. De esta manera, múltiples códigos CPT pueden compartir la misma descripción, al tratarse de procedimientos similares. 

- D_ICD: Esta tabla contiene la relación de códigos de diagnósticos y su descripción acorde al estándar “International Coding Definitions Version 9” (ICD-9). Son asignados al finalizar la estancia del paciente y se emplean en facturación. Contiene 14567 registros, cada uno correspondiente a un código de diagnóstico distinto.

- D_ICD_PROCEDURES: Similar a la tabla D_ICD_DIAGNOSES, contiene las descripciones de los códigos de procedimiento acorde al estándar ICD-9.

- D_ITEMS: Contiene la descripción de todos los elementos almacenados como “ITEMS”. Cada 

  Proviene de la base de datos de los dispositivos de monitorización Philips CareVue y Metavision. Se debe tener en cuenta que es posible hayar elementos duplicados, al encontrarse repetidos en ambas bases de datos, así como debido a la introducción manual de texto y diferencias en ortografía o puntuación. Los ITEMIDs provenientes del dispositivo Metavision son superiores a 220000.

- D_LABITEMS: Esta tabla proviene de la base de datos del hospital y contiene definiciones para todos los ITEMID asociados a medidas de laboratorio. Se indica que la información contenida en esta tabla es consistente, sin duplicados presentes. Se relaciona externamente con la base de datos LOINC, la cual presenta un estándar universal para la codificación de registros médicos. 

- DATETIMEEVENTS: Contiene el registro de fechas y horas de eventos relacionados con un paciente en la ICU. Para proteger la identidad de los pacientes, las fechas han sido desplazadas en el tiempo, de manera consistente al resto de datos, manteniendo así la cronología de los pacientes. 

- DIAGNOSES_ICD: Contiene los diagnósticos de los pacientes codificados mediante el estándar ICD-9. Se asignan con propósitos de facturación al finalizar la estancia hospitalaria de cada paciente. 

- DRGCODES: Contiene códigos de grupos de diagnósticos relacionados (DRG, ‘Diagnosis related groups’), para los pacientes.

- ICUSTAYS: Define cada estancia en unidad de cuidados intensivos. Es una tabla derivada del agrupamiento de la tabla TRANSFERS por ICUSTAY_ID

- INPUTEVENTS_CV: Proviene de la base de datos del sistema de
  monitorización Philips CareVue y contiene información acerca de fluidos
  administrados al paciente, como tubos de alimentación o soluciones
  intravenosas. 

- INPUTEVENTS_MV: Tabla análoga a INPUTEVENTS_CV, conteniendo los fármacos subministrados al paciente registrados por MetaVision.

- LABEVENTS: Contiene todas las medidas de laboratorio para un paciente dado, incluso aquellas tomadas en clínicas externas. Estas últimas no disponen de un identificador de admisión hospitalaria, al no haber sido tomadas en el hospital.

- MICROBIOLOGYEVENTS: Contiene registros de microbiología, entre ellos tests realizados y sensibilidades a distintas cepas de bacterias y virus, de pacientes en la UCI. 

- NOTEEVENTS: Contiene notas de texto acerca de los
  pacientes tomadas por el personal médico. Destaca información acerca del
  historial clínico de los pacientes, así como intepretaciones textuales de
  distintas pruebas, informes y notas de enfermería  o indicaciones a seguir tras el alta y
  medicaciones recetadas. 

- OUTPUTEVENTS: Contiene medidas sobre fluidos excretados por el paciente durante su estancia hositalaria, tales como orina, sangre, esputo, etc. 

- TRANSFERS: Contiene la localización de los pacientes a lo
  largo de su estancia hospitalaria. De esta tabla se deriva la tabla ICUSTAYS. 

- PATIENTS:Contiene información acerca de los pacientes, tal como su sexo, fecha de nacimiento, o de fallecimiento, dónde aplica. En aquellos pacientes de edad mayor a 89 años, se ha modificado su fecha de nacimiento, haciéndola constar como 300 años anterior a la fecha de primera admisión. Esta modificación se realiza para cumplir con la normativa de protección de datos estadounidense (HIPAA).  La mediana de edad para estos pacientes es de 91.4 años. 

- PRESCRIPTION: Contiene prescripciones de fármacos recetados a los pacientes e información relativa a su suministro: duracion, dosis, ratio, etc.

- PROCEDUREEVENTS_MV: Contiene información acerca de procedimientos
  médicos realizados en pacientes durante su estancia hospitalaria.

- SERVICES: Esta tabla describe los servicios bajo los que
  cada paciente fue admitido durante su estancia, que puede diferir del tipo de
  unidad de cuidados intensivos en que se aloja debido a diversos motivos, como
  por ejemplo falta de camas. Los servicios se almacenan empleando sus abreviaciones segun la tabla siguiente:

| Servicio | Significado             | Descripción                                        |
| -------- | ----------------------- | -------------------------------------------------- |
| CMED     | Cardiac Medical         | Admisiones   no-quirúrgicas por motivos cardíacos  |
| CSURG    | Cardiac Surgery         | Admisiones   quirúrgicas por motivos cardiacos     |
| DENT     | Dental                  | Admisiones dentales                                |
| ENT      | Ear, nose, throat       | Admisiones de   otorrinolaringología               |
| GU       | Genitourinary           | Admisiones   genitourinarias                       |
| GYN      | Gynecological           | Admisiones   ginecológicas                         |
| MED      | Medical                 | Admisiones generales                               |
| NB       | Newborn                 | Neonátos                                           |
| NBB      | Newborn Baby            | Neónatos                                           |
| NMED     | Neurological Medical    | Admisiones   neurológicas no quirúrgicas           |
| NSURG    | Neurological   Surgical | Admisiones   neurológicas quirúrgicas              |
| OBS      | Obstetrics              | Admisiones de   obstetricia                        |
| ORTHO    | Orthopaedic             | Admisiones   quirúrgicas de ortopedia              |
| OMED     | Orthopaedic medicine    | Admisiones no   quirúrgicas de ortopedia           |
| PSURG    | Plastic                 | Admisiones de   cirugía plásticas / reconstructiva |
| PSYCH    | Psychiatric             | Admisiones de   psiquiatría                        |
| SURG     | Surgical                | Admisiones de   cirugía general                    |
| TRAUM    | Trauma                  | Admisiones de   traumatología                      |
| TSURG    | Thoracic Surgical       | Admisiones de   cirugía torácica                   |
| VSURG    | Vascular Surgical       | Admisiones de   cirugía vascular no cardíacas      |

## Variable a predecir: mortalidad extra-hospitalaria

Obtenemos los grupos de esta variable a partir de la unión de las tablas ADMISSIONS y PATIENTS. En concreto, se extrae el periodo de tiempo en meses entre la fecha de alta del paciente, procedente de la tabla ADMISSIONS, y la fecha de fallecimiento del paciente, contenida en la tabla PATIENTS. En los casos en que el paciente no fallece en el hospital, esta fecha procede de la base de datos de la seguridad social estadounidense. En la base de datos, esta variable se distribuye de la siguiente forma:

![](C:\mimic-iii-project\plots\Labels\expire_days.png)



| Descriptor estadístico  | Valor           |
| ----------------------- | --------------- |
| Recuento                | 16548 registros |
| Media aritmética (μ)    | 708 dias        |
| Desviación estándar (σ) | 820 dias        |
| Valor mínimo            | 0.5 dias        |
| Percentil 25%           | 88 dias         |
| Percentil 50%           | 374 dias        |
| Percentil 75%           | 1067 dias       |
| Valor máximo            | 4327 dias       |

Se clasifican los pacientes en los siguientes tres grupos, de forma expresa para evitar clases descompensadas que dificulten la predicción posterior. 

| Mortalidad | Cantidad | Porcentaje |
| ---------- | -------- | ---------- |
| 12+ meses  | 8391     | 37 %       |
| 1-12 meses | 6095     | 27 %       |
| < 1 mes    | 8100     | 36 %       |

Para ello, empleamos la siguiente consulta, la cual aplica directamente la clasificación en grupos mediante una sentencia CASE en SQL. 

```sql
SELECT hadm_id,
	CASE
		WHEN
    		EXTRACT(epoch FROM (dod-dischtime))/(3600*24*30) > 12 
    	THEN '12+ months'
    	WHEN 
    		EXTRACT(epoch FROM (dod-dischtime))/(3600*24*30) < 12 AND
     		EXTRACT(epoch FROM (dod-dischtime))/(3600*24*30) >= 1

    	THEN '1-12 months'
    									
   		WHEN
    		EXTRACT(epoch FROM (dod-dischtime))/(3600*24*30) < 1 AND
    		EXTRACT(epoch FROM (dod-dischtime))/(3600*24*30) > -0.5
    	THEN '0-1 months'	
    									
    END
AS mortality
FROM admissions a
INNER JOIN patients p
ON a.subject_id = p.subject_id
```

Observamos que las clases se encuentran aproximadamente compensadas, lo cual permitirá un diseño eficaz de red neuronal y su posterior evaluación. 

## Variables predictorias

Tras leer biblografía, se recopilan una serie de variables que se consideran determinantes a la hora de determinar el tiempo de supervivencia tras el alta de la admisión hospitalaria: 

Las variables recopiladas se extraen a partir de consultas a la base de datos y en algunos casos al preprocesamiento de estas. 

### Información demográfica

Se recopilan cinco variables de índole demográfica: Edad, sexo, estado civil, religión y etnicidad. Estas variables se extraen directamente de la tabla ADMISSIONS, excepto la edad, que se calcula a partir de la diferencia de tiempo entre la fecha de nacimiento, almacenada en la tabla PATIENTS, y la fecha de admisión hospitalaria, procedente de la tabla ADMISSIONS. 

#### Edad

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

#### Sexo

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

#### Estado civil

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

#### Religion

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

#### Etnicidad

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

### Pruebas de laboratorio

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

### Señales fisológicas

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

### Información hospitalaria

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

#### Servicio médico

Se trata de una variable categórica que indica el servicio médico más relevante por el cual es atendido el paciente en la estáncia hospitalaria. Debido a que en numerosas ocasiones un paciente permanece en más de un servicio durante su estáncia, es necesario una función de preprocesado que extraiga el servicio de mayor importancia en función de un criterio. 

En concreto, se ha diseñado una función que utiliza la siguiente prioridad para extraer un único servicio para cada estáncia hospitalaria.

- Servicios de cirugía especializada 
- Servicio de cirugía general
- Servicio especializado
- Servicio de medicina general

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

#### Grupo de diagnóstico ICD9

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

#### Grupo de código ICD-9-CM de Procedimiento

De forma análoga a los códigos ICD-9 de diagnóstico, se presenta un subconjunto de códigos ICD-9 de procedimiento, los cuales permiten clasificar los procedimientos médicos realizados sobre cada paciente durante su estancia hospitalaria. Se emplean principalmente en la facturación de los servicios médicos. De la misma forma que con los códigos de diagnóstico, recopilaremos el código ICD-9 de procedimiento más relevante para cada admisión.

- Procedimientos e intervenciones no clasificados bajo otros conceptos (00-00)
- Operaciones sobre el sistema nervioso (01-05)
- Operaciones sobre el sistema endocrino (06-07)
- Operaciones sobre el ojo (08-16)
- Otros procedimientos diagnósticos y terapéuticos diversos (17-17)
- Operaciones sobre el oído (18-20)
- Operaciones sobre la nariz, boca y faringe (21-29)
- Operaciones sobre el aparato respiratorio (30-34)
- Operaciones sobre el aparato cardiovascular (35-39)
- Operaciones sobre el sistema hemático y linfático (40-41)
- Operaciones sobre el aparato digestivo (42-54)
- Operaciones sobre el aparato urinario (55-59)
- Operaciones sobre órganos genitales masculinos (60-64)
- Operaciones sobre órganos genitales femeninos (65-71)
- Procedimientos obstétricos (72-75)
- Operaciones sobre el aparato musculoesquelético (76-84)
- Operaciones sobre el aparato tegumentario (85-86)
- Procedimientos diagnósticos y terapéuticos misceláneos (87-99)

Utilizaremos una consulta a base de datos similar a la empleada para los  códigos ICD-9 de diagnóstico y posteriormente preprocesaremos los códigos para transformarlos a su apartado principal. 

```sql
SELECT hadm_id, procedures_icd.icd9_code 
FROM procedures_icd 
INNER JOIN d_icd_procedures 
ON procedures_icd.icd9_code = d_icd_procedures.icd9_code 
AND seq_num = 1
```

*** FALTA HACER ESTO, que se me ha olvidado ***

#### Realización de cirugía

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

#### Duración de estancia en UCI

De la base de datos es posible extraer directamente la duración de estancia en UCI en dias para cada paciente en una misma admisión hospitalaria. Esta información se haya en la tabla ICUSTAYS y la obtenemos mediante la siguiente consulta. 

```sql
SELECT hadm_id, 
sum(los) AS total_icu_time 
FROM icustays
GROUP BY hadm_id
```

Es necesario emplear la función agregada de suma en la consulta debido a que en ciertas ocasiones un paciente ingresa en la UCI, es transferido a otra sección y posteriormente regresa a la UCI, con lo cual se registran distintas duraciones para una misma estancia. De esta forma, obtenemos una variable continua, a la cual no aplicamos preprocesado.

#### Duración de estáncia hospitalaria

Obtenemos la duración de estáncia hospitalaria, incluyendo la duración en UCI, como la diferencia entre el tiempo de admisión y de alta. Para ello empleamos la función EXTRACT y epoch, propias de PostgreSQL.

```sql
SELECT hadm_id, 
EXTRACT(epoch FROM(dischtime - admittime))/(3600*24) AS total_los_days
FROM admissions
```

Esta variable se mide también en dias y no requiere preprocesado. 

#### Recuento de admisiones

Para cada admisión, indica la cantidad de estancias hospitalarias que ha realizado el mismo paciente, contando también la misma.

Esto permite identificar aquellas admisiones correspondientes a pacientes readmitidos en diversas ocasiones, lo cual puede ser indicador de sujetos con enfermedades crónicas, que requieren regularmente atención médica. 

Obtenemos esta variable mediante funciones de preprocesado sobre la tabla ADMISSIONS. 

#### Recuento de procedimientos

Indica la cantidad de procedimientos, tanto quirúrgicos como no quirúrgicos, realizados a un paciente en una misma estancia hospitalaria. Se trata de una variable numérica discreta que obtenemos mediante la siguiente consulta.

```sql
SELECT hadm_id, count(*) AS procedure_count
FROM procedures_icd
GROUP BY hadm_id
```

Esta variable no requiere de preprocesado. 

#### Tiempo en ventilación mecánica

Empleando de nuevo una vista materializada disponible en el repositorio de código de MIMIC-III, obtenemos el tiempo que pasa cada paciente en ventilación mecánica durante su estáncia hospitalaria. Utilizamos la siguiente consulta sobre la vista VENTDURATIONS.

```sql
SELECT hadm_id, SUM(duration_hours) AS total_mech_vent_time
FROM ventdurations v
INNER JOIN icustays i
ON v.icustay_id = i.icustay_id
GROUP BY hadm_id
```

En ocasiones, un paciente pasa un tiempo conectado al ventilador mecánico, es desconectado, y conectado de nuevo posteriormente. Es por ello que la vista materializada registra en ocasiones diversas entradas para una misma estancia en UCI, con lo cual es conveniente calcular la suma de duraciones para una estancia.

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

### Escala de coma de Glasgow

Se trata de una escala neurológica diseñada para medir facilmente y de forma objetiva el estado de cosciencia de una persona. Un paciente es puntuado segun unos criterios en diversos aspectos, y la suma de puntuaciones otorga una puntuación entre 3, indicando profunda inconsciencia, y 14, indicando un estado de alerta normal.

Se emplea también como variable para calcular los indicadores de severidad OASIS, SAPS y SOFA.  Se calcula siguiendo los criterios siguientes:

| Variable             | Respuesta                                                    | Puntaje                                                      |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Apertura ocular**  | Espontánea<br />A la orden<br />Ante un estímulo doloroso<br />Ausencia de apertura ocular | 4 puntos <br />3 puntos<br />2 puntos<br />1 punto           |
| **Respuesta verbal** | Orientado correctamente<br />Paciente confuso<br />Lenguaje inapropiado<br />Lenguaje incomprensible<br />Carencia de actividad verbal | 5 puntos<br />4 puntos<br />3 puntos<br />2 puntos<br />1 punto |
| **Respuesta motora** | Obedece órdenes correctamente<br />Localiza estímulos dolorosos<br />Responde al estimulo doloroso pero no localiza<br />Respuesta con flexión anormal de los miembros<br />Respuesta con extensión anormal de los miembros<br />Ausencia de respuesta motora | 6 puntos<br />5 puntos<br />4 puntos<br />3 puntos<br />2 puntos<br />1 punto |

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

## Modelo Predictivo

Con el fin de diseñar un modelo predictivo para la mortalidad extrahospitalaria, diseñamos una red neuronal. Para ello, se utiliza la librería Keras, escrita en Python. 

Se trata de una librería de código abierto escrita en Python capaz de ejecutarse sobre Tensorflow y Theano, principales librerías en cuanto a aprendizaje automático y redes neuronales; ofreciendo una API de alto nivel, modular y extensible.

Incluye numerosas implementaciones de objetos usados comunmente en la construcción de redes neuronales artificiales, tal como capas, funciones de activación y optimizadores. 

Keras fue inicialmente desarrollado por François Chollet, ingeniero de Google, como parte de la investigación para el proyecto ONEIROS (Open-ended Neuro-Electronic Intelligent Robot Operating System) en 2016.

### Preparación de datos

Para obtener un rendmiento óptimo de la red neuronal, los datos de entrada deben ser tratados. Principalmente, deben tratarse los datos faltantes, normalizar las variables numéricas para que se encuentren en rangos similares, y deconstruir las variables categóricas en variables binarias para cada una de sus clases. 

#### Imputación de valores faltantes (MICE)

Es común encontrar valores faltantes en la base de datos MIMIC III. Por ejemplo, es posible que aun paciente determinado no se le haya realizado alguna prueba de laboratorio, o no se le haya tomado cierta medida fisiológica por algun motivo. Es necesario que los datos de entrada de la red neuronal se encuentren completos con el fin de poder construir el modelo predictivo. 

Existen diversas maneras de enfocar esta problemática. Una posibilidad es eliminar todos los registros con algun valor faltante, aunque en este caso no es viable debido al gran número de variables, lo cual hace que más del 95% de registros tengan por lo menos un valor faltante, reduciendo de esta forma el conjunto de datos a menos de 200 registros completos. Esta cantidad no permitiria entrenar correctamente la red neuronal. Por otra parte, tambíen pueden sustituirse los valores faltantes por su promedio o su moda, aunque esto reduce la variabilidad del conjunto de datos y es posible cometer errores importantes. 

Finalmente, se decide imputar los valores faltantes mediante la técnica MICE (Multivariate Imputation by Chained Equations). Se trata de un proceso iterativo que construye un modelo de imputación para cada variable mediante una serie de modelos de regresión, a partir de los datos observados y sus relaciones existentes. Para ello, utilizamos la librería 'fancyimpute': [https://github.com/iskandr/fancyimpute].

Tras realizar la imputación, se calcula el error cuadrático medio de imputación para cada variable, al imputar 200 valores previamente conocidos. Eso permite validar que la imputación ha producido un resultado adecuado. 

| Variable                | % Error | Número de imputaciones | % Valores imputados |
| :---------------------- | ------: | ---------------------: | ------------------: |
| procedure_count         |      71 |                   6734 |                  11 |
| std_blood_urea_nitrogen |      64 |                   9432 |                  15 |
| std_platelet_count      |      57 |                   8503 |                  14 |
| std_white_blood_cells   |      51 |                   8629 |                  14 |
| avg_blood_urea_nitrogen |      50 |                   9036 |                  15 |
| avg_creatinine          |      49 |                   9039 |                  15 |
| total_icu_time          |      46 |                   1312 |                 2.2 |
| avg_platelet_count      |      41 |                   3185 |                 5.2 |
| std_sodium              |      41 |                   8426 |                  14 |
| std_blood_glucose       |      39 |                   9541 |                  16 |
| std_temp                |      37 |                  13060 |                  21 |
| std_hematrocrit         |      36 |                   8085 |                  13 |
| std_bicarbonate         |      34 |                   8467 |                  14 |
| std_hr                  |      32 |                   5364 |                 8.8 |
| std_spo2                |      32 |                  11170 |                  18 |
| avg_white_blood_cells   |      31 |                   3158 |                 5.2 |
| std_potasssium          |      30 |                   8321 |                  14 |
| std_resp_rate           |      23 |                   5482 |                   9 |
| std_sys_press           |      22 |                  11104 |                  18 |
| std_dias_press          |      21 |                  11134 |                  18 |
| oasis_avg               |      19 |                   1302 |                 2.1 |
| sofa_avg                |    17.2 |                   1302 |                 2.1 |
| saps_avg                |      17 |                   1302 |                 2.1 |
| avg_albumin             |      14 |                  29669 |                  49 |
| std_creatinine          |    13.9 |                   9430 |                  15 |
| avg_resp_rate           |      12 |                   3540 |                 5.8 |
| avg_blood_glucose       |      11 |                   9376 |                  15 |
| avg_hr                  |      10 |                   3551 |                 5.8 |
| avg_dias_press          |      10 |                  11075 |                  18 |
| avg_bicarbonate         |     9.6 |                   7190 |                  12 |
| avg_sys_press           |     8.9 |                  11075 |                  18 |
| avg_hematrocrit         |     8.6 |                   3046 |                   5 |
| avg_potasssium          |     5.8 |                   7189 |                  12 |
| avg_sodium              |       2 |                   7222 |                  12 |
| avg_spo2                |     1.2 |                  11114 |                  18 |
| avg_temp                |    0.57 |                  11876 |                  19 |

#### Normalización de variables numéricas

Debido a que el rango de valores de los datos varia ampliamente, ciertas funciones podrían no funcionar correctamente sin la normalización de estos. Por ejemplo, la mayoría de clasificadores calculan la distancia entre dos puntos mediante la distáncia euclídea. Si una de las dos características tiene un rango notablemente más amplio que otras, la distancia será marcada por esta característica, con lo cual su peso en el algoritmo será mucho mayor de lo que debiera. Por lo tanto, el rango de todas las características debe ser normalizada con el fin de que cada variable contribuya de forma equilibrada. De la misma forma, la normalización de las variables permite que el descenso de gradiente, paso indispensable en una red neuronal, llegue a converger a mayor velocidad. 

Debido a esto, se normalizan todas las variables numéricas para que se asemejen a una distribución normal, dónde la media es cero y la desviación típica es uno. 

![img](data:image/png;base64,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%0AnUH2VQAAAABJRU5ErkJggg==) 

Realizamos este proceso mediante el método 'scale' del módulo 'preprocessing' de la librería 'Scikit Learn'

#### Codificación de variables categóricas

Las variables categóricas deben ser codificadas para ser aceptadas por la red neuronal. En concreto, deben dividirse en columnas con valores binarios para cada uno de los valores que toma la variable.

| ID_Paciente |  Mortalidad  |
| :---------: | :----------: |
|     456     |   < 1 mes    |
|     321     | 1 - 12 meses |
|     678     |  12+ meses   |
|     543     | 1 -12 meses  |
|     987     |   < 1 mes    |

Por ejemplo, la tabla anterior se debe convertir al siguiente formato, donde cada columna corresponde a un intervalo de mortalidad.

| ID_Paciente | < 1 mes | 1 - 12 meses | 12+ meses |
| :---------: | :-----: | :----------: | :-------: |
|     456     |    1    |      0       |     0     |
|     321     |    0    |      1       |     0     |
|     678     |    0    |      0       |     1     |
|     543     |    0    |      1       |     0     |
|     987     |    1    |      0       |     0     |

Realizamos este proceso tanto para las variables a predecir, mortalidad y readmisión, como para aquellas variables predictorias categóricas, tales como la etnicidad del paciente, religión, o el grupo de código de diagnósticos ICD9, entre otras. 

Se lleva a cabo mediante el método get_dummies de la librería de cálculo numérico Pandas. 

#### División en conjunto de entrenamiento y evaluación

Es conveniente dividir el conjunto de datos en dos conjuntos, un primer conjunto mayor sobre el cual se entrena la red neuronal, y un conjunto de prueba de tamaño menor sobre el cual se evalua el rendimiento de la red. 

Se decide destinar el 7.5% del conjunto de datos a la evaluación del modelo, distribuyendose de la siguiente manera los conjuntos de datos de mortalidad y readmisión:

|                           |   Mortalidad    |
| :------------------------ | :-------------: |
| Conjunto de entrenamiento | 20778 registros |
| Conjunto de evaluación    | 1685 registros  |
| Total                     | 22463 registros |

Se realiza facilmente mediante la utilizad 'train_test_split' de la librería 'Scikit Learn'

### Sobreajuste y sobregeneralización

En determinadas ocasiones, un modelo predictivo puede ajustarse demasiado al conjunto de datos de datos de entreno, siendo incapaz de generalizar la predicción para datos con los que no ha sido entrenado. Por otra parte, también se puede dar la situación contraria, es decir, que no haya sido capaz de extraer relaciones significantes durante el proceso de entreno, y por lo tal tampoco pueda realizar predicciones correctas. 

![](C:\mimic-iii-project\plots\Useful_plots\overfit.png)

De esta manera, es necesario encontrar un modelo que no 'memorice' los datos usados durante su entrenamiento, pero que sea capaz de extraer las relaciones significativas. No siempre el modelo con mayor precisión sobre los datos de entreno es el mejor, ya que puede ser un modelo sobreajustado.  

Un modelo sobregeneralizado presenta error alto tanto en los datos de entreno como en los datos de test, mientras que un modelo sobreajutado presenta error muy bajo sobre el conjunto de entreno y error alto sobre el conjunto de test. 

Será necesario evaluar este factor tras entrenar la red neuronal. 

### Métricas de evaluación

El uso correcto de las métricas de evaluación en un modelo clasificatorio es indispensable para entender el rendimiento de este. 

#### Precisión de clasificación

Se trata de la relación entre predicciones correctas y el número total de predicciones. Es útil cuando las clases a predecir se encuentran balanceadas, tal como en el caso que nos ocupa. En el caso contrario, suele inducir a errores de interpretación. Por ejemplo, en una tarea clasificatoria de imágenes del 0 al 9, si se desea construir un clasificador que detecte el número 6, basta con que el algoritmo clasifique cada registro como distinto al 6 para obtener una precisión del 90%, ya que solo el 10% de las imágenes son 6. Esta es una problemática mayor en tareas de aprendizaje automático y es por ello que deben emplearse diversas métricas para estudiar un mismo modelo. 
$$
Precisión = \frac{\textrm{Predicciones correctas}}{\textrm{Total de predicciones}}
$$

#### F1 Score

La precisión, la cual indica el porcentaje de predicciones correctas por el modelo, y la sensibilidad, que señala que porcentaje de registros fueron predichos correctamente.

Estas dos métricas se combinan en una misma mediante el 'F-Score'. Se cálcula a partir de la media harmónica de precisión y sensibilidad, y por lo tanto, solo devolverá un valor elevado si tanto la sensibilidad como la precisión son elevadas. 
$$
F1 =2 · \frac{\textrm{Precisión · Sensibilidad}}{\textrm{Precisión + Sensibilidad}}
$$

#### Entropia cruzada categórica

También llamada pérdida logarítmica, penaliza las clasificaciones falsas. Se trata de una métrica de evaluación para modelos que predicen clases mutuamente exclusivas, como es este caso, que permite medir la diferencia entre las probabilidades predecidas y los valores reales. Durante el entrenamiento, se persigue minimizar esta diferencia. Minimizar la entropia cruzada categórica es equivalente a minimizar la probabilidad logarítmica negativa de los datos, lo cual es una medida directa de la capacidad de predicción del modelo. 

Se calcula mediante la siguiente expresión, donde $y_{ij}$ indica si la clase $i$ pertenece a la clase $j$ y $p_{ij}$ indica la probabilidad de que la muestra $i$ pertenezca a la clase $j$ 
$$
\textrm{Pérdida Logarítmica} = \frac{1}{\textrm{N}}\sum_{i=1}^{\N} \sum_{j=1}^{M}y_{ij} * log(p_{ij})
$$

#### Error cuadrático medio

De forma similar la métrica anterior, mide el promedio de los errores al cuadrado entre los valores obtenidos y los reales. Se calcula mediante la siguiente expresión y es conveniente minimizar su valor. Sus siglas en inglés son MSE (Mean Squared Error).
$$
\textrm{RME} = \frac{1}{\textrm{N}}\sum_{j=1}^{\N} ·  log(p_{ij})
$$

$$
\textrm{MSE} = \frac{1}{\textrm{N}}\sum_{j=1}^{\N}  (y_j -\bar y_j )^2
$$

#### AUROC  (Area under Receiver Operating Characteristic)

En una curva ROC (Receiver Operating Characteristic) se muestra el ratio de verdaderos positivos, la sensibilidad, en función del ratio de falsos positivos, la especificidad. Cada punto de la curva ROC representa la relacion entre sensibilidad y especificad correspondiente a un valor umbral determinado. 
$$
Sensibilidad =  \frac{\textrm{Verdaderos positivos + Falsos negativos}}{\textrm{Número de muestras}}
$$

$$
Especificidad =  \frac{\textrm{Falsos positivos}}{\textrm{Falsos positivos + Verdaderos negativos}}
$$

El area bajo esta curva es una medida del grado de ajuste de un predictor en una tarea de clasificación. Mide la discriminación del modelo, es decir, la capacidad de clasificar correctamente los valores. 

Se considera que un modelo tiene una capacidad de predicción perfecta cuando este valor es 1, y aleatoria cuando es 0.5.

### Parámetros e hiperparámetros

Los hiperparámetros son las variables que determinan la estructura de la red neuronal, tal como el número de capas ocultas, y las variables que determinan como la red se entrena, por ejemplo el ratio de aprendizaje.

Los hiperparámetros se establecen antes de entrenar el modelo y determinan su rendimiento. Los principales hiperparámetros a seleccionar son los siguientes: 

- Número de capas ocultas y unidades: Se trata de las capas entre la capa de entrada y la capa de salida. Un número muy elevado de unidades en una misma capa junto con técnicas de regularización permite aumentar la precisión del modelo. Sin embargo, un número bajo de unidades puede llevar a la sobregeneralización del modelo.

- Dropout: Es una técnica para reducir el sobreajuste en redes neuronales. Consiste en desactivar aleatoriamente un porcentaje de neuronas en cada capa, con tal de disminuir su peso alternativamente en el modelo. De esta forma, la red aumenta su capacidad de generalizar los resultados. 

  ![](C:\mimic-iii-project\plots\Useful_plots\dropout.png)

- Función de activación: Se emplean para introducir no-linearidades en el modelo, lo cual permite al modelo de aprendizaje automático diseñar fronteras de predicción no lineares. Se suele emplear generalmente la función de rectificación de activación (ReLu). La función sigmoide es empleada en la capa de salida en modelos predictivos binarios, mientras que la capa 'Softmax' se emplea en modelos predictivos multiclase. 

![](C:\mimic-iii-project\plots\Useful_plots\sigmoid.png)

- Ratio de aprendizaje: Determina la velocidad de actualización de parámetros de una red. Un ratio de aprendizaje bajo alentece el proceso de aprendizaje, pero converge adecuadamente. Sin embargo, un ratio de aprendizaje alto acelera el entreno de la red, pero puede no lleger a los parámetros óptimos. Es por esto que se suelen emplear ratios de aprendizaje adaptativo, es decir, elevados al inicio del entreno de la red y lento una vez se acerca la convergencia. 
- Momento: Permite deducir la dirección del siguiente paso hacia la convergencia de la red a partir de los pasos anteriores, evitando así oscilaciones. 
- Epochs: Es la cantidad de veces que el conjunto de datos de entrenamiento es proporiconado a la red durante el entreno. 
- Batch Size: Es el número de muestras del conjunto de entreno tras el cual se actualizan los parámetros de la red. 
- Algoritmo de optimización: Se trata del algoritmo empleado para actualizar los parámetros del modelo, principalmente los pesos y varianzas de cada neurona. 

#### Ajuste de parámetros e hiperparámetros

La elección de los parámetros óptimos de una red neuronal es un proceso esencial en la obtención de un buen modelo predictivo. Existen diversos enfoques para encontrar estos valores.

- Grid Search: Consiste en probar todas las combinaciones posibles de parámetros hasta dar con aquella que minimiza la métrica de evaluación empleada. Es un método poco óptimo, únicamente útil en modelos sencillos y rápidos de compilar, ya que en el caso contrario requiere demasiado tiempo y recursos computacionales. 
- Búsqueda aleatoria: Se trata de probar aleatoriamente combinaciones de hiperparámetros hasta dar con alguna que devuelva un resultado adecuado. No garantiza encontrar los hiperparámetros óptimos.
- Búsqueda informada: Se buscan los hiperparámetros óptimos evaluando tras cada iteraciones el resultado obtenido. Tras cada iteracion, se decrece la probabilidad de escoger valores que no corresponden a la solucion óptima. De esta forma, se escoge un nuevo conjunto de parámetros, se observa si se ha aumentado o disminuido la calidad del modelo, y acorde a esto, se escoge un nuevo conjunto de parámetros en función de los anteriores. De esta manera, se optimiza la búsqueda de parámetros, ya que cada paso de cálculo se aproxima cada vez a los parámetros óptimos, además de no ser necesario evaluar todas las combinaciones de parámetros posibles. 

#### Optimización Bayesiana

Se realiza el ajuste de parámetros mediante la opción de búsqueda informada, en concreto, emplearemos la optimización Bayesiana. 

Es un enfoque basado en modelos probabilísticos para encontrar el mínimo de una función que devuelve una métrica real. En este caso, la función es multidimensional, ya que recibe como entrada un espacio de hiperparámetros. La óptimización Bayesiana reduce el número de veces que debemos entrenar y evaluar la red neuronal, proceso computacionalmente costoso. Se construye yn modelo probabilístico de la función objetivo que busca la correspondencia entre los valores de entrada, en este caso los hiperparámetors, y la salida, la métrica de evaluación. De esta manera, se recalcula la selección de hiperparámetros basandose en la nueva evidencia encontrada tras cada iteracion.

Para la implementación de este método utilizamos la librería Hyperopt. [https://github.com/hyperopt/hyperopt].

Primeramente diseñamos una función que permite entrenar la red neuronal partir de los parámetros de entrada y devuelve una métrica de evaluación, el AUROC, definido anteriormente. En este caso, como el método de optimización Bayesiana busca minimizar la función coste, se devuelve 1 - AUROC.

```python
def train_neural_network(X_train, Y_train, X_test, Y_test, params):
    
    n_layers = params['n_layers'];
    n_neurons = params['n_neurons'];
    batch_size = params['batch_size'];
    epochs = params['epochs'];
    optimizer = params['optimizer'];
    
    model = Sequential();
    for i in range(n_layers):
        model.add(Dense(n_neurons, activation='relu', input_shape=(101,)))
    model.add(Dense(3, activation='softmax'));
    model.compile(loss='binary_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy', 'mse'])

    model.fit(X_train, Y_train,epochs=epochs, batch_size=batch_size, verbose=0);
    
    Y_pred = model.predict(X_test);
    roc_auroc = roc_auc_score(Y_test, Y_pred);
    
    return 1 - roc_auroc;
```

Se observa que el modelo recibe como parámetros el número de capas, el número de neuronas por capa, el batch size, el número de epochs y la función de optimización. Empleamos el módulo roc_auc_score de la libreria 'Scikit-Learn' para obtener la métrica AUROC, ya que no se encuentra incluída por defecto en Keras. 

Envolvemos está función en una función objetivo, que recibe únicamente los parámetros y devuelve la métrica seleccionada, para ser utilizada por Hyperopt. 

```python
def f(params):
    return train_neural_network(X_train, Y_train, X_test, Y_test, params);
```

Posteriormente definimos el espacio de hiperparámetros en el cual buscaremos aquellos óptimos, que maximizen el AUROC del modelo.  En concreto, se prueban los siguientes parámetros..

- Número de capas: de 2 a 8.
- Número de neuronas: 8, 16, 32, 64.
- Funciones de optimización: 'Stochastic Gradient Descent, Adam, RMSProp, Adagrad.
- Epochs: 10, 25, 35
- Batch size: 1, 25, 50

Se utiliza el algoritmo por defecto de Hyperopt, TPE (Tree-structured Parzen Estimator), el cual explora inteligentemente el espacio de hiperparámetros reduciendo la búsqueda a aquellos óptimos tras cada iteracion. 

Tras 50 iteraciones y un tiempo de ejecución de 3.5 horas, obtenemos que los parámetros que máximizan el AUROC son los siguientes:

- Número de capas: 6
- Neuronas por capa: 8
- Batch Size: 50
- Epoch: 25
- Función de optimización: Adam

### Arquitectura y parámetros escogidos

Empleando los parámetros obtenidos anteriormente mediante optimización bayesiana, obtenemos la siguiente arquitectura de red, consistente en seis capas totalmente conectadas con 16 neuronas por capa. La capa de entrada es un vector de 101 elementos, tantos como variables de entrada tras su procesado, aunque para representarlo visualmente se muestra como un único nodo. 

![](C:\mimic-iii-project\plots\Useful_plots\architecture.svg)

Una vez entrenada y evaluada la red, se juzgará la necesidad de añadir capas Dropout para regular el sobreajuste, si lo hubiera. 

Se utiliza la función activación 'ReLU' , Rectified Linear Unit. Esta función evita el problema de los gradientes desvanecientes. La red neuronal calcula los pesos de los parámetros a partir de la diferencia en la salida del modelo en función de estos. Ciertas funciones de activación comprimen el resultado en un rango determinado, por ejemplo [-1, 1 ] en el caso de la tangente hiperbólica. De esta forma, al entrenar los parámetros de las primeras capas de la red mediante propagación hacia atrás, la convergencia de los parámetros de estas capas se hace muy lenta, debido a que los cambios de parámetros producen efectos negligibles sobre la salida de la red. 

La función de activación ReLu evita este problema, ya que no restringe la salida de la capa a un rango determinado, sinó que permite valores en el intervalo [0, ∞].

Tambíen reduce la carga computacional en función a otras funciones, ya que su cálculo es sencillo e inmediato, sin requerir funciones trigonométricas o exponenciales. Esto permite entrenar la red más rápido. 

![](C:\mimic-iii-project\plots\Useful_plots\relu.png)

En cuanto al algoritmo de optimización, utilizaremos la función 'Adam', basado en la adaptación estimada del momento. Fue presentado en 2015 por investigadores de la Universidad de Toronto. El método computa el ratio de aprendizaje de la red de forma adaptativa para diferentes parámetros a partir de estimaciones del primer y segundo momento de los gradientes. Combina las ventajas de otras  extensiones del método clásico, el algoritmo Stochastic Gradient Descent. Los resultados empíricos muestran que Adam funciona correctamente en la práctica y se compara favorablemente con otros métodos estocásticos de optimización.

![](C:\mimic-iii-project\plots\Useful_plots\optomization_algorithms.png)

Por otra parte, haremos 25 pasadas del conjunto de datos durante el entreno de la red neuronal y actualizaremos los parámetros cada 50 muestras, empleando los valores óptimos de epoch y batch size obtenidos en el paso anterior.

### Evaluación del modelo

Una vez escogidos los parámetros para la red, es conveniente evaluar su rendimiento a partir de sus métricas de evaluación, además de determinar si se produce el sobreajuste a los datos de entreno.

| Métrica                          | Valor |
| -------------------------------- | ----- |
| Precisión sobre datos de entreno | 0.656 |
| Precisión sobre datos de test    | 0.632 |
| Categorical Cross Entropy Loss   | 0.461 |
| Error cuadrático medio           | 0.154 |
| AUROC                            | 0.812 |

Observamos que la red no produce ni sobreajuste ni sobregeneralización, ya que como es correcto, la precisión sobre los datos de entreno es ligeramente mayor a la precisión sobre los datos de evaluación.

Calculamos por separado el AUROC para cada una de las tres clases predichas y representamos sus curvas: 

| Clase | Mortalidad   | AUROC |
| ----- | ------------ | ----- |
| 0     | < 1 mes      | 0.89  |
| 1     | 1 - 12 meses | 0.72  |
| 2     | > 12 meses   | 0.81  |

![](C:\mimic-iii-project\plots\Evaluation\3Curvas SPA.png)

El AUROC combinado de las tres clases obtenido indica que se trata de un buen modelo, con buena capacidad diagnóstica, especialmente en la clase con mayor valor médico, la de los pacientes que fallecen antes de un mes de su alta hospitalaria. Obtenemos una capacidad predictoria también buena para la clase superior a un año, aunque moderada para el grupo de entre 1 y 12 meses. 

En cuanto a la matriz de confusión normalizada del modelo, obtenemos el siguiente resultado: 

![](C:\mimic-iii-project\plots\Evaluation\matriz_confusion_normalizada_seaborn.png)

De nuevo, se observa que el modelo posee dificultades para discernir pacientes en el intervalo de 1 a 12 meses, aunque no lo hace para las otras dos clases.

El reporte de métricas de evaluación para las tres clases es el siguiente.

| Clase        | Precisión | Recall | F1 Score |
| ------------ | --------- | ------ | -------- |
| <1 mes       | 0.79      | 0.71   | 0.75     |
| 1 - 12 meses | 0.47      | 0.38   | 0.42     |
| >12 meses    | 0.57      | 0.72   | 0.64     |

### Ejemplos de uso

Para utilizar el modelo para hacer predicciones se debe realizar el siguiente procedimiento.

Primeramente hay que proporcionar información categórica relacionada con el paciente y su estancia a través de un objeto: 

``` python
patient_categorical_features = {'gender': 'M',
                                'marital_status':'SINGLE',
                                'religion':'CHRISTIAN',
                                'ethnicity':'WHITE',
                                'service':'CSURG',
                                'icd9_group':'diseases of the circulatory system',
                                'SURGERY_FLAG':'NARROW'
                                };

```



Los valores que pueden tomar estas variables se hayan en la descripción de las variables predictorias. 

Posteriormente se debe rellenar la información numérica necesaria de la siguiente forma:

```python
patient_numerical_features = {'age':80,
                              'total_icu_time':10,
                              'total_los_days':12,
                              'admissions_count':3,
                              'procedure_count':4,
                              'oasis_avg':40,
                              'sofa_avg':7,
                              'saps_avg':20,
                              'gcs':9,
                              'total_mech_vent_time':130
                              };
```

Y en otros dos objetos, los resultados de los test de laboratorios y señales fisiológicos. Cada variable se debe introducir como un arreglo de elementos, del cual posteriormente se calcula el promedio y la desviación estándar. Las unidades de cada una se hayan también descritas en el apartado 'Variables predictorias'.

```python
patient_lab_tests = {'blood_urea_nitrogen': [23, 24, 24],
                     'platelet_count':[230, 240],
                     'hematocrit':[33, 35],
                     'potassium': [3.9,3.8,4.4],
                     'sodium':[140, 139],
                     'creatinine':[1.3,1.2,1.3],
                     'bicarbonate':[25,26],
                     'white_blood_cells':[8.5,9,13],
                     'blood_glucose':[130, 135,140],
                     'albumin':[3.5, 3.4]
                     };

patient_physio_measures = {'heart_rate':[100,108,105,99],
                           'resp_rate':[22,25,23],
                           'sys_press':[120, 121, 115],
                           'dias_press':[70,80,85],
                           'temp':[98, 98.2, 97.8],
                           'spo2':[97,97.8,98]
                           };
```

Posteriormente emplearemos la función preprocess_prediction_data, a la cual suministraremos las carácterísticas del paciente en forma de objeto, las variables numéricas con los valores faltantes previamente imputados y las variables categóricas. De esta forma, en caso de que hayan valores faltantes, por ejemplo si no se ha tomado la temperatura del paciente, podremos imputarlos mediante el método MICE anteriormente definido.

```python
prediction_data = NeuralNetworkService().preprocess_prediction_data(
    patient_features,
    imputed_numerical_features,
    categorical_features
	);

```

Esta función nos devuelve las variables predictorias del paciente tratadas para ser introducidas en el modelo. En concreto, se han normalizado las variables numéricas, imputado valores faltantes y categorizado las variables numéricas. Empleando estos valores, realizamos la predicción seguidamente:

```
prediction = keras_model.predict(prediction_data);
```

Para este paciente, el resultado de la prediccion nos devuelve las siguientes probabilidades por clase: 

| < 1 mes | 1 - 12 meses | > 12 meses |
| ------- | ------------ | ---------- |
| 0.54086 | 0.27766      | 0.18148    |

Viendo este resultado, se debería valorar el alta del paciente, ya que tiene amplias probabilidades de morir en menos de un mes desde su salida del hospital.

# Conclusiones

Se ha desarrollado satisfactoriamente un modelo predictivo de la mortalidad extra-hospitalaria con una buena capacidad diagnóstica. 

Este proyecto ha comportado la exploración de una gran base de datos con muchos tipos de valores diferentes: numéricos, categóricos, fechas, campos de texto, etc, y el tratamiento de ellos para ser procesados por la red neuronal.

Las variables necesarias para realizar predicciones con este modelo son fáciles de obtener y se recopilan de forma rutinaria, lo cual permitiría un uso extendido del algoritmo en la práctica médica, aunque siempre considerando que comete ciertas inexactitudes. Podría llegar a emplearse como segunda opinión médica, para confirmar o cancelar el alta de pacientes en unidad de cuidados intensivos. 

La mayor carga de trabajo ha recaído sobre la selección, extracción y preprocesado de las variables empleadas por el modelo. Este proceso a llevado al descarte de ciertas variables, por ejemplo la presión venosa central, por disponerse de pocas muestras.

Por otra parte, gracias a la optimización bayesiana de hiperparámetros ha sido relativamente sencillo, auque lento, encontrar la configuración de red que asegura un resultado óptimo. 

Como mejoras, se podrían extraer nuevas variables ignoradas en este estudio. Por ejemplo, en la base de datos se almacenan las notas médicas como campo libre de texto para cada paciente, las cuales incluyen anotaciones realizadas por el personal médico acerca del historial de los pacientes o situaciones médicas particulares. La extracción de estas características supondría un amplio trabajo de minería de textos que cae fuera del alcance de este proyecto.

Así mismo, sería posible desarrollar una pequeña interfaz o página web que permita realizar predicciones empleando el modelo diseñado. Esta interfaz permitiría al personal médico la introducción de las variables necesarias y devolvería la probabilidad de mortalidad del paciente. 

# Análisis económico

El mayor coste económico de este proyecto recae en el sueldo del Ingeniero que ha desarrollado la red neuronal que llevará a cabo la predicción de mortalidad. De esta manera, la mayor parte del coste económico irá destinada a pagar sus horas de trabajo, y otra pequeña parte irá a parar el coste indirecto del proyecto, consistente principalmente en el equipo informático que utiliza. 

## Costes directos

Son aquellos costes que pueden identificarse directamente con un objeto de costes, tal como materiales o mano de obra destinada al proyecto.

En este caso, el coste directo es completamente el sueldo del personal, al cual consideramos un trabajador autónomo que factura por horas. 

Consideramos que el proyecto lo ha llevado a cabo un único desarrollador, con una facturación de 30€/h y una dedicación de 320, dando de esta manera un coste directo total de 9600€.

## Costes indirectos

El coste indirecto del proyecto corresponde al equipo informático empleado.

No existen costes asociados al software, ya que Python es un lenguaje de programación gratuito de código abierto y el sistema operativo del equipo es Elementary OS loki 0.4.1, distribución de Linux basada en Ubuntu y también gratuita. 

En cuando al hardware, se emplea un ordenador portátil del siguiente modelo:

- Toshiba Satellite Pro A50-D-1FZ Intel Core i7-7500U/8GB/256GB SSD/15.6" 

Su coste es de 695€. Considerando un periodo de amortización de tres años y un periodo de uso de cuatro meses, el coste indirecto de hardware es de 77.22 €.

De esta manera, el coste total del proyecto computado como la suma de costes directos e indirectos es de alrededor de 9700€.

# Bibliografia

- Pirracchio R, Petersen ML, Carone M, Rigon MR, Chevret S, van der LAAN MJ. Mortality prediction in the ICU: can we do better? Results from the Super ICU Learner Algorithm (SICULA) project, a population-based study. *The Lancet Respiratory medicine*. 2015;3(1):42-52. doi:10.1016/S2213-2600(14)70239-5.
- Aya Awad, Mohamed Bader-El-Den, James McNicholas, Jim Briggs. Early hospital mortality prediction of intensive care unit patients using an ensemble learning approach. .Int J Med Inform. 2017 Dec; 108: 185–195. Published online 2017 Oct 5. doi: 10.1016/j.ijmedinf.2017.10.002
- MIMIC Code Repository.  Cambridge: Laboratory for Computational Physiology, Massachusetts Institute of Technology; 2018 [updated March 15, 2018]. Disponible en: http:// github.com/MIT-LCP/mimic-code. Consultado el 15 mayo de 2018.
- Johnson AE, Pollard TJ, Shen L, et al. MIMIC-III, a freely accessible critical care database. Sci Data. 2016;3:160035. [http://dx.doi.org/10.13026/C2XW26] (2016)
- Azur MJ, Stuart EA, Frangakis C, Leaf PJ. Multiple Imputation by Chained Equations: What is it and how does it work? *International journal of methods in psychiatric research*. 2011;20(1):40-49. doi:10.1002/mpr.329.
- Pastur-Romay LA, Cedrón F, Pazos A, Porto-Pazos AB. Deep Artificial Neural Networks and Neuromorphic Chips for Big Data Analysis: Pharmaceutical and Bioinformatics Applications. González-Díaz H, Todeschini R, Pazos Sierra A, Arrasate Gil S, eds. *International Journal of Molecular Sciences*. 2016;17(8):1313. doi:10.3390/ijms17081313.
- Moreno RP, Metnitz PGH, Almeida E, et al. SAPS 3--From evaluation of the patient to evaluation of the intensive care unit. Part 2: Development of a prognostic model for hospital mortality at ICU admission. Intensive Care Med. 2005;31:1345–55. [[PMC free article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1315315/)][[PubMed](https://www.ncbi.nlm.nih.gov/pubmed/16132892)] 
- Awad, Aya et al. “Early hospital mortality prediction of intensive care unit patients using an ensemble learning approach.” *International journal of medical informatics* 108 (2017): 185-195 .
- Knaus WA, Wagner DP, Draper EA, et al. The APACHE III prognostic system. Risk prediction of hospital mortality for critically ill hospitalized adults. Chest. 1991;100:1619– 36. [[PubMed](https://www.ncbi.nlm.nih.gov/pubmed/1959406)] 
- Cook NR. Use and misuse of the receiver operating characteristic curve in risk prediction. Circulation. 2007;115:928–35. [[PubMed](https://www.ncbi.nlm.nih.gov/pubmed/17309939)] 
- Knaus WA, Harrell FE, Fisher CJ, et al. The clinical evaluation of new drugs for sepsis: a prospective analysis based on survival analysis. JAMA 1993; 270: 1233-41.
- W.G. Baxt. Application of artificial neural networks to clinical medicine. Lancet, 346 (2007), pp. 1135-1138
- P.O. Lang, D. Zekry, J.P. Michel, M. Drame, J.L. Novella, D. Jolly, *et al. Early markers of prolonged hospital stay in demented inpatients: a multicentre and prospective study. J Nutr Health Aging, 14 (2010), pp. 141-147-
- S.W. Meldon, L.C. Mion, R.M. Palmer, B.L. Drew, J.T. Connor, L.J. Lewicki, *et al. A brief risk-stratification tool to predict repeat emergency department visits and hospitalizations in older patients discharged from the emergency department. Acad Emerg Med, 10 (2003), pp. 224-232
- Lokhandwala S, McCague N, Chahin A, Escobar B, Feng M, Ghassemi MM, Stone DJ, Celi LA. [One-year mortality after recovery from critical illness: A retrospective cohort study](https://doi.org/10.1371/journal.pone.0197226). PLoS ONE, 13(5):e0197226, May 2018. ([doi:10.1371/journal.pone.0197226](http://dx.doi.org/10.1371/journal.pone.0197226)) 
- Johnson AEW, Stone DJ, Celi LA, Pollard TJ.[The MIMIC Code Repository: enabling reproducibility in critical care research](https://doi.org/10.1093/jamia/ocx084). J Am Med Inform Assoc, Sept. 2017. ([doi:10.1093/jamia/ocx084](http://dx.doi.org/10.1093/jamia/ocx084)) [(PMID:29036464)](http://www.ncbi.nlm.nih.gov/pubmed/29036464)
- Johnson AEW, Ghassemi MM, Nemati S, Niehaus KE, Clifton DA, Clifford GD. [Machine learning and decision support in critical care](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7390351). Proceedings of the IEEE, 104(2):444–466, Feb. 2016. ([PDF](https://mimic.physionet.org/about/publications/pdf/JohnsonProcIEEE2016.pdf)) ([doi:10.1109/JPROC.2015.2501978](http://dx.doi.org/10.1109/JPROC.2015.2501978)) [(PMID:27765959)](http://www.ncbi.nlm.nih.gov/pubmed/27765959)

