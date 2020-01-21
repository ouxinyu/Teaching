'''
@Author: Xin-Yu Ou (欧新宇)
@Description:
@LastEditorTime:
'''
# 导入线性回归模型等多个库
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# 配置参数使 matplotlib绘图工具可以显示中文
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

# 使用make_regression()函数生成数据集
X, y = make_regression(n_samples=50, n_features=1, n_informative=1, noise=50, random_state=1)

# 使用线性模型来拟合这3个样本点
lr = LinearRegression().fit(X, y)

print("直线方程为：\n")
w = lr.coef_[0]
b = lr.intercept_
print("y = {:.3f}".format(w), "x", "+ {:.3f}".format(b))
print("其中，权重系数为: {0:.3f}, 截距为: {1:.3f}。".format(w, b))

# 画出点和基于点生成的直线
z = np.linspace(-3, 3, 200)  # 生成 -3到3之间，元素个数为200的等差数列
z = z.reshape(-1, 1)  # 将矩阵转换为 n 行，1列的矩阵

plt.figure(dpi=100)
plt.scatter(X, y, c="b", s=40)  # s为散点的尺度
# 可视化预测结果，其中：
# 横坐标： 变量 z;
# 纵坐标： 基于 变量 z 和 线性模型 lr 生成的预测值。
# 第三个参数c：线的颜色
plt.plot(z, lr.predict(z), c="k")

# 设定图的显示信息并显示图片
plt.title("线性回归")
plt.show()
