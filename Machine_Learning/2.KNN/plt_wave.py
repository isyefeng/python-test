import matplotlib
import matplotlib.pyplot as plt

def DisplayWave(xline, yline):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)             #创建1个框图
    ax.scatter(xline,yline)
    plt.show()

