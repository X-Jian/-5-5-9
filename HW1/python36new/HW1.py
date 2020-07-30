import math
from plotDecBoundaries import *   # import all functions


#temp其实就是distance
#这一块先将train cvs文件拆分成x轴的，y轴的以及标签页面的
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
        tfile = train.read().splitlines() #按照行进行分隔，产生包含各行为元素的列表
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

    #这一块功能是计算各个点群的平均值
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
    return xaxis, yaxis, label, average     #这里已经算出了平均值

def distance_function(test_val1, average_val1, test_val2, average_val2):
    square = (test_val1 - average_val1) ** 2 + ((test_val2 - average_val2) ** 2)
    return math.sqrt(square)

#这一块功能是看测试点和点群的距离，然后进行判断，是打上1号的标签还是2号的标签
def judge(tdata, tmean):      #传过来test是一个二维数组，包含所有点集 mean是平均值  也是二维数组
    dis = [[], [], []]
    outcome = [0] * len(tdata)
    for point in tdata:
        dis[0].append(distance_function(point[0], tmean[0][0], point[1], tmean[0][1]))#每次循环 算出所有值距离一个点的距离
    for point2 in tdata:
        dis[1].append(distance_function(point2[0], tmean[1][0], point2[1], tmean[1][1]))#每次循环 算出所有值距离一个点的距离
    for point3 in tdata:
        dis[2].append(distance_function(point3[0], tmean[2][0], point3[1], tmean[2][1]))#每次循环 算出所有值距离一个点的距离
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

for k in range(13):
    for j in range(k+1, 13):       #循环78次  train文件和test文件
        choice = k
        choice2 = j
        x_data, y_data, label_data, mean_data = dispose('wine_train.csv', choice, choice2)
        #这里处理要进行测试的文件
        with open('wine_train.csv') as testdata:
            tfile2 = testdata.readlines()   #一行一行读取要测试的文件 读出来好像是字符形式的？？？
            for line2 in tfile2:
                temp5.append(line2.split(','))
            testdata = [data[choice: choice2 + 1: choice2 - choice] for data in temp5]       #取出坐标存储
            test_label = [data[13] for data in temp5]       #取出标签存储
            test_label = [int(test) for test in test_label]       #将label转换为int类型，将换行符分开 #这里的test_table是已经分好的标签，等会要与这个标签进行比较
        for m in range(len(testdata)):
            testdata[m] = [float(data) for data in testdata[m]]
        output = judge(testdata, mean_data)  # class_mean就等于mean_data 就是两个点
        count = 0
        for n in range(len(testdata)):
            if output[n] != test_label[n]:
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

print(errormean)
print(var)
print(deviation)


det_k2 = 0
det_j2 = 1
x_data2, y_data2, label_data2, mean_data2 = dispose('wine_train.csv', det_k2, det_j2)
train_dataset2 = []
train_dataset2.append(x_data2)
train_dataset2.append(y_data2)
train_dataset2 = np.array(train_dataset2)       #将输入转化为矩阵形式??? 矩阵的长度范围？？
mean_data2 = np.array(mean_data2)
label_data2 = np.array(label_data2)


x_data, y_data, label_data, mean_data = dispose('wine_train.csv', det_k, det_j)

# 这里处理要进行测试的文件
with open('wine_train.csv') as testdata:
    temp4 = list()
    tfile2 = testdata.readlines()  # 一行一行读取要测试的文件 读出来好像是字符形式的？？？
    for line2 in tfile2:
        temp4.append(line2.split(','))
    # 按照逗号进行分割，数据一堆一堆分好
    testdata = [data[det_k: det_j + 1: det_j - det_k] for data in temp4]  # 取出坐标存储
    # test_data = [data[det_k2: det_j2 + 1: det_j2 - det_k2] for data in test]  # 取出坐标存储
    print(det_k2)
    print(det_j2)
    # test_data = [data[det_k: det_j + 1: det_j - det_k] for data in test]  # 取出坐标存储
    test_label = [data[13] for data in temp4]  # 取出标签存储
    test_label = [int(test) for test in test_label]  # 将label转换为int类型，将换行符分开 #这里的test_table是已经分好的标签，等会要与这个标签进行比较
for m in range(len(testdata)):
    testdata[m] = [float(data) for data in testdata[m]]

output = judge(testdata, mean_data)  # class_mean就等于mean_data 就是两个点
# output = judge(test_data, mean_data2)  # class_mean就等于mean_data 就是两个点
print(mean_data)
print(testdata)
print(output)
print(test_label)
count = 0
for n in range(len(testdata)):
    if output[n] != test_label[n]:
        count = count + 1
error = count / len(testdata)
print(count)
print(error)

x_data, y_data, label_data, mean_data3 = dispose('wine_test.csv', det_k, det_j)

train_dataset = []
train_dataset.append(x_data)
train_dataset.append(y_data)
train_dataset = np.array(train_dataset)       #将输入转化为矩阵形式??? 矩阵的长度范围？？
mean_data = np.array(mean_data)
label_data = np.array(label_data)

# plotDecBoundaries(train_dataset2.T, label_data2, mean_data2)   #.T是矩阵的转置，？？？
plotDecBoundaries(train_dataset.T, label_data, mean_data)   #.T是矩阵的转置，？？？


