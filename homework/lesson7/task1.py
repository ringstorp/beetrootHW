"""A simple function.

Create a simple function called favorite_movie, which takes a string containing
the name of your favorite movie. The function should then print "My favorite movie is named {name}"
"""
def movie_asker():

    favorite_movie = input("What is your favorite movie?\n")
    print(f"My favorite movie is named {favorite_movie}")

movie_asker()
