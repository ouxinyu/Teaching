'''
@Author: Xin-Yu Ou (欧新宇)
@Description:
@LastEditorTime:
'''
import numpy as np
import matplotlib.pyplot as plt

# 配置参数使 matplotlib绘图工具可以显示中文
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

# 设置自变量 x：令x为-5到5之间，元素数量为100的等差数列
x = np.linspace(-5, 5, 100)

# 按照方程的数学表达式，定义直线方程
y = 0.5*x + 3

# 设置绘图内容的基本参数
plt.plot(x, y, c="blue")
# 设置图的题目
plt.title("直线 Straight Line")
# 激活绘图功能，在坐标轴上显示直线
plt.show()
