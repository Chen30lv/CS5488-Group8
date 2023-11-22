import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['main_info', 'area', 'rain', 'uv']
a = [7.278, 32.629, 4.366, 3.39]
c = [1.949, 7.119, 0.866, 1.675]
b = [6.592, 26.438, 4.191, 2.227]

x = np.arange(len(labels))  # 标签位置
width = 0.3  # 柱状图的宽度，可以根据自己的需求和审美来改

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, a, width, label='Serial', color = "#77c6fc")
rects2 = ax.bar(x, b, width, label='Multiprocessing', color = "#bbe3fe")
rects3 = ax.bar(x + width, c, width, label='Joblib', color = "#ddf1fe")


# 为y轴、标题和x轴等添加一些文本。
ax.set_ylabel('Time Consuming', fontsize=12)
ax.set_xlabel('Preprocessing Different Data', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """在*rects*中的每个柱状条上方附加一个文本标签，显示其高度"""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3点垂直偏移
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()

plt.show()