import creatingDictionary
dataset=creatingDictionary.test()
def populate():
    actorDictionary={}
    for film in dataset:
        if not(film['Actors1'] in actorDictionary):
            actorDictionary[film['Actors1']]=0
        if not(film['Actors2'] in actorDictionary):
            actorDictionary[film['Actors2']]=0
        if not(film['Actors3'] in actorDictionary):
            actorDictionary[film['Actors3']]=0
    return actorDictionary

def assignCount():
    actorsDictionary=populate()
    count=0
    for film in dataset:
        if (film['Actors1'] in actorsDictionary):
            actorsDictionary[film['Actors1']]+=1
        if (film['Actors2'] in actorsDictionary):
            actorsDictionary[film['Actors2']]+=1
        if (film['Actors3'] in actorsDictionary):
            actorsDictionary[film['Actors3']]+=1


    return actorsDictionary

def assignTotalRevenue():
    actorsDictionary=populate()
    count=0
    for film in dataset:
        if (film['Actors1'] in actorsDictionary):
            actorsDictionary[film['Actors1']]+=float(film['BoxOffice'])
        if (film['Actors2'] in actorsDictionary):
            actorsDictionary[film['Actors2']]+=float(film['BoxOffice'])
        if (film['Actors3'] in actorsDictionary):
            actorsDictionary[film['Actors3']]+=float(film['BoxOffice'])

    return actorsDictionary

def assignAverageRevenue():
    actorsTotal=assignTotalRevenue()
    actorsCount=assignCount()
    actorsAverage=populate()
    for actor in actorsAverage:
        actorsAverage[actor]=actorsTotal[actor]/actorsCount[actor]

    return actorsAverage




    



    
