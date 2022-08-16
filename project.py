from imdb import Cinemagoer
import csv

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# get a movie
movies = ia.search_movie('dr. strangelove') #searching by name
movie = movies[0].movieID #retrieves the ID
film=ia.get_movie(movies[0].movieID) #gets movie data
filmdata=film['plot'][0] #retreives the 1st plot from imdb
results = ia.get_movie_list("ls057339370") #pass the list to a variable
# for i in results:
#   MovieTitle=ia.get_movie(i.movieID)
#   Description=MovieTitle['plot'][0]
#   print(MovieTitle)

with open("plots.csv", "w") as file:
     writer=csv.DictWriter(file, fieldnames=["movie","plot"]) #variable for library to which we pass the new columns
     writer.writerow({"movie": "Movie", "plot": "Plot"}) #adds the headers
     for i in results:
        MovieTitle=ia.get_movie(i.movieID)
        Description=MovieTitle['plot'][0]
        writer.writerow({"movie":MovieTitle,"plot":Description}) #writes dictionary for each line
#def main():

#def function_1():

#def function_2():

#def function_n():
