import streamlit as st
import pandas as pd
import pickle
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
from sim import similarity

st.title('Proyecto Individual Cohorte 10')

st.markdown('***')

#Importamos las columnas que nos interesan 
columns = ['release_month', 'release_day', 'production_countries', 'belongs_to_collection', 'revenue', 'production_companies', 'title', 'budget', 'return', 'release_year' ]

#Cargamos el dataframe solo con esas columnas

df = pd.read_csv('./movies_clean.csv', usecols = columns)

st.title('Preguntas sobre nuestros datos')

st.subheader('¿Cuantas peliculas se estrenaron en el siguiente mes? :')
mes = st.text_input('Ingrese el nombre del mes:', 'por ejemplo: enero')

def peliculas_mes(mes : str):
    conteo_mes = (df['release_month'] == mes).sum()
    return mes, conteo_mes


valores = peliculas_mes(mes)
st.write('La cantidad de peliculas que se estrenaron en ', valores[0], ' fue: ', valores[1])

st.subheader('¿Cuantas peliculas se estrenaron en el siguiente dia de la semana? :')
dia = st.text_input('Ingrese el nombre del dia:', 'por ejemplo: lunes')

def peliculas_dia(dia : str):
    conteo_dia = (df['release_day'] == dia).sum()
    return dia, conteo_dia


valores = peliculas_dia(dia)
st.write('La cantidad de peliculas que se estrenaron el dia ', valores[0], ' fue: ', valores[1])

st.subheader('¿Cual es la cantidad de peliculas, ganancia total y ganancia promedio que tuvo la siguiente franquicia? :')
franquicia = st.text_input('Ingrese el nombre de la franquicia que desea conocer los datos', 'Nombre de la franquicia')

def franquicias(franquicia : str):
    franquicia_df = df[(df['belongs_to_collection'].notna()) & (df['belongs_to_collection'].str.contains(franquicia))]
    #utilizamos el comando .empty para saber si el dataframe esta vacio
    if franquicia_df.empty:
        return 'No se encontró la franquicia'
    #si no esta vacio continua con el codigo
    cantidad = franquicia_df.shape[0]
    ganancia_total = franquicia_df['revenue'].sum()
    ganancia_promedio = ganancia_total / cantidad

    return franquicia, cantidad, ganancia_total, ganancia_promedio


valores = franquicias(franquicia)
st.write('La franquicia ', valores[0], ' tiene ', valores[1], ' peliculas, su ganancia total fue de U$D', valores[2], ' y su ganancia promedio del ', valores[3])

st.subheader('¿Cuantas peliculas se produjeron en el siguiente pais? :')
pais = st.text_input('Ingrese un pais:', 'Por ejemplo United States of America')

def peliculas_pais(pais : str):
    cantidad = 0
    for lista_paises in df['production_countries']:
        try:
            if pais in lista_paises:
                cantidad += 1
        except TypeError:
            continue
    return pais, cantidad


valores = peliculas_pais(pais)
st.write('En ', valores[0], ' se produjeron  ', valores[1])

st.subheader('¿Cual fue la ganancia total y la cantidad de peliculas que produjo la siguiente productora? :')
productora = st.text_input('Ingrese el nombre de una productora:', 'Por ejemplo Pixar Animation Studios')

def productoras(productora):
    df_filtrado = df[df['production_companies'].apply(lambda x: productora in str(x))]
    cantidad = len(df_filtrado)
    ganancia = df_filtrado['revenue'].sum()
    return productora, ganancia, cantidad


valores = productoras(productora)
st.write('La productora ', valores[0], ' tuvo una ganancia total de U$D', valores[1], ' y produjo ', valores[2])

st.subheader('Ingrese el nombre de una pelicula para conocer cual fue su inversion, ganancia, retorno y el año en que se lanzo:')
pelicula = st.text_input('Ingrese el nombre de una pelicula:', 'Por ejemplo Toy Story')

def retorno_pelicula(pelicula:str):

    df_pelicula = df[df['title'] == pelicula] 
    inversion = df_pelicula['budget'].iloc[0]
    ganancia = df_pelicula['revenue'].iloc[0]
    retorno = df_pelicula['return'].iloc[0]
    anio = df_pelicula['release_year'].iloc[0]
    
    return pelicula, inversion, ganancia, retorno, anio

ejecutar = st.button("Ejecutar")
if ejecutar:
    valores = retorno_pelicula(pelicula)
    st.write('La pelicula ', valores[0], ' realizo una inversion de ', valores[1], ' tuvo una ganancia de ', valores[2], ' con un retorno del ', valores[3], ' y se estreno en el año ', valores[4])


#MODELO DE PREDICCION 

# Cargar datos y modelos necesarios
# movies_crop = df['title'].head(20000).to_frame()  # Asegúrate de tener df definido previamente
# cv = CountVectorizer(max_features=1000, stop_words='english')
# vector = cv.fit_transform(movies_crop['title']).toarray()
# similarity = cosine_similarity(vector)

movies_dict = pickle.load(open('listado.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Función de recomendación
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Interfaz de usuario con Streamlit
st.subheader('Lista de recomendaciones:')

movie_name = st.selectbox(
    'Seleccione una película',
    movies['title'].values
)

recomendar = st.button("Recomendar")
if recomendar:
    recommendations = recommend(movie_name)
    for i in recommendations:
        st.write(i)