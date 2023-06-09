## <h1 align=center> **Sistema de Recomendación de Peliculas** </h1>
# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

En este proyecto realicé un proceso de Extracción, Transformación y Carga (ETL) de datos junto con un Análisis Exploratorio de Datos (EDA) a un archivo CSV de películas. Luego construí una API para acceder y consultar los datos de las películas utilizando diferentes funciones. Además realicé un deploy en la plataforma de streamlit para tener una mejor interfaz grafica y un manejo más intuitivo de  nuestra aplicación. 
<br/>

## **Interfaz Grafica**

Puedes acceder a la web de streamlit a través del siguiente link: https://martinez-pablo-proyect-henry-main-k6ao6a.streamlit.app/
<br/>

## **Funciónes desarrolladas en el proyecto**

+ def peliculas_mes(mes):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes (nombre del mes, en str, ejemplo 'enero') historicamente'''
    return {'mes':mes, 'cantidad':respuesta}

+ def peliculas_dia(dia):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia (de la semana, en str, ejemplo 'lunes') historicamente'''
    return {'dia':dia, 'cantidad':respuesta}

+ def franquicia(franquicia):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    return {'franquicia':franquicia, 'cantidad':respuesta, 'ganancia_total':respuesta, 'ganancia_promedio':respuesta}

+ def peliculas_pais(pais):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''
    return {'pais':pais, 'cantidad':respuesta}

+ def productoras(productora):
    '''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron'''
    return {'productora':productora, 'ganancia_total':respuesta, 'cantidad':respuesta}

+ def retorno(pelicula):
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'''
    return {'pelicula':pelicula, 'inversion':respuesta, 'ganacia':respuesta,'retorno':respuesta, 'anio':respuesta}

+ def recomendacion('titulo'):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista de 5 valores'''
    return {'lista recomendada': respuesta}
<br/>

Si desea explorar la fuente de los datos con los datos originales sin transformaciones los invitamos a indagar el siguiente link:
## **Fuente de datos**

+ [Dataset](https://drive.google.com/file/d/1Rp7SNuoRnmdoQMa5LWXuK4i7W1ILblYb/view?usp=sharing): Archivo con los datos que requieren ser procesados, tengan en cuenta que hay datos que estan anidados (un diccionario o una lista como valores en la fila).
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit#gid=0): Diccionario con algunas descripciones de las columnas disponibles en el dataset.


## **Datos de contacto**

+ Gmail: martinezpabloagustin1@gmail.com
+ Whatsapp: +54 3875066128