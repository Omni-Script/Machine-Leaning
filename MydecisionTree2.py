from __future__ import print_function
import csv
import math

filename = 'clients.csv'

def readMyFile(filename):
    training_data = []
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            training_data.append(row)
    #training_data.pop(1)
    #training_data.pop(2)
    #print(len(training_data))
    # for i in range(len(training_data)):
    #print(training_data[2][24])
    # print(Digits)
    return training_data

training_data = readMyFile(filename)
# These are used only to print the tree.
header = ["ID", "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE", "PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5",
          "PAY_6", "BILL_AMT1", "BILL_AMT2",
          "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4",
          "PAY_AMT5", "PAY_AMT6", "default payment"]
# ARRAY HOLDING THE NUMBER OF POSIIBLE UNIQUE VALUS AN ATTRIBUTE CAN HAVE
NoUnique = [6, 6, 4, 2, 6, 11, 11, 11, 11, 11, 11, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 2]
#THE GROUPS INTO WHICH OUR DATA WAS DISCRETIZED BY K-MEANS
attributeValues = [],["A", "B", "C", "D", "E", "F"],["1", "2"],["1", "2", "3", "4"],[],["A6", "A5", "A4", "A3", "A2", "A1"],\
                  ["L", "K", "J", "I", "H", "G"],["L", "K", "J", "I", "H", "G"],["L", "K", "J", "I", "H", "G"],["L", "K", "J", "I", "H", "G"],\
                  ["L", "K", "J", "I", "H", "G"],["L", "K", "J", "I", "H", "G"],["R", "Q", "P", "O", "N", "M"],["R", "Q", "P", "O", "N", "M"],\
                  ["R", "Q", "P", "O", "N", "M"],["R", "Q", "P", "O", "N", "M"],["R", "Q", "P", "O", "N", "M"],["R", "Q", "P", "O", "N", "M"],\
                  ["X", "W", "V", "U", "T", "S"],["X", "W", "V", "U", "T", "S"],["X", "W", "V", "U", "T", "S"],["X", "W", "V", "U", "T", "S"],\
                  ["X", "W", "V", "U", "T", "S"],["X", "W", "V", "U", "T", "S"],["1","0"]

'''def findUniqueValuesInColumn(attribute):
    k = header.index(attribute)
    j,T,F = 0
    for i in range(2,len(training_data)):
        if(training_data[i][k]==1):
            j= j+1
    T = 1
    Tnum=j
    F=0
    Fnum = 30000-j
    print(T,F)
    return T,F,Tnum,Fnum

T,F,Tnum,Fnum=findUniqueValuesInColumn()'''

#Limt balance probalilities
def partition1():
    categoryF=[]
    categoryE=[]
    categoryD=[]
    categoryC=[]
    categoryB=[]
    categoryA=[]
    for i in range(2,30002):
        if(10000 <= int(training_data[i][1]) < 120000):
            categoryF.append(training_data[i][1])
            training_data[i][1]= "F"
        elif (120000 <= int(training_data[i][1]) <= 220000):
            categoryE.append(training_data[i][1])
            training_data[i][1] = "E"
        elif (220000 < int(training_data[i][1]) <= 320000):
            categoryD.append(training_data[i][1])
            training_data[i][1] = "D"
        elif (320000 < int(training_data[i][1]) <= 430000):
            categoryC.append(training_data[i][1])
            training_data[i][1] = "C"
        elif (430000 < int(training_data[i][1]) <= 570000):
            categoryB.append(training_data[i][1])
            training_data[i][1] = "B"
        elif (570000 < int(training_data[i][1]) <= 1000000):
            categoryA.append(training_data[i][1])
            training_data[i][1] = "A"
    '''print(len(categoryF))
    print(len(categoryE))
    print(len(categoryD))
    print(len(categoryC))
    print(len(categoryB))
    print(len(categoryA))
    #print(training_data[2][1])'''

    return categoryF, categoryE, categoryD, categoryC, categoryB, categoryA
partition1()
#Payments status
def partition2():
    categoryL=[]
    categoryK=[]
    categoryJ=[]
    categoryI=[]
    categoryH=[]
    categoryG=[]
    for i in range(2,30002):
        for j in range(6,12):
            if(-2 <= int(training_data[i][j]) < 0):
                categoryL.append(training_data[i][j])
                training_data[i][j]= "L"
            elif (0 <= int(training_data[i][j]) <= 1):
                categoryK.append(training_data[i][j])
                training_data[i][j] = "K"
            elif (1 < int(training_data[i][j]) <= 2):
                categoryJ.append(training_data[i][j])
                training_data[i][j] = "J"
            elif (2 < int(training_data[i][j]) <= 3):
                categoryI.append(training_data[i][j])
                training_data[i][j] = "I"
            elif (3 < int(training_data[i][j]) <= 5):
                categoryH.append(training_data[i][j])
                training_data[i][j] = "H"
            elif (5 < int(training_data[i][j]) <= 8):
                categoryG.append(training_data[i][j])
                training_data[i][j] = "G"

    return categoryL, categoryK, categoryJ, categoryI, categoryH, categoryG
