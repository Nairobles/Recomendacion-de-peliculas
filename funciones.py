import pandas as pd
from calendar import month_name
from unidecode import unidecode


df=pd.read_csv("2.base_de_datos.csv")

#Funcion que devuelve la cantidad de películas que fueron estrenadas en el mes.

def cantidad_filmaciones_mes(Mes):
    meses_espanol = {
        "enero": "01", "febrero": "02", "marzo": "03", "abril": "04",
        "mayo": "05", "junio": "06", "julio": "07", "agosto": "08",
        "septiembre": "09", "octubre": "10", "noviembre": "11", "diciembre": "12"
    }

    mes_numero = meses_espanol.get(Mes.lower())

    if mes_numero is None:
        return f"El mes '{Mes}' no es válido."

    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

    peliculas_mes = df[df['release_date'].dt.strftime('%m') == mes_numero]

    cantidad = len(peliculas_mes)

    meses_espanol_inv = {v: k for k, v in meses_espanol.items()}
    mes_espanol = meses_espanol_inv[mes_numero].capitalize()

    return f"{cantidad} película{'s' if cantidad != 1 else ''} {'fueron' if cantidad != 1 else 'fue'} estrenada{'s' if cantidad != 1 else ''} en el mes de {mes_espanol}"

#print(cantidad_filmaciones_mes("Junio"))


#Funcion que devuelve la cantidad de películas que fueron estrenadas por dia.

def cantidad_filmaciones_dia(Dia):

    dias_a_numeros = {
        'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3,
        'viernes': 4, 'sabado': 5, 'domingo': 6
    }

    dia_normalizado = unidecode(Dia.lower())

    dia_numero = dias_a_numeros.get(dia_normalizado)

    if dia_numero is None:
        return f"El día '{Dia}' no es válido."

    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

    peliculas_dia = df[df['release_date'].dt.dayofweek == dia_numero]

    cantidad = len(peliculas_dia)

    dias_espanol = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    dia_espanol = dias_espanol[dia_numero]

    return f"{cantidad} película{'s' if cantidad != 1 else ''} {'fueron' if cantidad != 1 else 'fue'} estrenada{'s' if cantidad != 1 else ''} en los días {dia_espanol}"

#print(cantidad_filmaciones_dia("domingo")) 

#Funcion que devuelve el título, el año de estreno y el score de una pelicula proporcionada por el usuario

def score_titulo(titulo_de_la_filmacion):
    pelicula = df[df['title'].str.lower() == titulo_de_la_filmacion.lower()]

    if pelicula.empty:
        return f"No se encontró la película '{titulo_de_la_filmacion}' en el dataset."

    if len(pelicula) > 1:
        pelicula = pelicula.iloc[0]
    else:
        pelicula = pelicula.squeeze()  

    titulo = pelicula['title']
    anio = pelicula['release_year']
    score = round(pelicula['popularity'],2)

    score_formateado = f"{score:.2f}"

    return f"La película '{titulo}' fue estrenada en el año {anio} con un popularidad de {score_formateado}"

#print(score_titulo("Forrest Gump"))


#Funcion que retorna el título, la cantidad de votos y el valor promedio de las votaciones.

def votos_titulo(titulo_de_la_filmacion):
    pelicula = df[df['title'].str.lower() == titulo_de_la_filmacion.lower()]

    if pelicula.empty:
        return f"No se encontró la película '{titulo_de_la_filmacion}' en el dataset."

    if len(pelicula) > 1:
        pelicula = pelicula.iloc[0]
    else:
        pelicula = pelicula.squeeze()

    titulo = pelicula['title']
    votos = pelicula['vote_count']
    promedio = pelicula['vote_average']
    anio = pelicula['release_year']

    if votos < 2000:
        return f"La película '{titulo}' no cumple con el mínimo de 2000 valoraciones. No se devuelve ningún valor."

    promedio_formateado = f"{promedio:.2f}"

    return f"La película '{titulo}' fue estrenada en el año {anio}. La misma cuenta con un total de {votos} valoraciones, con un promedio de {promedio_formateado}"

#print(votos_titulo("toy story"))


#Funcion  que retorna el éxito del actor a partir del retorno junto con la cantidad  de películas en las que ha participado 
#y el promedio de retorno

def get_actor(nombre_actor):
    peliculas_actor = df[df['cast'].str.contains(nombre_actor, case=False, na=False)]

    if peliculas_actor.empty:
        return f"No se encontraron películas para el actor '{nombre_actor}' en el dataset."

    cantidad_peliculas = len(peliculas_actor)
    retorno_total = peliculas_actor['return'].sum()
    retorno_promedio = retorno_total / cantidad_peliculas

    retorno_total_formateado = f"{retorno_total:.2f}"
    retorno_promedio_formateado = f"{retorno_promedio:.2f}"

    return (f"El actor {nombre_actor} ha participado de {cantidad_peliculas} filmaciones, "
            f"el mismo ha conseguido un retorno de {retorno_total_formateado} "
            f"con un promedio de {retorno_promedio_formateado} por filmación")

#print(get_actor("Jim Carter"))


# Funcion que retorna el nombre de un director junto con  el éxito del mismo medido a través del retorno. 
# Además se brinda el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

def get_director(nombre_director):
    peliculas_director = df[df['director'].str.contains(nombre_director, case=False, na=False)]

    if peliculas_director.empty:
        return f"No se encontraron películas para el director '{nombre_director}' en el dataset."

    retorno_total = peliculas_director['return'].sum()

    respuesta = f"Director: {nombre_director}, "
    respuesta += f"Retorno total: {retorno_total:.2f}; "
    respuesta += "Películas: "

    for _, pelicula in peliculas_director.iterrows():
        respuesta += f"Título: {pelicula['title']}, "
        respuesta += f"Fecha de lanzamiento: {pelicula['release_date']}, "
        respuesta += f"Retorno: {pelicula['return']:.2f}, "
        respuesta += f"Costo: ${pelicula['budget']:,.2f}, "
        respuesta += f"Ganancia: ${pelicula['revenue'] - pelicula['budget']:,.2f} "
        respuesta += ";"

    return respuesta

#print(get_director("Christopher Nolan"))


#Funcion que retorna 5 peliculas recomendadas a partir del titulo ingresado por el usuario, 
#utilizanco como parametro los puntos de popularidad en orden desdendente

def recomendacion(titulo):

    titulo_normalizado = titulo.lower().strip()
    

    pelicula = df[df['title'].str.lower().str.strip() == titulo_normalizado]
    
    if pelicula.empty:
        print(f"Película '{titulo}' no encontrada. Verificando títulos similares...")
        similares = df[df['title'].str.lower().str.contains(titulo_normalizado, na=False)]
        if not similares.empty:
            print("Títulos similares encontrados:")
            print(similares['title'].tolist())
        return "La película no se encuentra en la base de datos."
    
    popularidad_pelicula = pelicula['popularity'].values[0]
    
    df_temp = df.copy()
    df_temp['diff_popularity'] = abs(df_temp['popularity'] - popularidad_pelicula)
    
    recomendaciones = df_temp[df_temp['title'] != pelicula['title'].values[0]].sort_values('diff_popularity').head(5)

    titulos_recomendados = [titulo.strip().title() for titulo in recomendaciones['title']]
    
    return titulos_recomendados


#titulo_busqueda = 'Iron Man'
#recomendaciones = recomendacion(titulo_busqueda)

#print(f"Películas recomendadas similares a '{titulo_busqueda}' en popularidad:")
#for i, pelicula in enumerate(recomendaciones, 1):
#    print(f"{i}. {pelicula}")