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
average_1vr = list()
average_2vr = list()
average_3vr = list()
tdata = list()
tlabeltemp = list()
temp = list()
tlabel = list()
distance1 = list()
distance2 = list()
distance3 = list()
distance_1 = list()
distance_2 = list()
distance_3 = list()
distance_1r = list()
distance_2r = list()
distance_3r = list()
output = [0] * 89
count = 0
trainingdata = list()


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

xaverage_1 = sum(xaxis[0: 30]) / 30
xaverage_2 = sum(xaxis[30: 65]) / 35
xaverage_3 = sum(xaxis[65: 89]) / 24

xaverage_1r = sum(xaxis[30: 89]) / 59
xaverage_2r = (sum(xaxis[0: 30]) + sum(xaxis[65: 89])) / 54
xaverage_3r = sum(xaxis[0: 65]) / 65

yaverage_1 = sum(yaxis[0: 30]) / 30
yaverage_2 = sum(yaxis[30: 65]) / 35
yaverage_3 = sum(yaxis[65: 89]) / 24

yaverage_1r = sum(yaxis[30: 89]) / 59
yaverage_2r = (sum(yaxis[0: 30]) + sum(yaxis[65: 89])) / 54
yaverage_3r = sum(yaxis[0: 65]) / 65

average_1vr = [[xaverage_1, yaverage_1], [xaverage_1r, yaverage_1r]]
average_2vr = [[xaverage_2, yaverage_2], [xaverage_2r, yaverage_2r]]
average_3vr = [[xaverage_3, yaverage_3], [xaverage_3r, yaverage_3r]]
average_final = [[xaverage_1, yaverage_1], [xaverage_1r, yaverage_1r], [xaverage_2, yaverage_2], [xaverage_2r, yaverage_2r], [xaverage_3, yaverage_3], [xaverage_3r, yaverage_3r]]



trainingdata.append(xaxis)
trainingdata.append(yaxis)
trainingdata = np.array(trainingdata)       #input
trainingdata = trainingdata.T
label = np.array(label)


with open('wine_test.csv') as testdata:
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


def distance_function(test_val1, average_val1, test_val2, average_val2):
    square = (test_val1 - average_val1) ** 2 + ((test_val2 - average_val2) ** 2)
    return math.sqrt(square)


for dis_1 in tdata:
    distance_1.append(distance_function(dis_1[0], average_1vr[0][0], dis_1[1], average_1vr[0][1]))
for dis_1r in tdata:
    distance_1r.append(distance_function(dis_1r[0], average_1vr[1][0], dis_1r[1], average_1vr[1][1]))
for dis_2 in tdata:
    distance_2.append(distance_function(dis_2[0], average_2vr[0][0], dis_2[1], average_2vr[0][1]))
for dis_2r in tdata:
    distance_2r.append(distance_function(dis_2r[0], average_2vr[1][0], dis_2r[1], average_2vr[1][1]))
for dis_3 in tdata:
    distance_3.append(distance_function(dis_3[0], average_3vr[0][0], dis_3[1], average_3vr[0][1]))
for dis_3r in tdata:
    distance_3r.append(distance_function(dis_3r[0], average_3vr[1][0], dis_3r[1], average_3vr[1][1]))


for i in range(89):
    if (distance_1[i] < distance_1r[i]) and (distance_2r[i] < distance_2[i]) and (distance_3r[i] < distance_3[i]):
        output[i] = 1
    elif (distance_2[i] < distance_2r[i]) and (distance_1r[i] < distance_1[i]) and (distance_3r[i]< distance_3[i]):
        output[i] = 2
    elif (distance_3[i] < distance_3r[i]) and (distance_1r[i] < distance_1[i]) and (distance_2r[i] < distance_2[i]):
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


print(average)
print(average_final)
average = np.array(average)
average_final = np.array(average_final)
print(average)
print(average_final)
plotDecBoundaries(trainingdata3, label3, average_final)