partition2()
#Bill Amounts
def partition3():
    categoryR=[]
    categoryQ=[]
    categoryP=[]
    categoryO=[]
    categoryN=[]
    categoryM=[]
    for i in range(2,30002):
        for j in range(12,18):
            if(-339603 <= int(training_data[i][j]) < 27402):
                categoryR.append(training_data[i][j])
                training_data[i][j]= "R"
            elif (27402 <= int(training_data[i][j]) <= 73366):
                categoryQ.append(training_data[i][j])
                training_data[i][j] = "Q"
            elif (73366 < int(training_data[i][j]) <= 135634):
                categoryP.append(training_data[i][j])
                training_data[i][j] = "P"
            elif (135634 < int(training_data[i][j]) <= 221793):
                categoryO.append(training_data[i][j])
                training_data[i][j] = "O"
            elif (221793 < int(training_data[i][j]) <= 356375):
                categoryN.append(training_data[i][j])
                training_data[i][j] = "N"
            elif (356375 < int(training_data[i][j]) <= 1664089):
                categoryM.append(training_data[i][j])
                training_data[i][j] = "M"

    return categoryR, categoryQ, categoryP, categoryO, categoryN, categoryM
partition3()
# repayment amounts
def partition4():
    categoryX=[]
    categoryW=[]
    categoryV=[]
    categoryU=[]
    categoryT=[]
    categoryS=[]
    for i in range(2,30002):
        for j in range(18,24):
            if(-165580 <= int(training_data[i][j]) < 27402):
                categoryX.append(training_data[i][j])
                training_data[i][j]= "X"
            elif (27402 <= int(training_data[i][j]) <= 73366):
                categoryW.append(training_data[i][j])
                training_data[i][j] = "W"
            elif (73366 < int(training_data[i][j]) <= 135634):
                categoryV.append(training_data[i][j])
                training_data[i][j] = "V"
            elif (135634 < int(training_data[i][j]) <= 221793):
                categoryU.append(training_data[i][j])
                training_data[i][j] = "U"
            elif (221793 < int(training_data[i][j]) <= 356375):
                categoryT.append(training_data[i][j])
                training_data[i][j] = "T"
            elif (356375 < int(training_data[i][j]) <= 1684259):
                categoryS.append(training_data[i][j])
                training_data[i][j] = "S"

    return categoryX, categoryW, categoryV, categoryU, categoryT, categoryS
partition4()
#Age
def partition5():
    categoryA6=[]
    categoryA5=[]
    categoryA4=[]
    categoryA3=[]
    categoryA2=[]
    categoryA1=[]
    for i in range(2,30002):
            print(training_data[i][5])
            if( 21 <= int(training_data[i][5]) < 31):
                categoryA6.append(training_data[i][5])
                training_data[i][5]= "A6"
            elif (31 <= int(training_data[i][5]) <= 38):
                categoryA5.append(training_data[i][5])
                training_data[i][5] = "A5"
            elif (38 < int(training_data[i][5]) <= 45):
                categoryA4.append(training_data[i][5])
                training_data[i][5] = "A4"
            elif (45 < int(training_data[i][5]) <= 52):
                categoryA3.append(training_data[i][5])
                training_data[i][5] = "A3"
            elif (52 < int(training_data[i][5]) <= 60):
                categoryA2.append(training_data[i][5])
                training_data[i][5] = "A2"
            elif (60 < int(training_data[i][5]) <= 79):
                categoryA1.append(training_data[i][5])
                training_data[i][5] = "A1"

    return categoryA1, categoryA2, categoryA3, categoryA4, categoryA5, categoryA6
partition5()

# probability of each attribute over the entire dataset,
#finding D fro the hwole datatset
def findProb(attribute, attributeValues,training_data):
    attributeprob = []
    k = []
    column = header.index(attribute)
    for i in range(2,len(training_data)):
        k.append(training_data[i][column])
    for j in range(len(attributeValues[column])):
        attributeprob.append(k.count(attributeValues[column][j]) / len(k))
    D = len(k)
    print(attributeprob)
    return attributeprob,D

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
                p.append(training_data[i][24])
    attributeprob.append(p.count(0) / len(p))
    D_f = len(p)
    print(k)
    return attributeprob,D_f

EDUCATIONprob,EDUCATIONd = findFreatureProb("EDUCATION", attributeValues,training_data)

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

#Have to test for calculation over whole dataset
#Have to test for calculation over some specific
# values of a features
def entropy(attributeprob):
    for i in range(len(attributeprob)):
        H = -(attributeprob[i]*math.log(attributeprob[i],2))
    print(H)
    return H
#entropy(SEXprob)

#information gain, very faulty
'''def infoGain(atrribute,Domain,D_f):
    H(D)= entropy(Domain)
    H(D_f) = entropy(attribute)
    #some loop missing, find a way to iterate relavent features for calculation
        added = (D_f)*H(D_f)
    gain = H(D)- (1/D)*added'''


'''data= zip(*training_data)
print(training_data)
with open('output.csv', "w") as output:
    writer = csv.writer(output)
    writer.writerows(training_data)
    '''
