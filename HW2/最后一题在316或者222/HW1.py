import numpy as np
import matplotlib.pyplot as plt


y = np.linspace(-4, 10, 200)            # 图像仅在-5到15之间显示，显示100个点
x1 = -y + 5
x2 = ((-y) * 0) + 3
x3 = y - 1

fig = plt.figure()                  #建立图的大小是8*8的大小,创建画布
plt.plot(x1, y, color='black', linewidth=2)      #绘图的函数，这里一共绘制了3幅图 linewidth设置线宽，这里查一下如何设置标签，题目和x1以及x2
plt.plot(x2, y, color='darkolivegreen', linewidth=2)
plt.plot(x3, y, color='blue', linewidth=2)

plt.xlim((-4, 10))                  #这个方法是从x轴上的最小值到最大值
plt.ylim((-4, 10))                    #这个方法是从y轴上的最小值到最大值
plt.xlabel('x1', color='black')
plt.ylabel('x2', color='black')           #自己加的,横坐标x1，纵坐标x2

#设置坐标刻度
x_ticks = np.arange(-4, 10, 1)
y_ticks = np.arange(-4, 10, 1)
plt.xticks(x_ticks)
plt.yticks(y_ticks)



x_prime = np.linspace(-4, 10, 200)      # 坐标从-5到10，返回的样本数量是200个，产生从-5到10的等差数列
y12 = - x_prime + 5
y23 = x_prime + 1

plt.fill_between(x_prime, -4, y12, where=x_prime <= 3, color='grey', label='region 1')   #fill_between 填充两个函数中间的区域 横坐标x1,纵坐标y1到-5，并且x1小于3画图
plt.fill_between(x_prime, y12, 10, where=x_prime <= 2.1, color='limegreen', label='region 2') #先定义曲线x的坐标，再定义第一条曲线y1的坐标，定义第二条曲线y2的坐标
plt.fill_between(x_prime, y23, 10, where=x_prime > 2, color='limegreen') #先定义曲线x的坐标，再定义第一条曲线y1的坐标，定义第二条曲线y2的坐标
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


#圆，方，三角三个点
plt.plot(4, 1, 'ro', color='firebrick', label="in %s" % label1)
plt.plot(1, 5, 'bs', color='firebrick', label="in %s" % label2)
plt.plot(0, 0, 'g^', color='firebrick', label="in %s" % label3)

plt.legend()       #图例
plt.show()       #这一句语句是开始画上面的图

