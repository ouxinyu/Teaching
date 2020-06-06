'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 实例分析———基于Adult数据集的相亲问题
@LastEditorTime: 2020-01-18
'''
from sklearn import tree
from sklearn.model_selection import train_test_split
import pandas as pd

# 1. 载入数据集及数据预处理
data = pd.read_csv('datasets/adult/adult_train.csv', header=None, index_col=False,
                   names=['年龄', '单位性质', '权重', '学历', '受教育时长',
                          '婚姻状况', '职业', '家庭情况', '种族', '性别',
                          '资产所得', '资产损失', '周工作时长', '原籍',
                          '收入'])

# 为了方便展示，可以选取其中一部分特征（9个）进行显示
data_lite = data[['年龄', '单位性质', '学历', '婚姻状况', '种族', '性别', '周工作时长', '职业', '收入']]
data_dummies = pd.get_dummies(data_lite)

features = data_dummies.loc[:, '年龄':'职业_ Transport-moving']
X = features.values
y = data_dummies['收入_ >50K'].values

# 拆分数据集，并用训练数据拟合决策树模型
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# 2. 训练模型
dt = tree.DecisionTreeClassifier(max_depth=5)
dt.fit(X_train, y_train)

# 3. 输出预测准确率
print('模型得分:{:.2f}'.format(dt.score(X_test, y_test)))


# 4. 利用给定数据进行分类预测
Mr_Right = [[27, 35, 0, 0, 0, 0, 0, 0, 0, 1,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 1, 0, 0, 0, 0]]

pred = dt.predict(Mr_Right)
if dt == 1:
    print("大胆去追求真爱吧，这哥们月薪过5万了！")
else:
    print("不用去了，不满足你的要求")
