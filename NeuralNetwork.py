import numpy as np
import scipy
import matplotlib
import csv
import math

class network():
    filename = 'clients.csv'
    def readMyFile(filename):
        training_data = []
        with open(filename) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                training_data.append(row)
        # training_data.pop(1)
        # training_data.pop(2)
        # print(len(training_data))
        # for i in range(len(training_data)):
        # print(training_data[2][24])
        # print(Digits)
        return training_data

    inputs_list =[]
    targets_list =[]
    training_data = np.array(readMyFile(filename))
    # chhoseing data inouts and taget to give to network.
    for i in range(2,23):
        inputs_list.append(training_data[:][i])
    targets_list =training_data[1:,:24]
    print(targets_list)
    #giving initial network parameters and conditions
    inputnodes =30000
    outputnodes =30000*2
    hiddennodes =30000
    learningrate = 0.5

    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
    # set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
    # link weight matrices, wih and who
    # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
    # w11 w21
    # w12 w22 etc
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
    # learning rate
        self.lr = learningrate
    # activation function is the sigmoid function
        self.activation_function =lambda x: scipy.special.expit(x)

    pass

        # query the neural network
    def query(self, inputs_list):
    # convert inputs list to 2d array
            inputs = np.array(inputs_list, ndmin=2).T
    # calculate signals into hidden layer
            hidden_inputs = np.dot(self.wih, inputs)
    # calculate the signals emerging from hidden layer
            hidden_outputs =self.activation_function(hidden_inputs)
    # calculate signals into final output layer
            final_inputs = np.dot(self.who, hidden_outputs)
    # calculate the signals emerging from final output layer
            final_outputs = self.activation_function(final_inputs)

            return final_outputs


    # train the neural network
    def train(self, inputs_list, targets_list):
    # convert inputs list to 2d array
            inputs = np.array(inputs_list, ndmin=2).T
            targets = np.array(targets_list, ndmin=2).T
    # calculate signals into hidden layer
            hidden_inputs = np.dot(self.wih, inputs)
    # calculate the signals emerging from hidden layer
            hidden_outputs =self.activation_function(hidden_inputs)
    # calculate signals into final output layer
            final_inputs = np.dot(self.who, hidden_outputs)
    # calculate the signals emerging from final output layer
            final_outputs =self.activation_function(final_inputs)
    # output layer error is the (target - actual)
            output_errors = targets - final_outputs
    # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
            hidden_errors = np.dot(self.who.T, output_errors)
    # update the weights for the links between the hidden and output layers
            self.who +=self.lr * np.dot((output_errors * final_outputs * (1.0- final_outputs)), np.transpose(hidden_outputs))
    # update the weights for the links between the input and hidden layers
            self.wih +=self.lr * np.dot((hidden_errors * hidden_outputs * (1.0- hidden_outputs)), np.transpose(inputs))

    #NNED TO SOLVE SOME ARRAY REPRESETATION ISSUES
    # THE PRINT STATEMENTS BELOW DONT MAKE SENSE.

    '''evaluation = 0
    evaluation2 =0
    for i in range(1,30000):
            if training_data[i][24] == targets_list[i]:
                evaluation += 1
            else:
                evaluation2 += 1
    print(evaluation)
    print(evaluation2)'''

