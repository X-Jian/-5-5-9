import math
import numpy as np
from plotDecBoundaries import *   # import all functions



#这一块先将train cvs文件拆分成x轴的，y轴的以及标签页面的
def read_and_mean(filename):
    with open(filename) as train_data:
        reader = train_data.read().splitlines() #按照行进行分隔，产生包含各行为元素的链表
        x_data, y_data, label = [], [], []
        for rows in reader:
            rows = rows.split(',')      # cut to piece
            x_data.append(rows[0])
            y_data.append(rows[1])
            label.append(rows[2])
        x_data = [float(x) for x in x_data]  # transfer to float
        y_data = [float(y) for y in y_data]  # transfer to float
        label = [int(l) for l in label]

    class_no = len(set(label))  # number of class labels  set不会重复，只含有1或者2 len就说明只是2
    # class_index = [[] for i in range(class_no)]   # the index of classes with size k * n
    #这一块功能是计算各个点群的平均值
    class_mean = []
    for i in range(class_no):
        temp = [j for j in range(len(label)) if label[j] == (i + 1)]
        # class_index[i] = temp
        mean_coordinate = []
        mean_coordinate.append(sum(x_data[min(temp):(max(temp) + 1)]) / len(temp))  # mean  计算平均值
        mean_coordinate.append(sum(y_data[min(temp):(max(temp) + 1)]) / len(temp))
        class_mean.append(mean_coordinate)
    return x_data, y_data, label, class_mean


#这一块功能是看测试点和点群的距离，然后进行判断，是打上1号的标签还是2号的标签
def judge(test, mean):
    temp = []
    out_put = [None] * len(test)
    for i in range(len(mean)):
        temp.append([math.sqrt((test1[0] - mean[i][0]) ** 2 + ((test1[1] - mean[i][1]) ** 2)) for test1 in test])
    for i in range(len(test)):
        out_put[i] = 1 if temp[0][i] < temp[1][i] else 2
    return out_put


x_data, y_data, label_data, mean_data = read_and_mean('synthetic1_train.csv')


with open('synthetic1_train.csv', 'r') as train_data:
    reader = train_data.readlines()
    test = [rows.split(',') for rows in reader]
    test_data = [data[:2] for data in test]
    test_label = [data[2] for data in test]
    test_label = list(map(int, test_label))

for i in range(len(test_data)):
    test_data[i] = list(map(float, test_data[i]))

output = judge(test_data, mean_data)
print(mean_data)     # class_mean就等于mean_data

train_dataset = []
train_dataset.append(x_data)
train_dataset.append(y_data)
train_dataset = np.array(train_dataset)
mean_data = np.array(mean_data)
label_data = np.array(label_data)
plotDecBoundaries(train_dataset.T, label_data, mean_data)

#print(test_label)
