# Descripción del conjunto de datos

MIMIC-III ("Medical information Mart for Intensive Care") es una base de datos correspondiente a los ingresos hospitalarios en unidad de cuidados intensivos en el hospital Beth Israel Deaconess Medical Center, en Boston, Massachussets, EE.UU. Incluye información relativa a los signos vitales de los pacientes, medicación, medidas de laboratorio, observaciones y notas tomadas por el personal médico, balance de fluidos, códigos de procedimientos, códigos de diagnósticos, reportes de imágenes médicas, duración de la estancia hospitalaria y datos de la supervivencia de los pacientes, entre otros. Estos datos se encuentran deidentificados y són de ámbito público para el uso académico.

Es la única base de datos libremente accesible de este tipo. Además, destaca por su gran cantidad de registros, obtenidos a lo largo de más de una década, concretamente entre los años 2001 y 2012 

Contiene datos asociados con 53423 admisiones hospitalarias para pacientes adultos mayores de 16 años en unidad de cuidados intensivos entre 2001 y 2012. Así mismo, contiene información sobre 7870 neonatos admitidos entre 2001 y 2008. La mediana de edad de los pacientes es de 65.8 años, el 55.9% de los pacientes son hombres y la mortalidad hospitalaria es del 11.5%. La duración mediana de una estáncia en la unidad de cuidados intensivos es de 2.1 dias y la mediana de duración en el hospital es de 6.9 dias. 

Contiene tipos variados de datos, desde medidas fisiológicas realizadas por el personal médico, hasta interpretaciones textuales de imágenes médicas provenientes del departamento de radiología. 

Como sistemas de monitorización y recogida de datos, se emplearon dos dispositivos: Philips CareVue Clinical Information System (M2331A y M1215A) y iMDsoft MetaVision ICU. Estos dispositivos fueron la fuente de diversos datos clínicos, tales como medidas fisiológicas como el ritmo cardíaco, la presión arterial o el ritmo respiratorio, notas acerca del progreso de los pacientes o suministro de medicamentos. MIMIC - III fusiona los datos provenientes de los dos dispositivos en los casos en que es posible. 

Informació adicional fue recopilada de los sistemas de registro hospitalarios, principalmente datos relativos a la demografia de los pacientes y la mortalidad hospitalaria, resultados de test de laboratorios, reportes sobre electrocardiogramas y imágenes médicas, y códigos de diagnóstico y de procedimientos. Así mismo, se recopila información acerca de la mortalidad extra-hospitalaria a partir de los archivos de la seguridad social estadounidense. 

## Deidentifación, privacidad y condiciones de acceso

Todos los ficheros fueron deidentifacos antes de ser introducidos en MIMIC-III, de acuerdo la normativa estadounidense vigente, "Health Insurance Portability and Accountability Act (HIPAA)". Para ello, se eliminó toda la información que permitia identificar los pacientes, tal cómo el número de teléfono, nombre, dirección, etc. 

En cuanto a las fechas, fueron desplazadas en el futuro de forma aleatoria de manera consistente para cada individuo, resultando en estancias que ocurren entre el año 2100 y 2200. Sin embargo, la hora, dia de la semana y estación fueron conservadas en este proceso de modifcación de fechas. 

Así mismo, la edad de los pacientes mayores a 89 años fue enmascarada para preservar su intimidad según la regulación vigente. Es por ello que aparecen con edades superiores a 300 años. 

Para acceder a la base de datos es necesario realizar un proceso consistente en completar un curso reconocido sobre la protección de datos de los participantes en el estudio, acorde con las regulaciones del HIPPA, y firmar un acuerdo de uso, el cual delimita un uso adecuado de la información y estándares de seguridad, además de prohibir expresamente la identifación de los usuarios. El proceso requiere alrededor de una semana y se realiza por internet. 

En concreto, se debe realizar el curso  ‘Data or Specimens Only Research’ proprcionado por el Massachusetts Institute of Technology  a través del Programa CITI, Collaborative Institutional Training Initiative.  

Una vez completado se recibe un certificado de finalización, el cual debe ser enviado a los administradores de MIMIC-III con tal de obtener las claves de acceso necesarias.

