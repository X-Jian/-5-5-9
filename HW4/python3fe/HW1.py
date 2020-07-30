import numpy as np
import copy
from plotDecBoundaries import plotDecBoundaries
from matplotlib import pyplot as plt

xaxistemp = list()
yaxistemp = list()
labeltemp = list()
xaxis = list()
yaxis = list()
label = list()
temptemp3 = list()
temptemp4 = list()
trainingdata = list()
point2 = list()
label2 = list()
reflected2 = list()
weight = [0.1, 0.1, 0.1]
ran = np.random.permutation(92)



for i in range(92):
    temptemp3.append([])
    temptemp4.append([])
    point2.append([])
    label2.append([])
    reflected2.append([])


with open('label_train.csv') as traintrain:
    tfiletfile = traintrain.readlines()
    for lineline in tfiletfile:
        lineline = lineline.split(',')
        labeltemp.append(lineline[0])
    for k in labeltemp:
        label.append(int(k))


with open('feature_train.csv') as train:
    tfile = train.readlines()
    for line in tfile:
        line = line.split(',')
        xaxistemp.append(line[0])
        yaxistemp.append(line[1])

    for i in xaxistemp:
        xaxis.append(float(i))
    for j in yaxistemp:
        yaxis.append(float(j))


    for i in range(92):
        temptemp3[i].append(xaxis[i])
        temptemp3[i].append(yaxis[i])
        temptemp3[i].append(1)
        if label[i] == 1:
            temptemp4[i].append(xaxis[i])
            temptemp4[i].append(yaxis[i])
            temptemp4[i].append(1)
        elif label[i] == 2:
            temptemp4[i].append(-xaxis[i])
            temptemp4[i].append(-yaxis[i])
            temptemp4[i].append(-1)

point = np.array(temptemp3)
reflected = np.array(temptemp4)
label = np.array(label)




point2 = point[ran]
reflected2 = reflected[ran]
label2 = label[ran]


for i in range(1000):
    for i in range(92):
        if sum(weight * reflected2[i]) <= 0:
            weight = weight + reflected2[i]


def compute(wei):
    count = 0
    for i in range(92):
        if point2[i][0] * wei[0] + point2[i][1] * wei[1] + wei[2] < 0 and label2[i] == 1:
            count = count + 1
        elif point2[i][0] * wei[0] + point2[i][1] * wei[1] + wei[2] > 0 and label2[i] == 2:
            count = count + 1
    err = count / 92
    return err


error = compute(weight)

print(weight)
print(error)

plotDecBoundaries(point, label, weight)