'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 
@LastEditorTime: 
'''
# 导入线性回归模型
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# 配置参数使 matplotlib绘图工具可以显示中文
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

# 输入三个点的坐标，分别保存在矩阵 x 和 y 中
X = [[1], [4], [3]]
y = [3, 5, 3]

# 使用线性模型来拟合这3个样本点
lr = LinearRegression().fit(X, y)

print("直线方程为：\n")
print("y = {:.3f}".format(lr.coef_[0]), "x", "+ {:.3f}".format(lr.intercept_))

# 画出点和基于点生成的直线
z = np.linspace(0, 5, 20)  # 生成 0到5之间，元素个数为20的等差数列
z = z.reshape(-1, 1)  # 将矩阵转换为 n 行，1列的矩阵

plt.scatter(X, y, s=80)
# 可视化预测结果，其中：
# 横坐标： 变量 z;
# 纵坐标： 基于 变量 z 和 线性模型 lr 生成的预测值。
# 第三个参数c：线的颜色
plt.plot(z, lr.predict(z), c="k")

# 设定图的显示信息并显示图片
plt.title("直线 Straight Line")
plt.show()
