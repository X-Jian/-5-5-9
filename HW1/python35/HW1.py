import math
from plotDecBoundaries import *   # import all functions

xaxistemp = list()
yaxistemp = list()
labeltemp = list()
xaxis = list()
yaxis = list()
label = list()
average = list()
tdata = list()
tlabeltemp = list()
temp = list()
tlabel = list()
distance1 = list()
distance2 = list()
output = [0] * 100   #长度为100 建立一个空数组
count = 0
trainingdata = list()

def distance_function(test_val1, average_val1, test_val2, average_val2):
    square = (test_val1 - average_val1) ** 2 + ((test_val2 - average_val2) ** 2)
    return math.sqrt(square)

with open('synthetic1_train.csv') as train:
    reader = train.readlines()
    for rows in reader:
        rows = rows.split(',')      # cut to piece
        xaxistemp.append(rows[0])
        yaxistemp.append(rows[1])
        labeltemp.append(rows[2])
    for x in xaxistemp:             # to float
        xaxis.append(float(x))
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
trainingdata = np.array(trainingdata)       #将输入转化为矩阵形式??? 矩阵的长度范围？？
trainingdata = trainingdata.T
average = np.array(average)
label = np.array(label)


#这里处理要进行测试的文件
with open('synthetic1_train.csv') as testdata:
    reader2 = testdata.readlines()   #一行一行读取要测试的文件 读出来好像是字符形式的？？？
    for rows2 in reader2:
        temp.append(rows2.split(','))                           #按照逗号进行分割，数据一堆一堆分好
    for data in temp:
        tdata.append(data[0:2])
    for i in range(100):
        tdata[i] = [float(data) for data in tdata[i]]          #这里不能改的原因是二维数组不能一个一个加进去
    for data in temp:
        tlabeltemp.append(data[2])                    #取出标签存储
    for temp in tlabeltemp:
        tlabel.append(int(temp))                      #将label转换为int类型，将换行符分开 #这里的test_table是已经分好的标签，等会要与这个标签进行比较


#output = judge(test_data, average)    # class_mean就等于mean_data 就是两个点
#这一块功能是看测试点和点群的距离，然后进行判断，是打上1号的标签还是2号的标签
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

#传的x和y是测试和训练 是啥传啥， label也是， 只有average是始终不变的，是training的数据

plotDecBoundaries(trainingdata, label, average)   #.T是矩阵的转置，？？？


