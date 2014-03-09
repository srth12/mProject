import creatingDictionary
dataset=creatingDictionary.test()
def populate():
    actorDictionary={}
    for film in dataset:
        if not(film['actors1'] in actorDictionary):
            actorDictionary[film['actors1']]=0

return actorDictionary
