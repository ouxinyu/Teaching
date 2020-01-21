'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 岭回归基本方法（糖尿病数据集）
@Destination：alpha对coef_属性的影响
@LastEditorTime: 2020-01-17
'''
# 0.导入数据集生成工具和拆分工具
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 配置参数使 matplotlib绘图工具可以显示中文
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

# 1. 载入糖尿病情数据集
X = load_diabetes().data
y = load_diabetes().target

# 2. 使用train_test_split()函数对数据集进行划分
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)

# 3. 使用线性回归模型计算权重 *w* 和 截距 *b* 的值，并给出回归模型的方程
lr = LinearRegression().fit(X_train, y_train)
ridge0 = Ridge(alpha=0).fit(X_train, y_train)
ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)
ridge1 = Ridge(alpha=1).fit(X_train, y_train)
ridge10 = Ridge(alpha=10).fit(X_train, y_train)

# 4. 将超参数 alpha 对 参数coef_ 的影响进行可视化
# 分别绘制线性回归模型, alpha = [0, 0.1, 1, 10]时的图形
plt.figure(dpi=120)  # 设置图形的尺度
plt.plot(lr.coef_, "s", label="线性回归模型")
plt.plot(ridge0.coef_, "^", label="岭回归模型(alpha=0)")
plt.plot(ridge01.coef_, "o", label="岭回归模型(alpha=0.1)")
plt.plot(ridge1.coef_, "<", label="岭回归模型(alpha=1)")
plt.plot(ridge10.coef_, "+", label="岭回归模型(alpha=10)")

plt.xlabel("权重系数序号")
plt.ylabel("权重系数量级")
plt.hlines(0, 0, len(lr.coef_))  # 绘制当前坐标轴上的水平线
plt.legend(loc='best')

plt.show()
