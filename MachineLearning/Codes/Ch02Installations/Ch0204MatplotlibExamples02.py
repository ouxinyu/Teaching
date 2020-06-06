# 通过inline指令，实现在Jupyter中的实时绘图功能
# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
x_index = np.arange(6)  # 柱的索引
x_data = ('China', 'America', 'Japan', 'Germany', 'France', 'Italy')
y1_data = (120, 325, 310, 235, 227, 256)
y2_data = (225, 312, 314, 221, 253, 341)
y3_data = (232, 332, 222, 241, 190, 299)
bar_width = 0.2  # 定义一个数字代表每个独立柱的宽度

# 使用 bar()函数定义柱状图的各个参数，依次包括：左偏移、高度、柱宽、透明度、颜色、图例
# 关于左偏移，不用关心每根柱的中心不中心，因为只要把刻度线设置在柱的中间就可以了
rects1 = plt.bar(x_index, y1_data, width=bar_width,
                 alpha=0.4, color='b', label='legend1')
rects2 = plt.bar(x_index + bar_width, y2_data, width=bar_width,
                 alpha=0.5, color='r', label='legend2')
rects3 = plt.bar(x_index + bar_width + bar_width, y3_data,
                 width=bar_width, alpha=0.5, color='c', label='legend3')

# 使用 xticks() 函数设置x轴的刻度线
plt.xticks(x_index + bar_width/2, x_data)
plt.legend()  # 显示图例
plt.show()
