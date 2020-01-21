# 通过inline指令，实现在Jupyter中的实时绘图功能
# %matplotlib inline

# 使用import关键字引入matplotlib库，为了简便使用缩写 “plt”来表示matplotlib库。
import matplotlib.pyplot as plt
import numpy as np

# 使用linspace()函数生成一个-20到20，元素个数为10的等差数列。
# 令数列中的值为 x, 并根据表达式计算对应的 y值。
x = np.linspace(-20, 20, 10)
y = 2*x**2 - 3*x**4 + 6*x - 3

# 使用plot()函数绘制出曲线图
plt.plot(x, y, marker="o")
plt.show()
