import math
from plotDecBoundaries import *

xaxistemp = list()
yaxistemp = list()
labeltemp = list()
xaxis = list()
yaxis = list()
label = list()
xaxistemp2 = list()
yaxistemp2 = list()
labeltemp2 = list()
xaxis2 = list()
yaxis2 = list()
label2 = list()
average = list()
tdata = list()
tlabeltemp = list()
temp = list()
tlabel = list()
distance1 = list()
distance2 = list()
output = [0] * 100
count = 0
trainingdata = list()
trainingdata2 = list()


def distance_function(test_val1, average_val1, test_val2, average_val2):
    square = (test_val1 - average_val1) ** 2 + ((test_val2 - average_val2) ** 2)
    return math.sqrt(square)


with open('synthetic2_train.csv') as train:
    tfile = train.readlines()
    for line in tfile:
        line = line.split(',')      # cut to piece
        xaxistemp.append(line[0])
        yaxistemp.append(line[1])
        labeltemp.append(line[2])
    print(xaxistemp)
    for x in xaxistemp:             # to float
        xaxis.append(float(x))
    print(xaxis)
    for y in yaxistemp:             # to float
        yaxis.append(float(y))
    for l in labeltemp:             # to float
        label.append(int(l))

xaverage = sum(xaxis[0: 50]) / 50
xaverage2 = sum(xaxis[50: 100]) / 50
yaverage = sum(yaxis[0: 50]) / 50
yaverage2 = sum(yaxis[50: 100]) / 50
average = [[xaverage, yaverage], [xaverage2, yaverage2]]

trainingdata.append(xaxis)
trainingdata.append(yaxis)
trainingdata = np.array(trainingdata)       #input
trainingdata = trainingdata.T
label = np.array(label)


with open('synthetic2_train.csv') as testdata:
    tfile2 = testdata.readlines()
    for line2 in tfile2:
        temp.append(line2.split(','))
    for data in temp:
        tdata.append(data[0:2])
    for i in range(100):
        tdata[i] = [float(data) for data in tdata[i]]
    for data in temp:
        tlabeltemp.append(data[2])
    for temp in tlabeltemp:
        tlabel.append(int(temp))

for dis in tdata:
    distance1.append(distance_function(dis[0], average[0][0], dis[1], average[0][1]))
for dis2 in tdata:
    distance2.append(distance_function(dis2[0], average[1][0], dis2[1], average[1][1]))

for i in range(100):
    if distance1[i] < distance2[i]:
        output[i] = 1
    else:
        output[i] = 2
for i in range(len(tdata)):
    if output[i] != tlabel[i]:
        count = count + 1
error = count / 100


print(average)
print(output)
print(tlabel)
print(error)
average = np.array(average)


with open('synthetic2_train.csv') as train2:
    tfile2 = train2.readlines()
    for line2 in tfile2:
        line2 = line2.split(',')      # cut to piece
        xaxistemp2.append(line2[0])
        yaxistemp2.append(line2[1])
        labeltemp2.append(line2[2])
    for x2 in xaxistemp2:             # to float
        xaxis2.append(float(x2))
    for y2 in yaxistemp2:             # to float
        yaxis2.append(float(y2))
    for l2 in labeltemp2:             # to float
        label2.append(int(l2))
trainingdata2.append(xaxis2)
trainingdata2.append(yaxis2)
trainingdata2 = np.array(trainingdata2)       #input
trainingdata2 = trainingdata2.T
label2 = np.array(label2)


plotDecBoundaries(trainingdata2, label2, average)


