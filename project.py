from imdb import Cinemagoer
import csv
import wordcloud
import matplotlib.pyplot as plt
import sys
import re
# create an instance of the Cinemagoer class
ia = Cinemagoer()
results=[]

def main():
    print("Have you ever been curious to see what your favourite movies or tv-shows have in common?\nNow you can visualize the main topics that your motion pictures share!")
    prompt=input("Please input a public list URL: ")
    store_source_data(get_list(prompt)) 
    read_source_data() 
    build_wordcloud(read_source_data())
    
def get_list(Imdblist):
    if not re.search(r"ls[0-9]*",Imdblist):
        sys.exit("Invalid format\nYou may want to check and see if your link contains a string starting with ls")
    else:
        listinput=re.search(r"(ls[0-9]*)",Imdblist).group(1)
    results = ia.get_movie_list(listinput)
    return results

def store_source_data(IMDBlist):
    with open("plots.csv", "w", newline='') as file: #writes a csv in which we'll store the name of the movies and the description
     writer=csv.DictWriter(file, fieldnames=["movie","plot"]) #variable for library to which we pass the new columns
     writer.writerow({"movie": "Movie", "plot": "Plot"}) #adds the headers
     for i in IMDBlist:
        MovieTitle=ia.get_movie(i.movieID) #gets movie Data for each element in the list
        Description=MovieTitle['plot'][0] #retrieves the 1st plot from each element of the list
        writer.writerow({"movie":MovieTitle,"plot":Description}) #writes dictionary for each line

def read_source_data():
    description=""
    with open ("plots.csv", "r", newline='') as datasource: #opens the file saved beforehand
                reader=csv.DictReader(datasource) #variable for library to which we pass the temporary file
                for line in reader: #reiterates over line in csv-each new line is a dictionary
                    description +=" "+line['Plot'].lower()+" "
    return description

def build_wordcloud(words):   
    wordcloudMovies=wordcloud.WordCloud(width = 1000, height = 1000,
                background_color =None,
                stopwords = None,
                mode="RGBA",
                min_font_size = 5).generate(words).to_file("Image.png")
    plt.figure()
    plt.imshow(wordcloudMovies, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()



