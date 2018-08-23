# Conclusiones

Se ha desarrollado satisfactoriamente un modelo predictivo de la mortalidad extra-hospitalaria con una buena capacidad diagnóstica. 

Este proyecto ha comportado la exploración de una gran base de datos con muchos tipos de valores diferentes: numéricos, categóricos, fechas, campos de texto, etc, y el tratamiento de ellos para ser procesados por la red neuronal.

Las variables necesarias para realizar predicciones con este modelo son fáciles de obtener y se recopilan de forma rutinaria, lo cual permitiría un uso extendido del algoritmo en la práctica médica, aunque siempre considerando que comete ciertas inexactitudes. Podría llegar a emplearse como segunda opinión médica, para confirmar o cancelar el alta de pacientes en unidad de cuidados intensivos. 

La mayor carga de trabajo ha recaído sobre la selección, extracción y preprocesado de las variables empleadas por el modelo. Este proceso a llevado al descarte de ciertas variables, por ejemplo la presión venosa central, por disponerse de pocas muestras.

Por otra parte, gracias a la optimización bayesiana de hiperparámetros ha sido relativamente sencillo, auque lento, encontrar la configuración de red que asegura un resultado óptimo. 

Como mejoras, se podrían extraer nuevas variables ignoradas en este estudio. Por ejemplo, en la base de datos se almacenan las notas médicas como campo libre de texto para cada paciente, las cuales incluyen anotaciones realizadas por el personal médico acerca del historial de los pacientes o situaciones médicas particulares. La extracción de estas características supondría un amplio trabajo de minería de textos que cae fuera del alcance de este proyecto.

Así mismo, sería posible desarrollar una pequeña interfaz o página web que permita realizar predicciones empleando el modelo diseñado. Esta interfaz permitiría al personal médico la introducción de las variables necesarias y devolvería la probabilidad de mortalidad del paciente. 

