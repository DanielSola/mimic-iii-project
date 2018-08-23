# Variable a predecir

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

Observamos que las clases se encuentran aproximadamente compensadas, lo cual permitirá un diseño eficaz de red neuronal y su posterior evaluación. 

