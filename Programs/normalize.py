import genreRating
def normalize():
    dictionary=genreRating.assignAverageRevenue()
    output=genreRating.populate()
    total=sum(dictionary.values())
    minimum=min(dictionary.values())
    maximum=max(dictionary.values())
    length=len(dictionary)
    average=total/length
    maximin=maximum-minimum
    for genre in output:
        norm=(dictionary[genre]-average)/maximin
        output[genre]=norm

    return output
    

