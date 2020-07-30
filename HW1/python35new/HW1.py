import math
from plotDecBoundaries import *   # import all functions

#temp其实就是distance
#这一块先将train cvs文件拆分成x轴的，y轴的以及标签页面的
def read_and_mean(filename, choice, choice2):
    with open(filename) as train_data:
        reader = train_data.read().splitlines() #按照行进行分隔，产生包含各行为元素的列表
        x_data = []
        y_data = []
        label = []
        for rows in reader:
            rows = rows.split(',')      # cut to piece
            x_data.append(rows[choice])
            y_data.append(rows[choice2])
            label.append(rows[13])
        x_data = [float(x) for x in x_data]  # transfer to float
        y_data = [float(y) for y in y_data]  # transfer to float
        label = [int(l) for l in label]

    # class_no = len(set(label))  # number of class labels  set不会重复，只含有1或者2 len就说明只是2
    # class_index = [[] for i in range(class_no)]   # the index of classes with size k * n
    #这一块功能是计算各个点群的平均值
    class_mean = []
    for i in range(3):
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
    for i in range(len(mean)):
        temp.append([math.sqrt((mytest[0] - mean[i][0]) ** 2 + ((mytest[1] - mean[i][1]) ** 2)) for mytest in test]) #每次循环 算出所有值距离一个点的距离
    for i in range(len(test)):
        if temp[0][i] < temp[1][i]:
            if temp[1][i] < temp[2][i]:
                out_put[i] = 1
            else:
                if temp[0][i] < temp[2][i]:
                    out_put[i] = 1
                else:
                    out_put[i] = 3
        else:
            if temp[0][i] < temp[2][i]:
                out_put[i] = 2
            else:
                if temp[1][i] < temp[2][i]:
                    out_put[i] = 2
                else:
                    out_put[i] = 3
    return out_put


min_error = float("inf")
det_k = 100
det_j = 100

for k in range(13):
    for j in range(k+1, 13):       #循环78次  train文件和test文件
        choice = k
        choice2 = j

        x_data, y_data, label_data, mean_data = read_and_mean('wine_train.csv', choice, choice2)

        #这里处理要进行测试的文件
        with open('wine_train.csv') as test_data:
            reader = test_data.readlines()   #一行一行读取要测试的文件 读出来好像是字符形式的？？？
            test = [rows.split(',') for rows in reader]   #按照逗号进行分割，数据一堆一堆分好
            test_data = [data[choice: choice2+1: choice2-choice] for data in test]       #取出坐标存储
            test_label = [data[13] for data in test]       #取出标签存储
            test_label = [int(test) for test in test_label]       #将label转换为int类型，将换行符分开 #这里的test_table是已经分好的标签，等会要与这个标签进行比较
        for m in range(len(test_data)):
            test_data[m] = [float(data) for data in test_data[m]]

        output = judge(test_data, mean_data)  # class_mean就等于mean_data 就是两个点

        count = 0
        for n in range(len(test_data)):
            if output[n] != test_label[n]:
                count = count + 1
        error = count / len(test_data)

        if error < min_error:
            min_error = error
            det_k = choice
            det_j = choice2
        print(min_error)
        print(det_k)
        print(det_j)




x_data, y_data, label_data, mean_data = read_and_mean('wine_train.csv', det_k, det_j)

# 这里处理要进行测试的文件
with open('wine_test.csv') as test_data:
    reader = test_data.readlines()  # 一行一行读取要测试的文件 读出来好像是字符形式的？？？
    test = [rows.split(',') for rows in reader]  # 按照逗号进行分割，数据一堆一堆分好
    test_data = [data[det_k: det_j + 1: det_j - det_k] for data in test]  # 取出坐标存储
    test_label = [data[13] for data in test]  # 取出标签存储
    test_label = [int(test) for test in test_label]  # 将label转换为int类型，将换行符分开 #这里的test_table是已经分好的标签，等会要与这个标签进行比较
for m in range(len(test_data)):
    test_data[m] = [float(data) for data in test_data[m]]

output = judge(test_data, mean_data)  # class_mean就等于mean_data 就是两个点

count = 0
for n in range(len(test_data)):
    if output[n] != test_label[n]:
        count = count + 1
error = count / len(test_data)
print(error)

x_data, y_data, label_data, mean_data2 = read_and_mean('wine_test.csv', det_k, det_j)


train_dataset = []
train_dataset.append(x_data)
train_dataset.append(y_data)
train_dataset = np.array(train_dataset)       #将输入转化为矩阵形式??? 矩阵的长度范围？？
mean_data = np.array(mean_data)
label_data = np.array(label_data)
plotDecBoundaries(train_dataset.T, label_data, mean_data)   #.T是矩阵的转置，？？？


