
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

#
def plot_1(font1,color):
    x = np.arange(1,11)
    y =  2  * x +  5
    plt.title("Matplotlib demo", fontproperties=font1)
    plt.xlabel("x axis caption", fontproperties=font1)
    plt.ylabel("y axis caption", fontproperties=font1)
    plt.plot(x,y,color)
    plt.show()

# matplotlib 生成正弦波图
def plot_sin(f,c):
    x =np.arange(0,3 *np.pi,0.1)
    y_sin =np.sin(x)
    y_cos =np.cos(x)
    #激活一个subplot
    plt.subplot(2,  1,  1)
    plt.title("sine save form ",fontproperties=f)
    plt.plot(x,y_sin,c)

    # 将第二个 subplot 激活，并绘制第二个图像
    plt.subplot(2,  1,  2)
    plt.title("cos save form ",fontproperties=f)
    plt.plot(x,y_cos,c)

    plt.show()


#pyplot 子模块提供 bar() 函数来生成条形图。
def plot_bar():
    x =  [5,7,8,10]
    y =  [12,99,76,66]
    x2 =  [6,9,12]
    y2 =  [46,55,72]
    plt.bar(x, y, align =  'center')
    plt.bar(x2, y2, color =  'g', align =  'center')
    plt.title('Bar graph')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()



#numpy.histogram() 函数是数据的频率分布的图形表示。 水平尺寸相等的矩形对应于类间隔，称为 bin，变量 height 对应于频率。
#numpy.histogram()函数将输入数组和 bin 作为两个参数。 bin 数组中的连续元素用作每个 bin 的边界。
def plot_histogram():
    a = np.array([21,2,15,16,1,5,44,88,90,67,89,77,55,43,64,48,68,65,45,25,22,57,87])
    bins =np.array([0,20,40,60,80,100])
    hist,bins =np.histogram(a,bins=bins)
    print("hist:",hist)
    print("bins",bins)

    plt.hist(a,bins)
    plt.title("histogram ")
    plt.show()

#打印自带的字体
def sys_fonts():
    print("matplotlib.fonts :")
    for i in sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist]):
        print(i)


if __name__ == '__main__':
    #sys_fonts()
    # fname 为 你下载的字体库路径，注意 SimHei.ttf 字体的路径
    font1 = matplotlib.font_manager.FontProperties(fname="/Users/Liuhua/Projects/pythonprojects/fonts/Calibri.ttf")
    #plot_1(font1=font1,color="r")
    plot_sin(f=font1,c="r")
    #plot_histogram()
    print("end work !")
