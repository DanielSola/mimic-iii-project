# Conclusiones

Se ha desarrollado satisfactoriamente un modelo predictivo de la mortalidad extra-hospitalaria con una buena capacidad diagnóstica. 

Este proyecto ha comportado la exploración de una gran base de datos con muchos tipos de valores diferentes: numéricos, categóricos, fechas, campos de texto, etc, y el tratamiento de ellos para ser procesados por la red neuronal.

Las variables necesarias para realizar predicciones con este modelo son fáciles de obtener y se recopilan de forma rutinaria, lo cual permitiría un uso extendido del algoritmo en la práctica médica, aunque siempre considerando que comete ciertas inexactitudes. Podría llegar a emplearse como segunda opinión médica, para confirmar o cancelar el alta de pacientes en unidad de cuidados intensivos. 

La mayor carga de trabajo ha recaído sobre la selección, extracción y preprocesado de las variables empleadas por el modelo. Este proceso a llevado al descarte de ciertas variables, por ejemplo la presión venosa central, por disponerse de pocas muestras.

Por otra parte, gracias a la optimización bayesiana de hiperparámetros ha sido relativamente sencillo, auque lento, encontrar la configuración de red que asegura un resultado óptimo. 

Como mejoras, se podrían extraer nuevas variables ignoradas en este estudio. Por ejemplo, en la base de datos se almacenan las notas médicas como campo libre de texto para cada paciente, las cuales incluyen anotaciones realizadas por el personal médico acerca del historial de los pacientes o situaciones médicas particulares. La extracción de estas características supondría un amplio trabajo de minería de textos que cae fuera del alcance de este proyecto.

Así mismo, sería posible desarrollar una pequeña interfaz o página web que permita realizar predicciones empleando el modelo diseñado. Esta interfaz permitiría al personal médico la introducción de las variables necesarias y devolvería la probabilidad de mortalidad del paciente. 

El mayor coste económico de este proyecto recae en el sueldo del Ingeniero que ha desarrollado la red neuronal que llevará a cabo la predicción de mortalidad. De esta manera, la mayor parte del coste económico irá destinada a pagar sus horas de trabajo, y otra pequeña parte irá a parar el coste indirecto del proyecto, consistente principalmente en el equipo informático que utiliza. 

## Costes directos

Son aquellos costes que pueden identificarse directamente con un objeto de costes, tal como materiales o mano de obra destinada al proyecto.

En este caso, el coste directo es completamente el sueldo del personal, al cual consideramos un trabajador autónomo que factura por horas. 

Consideramos que el proyecto lo ha llevado a cabo un único desarrollador, con una facturación de 30€/h y una dedicación de 320, dando de esta manera un coste directo total de 9600€.

## Costes indirectos

El coste indirecto del proyecto corresponde al equipo informático empleado.

No existen costes asociados al software, ya que Python es un lenguaje de programación gratuito de código abierto y el sistema operativo del equipo es Elementary OS loki 0.4.1, distribución de Linux basada en Ubuntu y también gratuita. 

En cuando al hardware, se emplea un ordenador portátil del siguiente modelo:

+ Toshiba Satellite Pro A50-D-1FZ Intel Core i7-7500U/8GB/256GB SSD/15.6" 

Su coste es de 695€. Considerando un periodo de amortización de tres años y un periodo de uso de cuatro meses, el coste indirecto de hardware es de 77.22 €.

De esta manera, el coste total del proyecto computado como la suma de costes directos e indirectos es de alrededor de 9700€.