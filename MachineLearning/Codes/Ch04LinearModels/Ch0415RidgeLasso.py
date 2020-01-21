'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 岭回归Ridge和套索回归Lasso的对比
@LastEditorTime: 2020-01-17
'''
# 0.导入数据集生成工具和拆分工具
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 配置参数使 matplotlib绘图工具可以显示中文
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

# 1. 载入糖尿病情数据集
X = load_diabetes().data
y = load_diabetes().target

# 2. 使用train_test_split()函数对数据集进行划分
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)

lasso1 = Lasso(alpha=1, max_iter=100000).fit(X_train, y_train)
lasso01 = Lasso(alpha=0.1, max_iter=100000).fit(X_train, y_train)
lasso00001 = Lasso(alpha=0.0001, max_iter=100000).fit(X_train, y_train)
ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)

plt.figure(dpi=120)
plt.plot(lasso1.coef_, 's', label="Lasso (alpha = 1)")
plt.plot(lasso01.coef_, '^', label="Lasso (alpha = 0.1)")
plt.plot(lasso00001.coef_, 'v', label="Lasso (alpha = 0.0001)")
plt.plot(ridge01.coef_, 'o', label="Ridge (alpha = 0.1)")
plt.legend(loc="best")
plt.xlabel("权重系数序号")
plt.ylabel("权重系数量级")
plt.hlines(0, 0, len(ridge01.coef_))  # 绘制当前坐标轴上的水平线

plt.show()
