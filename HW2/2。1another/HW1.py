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
distance3 = list()
output = [0] * 100
count = 0
trainingdata = list()


def distance_function(test_val1, average_val1, test_val2, average_val2):
    square = (test_val1 - average_val1) ** 2 + ((test_val2 - average_val2) ** 2)
    return math.sqrt(square)


with open('wine_train.csv') as train:
    tfile = train.readlines()
    for line in tfile:
        line = line.split(',')      # cut to piece
        xaxistemp.append(line[0])
        yaxistemp.append(line[1])
        labeltemp.append(line[13])
    for x in xaxistemp:             # to float
        xaxis.append(float(x))
    for y in yaxistemp:             # to float
        yaxis.append(float(y))
    for l in labeltemp:             # to float
        label.append(int(l))

xaverage = sum(xaxis[0: 30]) / 30
xaverage2 = sum(xaxis[30: 65]) / 35
xaverage3 = sum(xaxis[65: 89]) / 24

yaverage = sum(yaxis[0: 30]) / 30
yaverage2 = sum(yaxis[30: 65]) / 35
yaverage3 = sum(yaxis[65: 89]) / 24
average = [[xaverage, yaverage], [xaverage2, yaverage2], [xaverage3, yaverage3]]

trainingdata.append(xaxis)
trainingdata.append(yaxis)
trainingdata = np.array(trainingdata)       #input
trainingdata = trainingdata.T
label = np.array(label)


with open('wine_train.csv') as testdata:
    tfile2 = testdata.readlines()
    for line2 in tfile2:
        temp.append(line2.split(','))
    for data in temp:
        tdata.append(data[0:2:1])
    for i in range(89):
        tdata[i] = [float(data) for data in tdata[i]]
    for data in temp:
        tlabeltemp.append(data[13])
    for temp in tlabeltemp:
        tlabel.append(int(temp))

for dis in tdata:
    distance1.append(distance_function(dis[0], average[0][0], dis[1], average[0][1]))
for dis2 in tdata:
    distance2.append(distance_function(dis2[0], average[1][0], dis2[1], average[1][1]))
for dis3 in tdata:
    distance3.append(distance_function(dis3[0], average[2][0], dis3[1], average[2][1]))


for i in range(89):
    if ((distance1[i] < distance2[i]) and (distance1[i] < distance3[i])) and (
            (distance2[i] > distance3[i]) or (distance2[i] > distance1[i])) and (
            (distance3[i] > distance1[i]) or (distance3[i] > distance2[i])):
        output[i] = 1
    elif ((distance2[i] < distance1[i]) and (distance2[i] < distance3[i])) and (
            (distance1[i] > distance2[i]) or (distance1[i] > distance3[i])) and (
            (distance3[i] > distance1[i]) or (distance3[i] > distance2[i])):
        output[i] = 2
    elif ((distance3[i] < distance2[i]) and (distance3[i] < distance1[i])) and (
            (distance1[i] > distance2[i]) or (distance1[i] > distance3[i])) and (
            (distance2[i] > distance1[i]) or (distance2[i] > distance3[i])):
        output[i] = 3

for i in range(len(tdata)):
    if output[i] != tlabel[i]:
        count = count + 1
error = count / len(tdata)


print(average)
print(output)
print(tlabel)
print(count)
print(error)


# 这里是用来再次画图的
xaxistemp3 = list()
yaxistemp3 = list()
labeltemp3 = list()
xaxis3 = list()
yaxis3 = list()
label3 = list()
trainingdata3 = list()
with open('wine_test.csv') as train3:
    tfile3 = train3.readlines()
    for line3 in tfile3:
        line3 = line3.split(',')      # cut to piece
        xaxistemp3.append(line3[0])
        yaxistemp3.append(line3[1])
        labeltemp3.append(line3[13])
    for x3 in xaxistemp3:             # to float
        xaxis3.append(float(x3))
    for y3 in yaxistemp3:             # to float
        yaxis3.append(float(y3))
    for l3 in labeltemp3:             # to float
        label3.append(int(l3))
trainingdata3.append(xaxis3)
trainingdata3.append(yaxis3)
trainingdata3 = np.array(trainingdata3)       #input
trainingdata3 = trainingdata3.T
label3 = np.array(label3)
#就保持average不变
average = np.array(average)
plotDecBoundaries(trainingdata3, label3, average)




