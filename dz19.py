films_dict = {"Casablanca": 1942, "Gone with the Wind": 1939, "The Godfather": 1972, "Psycho": 1960}

def old_film(films_dict):
    name_film = None
    film_year = None
    for film, year in films_dict.items():
        if not name_film or year < film_year:
            name_film = film
            film_year = year
    return name_film

print(old_film(films_dict))