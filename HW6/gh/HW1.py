import math
from plotDecBoundaries import *   # import all functions
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.multiclass import OneVsRestClassifier
np.set_printoptions(threshold=np.inf)
# np.set_printoptions(precision=9)
from sklearn import preprocessing





def dispose(file, choice, choice2):
    xaxis = list()
    yaxis = list()
    label = list()
    xaxistemp = list()
    yaxistemp = list()
    labeltemp = list()
    average = list()
    temp = list()
    temp2 = list()
    temp3 = list()
    with open(file) as train:
        tfile = train.read().splitlines()
        for line in tfile:
            line = line.split(',')      # cut to piece
            xaxistemp.append(line[choice])
            yaxistemp.append(line[choice2])
            labeltemp.append(line[13])
        for x in xaxistemp:  # to float
            xaxis.append(float(x))
        for y in yaxistemp:  # to float
            yaxis.append(float(y))
        for l in labeltemp:  # to float
            label.append(int(l))
    for j in range(len(label)):
        if label[j] == 1:
            temp.append(j)
        if label[j] == 2:
            temp2.append(j)
        if label[j] == 3:
            temp3.append(j)
    xaverage = sum(xaxis[min(temp): max(temp) + 1]) / len(temp)
    yaverage = sum(yaxis[min(temp): max(temp) + 1]) / len(temp)
    xaverage2 = sum(xaxis[min(temp2): max(temp2) + 1]) / len(temp2)
    yaverage2 = sum(yaxis[min(temp2): max(temp2) + 1]) / len(temp2)
    xaverage3 = sum(xaxis[min(temp3): max(temp3) + 1]) / len(temp3)
    yaverage3 = sum(yaxis[min(temp3): max(temp3) + 1]) / len(temp3)
    average = [[xaverage, yaverage], [xaverage2, yaverage2], [xaverage3, yaverage3]]
    return xaxis, yaxis, label, average

def dispose2(file, choice,choice1,choice2,choice3,choice4,choice5,choice6,choice7,choice8,choice9,choice10,choice11,choice12):
    xaxis = list()
    yaxis = list()
    yaxis2 = list()
    yaxis3 = list()
    yaxis4 = list()
    yaxis5 = list()
    yaxis6 = list()
    yaxis7 = list()
    yaxis8 = list()
    yaxis9 = list()
    yaxis10 = list()
    yaxis11 = list()
    yaxis12 = list()
    label = list()
    xaxistemp = list()
    yaxistemp = list()
    yaxistemp2 = list()
    yaxistemp3 = list()
    yaxistemp4 = list()
    yaxistemp5 = list()
    yaxistemp6 = list()
    yaxistemp7 = list()
    yaxistemp8 = list()
    yaxistemp9 = list()
    yaxistemp10 = list()
    yaxistemp11 = list()
    yaxistemp12 = list()
    labeltemp = list()
    average = list()
    temp = list()
    temp2 = list()
    temp3 = list()
    with open(file) as train:
        tfile = train.read().splitlines()
        for line in tfile:
            line = line.split(',')      # cut to piece
            xaxistemp.append(line[choice])
            yaxistemp.append(line[choice1])
            yaxistemp2.append(line[choice2])
            yaxistemp3.append(line[choice3])
            yaxistemp4.append(line[choice4])
            yaxistemp5.append(line[choice5])
            yaxistemp6.append(line[choice6])
            yaxistemp7.append(line[choice7])
            yaxistemp8.append(line[choice8])
            yaxistemp9.append(line[choice9])
            yaxistemp10.append(line[choice10])
            yaxistemp11.append(line[choice11])
            yaxistemp12.append(line[choice12])
            labeltemp.append(line[13])
        for x in xaxistemp:  # to float
            xaxis.append(float(x))
        for y in yaxistemp:  # to float
            yaxis.append(float(y))
        for y2 in yaxistemp2:  # to float
            yaxis2.append(float(y2))
        for y3 in yaxistemp3:  # to float
            yaxis3.append(float(y3))
        for y4 in yaxistemp4:  # to float
            yaxis4.append(float(y4))
        for y5 in yaxistemp5:  # to float
            yaxis5.append(float(y5))
        for y6 in yaxistemp6:  # to float
            yaxis6.append(float(y6))
        for y7 in yaxistemp7:  # to float
            yaxis7.append(float(y7))
        for y8 in yaxistemp8:  # to float
            yaxis8.append(float(y8))
        for y9 in yaxistemp9:  # to float
            yaxis9.append(float(y9))
        for y10 in yaxistemp10:  # to float
            yaxis10.append(float(y10))
        for y11 in yaxistemp11:  # to float
            yaxis11.append(float(y11))
        for y12 in yaxistemp12:  # to float
            yaxis12.append(float(y12))
        for l in labeltemp:  # to float
            label.append(int(l))
    for j in range(len(label)):
        if label[j] == 1:
            temp.append(j)
        if label[j] == 2:
            temp2.append(j)
        if label[j] == 3:
            temp3.append(j)
    xaverage = sum(xaxis[min(temp): max(temp) + 1]) / len(temp)
    yaverage = sum(yaxis[min(temp): max(temp) + 1]) / len(temp)
    xaverage2 = sum(xaxis[min(temp2): max(temp2) + 1]) / len(temp2)
    yaverage2 = sum(yaxis[min(temp2): max(temp2) + 1]) / len(temp2)
    xaverage3 = sum(xaxis[min(temp3): max(temp3) + 1]) / len(temp3)
    yaverage3 = sum(yaxis[min(temp3): max(temp3) + 1]) / len(temp3)
    average = [[xaverage, yaverage], [xaverage2, yaverage2], [xaverage3, yaverage3]]
    return xaxis, yaxis,yaxis2,yaxis3,yaxis4,yaxis5,yaxis6,yaxis7,yaxis8,yaxis9,yaxis10,yaxis11,yaxis12, label, average

