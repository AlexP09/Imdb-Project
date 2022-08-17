# WordCloud of an IMDb list
from imdb import Cinemagoer, IMDbError
import csv
import wordcloud
import matplotlib.pyplot as plt
import sys
import re

# create an instance of the Cinemagoer class
try:
    ia = Cinemagoer()
except IMDbError as error:
    print("Something went wrong. Please contact project creator.")
results = []  # blank variable
# Welcome the user, obtaing the input, and call the rest of the functions
def main():
    print(
        "Have you ever been curious to see what your favourite movies or tv-shows have in common?\nNow you can visualize the main topics that your motion pictures share!"
    )
    prompt = input("Please input a public list URL: ")
    store_source_data(get_list(prompt))
    read_source_data()
    build_wordcloud(read_source_data())
    print("Done!")


# Receives the list provided by the user, makes sure that the list has the correct format using regex and storing the IMDb data to the blank variable
def get_list(Imdblist):
    if not re.search(r"ls[0-9]*", Imdblist):
        sys.exit(
            "Invalid format\nYou may want to check and see if your link contains a string starting with ls"
        )
    else:
        listinput = re.search(r"(ls[0-9]*)", Imdblist).group(1)
    try:
        results = ia.get_movie_list(listinput)
        return results
    except IMDbError as error:
        print("Something went wrong. Please contact project creator.")


# Writes a csv where we will store the name and description of the elements in the list provided by the user(parsing with Cinemagoer)
def store_source_data(IMDBlist):
    if IMDBlist==[]:
        sys.exit(
            "No elements could be retrieved from the URL given. Please make sure that the list is public!"
        )
    with open("plots.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["movie", "plot"])
        writer.writerow({"movie": "Movie", "plot": "Plot"})
        for i in IMDBlist:
            try:
                MovieTitle = ia.get_movie(i.movieID)
                Description = MovieTitle["plot"][0]
                writer.writerow({"movie": MovieTitle, "plot": Description})
            except IMDbError as error:
                print("Something went wrong. Please contact project creator.")
            except KeyError:
                Description=""


# Open the csv file and retrieves only the descriptions (at this point) and stores them in a long string-necessary for wordcloud input
def read_source_data():
    description =""
    with open(
        "plots.csv", "r", newline=""
    ) as datasource:  # opens the file saved beforehand
        reader = csv.DictReader(
            datasource
        )  # variable for library to which we pass the temporary file
        for line in reader:  # reiterates over line in csv-each new line is a dictionary
            description += " " + line["Plot"].lower() + " "
    return description


# Builidng the wordcloud file using as few parameters due to code running time
def build_wordcloud(words):
    wordcloudMovies = (
        wordcloud.WordCloud(
            width=1000,
            height=1000,
            background_color=None,
            stopwords=None,
            mode="RGBA",
            min_font_size=5,
        )
        .generate(words)
        .to_file("Image.png")
    )
    plt.figure()
    plt.imshow(wordcloudMovies, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
