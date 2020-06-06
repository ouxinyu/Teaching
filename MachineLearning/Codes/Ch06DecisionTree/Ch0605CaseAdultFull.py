'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 实例分析———基于Adult数据集的相亲问题
@LastEditorTime: 2020-01-18
'''
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

dt = tree.DecisionTreeClassifier(max_depth=5)
dt.fit(X_train, y_train)

forest = RandomForestClassifier(n_estimators=6, random_state=3, n_jobs=-1)
forest.fit(X_train, y_train)

# 3. 输出预测准确率

print('决策树模型: 训练集得分: {0:.3f}，测试集得分: {1:.3f}'.format(
    dt.score(X_train, y_train), dt.score(X_test, y_test)))
print('随机森林模型: 训练集得分: {0:.3f}，测试集得分: {1:.3f}'.format(
    forest.score(X_train, y_train), forest.score(X_test, y_test)))
