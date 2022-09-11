from flask import Flask, request, render_template
from utils import title_func, from_to_func, rating_func, genre_func


app = Flask(__name__)


@app.route("/movie/<title>")
def view_title(title):
    """Вьюшка для вывода данных про фильм"""
    movie_info = title_func(title)
    return render_template('movie_info.html', movie_info=movie_info, title=title)


@app.route("/movie/<from_year>/to/<to_year>")
def view_movie_list(from_year, to_year):
    """Вьюшка для вывода фильмов по диапазону"""
    movie_list = from_to_func(from_year, to_year)
    return render_template('movie_list.html', movie_list=movie_list, from_year=from_year, to_year=to_year)


@app.route("/rating/<rating>")
def view_movie_rating(rating):
    """Вьюшка для вывода фильмов по рейтингу"""
    rating_list = ()
    if rating == 'children':
        rating_list = ('G', '')
    elif rating == 'family':
        rating_list = ('G', 'PG', 'PG-13')
    elif rating == 'adult':
        rating_list = ('R', 'NC-17')
    # else:

    movie_list = rating_func(rating_list)
    return render_template('movie_by_rating.html', movie_list=movie_list, rating=rating)


@app.route("/genre/<genre>")
def view_movie_genre(genre):
    """Вьюшка для вывода фильмов по жанру"""
    movie_list = genre_func(genre)
    return render_template('movie_by_genre.html', movie_list=movie_list, genre=genre)


if __name__ == '__main__':
    app.run()
