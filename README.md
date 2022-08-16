# WordCloud of an IMDb list 
    #### Video Demo:  <URL HERE>
    #### Description: The project aims to delve into the world of data analysis, since it is a developing area for both future career options as well as individuals' interests.
    Thus, the project will try to output a visual graphic related to movies, since the latter is another area I am interested in.

    I have started by researching if Imdb has an official API, and it seems that it does not(source: https://github.com/kunalnagarco/imdb-scraper#are-you-scraping-the-imdb-website-for-results)
    Thus, I have found a library that assists in parsing the data found on the website. https://cinemagoer.github.io/. After reading the documentation and making several small tests to get a feel for the usage of the library, I encountered the first problem. The documentations does not clearly define a method for iterating over an IMDb list, which was my main goal in gathering data for the wordcloud. Luckily I found the conversation on the library's github regarding lists and found user aapjeisbaas that developed upon the library's initial code and comitted some code that helped in iterating over lists.(https://github.com/cinemagoer/cinemagoer/pull/273/commits/578edfaa80eb1a8f9c8e380da53c5384216fb96d)
    After making sure that I have understood the usage of the code, I wondered
    TODO
    1. research api of imdb or imdb library?
        Yes. Because IMDb doesn't have an official API, yet. https://github.com/kunalnagarco/imdb-scraper
        Cinemagoer module
    2. store plots? 
        yes, in a csv, which will need to be accessed to pull the data
    3. research world cloud libraries
        https://www.geeksforgeeks.org/generating-word-cloud-python/
    4. learn to use the api/libraries
        Read the documentations
    5. define what the project will output
        a csv file( useful for later use maybe?), an image for wordlcloud
    6. define what the functions need to do
        1. get list
        2. create csv file
        3. read csv file and retrieve the descriptions
        4.output wordcloud


Your README.md file should be minimally multiple paragraphs in length, and should explain what your project is, what each of the files you wrote for the project contains and does, and if you debated certain design choices, explaining why you made them. Ensure you allocate sufficient time and energy to writing a README.md that documents your project thoroughly. Be proud of it! If it is too short, the system will reject it.