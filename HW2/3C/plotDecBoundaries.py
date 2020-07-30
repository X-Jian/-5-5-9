################################################
## EE559 HW Wk2, Prof. Jenkins, Spring 2018
## Created by Arindam Jati, TA
## Tested in Python 3.6.3, OSX El Captain
################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

def plotDecBoundaries(training, label_train, sample_mean):

    #Plot the decision boundaries and data points for minimum distance to
    #class mean classifier
    #
    # training: traning data
    # label_train: class lables correspond to training data
    # sample_mean: mean vector for each class
    #
    # Total number of classes
    nclass =  max(np.unique(label_train))         #去除数组中重复的数字，排序后将其输出,max取最大，所以输出是3

    # Set the feature range for ploting
    max_x = np.ceil(max(training[:, 0])) + 1            #一个是计算大于等于该值的最小整数，另一个是计算小于等于该值的整数
    min_x = np.floor(min(training[:, 0])) - 1           #取所有行的第0列元素
    max_y = np.ceil(max(training[:, 1])) + 1            #取所有行的第1列元素 即是取出了红酒的第一个特征和第二个特征
    min_y = np.floor(min(training[:, 1])) - 1           #为什么要减去1？？？？

    xrange = (min_x, max_x)                           #保存一下范围，这是不可变的数组
    yrange = (min_y, max_y)

    # step size for how finely you want to visualize the decision boundary.
    inc = 0.005

    # generate grid coordinates. this will be the basis of the decision
    # boundary visualization.
    #arrange从起点到终点，步长为1，不包括终
    (x, y) = np.meshgrid(np.arange(xrange[0], xrange[1]+inc/100, inc), np.arange(yrange[0], yrange[1]+inc/100, inc)) #网格点和坐标矩阵来保存位置
    #x从10到16  y从-0。995到1  步长0。005 有（x,y）就有网格坐标了

    # size of the (x, y) image, which will also be the size of the
    # decision boundary image that is used as the plot background.
    image_size = x.shape         #.shape0表示第一维的长度，。shape1 表示第二维的长度
    xy = np.hstack( (x.reshape(x.shape[0]*x.shape[1], 1, order='F'), y.reshape(y.shape[0]*y.shape[1], 1, order='F')) ) # make (x,y) pairs as a bunch of row vectors.

    # distance measure evaluations for each (x,y) pair.
    dist_mat = cdist(xy, sample_mean)
    pred_label = np.argmin(dist_mat, axis=1)

    # reshape the idx (which contains the class label) into an image.
    decisionmap = pred_label.reshape(image_size, order='F')


    #show the image, give each coordinate a color according to its class label
    plt.imshow(decisionmap, extent=[xrange[0], xrange[1], yrange[0], yrange[1]], origin='lower')
    #plt.imshow()函数负责对图像进行处理，并显示其格式，而plt.show()则是将plt.imshow()处理后的函数显示出来。

    # plot the class training data.
    plt.plot(training[label_train == 1, 0],training[label_train == 1, 1])    #在数据中把标号为1的全挑出来，画散点  label_train == 1会返回下标？？？
    plt.plot(training[label_train == 2, 0],training[label_train == 2, 1])    #标签为2的x和y
    if nclass == 3:
        plt.plot(training[label_train == 3, 0],training[label_train == 3, 1])


    # include legend for training data
    if nclass == 3:
        l = plt.legend(('Class 1', 'Class 2', 'Class 3'), loc=2)      #这是设置位置的
    else:
        l = plt.legend(('Class 1', 'Class 2'), loc=2)
    plt.gca().add_artist(l)

    # plot the class mean vector. 画平均值  只关心第一个值，不关心后面的值，所以逗号表示
    m1, = plt.plot(sample_mean[0,0], sample_mean[0,1], 'rd', markersize=12, markerfacecolor='r', markeredgecolor='w')
    m2, = plt.plot(sample_mean[1,0], sample_mean[1,1], 'gd', markersize=12, markerfacecolor='g', markeredgecolor='w')
    if nclass == 3:
        m3, = plt.plot(sample_mean[2,0], sample_mean[2,1], 'bd', markersize=12, markerfacecolor='b', markeredgecolor='w')


    # include legend for class mean vector
    if nclass == 3:
        l1 = plt.legend([m1,m2,m3],['Class 1 Mean', 'Class 2 Mean', 'Class 3 Mean'], loc=4)
    else:
        l1 = plt.legend([m1,m2], ['Class 1 Mean', 'Class 2 Mean'], loc=4)

    plt.gca().add_artist(l1)

    plt.show()