def distance_function(test_val1, average_val1, test_val2, average_val2):
    square = (test_val1 - average_val1) ** 2 + ((test_val2 - average_val2) ** 2)
    return math.sqrt(square)


def choi(tdata, tmean):
    dis = [[], [], []]
    outcome = [0] * len(tdata)
    for point in tdata:
        dis[0].append(distance_function(point[0], tmean[0][0], point[1], tmean[0][1]))
    for point2 in tdata:
        dis[1].append(distance_function(point2[0], tmean[1][0], point2[1], tmean[1][1]))
    for point3 in tdata:
        dis[2].append(distance_function(point3[0], tmean[2][0], point3[1], tmean[2][1]))
    for i in range(len(tdata)):
        if dis[0][i] < dis[1][i]:
            if dis[1][i] < dis[2][i]:
                outcome[i] = 1
            else:
                if dis[0][i] < dis[2][i]:
                    outcome[i] = 1
                else:
                    outcome[i] = 3
        else:
            if dis[0][i] < dis[2][i]:
                outcome[i] = 2
            else:
                if dis[1][i] < dis[2][i]:
                    outcome[i] = 2
                else:
                    outcome[i] = 3
    return outcome


min_error = float("inf")
det_k = 100
det_j = 100
errormean = 0
errorall = list()
var = 0
temp5 = []


#这里是用来挑出误差最小的两组
for k in range(13):
    for j in range(k+1, 13):
        choice = k
        choice2 = j
        x, y, l, mdata = dispose('wine_train.csv', choice, choice2)

        with open('wine_train.csv') as testdata:
            tfile2 = testdata.readlines()
            for line2 in tfile2:
                temp5.append(line2.split(','))
            testdata = [data[choice: choice2 + 1: choice2 - choice] for data in temp5]
            tlabel = [data[13] for data in temp5]
            tlabel = [int(test) for test in tlabel]
        for m in range(len(testdata)):
            testdata[m] = [float(data) for data in testdata[m]]
        output = choi(testdata, mdata)
        count = 0
        for n in range(len(testdata)):
            if output[n] != tlabel[n]:
                count = count + 1
        error = count / len(testdata)
        errorall.append(error)
        if error < min_error:
            min_error = error
            det_k = choice
            det_j = choice2

for errormean2 in errorall:
    errormean = errormean + errormean2
errormean = errormean / 78

for errormean3 in errorall:
    var = var + ((errormean3 - errormean)**2)
var = var / (78 - 1)
deviation = math.sqrt(var)








#训练数据
x0,x1,lx2,mdatax2 = dispose('wine_train.csv', 0,1)
trainingx2 = []
trainingx2.append(x0)
trainingx2.append(x1)
trainingx2 = np.array(trainingx2)
trainingx2 = trainingx2.T
mdatax2 = np.array(mdatax2)
lx2 = np.array(lx2)

std2 = StandardScaler()
std2.fit(trainingx2)   #这一步把那些要求的全部求出来
train_std2 = std2.fit_transform(trainingx2)




y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,l2,mdata2 = dispose2('wine_train.csv', 0,1,2,3,4,5,6,7,8,9,10,11,12)
training2 = []
training2.append(y0)
training2.append(y1)
training2.append(y2)
training2.append(y3)
training2.append(y4)
training2.append(y5)
training2.append(y6)
training2.append(y7)
training2.append(y8)
training2.append(y9)
training2.append(y10)
training2.append(y11)
training2.append(y12)
training2 = np.array(training2)
training2 = training2.T
mdata2 = np.array(mdata2)
l2 = np.array(l2)

std = StandardScaler()
std.fit(training2)   #这一步把那些要求的全部求出来
train_std = std.fit_transform(training2)
# print('\n')
# print(std.n_samples_seen_)   #已经处理样本的个数
# print(std.mean_)     #平均值
# print(std.var_)     #方差
# print(std.scale_)  #缩放比例
# print(train_std)   #处理后的结果
# print(std.inverse_transform(train_std))   #返回来






