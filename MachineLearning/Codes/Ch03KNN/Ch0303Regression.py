'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 基于KNN的回归
@LastEditorTime: 2020-1-16
'''

# 1. 生成数据集
# 导入样数据集生成器
# 导入计算库
import numpy as np
# 从近邻算法子库中导入K近邻回归器KNeighborsRegressor
from sklearn.neighbors import KNeighborsRegressor
# 导入绘图工具箱 matplotlib
import matplotlib.pyplot as plt
# 从模型选择子库中导入数据集拆分工具
from sklearn.model_selection import train_test_split

# 导入make_regression数据集生成器
from sklearn.datasets import make_regression

# 生成特征数为 1, 噪声为 50的的数据集
X, y = make_regression(n_samples=1000, n_features=1,
                       n_informative=1, noise=50, random_state=8)

# 用散点图将数据点纪念性可视化
plt.scatter(X, y, c='orange', edgecolor='k')
# plt.show()

# 2. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=8, test_size=0.3)


# 3. 基于训练集数据训练KNN模型

# 用 KNN模型拟合数据
reg = KNeighborsRegressor(n_neighbors=5)  # n_neighbors=5 是 K近邻算法的默认值
reg.fit(X_train, y_train)


# 4. 预测及评分

# 把预测结果用图像进行可视化
z = np.linspace(-3, 3, 200).reshape(-1, 1)
plt.scatter(X, y, c='orange', edgecolor='k')
plt.plot(z, reg.predict(z), c='k', linewidth=3)

# 向图像添加标题
plt.title("KNN Regressor")

print("模型评分：{:.2f}".format(reg.score(X_test, y_test)))

# plt.show()

# 5. 模型优化

# 减少模型的近邻数 n_neighbors参数为 2
reg2 = KNeighborsRegressor(n_neighbors=13)
reg2.fit(X_train, y_train)

# 重新进行可视化
plt.scatter(X, y, c='orange', edgecolor='k')
plt.plot(z, reg2.predict(z), c='k', linewidth=3)
plt.title('KNN Regressor: n_neighbors = 2')

print("优化后的模型评分: {:.2f}".format(reg2.score(X_test, y_test)))

plt.show()
