import sqlite3
import json

with sqlite3.connect("./netflix.db", check_same_thread=False) as connection:
    cursor = connection.cursor()


def title_func(title):
    #Принимает title и возвращает данные в формате json
    sqlite_query = 'SELECT *' \
                   'FROM netflix' \
                   'ORDER BY date_added DESC'

    cursor.execute(sqlite_query)

    for row in cursor.fetchall():
        if title.lower() == row[2]:
            title_data = {
                          "title": row[2],
                          "country": row[5],
                          "release_year": row[7],
                          "genre": row[1],
                          "description": row[12]
                          }
            title_json = json.dumps(title_data)
            return title_json


def from_to_func(from_year, to_year):
    # Принимает диапазон лет (от, до) и возвращает данные в формате json
    sqlite_query = 'SELECT `title`, `release_year`' \
                   'FROM netflix' \
                   f'WHERE `release_year` BETWEEN {from_year} AND {to_year} LIMIT 100'

    cursor.execute(sqlite_query)
    movie_list = []

    for row in cursor.fetchall():
        movie_data = {
                      "title": row[0],
                      "release_year": row[1],
                     }
        movie_list.append(movie_data)

    movie_json = json.dumps(movie_list)
    return movie_json


def rating_func(rating_list):
    # Осуществляет поиск по рейтингу и возвращает данные в формате json
    sqlite_query = "SELECT * " \
                   "FROM netflix " \
                   "WHERE rating != '' " \
                   f"AND rating IN {rating_list} LIMIT 100"

    cursor.execute(sqlite_query)
    movie_list = []

    for row in cursor.fetchall():
        movie_data = {
                      "title": row[2],
                      "rating": row[8],
                      "description": row[12],
                     }
        movie_list.append(movie_data)

    movie_json = json.dumps(movie_list)
    return movie_json


def genre_func(genre):
    # Осуществляет поиск по жанру и возвращает данные в формате json
    sqlite_query = "SELECT `title`, `description`, `listed_in`, `date_added` " \
                   "FROM netflix " \
                   f"WHERE `listed_in` LIKE ('%{genre.title()}%') " \
                   "ORDER BY `date_added` DESC " \
                   "LIMIT 10"

    cursor.execute(sqlite_query)
    movie_list = []

    for row in cursor.fetchall():
        movie_data = {
                      "title": row[0],
                      "description": row[1],
                     }
        movie_list.append(movie_data)

    movie_json = json.dumps(movie_list)
    return movie_json


def cast_func(cast_one, cast_two):
    # Принимает двух актеров,
    # осуществляет поиск актеров которые играли с ними более 2 раз
    # и возвращает список
    sqlite_query = "SELECT `cast`" \
                   "FROM netflix " \
                   f"WHERE `cast` LIKE ('%{cast_one}%') " \
                   f"AND `cast` LIKE ('%{cast_two}%')"

    cursor.execute(sqlite_query)
    cast_list = []

    for row in cursor.fetchall():
        for cast_ in row:
            x = cast_.split(", ")
            for element in x:
                cast_list.append(element)

    match_list = []
    for cast in cast_list:
        if cast_list.count(cast) >= 3:
            match_list.append(cast)

    match_list = list(set(match_list))
    match_list.remove(cast_one)
    match_list.remove(cast_two)

    return match_list


def type_func(type, release_year, genre):
    #Принимает type, release_year, genre и возвращает данные в формате json
    sqlite_query = "SELECT `title`, `description`, `type`, `release_year`, `listed_in`" \
                   "FROM netflix " \
                   f"WHERE `type` LIKE ('%{type}%') " \
                   f"AND `release_year` LIKE ('%{release_year}%') " \
                   f"AND `listed_in` LIKE ('%{genre}%') " \
                   f"LIMIT 100"

    cursor.execute(sqlite_query)
    movie_list = []

    for row in cursor.fetchall():
        movie_data = {
                      "title": row[0],
                      "description": row[1],
                     }
        movie_list.append(movie_data)

    movie_json = json.dumps(movie_list)
    return movie_json
