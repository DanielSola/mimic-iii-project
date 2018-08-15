# Variables a predecir

Según la OMS, un destino médico es un cambio en el estado de salud de un invididuo, colectivo, o población, atribuible a intervenciones determinadas. 

La predicción de destinos médicos es una rama de la investigación médica que estudia el resultado final de la estructura y procesos del sistema médico en la salud y el bienestar de pacientes y poblaciones.

Es un pilar importante en la toma de decisiones y en análisis de políticas y procedimientos, ya que permite la evaluación de la calidad del cuidado médico, su eficiencia y efectividad.

Su objetivo es identificar fallos en la práctica médica que afectan a la salud del paciente y desarrollar estrategias que mejoren el cuidado. Para ello, mide eventos tangibles experimentados por el paciente, tales como la mortalidad, la readmisión o la morbilidad.

El resultado de la investigación sobre destinos médicos se utiliza para informar a los cuerpos legistlativos que toman decisiones realacionadas con la sanidad, así como a órganos financieros, tales como el gobierno o compañias aseguradoras, que buscan minimizar costes médicos proporcionando un cuidado médico adecuado.

La recolecta estandarizada de estadísticas y datos médicos acerca del cuidado médico que reciben los pacientes ha permitido que los registros médicos puedan ser empleados como una fuente fiable para la investigación.

Dos de los destinos médicos más relevantes son la mortalidad y la readmisión de los pacientes. El objetivo de este estudio es la predicción de estas variables mediante redes neuronales artificiales.

 En concreto, se trata de una tarea de la predicción clasificatoria en tres franjas temporales (0 - 1 meses, 1 - 12 meses, 12+ meses) de estas dos variables.

Para ello se emplean un total de 43 variables predictorias, incluyendo información demográfica, señales fisiológicas, resultados de pruebas de laboratorio y otras variables relacionadas con la estáncia hospitalaria de los pacientes.

## Mortalidad

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

``` sql
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

## Readmisión

Esta variable se obtiene a partir de aplicar una función de preprocesado sobre la tabla ADMISSIONS. En concreto, extraemos los identificadores de paciente y admisión, y las fechas de alta e ingreso, devolviendo el resultado ordenado ascendiemente por identificador de paciente. Se realiza mediante la siguiente consulta sencilla. 

```sql
SELECT hadm_id, subject_id, admittime, dischtime
FROM admissions
ORDER BY subject_id
```

Esta función itera sobre la tabla, ordenada ascendientemente por identificador de paciente, para encontrar el tiempo entre el alta y la próxima admisión de un mismo paciente, clasificando el resultado en los grupos descritos anteriormente.

```python
def extract_readmissions(admissions_data):
    total_readmissions = [];
    for index in range(admissions_data.shape[0] - 1):
        if admissions_data.ix[index].subject_id == admissions_data.ix[index + 1].subject_id:
            if (admissions_data.ix[index + 1].admittime - admissions_data.ix[index].dischtime).days 			< (30 * 6):
                readmission = '0-6 months';
            else:
                readmission = '6+ months';
        else:
            readmission = 'no-readmission';
    
        total_readmissions.append({
                    'hadm_id': admissions_data.ix[index].hadm_id, 
                    'readmission': readmission
                    });
    
    return pd.DataFrame(total_readmissions);
```

Tras realizar este proceso, obtenemos la siguiente distribución de resultados.

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

| Readmisión    | Cantidad | Porcentaje |
| ------------- | -------- | ---------- |
| No readmitido |          |            |
| 6+ meses      |          |            |
| 0 - 6 meses   |          |            |