Una vez hecho este proceso, la información se obtiene como una colección de CSVs, junto con scripts para importarlos en bases de datos. En la web oficial de mimic (<https://mimic.physionet.org>) se encuentran los pasos y los scripts necesarios para cargar los archivos en una base de datos local en PostgreSQL, así como para la creación de índices de búsqueda. 

 ## Tablas

La base de datos comprende un total de 26, las cuales se detallan a continuación:

* ADMISSIONS: Define la admisión hospitalaria de cada paciente, identificando cada una con un ID, HADM_ID. Contiene **58976** registros.  La información proviene de la base de datos del hospital. Así mismo, contiene algunas entradas relativas a la donación de órganos de pacientes fallecidos en el hospital.

* CALLOUT: Esta tabla contiene información de pacientes listos para ser dados de alta de la UCI. Cuando esto ocure, se dice que un paciente está ‘Called out’. Esta información no está disponible para todos los pacientes, ya que se empezó a recolectar después del inicio de creación de la base de datos. Así mismo, por motivos no especificados, no se incluyen entradas relativas a neonatos. Contiene 34499 registros. 

  Cuando un paciente está listo para ser dado de alta de la UCI, el personal médico encargado crea una petición de ‘call out’, la cual es posteriormente admitida. Posteriormente es transferido fuera de la UCI.

* CAREGIVERS: Esta tabla proporciona información acerca del personal médico y sus intervenciones sobre los pacientes. Contiene 7567 registros y proviene de la base de datos de los dispositivos de monitorización CareVue y Metavision. 

* CHARTEVENTS: Esta tabla contiene información relativa a los pacientes durante su estancia en la unidad de cuidados intensivos, tal como sus signos vitales, e información relevante asociada a su cuidado, como los ajustes de ventilación mecánica, pruebas de laboratorio, estado mental, etc. Contiene ciertos valores repetidos con la tabla LABEVENTS, que fueron incluidos por el personal médico con el objetivo de unificar la información en una sola tabla. En caso de discrepancias entre los valores, se toman como correctos los de la tabla LABEVENTS. Contiene alrededor de 330.000 registros.

* CPTEVENTS: Esta tabla contiene CPT (Current Procedural Terminology), códigos que identifican los procedimientos llevados a cabo en cada paciente. Se emplean principalmente para facturación. 

* D_CPT: Contiene definiciones generales, poco detalladas, de códigos CPT empleados en la tabla CPTEVENTS. Se trata de una tabla auxiliar que no presenta una relación única con las entradas de CPT, cada entrada de D_CPT se corresponde con un rango de códigos. De esta manera, múltiples códigos CPT pueden compartir la misma descripción, al tratarse de procedimientos similares. 

* D_ICD: Esta tabla contiene la relación de códigos de diagnósticos y su descripción acorde al estándar “International Coding Definitions Version 9” (ICD-9). Son asignados al finalizar la estancia del paciente y se emplean en facturación. Contiene 14567 registros, cada uno correspondiente a un código de diagnóstico distinto.

* D_ICD_PROCEDURES: Similar a la tabla D_ICD_DIAGNOSES, contiene las descripciones de los códigos de procedimiento acorde al estándar ICD-9.

* D_ITEMS: Contiene la descripción de todos los elementos almacenados como “ITEMS”. Cada 

  Proviene de la base de datos de los dispositivos de monitorización Philips CareVue y Metavision. Se debe tener en cuenta que es posible hayar elementos duplicados, al encontrarse repetidos en ambas bases de datos, así como debido a la introducción manual de texto y diferencias en ortografía o puntuación. Los ITEMIDs provenientes del dispositivo Metavision son superiores a 220000.

* D_LABITEMS: Esta tabla proviene de la base de datos del hospital y contiene definiciones para todos los ITEMID asociados a medidas de laboratorio. Se indica que la información contenida en esta tabla es consistente, sin duplicados presentes. Se relaciona externamente con la base de datos LOINC, la cual presenta un estándar universal para la codificación de registros médicos. 

* DATETIMEEVENTS: Contiene el registro de fechas y horas de eventos relacionados con un paciente en la ICU. Para proteger la identidad de los pacientes, las fechas han sido desplazadas en el tiempo, de manera consistente al resto de datos, manteniendo así la cronología de los pacientes. 

* DIAGNOSES_ICD: Contiene los diagnósticos de los pacientes codificados mediante el estándar ICD-9. Se asignan con propósitos de facturación al finalizar la estancia hospitalaria de cada paciente. 

* DRGCODES: Contiene códigos de grupos de diagnósticos relacionados (DRG, ‘Diagnosis related groups’), para los pacientes.

* ICUSTAYS: Define cada estancia en unidad de cuidados intensivos. Es una tabla derivada del agrupamiento de la tabla TRANSFERS por ICUSTAY_ID

* INPUTEVENTS_CV: Proviene de la base de datos del sistema de
  monitorización Philips CareVue y contiene información acerca de fluidos
  administrados al paciente, como tubos de alimentación o soluciones
  intravenosas. 

* INPUTEVENTS_MV: Tabla análoga a INPUTEVENTS_CV, conteniendo los fármacos subministrados al paciente registrados por MetaVision.

* LABEVENTS: Contiene todas las medidas de laboratorio para un paciente dado, incluso aquellas tomadas en clínicas externas. Estas últimas no disponen de un identificador de admisión hospitalaria, al no haber sido tomadas en el hospital.

* MICROBIOLOGYEVENTS: Contiene registros de microbiología, entre ellos tests realizados y sensibilidades a distintas cepas de bacterias y virus, de pacientes en la UCI. 

* NOTEEVENTS: Contiene notas de texto acerca de los
  pacientes tomadas por el personal médico. Destaca información acerca del
  historial clínico de los pacientes, así como intepretaciones textuales de
  distintas pruebas, informes y notas de enfermería  o indicaciones a seguir tras el alta y
  medicaciones recetadas. 

* OUTPUTEVENTS: Contiene medidas sobre fluidos excretados por el paciente durante su estancia hositalaria, tales como orina, sangre, esputo, etc. 

* TRANSFERS: Contiene la localización de los pacientes a lo
  largo de su estancia hospitalaria. De esta tabla se deriva la tabla ICUSTAYS. 

* PATIENTS:Contiene información acerca de los pacientes, tal como su sexo, fecha de nacimiento, o de fallecimiento, dónde aplica. En aquellos pacientes de edad mayor a 89 años, se ha modificado su fecha de nacimiento, haciéndola constar como 300 años anterior a la fecha de primera admisión. Esta modificación se realiza para cumplir con la normativa de protección de datos estadounidense (HIPAA).  La mediana de edad para estos pacientes es de 91.4 años. 

* PRESCRIPTION: Contiene prescripciones de fármacos recetados a los pacientes e información relativa a su suministro: duracion, dosis, ratio, etc.

* PROCEDUREEVENTS_MV: Contiene información acerca de procedimientos
  médicos realizados en pacientes durante su estancia hospitalaria.

* SERVICES: Esta tabla describe los servicios bajo los que
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

