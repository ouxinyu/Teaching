'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 岭回归基本方法（糖尿病数据集）
alpha = 0.1
@LastEditorTime: 2020-01-17
'''
# 0.导入数据集生成工具和拆分工具
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

# 1. 载入糖尿病情数据集
from sklearn.datasets import load_diabetes
X = load_diabetes().data
y = load_diabetes().target

# 2. 使用train_test_split()函数对数据集进行划分
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)

# 3. 使用线性回归模型计算权重 *w* 和 截距 *b* 的值，并给出回归模型的方程
ridge = Ridge(alpha=0.1).fit(X_train, y_train)
# ridge = Ridge(alpha=10).fit(X_train, y_train)
# ridge = Ridge(alpha=0).fit(X_train, y_train)

# 4. 性能分析
score_train = ridge.score(X_train, y_train)
score_test = ridge.score(X_test, y_test)
print("训练集得分: {:.3f}".format(score_train))
print("测试集得分: {:.3f}".format(score_test))
