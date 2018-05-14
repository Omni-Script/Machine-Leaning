from __future__ import print_function
import csv
import math
filename = 'output.csv'
def readMyFile(filename):
    training_data = []
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            training_data.append(row)
    #training_data.pop(1)
    #training_data.pop(2)
    #print(len(training_data))
    #for i in range(len(training_data)):
    #    print(training_data[i][23])
    # print(Digits)
    return training_data

training_data = readMyFile(filename)

header = ["LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE", "PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5",
          "PAY_6", "BILL_AMT1", "BILL_AMT2",
          "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4",
          "PAY_AMT5", "PAY_AMT6", "default payment"]
#THE GROUPS INTO WHICH OUR DATA WAS DISCRETIZED BY K-MEANS
attributeValues = ["A", "B", "C", "D", "E", "F"],["1", "2"],["1", "2", "3", "4"],["1","2","3"],["A6", "A5", "A4", "A3", "A2", "A1"],\
                  ["L", "K", "J", "I", "H", "G"],["L", "K", "J", "I", "H", "G"],["L", "K", "J", "I", "H", "G"],["L", "K", "J", "I", "H", "G"],\
                  ["L", "K", "J", "I", "H", "G"],["L", "K", "J", "I", "H", "G"],["R", "Q", "P", "O", "N", "M"],["R", "Q", "P", "O", "N", "M"],\
                  ["R", "Q", "P", "O", "N", "M"],["R", "Q", "P", "O", "N", "M"],["R", "Q", "P", "O", "N", "M"],["R", "Q", "P", "O", "N", "M"],\
                  ["X", "W", "V", "U", "T", "S"],["X", "W", "V", "U", "T", "S"],["X", "W", "V", "U", "T", "S"],["X", "W", "V", "U", "T", "S"],\
                  ["X", "W", "V", "U", "T", "S"],["X", "W", "V", "U", "T", "S"],["1","0"]
# probability of each attribute over the entire dataset,
#finding D fro the hwole datatset
def findProb(attribute, attributeValues,training_data):
    attributeNoProb = []
    attributeYesProb = []
    D_fArray = []
    yesCount=0
    D_f = 0
    column = header.index(attribute)
    for p in range(len(attributeValues[column])):
        for j in range(2,len(training_data)):
           #print(attributeValues[column][p])
           if(training_data[j][column] == attributeValues[column][p]):
               #print("the're")
               D_f += 1
               if(training_data[j][23] == 1):
                print("check")
                yesCount = yesCount + 1
                print("here",yesCount)

        D_fArray.append(D_f)
        D_f=0
        # print("D",D_f)
        yesProb = yesCount/30000
        noProb = 1 - yesProb
        # print(yesProb)
        attributeYesProb.append(yesProb)
        attributeNoProb.append(noProb)

    print(D_fArray)
    #print(attributeYesProb)
    #print(attributeNoProb)
    '''for i in range(2,len(training_data)):
        k.append(training_data[i][column])
    for j in range(len(attributeValues[column])):
        attributeprob.append(k.count(attributeValues[column][j]) / len(k))
    D = len(k)
    print(attributeprob)'''
    return attributeNoProb,attributeYesProb,D_f

Noprob,YesProb,D_Education = findProb("EDUCATION", attributeValues,training_data)

def probOverDataset():
    yesCount = 0
    for i in range(2,30003):
        if(training_data[i][23]==1):
            yesCount += 1
    probYes = yesCount/30000
    probNo = 1 - probYes

    return probYes,probNo

#Have to test for calculation over whole dataset
#Have to test for calculation over some specific
# values of a features
def entropy(probYes,probNo):
    H = -(probYes*math.log(probYes,2)+probNo*math.log(probNo,2))
    print(H)
    return H

#here i want to find the probabilities of the attributes
#subject to each value the attricbutes can take, so as to
# get the probabilities for calculating the entopy
#finding D_feature and associated probabilities
def findFreatureProb(attribute, attributeValues,training_data):
    attributeprob = []
    D_f = 0
    k = []
    p =[]
    row = header.index(attribute)
    for i in range(2, len(training_data)):
        for j in range(len(attributeValues[row])):
            if(attributeValues[row][j] == training_data[i][row]):
                k.append(training_data[i][row])
                p.append(training_data[i][23])
    attributeprob.append(p.count(0) / len(p))
    D_f = len(p)
    print(k)
    return attributeprob,D_f

'''SEXprob,SEXd = findProb("SEX", attributeValues,training_data)
EDUCATIONprob,EDUCATIONd = findProb("EDUCATION", attributeValues,training_data)
MARRIAGEprob,MARRIAGEd = findProb("MARRIAGE", attributeValues,training_data)
PAY_0prob,PAY_0d = findProb("PAY_0", attributeValues,training_data)
PAY_2prob,PAY_2d = findProb("PAY_2", attributeValues,training_data)
PAY_3prob,PAY_3d = findProb("PAY_3", attributeValues,training_data)
PAY_4prob,PAY_4d = findProb("PAY_4", attributeValues,training_data)
PAY_5prob,PAY_5d = findProb("PAY_5", attributeValues,training_data)
PAY_6prob,PAY_6d = findProb("PAY_6", attributeValues,training_data)
LIMIT_BALprob,LIMIT_BALd = findProb("LIMIT_BAL", attributeValues,training_data)'''


#information gain, very faulty
'''def infoGain(atrribute,Domain,D_f):
    H(D)= entropy(Domain)
    H(D_f) = entropy(attribute)
    #some loop missing, find a way to iterate relavent features for calculation
        added = (D_f)*H(D_f)
    gain = H(D)- (1/D)*added'''


