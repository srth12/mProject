import os
#Functions in this file converts the dataset which is in text csv format into
# a list of Python dictionaries.
DATADIR = ""
DATAFILE = "TrainingData.txt"


def parse_file(datafile):
    '''
    This function converts the dataset(comprising of information regarding
    around 2000 films) in csv format to a list of python dictionaries.    
    '''
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        #The header variable is a list which stores the names of the keys
        #in our output list of dictionaries.
        #The first line in the database is the names of the featues separated
        #by commas. ie a python string.
        #Calling split on this string with delimiter comma(",") returns the
        #names of the features as a list
        counter = 0
        for line in f:
            if counter == 100:
                break
            fields = line.split()
            #The values themselves are separated by spaces in the dataset.
            #Space is the default argument for the split method. So there is no
            #need to provide the parameter here.
            #Now the values of the attributes for a single film is stored as a
            #list in the fields variable
            entry = {}

            for i,value in enumerate(fields):
                entry[header[i].strip()]=value.strip()
                #Strip method removes the unnecessary whitespaces from the
                #the beginning and end of a string.
                #This for loop populates the list of dictionaries,
                #by assigning the appropriate values
                

            data.append(entry)
            counter+=1

    return data


def test():
    # The test function is the driver program.
    #This runs the parse_file method on our input dataset 
    #by calling it with the proper arguments.
    
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    return d
  
test()
