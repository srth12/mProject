import creatingDictionary
dataset=creatingDictionary.test()
def populate():
    productionDictionary={}
    for film in dataset:
        if not(film['Production'] in productionDictionary):
            productionDictionary[film['Production']]=0
    return productionDictionary

def assignCount():
    productionDictionary=populate()
    count=0
    for film in dataset:
        if (film['Production'] in productionDictionary):
            productionDictionary[film['Production']]+=1



    return productionDictionary

def assignTotalRevenue():
    productionDictionary=populate()
    count=0
    for film in dataset:
        if (film['Production'] in productionDictionary):
            productionDictionary[film['Production']]+=float(film['BoxOffice'])



    return productionDictionary

def assignAverageRevenue():
    productionTotal=assignTotalRevenue()
    productionCount=assignCount()
    productionAverage=populate()
    for production in productionAverage:
        productionAverage[production]=productionTotal[production]/productionCount[production]

    return productionAverage






    



    
