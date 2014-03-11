import actorRating
import directorRating
import genreRating
import mpaaRating
import productionHouseRating
import writerRating
import os,sys

def normalize():
    output=[1,2,3,4,5,6]
    i=0
    features=['actorRating','directorRating','genreRating','mpaaRating']
    features=features+['productionHouseRating','writerRating']
    for name in features:
        dictionary=eval(name+'.assignAverageRevenue()')
        temp=eval(name+'.populate()')
        total=sum(dictionary.values())
        minimum=min(dictionary.values())
        maximum=max(dictionary.values())
        length=len(dictionary)
        average=total/length
        maximin=maximum-minimum
        for genre in temp:
            norm=(dictionary[genre]-average)/maximin
            temp[genre]=norm

        output[i]=temp
        i=i+1
        temp={}

    f = open('out.txt', 'w')
    print >> f, output
    f.close()

    return output
    

