import os
#Functions in this file converts the dataset which is in text csv format into
# a list of Python dictionaries.
DATADIR = ""
DATAFILE = "TrainingData.txt"


def parse_file(datafile):
    '''
    parse_file(number)->float
    '''
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                break
            fields = line.split()
            entry = {}

            for i,value in enumerate(fields):
                entry[header[i].strip()]=value.strip()

            data.append(entry)
            counter+=1

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    return d
  
test()
