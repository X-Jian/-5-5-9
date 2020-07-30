import math
from plotDecBoundaries import *   # import all functions



#这一块先将train cvs文件拆分成x轴的，y轴的以及标签页面的
def read_and_mean(filename):
    with open(filename) as train_data:
        reader = train_data.read().splitlines() #按照行进行分隔，产生包含各行为元素的列表
        print(reader)
        x_data, y_data, label = [], [], []
        for rows in reader:
            rows = rows.split(',')      # cut to piece
            x_data.append(rows[0])
            y_data.append(rows[1])
            label.append(rows[2])
        x_data = [float(x) for x in x_data]  # transfer to float
        y_data = [float(y) for y in y_data]  # transfer to float
        label = [int(l) for l in label]

    # class_no = len(set(label))  # number of class labels  set不会重复，只含有1或者2 len就说明只是2
    # class_index = [[] for i in range(class_no)]   # the index of classes with size k * n
    #这一块功能是计算各个点群的平均值
    class_mean = []
    for i in range(2):
        temp = []
        for j in range(len(label)):
            if label[j] == (i + 1):
                temp.append(j)
        mean_coordinate = []
        mean_x = sum(x_data[min(temp): max(temp) + 1]) / len(temp)
        mean_y = sum(y_data[min(temp): max(temp) + 1]) / len(temp)
        mean_coordinate.append(mean_x)  # mean  计算平均值
        mean_coordinate.append(mean_y)
        class_mean.append(mean_coordinate)
    return x_data, y_data, label, class_mean     #这里已经算出了平均值


#这一块功能是看测试点和点群的距离，然后进行判断，是打上1号的标签还是2号的标签
def judge(test, mean):      #传过来test是一个二维数组，包含所有点集 mean是平均值  也是二维数组
    temp = []
    out_put = [None] * len(test)   #长度为100 建立一个空数组
    print(len(test))
    print(out_put)
    for i in range(len(mean)):
        temp.append([math.sqrt((test1[0] - mean[i][0]) ** 2 + ((test1[1] - mean[i][1]) ** 2)) for test1 in test])
    print('临时temp')
    print(len(mean))
    print(temp)
    print(temp[0][0])
    print(temp[0][1])
    print(temp[1][0])
    print(temp[1][1])
    for i in range(len(test)):
        out_put[i] = 1 if temp[0][i] < temp[1][i] else 2
    return out_put


x_data, y_data, label_data, mean_data = read_and_mean('synthetic1_train.csv')


#这里处理要进行测试的文件
with open("synthetic1_test.csv") as train_data:
    reader = train_data.readlines()   #一行一行读取要测试的文件 读出来好像是字符形式的？？？
    print(reader)
    test = [rows.split(',') for rows in reader]   #按照逗号进行分割，数据一堆一堆分好
    print(test)
    test_data = [data[:2] for data in test]       #取出坐标存储
    print(test_data)
    test_label = [data[2] for data in test]       #取出标签存储
    print(test_label)
    test_label = [int(test) for test in test_label]       #将label转换为int类型，将换行符分开
    print(test_label)                            #这里的test_table是已经分好的标签，等会要与这个标签进行比较

for i in range(len(test_data)):
    test_data[i] = [float(data) for data in test_data[i]]
print(test_data)

output = judge(test_data, mean_data)
print(mean_data)     # class_mean就等于mean_data 就是两个点

print('\n')

train_dataset = []
print(x_data)
train_dataset.append(x_data)
print(train_dataset)
train_dataset.append(y_data)
print(train_dataset)
train_dataset = np.array(train_dataset)       #将输入转化为矩阵形式??? 矩阵的长度范围？？
print(train_dataset)
mean_data = np.array(mean_data)

print(label_data)
label_data = np.array(label_data)
print(label_data)
print(mean_data)
plotDecBoundaries(train_dataset.T, label_data, mean_data)   #.T是矩阵的转置，？？？


