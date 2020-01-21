'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 实例分析———基于Adult数据集的相亲问题
@LastEditorTime: 2020-01-18
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
import pandas as pd

# 1. 载入数据集及数据预处理
train = pd.read_csv('datasets/adult/adult_train.csv', header=None, index_col=False,
                    names=['年龄', '单位性质', '权重', '学历', '受教育时长',
                           '婚姻状况', '职业', '家庭情况', '种族', '性别',
                           '资产所得', '资产损失', '周工作时长', '原籍',
                           '收入'])

test = pd.read_csv('datasets/adult/adult_test.csv', header=None, index_col=False,
                   names=['年龄', '单位性质', '权重', '学历', '受教育时长',
                          '婚姻状况', '职业', '家庭情况', '种族', '性别',
                          '资产所得', '资产损失', '周工作时长', '原籍',
                          '收入'])
test = test.loc[1:]

train_dummies = pd.get_dummies(train)
test_dummies = pd.get_dummies(test)

# axis = 0表示在纵轴上进行合并； axis = 1 表示在横轴上进行合并。
data = pd.concat([train, test], ignore_index=True, axis=0)
data_dummies = pd.get_dummies(data)

train_dummies = data_dummies.loc[0:train.shape[0] - 1]
test_dummies = data_dummies.loc[train.shape[0]:]

X_train = train_dummies.loc[:, '权重':'原籍_ Yugoslavia'].values
y_train = train_dummies['收入_ >50K'].values

X_test = test_dummies.loc[:, '权重':'原籍_ Yugoslavia'].values
y_test = test_dummies['收入_ >50K'].values

# 2. 分别使用决策树模型和随机森林进行模型训练
# 设置超参数
# 对于决策树，我们遍历树的深度，设 max_depth = [1 : 100]
# 对于随机森林，我们遍历森林的规模，设 n_estimators = [1 : 100]

n = 100
# 第1-4列分别为：score_train_dt,score_test_dt,score_train_rf,score_test_rf
scores = np.zeros([4, n])
num = np.arange(0, n)


for i in num:
    n = i + 1

    # 利用当行刷新方法显示正在计算的模型
    print("\r 正在计算第{}/{}个模型，请稍等...".format(n, num.shape[0]), end="")

    dt = tree.DecisionTreeClassifier(max_depth=n)
    dt.fit(X_train, y_train)

    rf = RandomForestClassifier(n_estimators=n, random_state=3, n_jobs=-1)
    rf.fit(X_train, y_train)

    scores[0, i] = dt.score(X_train, y_train)
    scores[1, i] = dt.score(X_test, y_test)
    scores[2, i] = rf.score(X_train, y_train)
    scores[3, i] = rf.score(X_test, y_test)

    if i == num.shape[0] - 1:
        print("计算完毕！")

# 输出参数敏感"性能曲线图"

plt.figure(dpi=100)
plt.plot(num, scores[0, :], label="DecisionTree_Train")
plt.plot(num, scores[1, :], label="DecisionTree_Test")
plt.plot(num, scores[2, :], label="ForestClassifier_Train")
plt.plot(num, scores[3, :], label="ForestClassifier_Test")

plt.legend()
plt.show()
