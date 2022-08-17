# WordCloud of an IMDb list 
    #### Video Demo:  <URL HERE>
    #### Description: The project aims to delve into the world of data analysis, since it is a developing area for both future career options as well as individuals' interests.
    Thus, the project will try to output a visual graphic related to movies, since the latter is another area I am interested in.
    ![Alt text](Image.png)
    I have started by researching if Imdb has an official API, and it seems that it does not(source: https://github.com/kunalnagarco/imdb-scraper#are-you-scraping-the-imdb-website-for-results)
    Thus, I have found a library that assists in parsing the data found on the website. https://cinemagoer.github.io/. After reading the documentation and making several small tests to get a feel for the usage of the library, I encountered the first problem. The documentations does not clearly define a method for iterating over an IMDb list, which was my main goal in gathering data for the wordcloud. Luckily I found the conversation on the library's github regarding lists and found user aapjeisbaas that developed upon the library's initial code and comitted some code that helped in iterating over lists.(https://github.com/cinemagoer/cinemagoer/pull/273/commits/578edfaa80eb1a8f9c8e380da53c5384216fb96d)
    After making sure that I have understood the usage of the code, I wondered how I should go about storing all the data I was pulling. Thus, I have decided to use csv files, mainly because I had a clear understanding of them during the CS50 course, and secondly because the project may be developed in the future to store multiple other things, like cast, ratings, or directors - to provide further data analysis.
    After writing the 2 functions that deal with storing and retrieving the data from the list provided by the user in a csv file. I have started researching how can wordclouds, one of the more simple data visualizations, be implemented in Python. Thus, I stumbled upon the following tutorial https://www.geeksforgeeks.org/generating-word-cloud-python/. From here I started reading the simple documentation of the wordcloud library and understadning the various parameters and ways of working : https://amueller.github.io/word_cloud/index.html
    After making several tests with wordcloud files in order to understand the library I needed to decide how the functionalities of the project need to be split into functions in a clear and logical manner. Thus, I have decided that in the main function I will prompt the user for the IMDb list and call the different functions. In order to split the code in a thoughtful manner, I decided that one function will deal with parsing over the IMDb list provided by the user - and implementing early a method of catching errors using regex, the next one will start storing the parsed data into a csv file( decision explain above-useful for later use in case of development of the project), while the following one will read the same csv file and retrieve only the formatted descriptions(at this moment) which would have been needed by the wordcloud library. Finally, the last functions deals with buildwing the wordcloud in a simple 1000x1000 transparent png image with the words passed from the descriptions as well as saving it as an image for later uses. Here another question that I have asked myself is if I should ask the user for further customization of the wordcloud image, however, I have decided against it, since the code already took a bit longer than expected when passed a list of 150 IMDb titles(https://www.imdb.com/list/ls057339370/ - 8 mins) and I decided to use as few parameters and customizations as possibles.
    After seeing that the code works as intended, using one list, I needed to think of various tests, raise exceptions and implement them. I have started raising the exceptions proposed by the Cinamegoer library whenever the module was used. Afterwards, while testing the build_wordcloud function I have seen that the library already raises by its own a ValueError whenever passed a blank list of words, thus I have deleted my own raise ValueError. During the testing phase, I tried finding ways of testing the csv, image creation part of the project since the functions do not return strings, however after reaseaching it on the web for several hours, I decided that this is something that I will have to learn further, since it involves numerous other libraries or functionality fixture of pytest:(https://stackoverflow.com/questions/3942820/how-to-do-unit-testing-of-functions-writing-files-using-pythons-unittest, https://stackoverflow.com/questions/65874869/how-to-test-python-function-used-to-generate-report-using-pytest) Thus, I resorted to only raising errors and checking for them in the test file. 
    One thing I have been able to find out while "manual" testing the project is that when I passed it a random public IMDb list found on the web it returned an error I never encountered(and it was not caught by the IMDBError exception provided by the module), that when an element(movie) of the list did not have  a plot( https://www.imdb.com/list/ls567670735/, https://www.imdb.com/list/ls507182300/), it would raise a KeyError, so I proceeded to catching this error with an except clause, setting the plot as "", since it would not alter too much the wordcloud. 


    
    TODO
    3. video url
    0-testing the output files
    I-sys arguments for top 250 movies if personal list n/a
    II-letterboxd option
    