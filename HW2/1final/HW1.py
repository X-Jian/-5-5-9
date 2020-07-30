import numpy as np
import matplotlib.pyplot as plt


y = np.linspace(-4, 10, 200)
x1 = -y + 5
x2 = ((-y) * 0) + 3
x3 = y - 1

fig = plt.figure()
plt.plot(x1, y, color='black', linewidth=2)
plt.plot(x2, y, color='darkolivegreen', linewidth=2)
plt.plot(x3, y, color='blue', linewidth=2)

plt.xlim((-4, 10))
plt.ylim((-4, 10))
plt.xlabel('x1', color='black')
plt.ylabel('x2', color='black')


x_ticks = np.arange(-4, 10, 1)
y_ticks = np.arange(-4, 10, 1)
plt.xticks(x_ticks)
plt.yticks(y_ticks)



x_prime = np.linspace(-4, 10, 200)
y12 = - x_prime + 5
y23 = x_prime + 1

plt.fill_between(x_prime, -4, y12, where=x_prime <= 3, color='grey', label='region 1')
plt.fill_between(x_prime, y12, 10, where=x_prime <= 2.1, color='limegreen', label='region 2')
plt.fill_between(x_prime, y23, 10, where=x_prime > 2, color='limegreen')
plt.fill_between(x_prime, -4, y23, where=x_prime >= 3, color='plum', label='region 3')


def judge(xaxis, yaxis):
    if (-xaxis - yaxis + 5 == 0) or (-xaxis + 3 == 0) or (-xaxis + yaxis - 1 == 0):
        return 0
    elif(-xaxis - yaxis + 5 > 0) and (-xaxis + 3 > 0):
        return 1
    elif(-xaxis - yaxis + 5 < 0) and (-xaxis + yaxis - 1 > 0):
        return 2
    elif(-xaxis + 3 < 0) and (-xaxis + yaxis - 1 < 0):
        return 3
    else:
        return 0


label1 = judge(4, 1)
label2 = judge(1, 5)
label3 = judge(0, 0)


if label1 == 0:
    label1 = "indeterminate"
if label2 == 0:
    label2 = "indeterminate"
if label3 == 0:
    label4 = "indeterminate"


plt.plot(4, 1, 'ro', color='firebrick', label="in %s" % label1)
plt.plot(1, 5, 'bs', color='firebrick', label="in %s" % label2)
plt.plot(0, 0, 'g^', color='firebrick', label="in %s" % label3)

plt.legend()
plt.show()

