import creatingDictionary
dataset=creatingDictionary.test()
def populate():
    writerDictionary={}
    for film in dataset:
        if not(film['Writer'] in writerDictionary):
            writerDictionary[film['Writer']]=0
    return writerDictionary

def assignCount():
    writerDictionary=populate()
    count=0
    for film in dataset:
        if (film['Writer'] in writerDictionary):
            writerDictionary[film['Writer']]+=1



    return writerDictionary

def assignTotalRevenue():
    writerDictionary=populate()
    count=0
    for film in dataset:
        if (film['Writer'] in writerDictionary):
            writerDictionary[film['Writer']]+=float(film['BoxOffice'])



    return writerDictionary

def assignAverageRevenue():
    writerTotal=assignTotalRevenue()
    writerCount=assignCount()
    writerAverage=populate()
    for writer in writerAverage:
        writerAverage[writer]=writerTotal[writer]/writerCount[writer]

    return writerAverage






    



    
