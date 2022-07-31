from pathlib import Path
import json
import logging

CUR_DIR = Path(__file__).resolve().parent
DATA_FILE = CUR_DIR /"data" / "movies.json"

logging.basicConfig(level=logging.INFO,
                    # filename=CUR_DIR/"movie.log",
                    format='%(asctime)s - %(levelname)s - %(message)s')


def get_movies():
    movie_titles = Movie._get_movies()
    return [Movie(f"{movie_title}") for movie_title in movie_titles]


class Movie:
    def __init__(self, title: str):
        self.title = title.title()
    
    def __str__(self):
        return self.title

    @classmethod
    def _get_movies(cls):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, movies: list[str]):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.info(f"{self.title} est déjà sauvegardé !")
            return False

    def remove_from_movies(self):
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.info(f"{self.title} n'est pas sauvegardé !")
            return False




if __name__ == "__main__":
    film_1 = Movie("harry potter 2")
    # print(film_1.title)
    # print(film_1)
    # film_1._write_movies(["Barry London", "Le Seigneur des Anneaux"])
    print(film_1._get_movies())
    # film_1.add_to_movies()
    # film_1.remove_from_movies()
    print(get_movies()[0])