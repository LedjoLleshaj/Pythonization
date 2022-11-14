film_directors = {
    'The Godfather': 'Francis Ford Coppola',
    'The Shawshank Redemption': 'Frank Darabont',
    'The Dark Knight': 'Christopher Nolan',
}
#print(film_directors.get('The Godfather')) # Francis Ford Coppola
#print(film_directors.get("Bad Boys", "No director found")) # No director found
film_directors.setdefault("Bad Boys", "Michael Bay") # if key is not found, adds it
print(film_directors) 

film_directors.setdefault("Bad Boys", "Second time will not work") # if key is found, does not change it
print(film_directors)