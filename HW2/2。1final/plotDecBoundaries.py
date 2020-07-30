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
    nclass =  max(np.unique(label_train))

    # Set the feature range for ploting
    max_x = np.ceil(max(training[:, 0])) + 1
    min_x = np.floor(min(training[:, 0])) - 1
    max_y = np.ceil(max(training[:, 1])) + 1
    min_y = np.floor(min(training[:, 1])) - 1

    xrange = (min_x, max_x)
    yrange = (min_y, max_y)

    # step size for how finely you want to visualize the decision boundary.
    inc = 0.005

    # generate grid coordinates. this will be the basis of the decision
    # boundary visualization.

    (x, y) = np.meshgrid(np.arange(xrange[0], xrange[1]+inc/100, inc), np.arange(yrange[0], yrange[1]+inc/100, inc))

    # size of the (x, y) image, which will also be the size of the
    # decision boundary image that is used as the plot background.
    image_size = x.shape
    xy = np.hstack( (x.reshape(x.shape[0]*x.shape[1], 1, order='F'), y.reshape(y.shape[0]*y.shape[1], 1, order='F')) ) # make (x,y) pairs as a bunch of row vectors.

    # distance measure evaluations for each (x,y) pair.
    pred_label2 = list()
    dist_mat = cdist(xy, sample_mean)
    print(dist_mat[0])
    print(dist_mat[1])
    print(dist_mat[2])
    print(dist_mat[3])
    print(dist_mat[4])
    print(dist_mat[5])
    print(dist_mat[6])
    print(dist_mat[7])
    for i in range(len(dist_mat)):
        if (dist_mat[i][0] < dist_mat[i][1]) and (dist_mat[i][3] < dist_mat[i][2]) and (dist_mat[i][5] < dist_mat[i][4]):
            pred_label2.append(2)
        elif (dist_mat[i][2] < dist_mat[i][3]) and (dist_mat[i][1] < dist_mat[i][0]) and (dist_mat[i][5] < dist_mat[i][4]):
            pred_label2.append(3)
        elif (dist_mat[i][4] < dist_mat[i][5]) and (dist_mat[i][1] < dist_mat[i][0]) and (dist_mat[i][3] < dist_mat[i][2]):
            pred_label2.append(4)
        else:
            pred_label2.append(6)

    print(len(pred_label2))
    pred_label = np.argmin(dist_mat, axis=1)
    print('\n')
    print(dist_mat)
    print('\n')
    print(pred_label)
    print(len(pred_label))
    pred_label2 = np.array(pred_label2)

    # reshape the idx (which contains the class label) into an image.
    decisionmap = pred_label2.reshape(image_size, order='F')

    print('\n')
    print(decisionmap)
    print(len(decisionmap))


    #show the image, give each coordinate a color according to its class label
    plt.imshow(decisionmap, extent=[xrange[0], xrange[1], yrange[0], yrange[1]], origin='lower')


    # plot the class training data.
    plt.plot(training[label_train == 1, 0],training[label_train == 1, 1], 'rx')
    plt.plot(training[label_train == 2, 0],training[label_train == 2, 1], 'go')
    if nclass == 3:
        plt.plot(training[label_train == 3, 0],training[label_train == 3, 1], 'b*')


    # include legend for training data
    if nclass == 3:
        l = plt.legend(('Class 1', 'Class 2', 'Class 3'), loc=2)
    else:
        l = plt.legend(('Class 1', 'Class 2'), loc=2)
    plt.gca().add_artist(l)


    m1, = plt.plot(sample_mean[0,0], sample_mean[0,1], 'rd', markersize=12, markerfacecolor='r', markeredgecolor='w')
    m2, = plt.plot(sample_mean[2,0], sample_mean[2,1], 'gd', markersize=12, markerfacecolor='g', markeredgecolor='w')
    if nclass == 3:
        m3, = plt.plot(sample_mean[4,0], sample_mean[4,1], 'bd', markersize=12, markerfacecolor='b', markeredgecolor='w')


    # include legend for class mean vector
    if nclass == 3:
        l1 = plt.legend([m1,m2,m3],['Class 1 Mean', 'Class 2 Mean', 'Class 3 Mean'], loc=4)
    else:
        l1 = plt.legend([m1,m2], ['Class 1 Mean', 'Class 2 Mean'], loc=4)

    plt.gca().add_artist(l1)

    plt.show()


