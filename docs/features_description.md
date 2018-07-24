

# Variables predictorias

Tras leer biblografía, se recopilan una serie de variables que se consideran determinantes a la hora de determinar el tiempo de supervivencia tras el alta de la admisión hospitalaria: 

| Tipo        | Nombre       | Tabla de origen | Unidad de medida | Tipo de variable       |
| ----------- | ------------ | --------------- | ---------------- | ---------------------- |
| Demográfica | Edad         | ADMISSIONS      | Años             | Numérica continua      |
| Demográfica | Sexo         | ADMISSIONS      | -                | Categórica (2 valores) |
| Demográfica | Estado civil | ADMISSIONS      | -                | Categórica (5 valores) |
| Demográfica | Religión     | ADMISSIONS      | -                | Categórica (6 valores) |
| Demográfica | Etnicidad    | ADMISSIONS      |                  | Categórica (6 valores) |
|             |              |                 |                  |                        |
|             |              |                 |                  |                        |
|             |              |                 |                  |                        |
|             |              |                 |                  |                        |

## Extracción y preprocesado

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

#### Sexo ####

Extraemos esta variable para cada admisión hospitalaria directamente de la base de datos, sin ningún tipo de preprocesado, mediante la siguiente consulta simple. 

```sql
SELECT hadm_id, gender
FROM admissions a
INNER JOIN patients p
ON a.subject_id = p.subject_id

```

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

**WORK IN PROGRESS**