import creatingDictionary
dataset=creatingDictionary.test()
def populate():
    directorDictionary={}
    for film in dataset:
        if not(film['Director'] in directorDictionary):
            directorDictionary[film['Director']]=0
    return directorDictionary

def assignCount():
    directorsDictionary=populate()
    count=0
    for film in dataset:
        if (film['Director'] in directorsDictionary):
            directorsDictionary[film['Director']]+=1



    return directorsDictionary

def assignTotalRevenue():
    directorsDictionary=populate()
    count=0
    for film in dataset:
        if (film['Director'] in directorsDictionary):
            directorsDictionary[film['Director']]+=float(film['BoxOffice'])



    return directorsDictionary

def assignAverageRevenue():
    directorsTotal=assignTotalRevenue()
    directorsCount=assignCount()
    directorsAverage=populate()
    for director in directorsAverage:
        directorsAverage[director]=directorsTotal[director]/directorsCount[director]

    return directorsAverage




    



    
