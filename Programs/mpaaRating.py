import creatingDictionary
dataset=creatingDictionary.test()
def populate():
    mpaaDictionary={}
    for film in dataset:
        if not(film['Rated'] in mpaaDictionary):
            mpaaDictionary[film['Rated']]=0
    return mpaaDictionary

def assignCount():
    mpaaDictionary=populate()
    count=0
    for film in dataset:
        if (film['Rated'] in mpaaDictionary):
            mpaaDictionary[film['Rated']]+=1



    return mpaaDictionary

def assignTotalRevenue():
    mpaaDictionary=populate()
    count=0
    for film in dataset:
        if (film['Rated'] in mpaaDictionary):
            mpaaDictionary[film['Rated']]+=float(film['BoxOffice'])



    return mpaaDictionary

def assignAverageRevenue():
    mpaaTotal=assignTotalRevenue()
    mpaaCount=assignCount()
    mpaaAverage=populate()
    for mpaa in mpaaAverage:
        mpaaAverage[mpaa]=mpaaTotal[mpaa]/mpaaCount[mpaa]

    return mpaaAverage






    



    
