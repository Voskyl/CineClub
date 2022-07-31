from PySide2 import QtWidgets, QtCore

from movie import get_movies, Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()
    
    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)  # type: ignore

        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)  # type: ignore
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.le_movieTitle)
        self.layout.addWidget(self.btn_addMovie)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_removeMovies)

    def populate_movies(self):
        movies = get_movies()
        
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)   # type: ignore # permet d'attacher l'instance du film
            self.lw_movies.addItem(lw_item)  # type: ignore

    def setup_connections(self):
        self.le_movieTitle.returnPressed.connect(self.add_movie)  # type: ignore
        self.btn_addMovie.clicked.connect(self.add_movie)  # type: ignore
        self.btn_removeMovies.clicked.connect(self.remove_movie)  # type: ignore

    def add_movie(self):
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False

        movie = Movie(movie_title)
        if movie.add_to_movies():
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)   # type: ignore # permet d'attacher l'instance du film
            self.lw_movies.addItem(lw_item)  # type: ignore
        
        self.le_movieTitle.setText("")
        return True

    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item)) 




app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
