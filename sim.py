import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

columns = ['release_month', 'release_day', 'production_countries', 'belongs_to_collection', 'revenue', 'production_companies', 'title', 'budget', 'return', 'release_year' ]

#Cargamos el dataframe solo con esas columnas

df = pd.read_csv('./movies_clean.csv', usecols = columns)

movies_crop = df['title'].head(17000).to_frame()  # Asegúrate de tener df definido previamente
cv = CountVectorizer(max_features=1000, stop_words='english')
vector = cv.fit_transform(movies_crop['title']).toarray()
similarity = cosine_similarity(vector)

