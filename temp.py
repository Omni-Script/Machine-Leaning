attributeprob = []
D_f = 0
k = []
row = header.index(attribute)
for i in range(2, len(training_data)):
    k.append(training_data[i][row])
for j in range(len(attributeValues[row])):
    while (attributeValues[row][j] == training_data[i][row]):
        D_f = ++D_f
    attributeprob.append(k.count(attributeValues[row][j]) / len(K))