#测试数据

test_x0,test_x1,test_lx2,test_mdatax2 = dispose('wine_test.csv', 0,1)
test_trainingx2 = []
test_trainingx2.append(test_x0)
test_trainingx2.append(test_x1)
test_trainingx2 = np.array(test_trainingx2)
test_trainingx2 = test_trainingx2.T
test_mdatax2 = np.array(test_mdatax2)
test_lx2 = np.array(test_lx2)

test_train_std2 = std2.transform(test_trainingx2)





test_y0,test_y1,test_y2,test_y3,test_y4,test_y5,test_y6,test_y7,test_y8,test_y9,test_y10,test_y11,test_y12,test_l2,test_mdata2 = dispose2('wine_test.csv', 0,1,2,3,4,5,6,7,8,9,10,11,12)
test_training2 = []
test_training2.append(test_y0)
test_training2.append(test_y1)
test_training2.append(test_y2)
test_training2.append(test_y3)
test_training2.append(test_y4)
test_training2.append(test_y5)
test_training2.append(test_y6)
test_training2.append(test_y7)
test_training2.append(test_y8)
test_training2.append(test_y9)
test_training2.append(test_y10)
test_training2.append(test_y11)
test_training2.append(test_y12)
test_training2 = np.array(test_training2)
test_training2 = test_training2.T
test_mdata2 = np.array(test_mdata2)
test_l2 = np.array(test_l2)

test_train_std = std.transform(test_training2)
# print('\n')
# print(std.n_samples_seen_)   #已经处理样本的个数
# print(std.mean_)     #平均值
# print(std.var_)     #方差
# print(std.scale_)  #缩放比例
# print(train_std)   #处理后的结果
# print(std.inverse_transform(train_std))   #返回来



# lr = LinearRegression()
# lr.fit(train_std2, lx2)
# # y_predict = lr.predict(training2)
# macc = lr.score(test_train_std2, test_lx2)
# print(macc)

class MSE_binary(LinearRegression):
    def __init__(self):
        print("Calling newly created MSE binary function")
        super(MSE_binary, self).__init__()
    def predict(self,X):
        thr = 0.5
        y = self._decision_function(X)
        for i in range((len(y))):
            if y[i] <= thr:
                y[i] = 0
            elif y[i] >thr:
                y[i] = 1
        return y


binary_model = MSE_binary()
model = OneVsRestClassifier(binary_model)
model.fit(train_std, l2)
macc = model.score(test_train_std, test_l2)
print(macc)





















# #开始感知器分类
# # 定义感知机
# max_number = 0
# max_weight = [[], [], []]
# for i in range(100):
#     clf = Perceptron(class_weight={1:np.random.randn(), 2:np.random.rand(), 3:np.random.randn()})
#     # 使用训练数据进行训练
#     clf.fit(train_std, l2)
#     # 得到训练结果，权重矩阵
#     acc = clf.score(train_std, l2)
#     if acc > max_number:
#         max_number = acc
#         max_weight = clf.coef_
#     print('\n')
#     print(clf.coef_)
#     print(acc)
#     print(max_number)
#     print(max_weight)

















#
# #这里本来是用来画train的图的
# x, y, l, mdata = dispose('wine_train.csv', det_k, det_j)
#
#
#
# #这里是为了test的计算正确率
# with open('wine_test.csv') as testdata:
# #with open('wine_train.csv') as testdata:
#     temp4 = list()
#     tfile2 = testdata.readlines()
#     for line2 in tfile2:
#         temp4.append(line2.split(','))
#     testdata = [data[det_k: det_j + 1: det_j - det_k] for data in temp4]
#     # test_data = [data[det_k2: det_j2 + 1: det_j2 - det_k2] for data in temp4]
#     tlabel = [data[13] for data in temp4]
#     tlabel = [int(test) for test in tlabel]
# for m in range(len(testdata)):
#     testdata[m] = [float(data) for data in testdata[m]]
#
# output = choi(testdata, mdata)
# # output = choi(test_data, mean_data2)
# # print(mdata)
# # print(testdata)
# # print(output)
# # print(tlabel)
# count = 0
# for n in range(len(testdata)):
#     if output[n] != tlabel[n]:
#         count = count + 1
# error = count / len(testdata)
# # print(count)
# # print(error)
#
#
#
# #这里是获取x轴，y轴和label的标签，用于画图
# x, y, l, mean_data3 = dispose('wine_test.csv', det_k, det_j)
# training1 = []
# training1.append(x)
# training1.append(y)
# training1 = np.array(training1)
# mdata = np.array(mdata)
# l = np.array(l)
#
#
#
#
#
# # plotDecBoundaries(train_dataset2.T, label_data2, mean_data2)
# plotDecBoundaries(training1.T, l, mdata)
#



