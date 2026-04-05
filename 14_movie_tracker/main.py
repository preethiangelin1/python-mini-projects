import os
import json

FILENAME = "movies.json"

movies = []

def load_movies():
    if os.path.exists(FILENAME):
        with open(FILENAME) as f:
            return json.load(f)
    return []
        
def save_movies(movies):
    with open(FILENAME, "w") as f:
        json.dump(movies, f, indent=2)

def add_movie(user_choice_title, user_choice_genre, user_choice_rating):

    movies = load_movies()
    movie = {
        "title": user_choice_title,
        "genre": user_choice_genre,
        "rating": user_choice_rating
    }

    movies.append(movie)

    save_movies(movies)

def view_movies():
    movies = load_movies()
    for movie in movies:
        print(f"Title:{movie['title']}\nGenre:{movie['genre']}\nRating:{movie['rating']}\n")

def search_movies(title):
    movies = load_movies()
    for movie in movies:
        if movie["title"] == title:
            print(movie)

def main():
    while True:
        print("1.Add a movie\n2.View all movies\n3.Search movies by title or genre\n4.Exit the app")
        print()
        user_input = int(input("Choose a number between (1-4): \n"))
        if user_input == 1:
            user_choice_title = input("Enter the movie Title: ")
            user_choice_genre = input("Enter the movie Genre: ")
            user_choice_rating = int(input("Enter the movie Rating(out of 10): "))
            add_movie(user_choice_title, user_choice_genre, user_choice_rating)

        elif user_input == 2:
            view_movies()
        elif user_input == 3:
            search_title = input("Enter the title to be searched: ")
            search_movies(search_title)
        elif user_input == 4:
            print("Exiting the app...")
            break


if __name__ == "__main__":
    main()