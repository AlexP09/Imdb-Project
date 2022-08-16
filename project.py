from imdb import Cinemagoer
import csv

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# get a movie
movies = ia.search_movie('dr. strangelove') #searching by name
movie = movies[0].movieID #retrieves the ID
film=ia.get_movie(movies[0].movieID) #gets movie data
filmdata=film['plot'][0] #retreives the 1st plot from imdb

#print(film)

with open("plots.csv", "a") as file:
    
    writer=csv.DictWriter(file, fieldnames=["movie","plot"])
    writer.writerow({"movie": film, "plot":filmdata})
#def main():

#def function_1():

#def function_2():

#def function_n():
