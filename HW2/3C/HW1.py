import math
from plotDecBoundaries import *


label4 = [1, 2, 3]
average4 = [[0, -2], [0, 1], [2, 0]]
label4 = np.array(label4)
average4 = np.array(average4)
print(average4)

trainingdata4 = [[2, -3, 2], [-3, 2, 2]]
trainingdata4 = np.array(trainingdata4)       #input
trainingdata4 = trainingdata4.T


plotDecBoundaries(trainingdata4, label4, average4)




