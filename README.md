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
    After seeing that the code works as intended, using one list, I needed to think of various tests, raise exceptions and implement them.
    TODO
    1. raise exceptions
    2. write tests
    3. video url