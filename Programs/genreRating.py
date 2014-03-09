import creatingDictionary
dataset=creatingDictionary.test()
def populate():
    genreDictionary={}
    for film in dataset:
        if not(film['Genre'] in genreDictionary):
            genreDictionary[film['Genre']]=0
    return genreDictionary

def assignCount():
    genresDictionary=populate()
    count=0
    for film in dataset:
        if (film['Genre'] in genresDictionary):
            genresDictionary[film['Genre']]+=1



    return genresDictionary

def assignTotalRevenue():
    genresDictionary=populate()
    count=0
    for film in dataset:
        if (film['Genre'] in genresDictionary):
            genresDictionary[film['Genre']]+=float(film['BoxOffice'])



    return genresDictionary

def assignAverageRevenue():
    genresTotal=assignTotalRevenue()
    genresCount=assignCount()
    genresAverage=populate()
    for genre in genresAverage:
        genresAverage[genre]=genresTotal[genre]/genresCount[genre]

    return genresAverage




    



    
