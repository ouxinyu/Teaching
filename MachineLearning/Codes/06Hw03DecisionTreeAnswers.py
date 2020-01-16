# 加载 pandas库，并使用read_csv()函数读取糖尿病预测数据集diabetes
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = pd.read_csv('datasets/diabetes.csv')

# 将数据中的特征和标签进行分离，其中第0位位索引号，第1-8位位特征，第9位为标签
X = data.iloc[:, 0:8]
y = data.iloc[:, 8]

# 以 70%:30%的比例对训练集和测试集进行拆分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

n = 40
# 第1-4列分别为：score_train_dt,score_test_dt,score_train_rf,score_test_rf
scores = np.zeros([4, n])
num = np.arange(0, n)

for i in num:
    n = i + 1

    # 利用当行刷新方法显示正在计算的模型
    print("\r 正在计算第{}/{}个模型，请稍等...".format(n, num.shape[0]), end="")

    dt = tree.DecisionTreeClassifier(max_depth=n)
    dt.fit(X_train, y_train)

    rf = RandomForestClassifier(n_estimators=n, random_state=8, n_jobs=-1)
    rf.fit(X_train, y_train)

    scores[0, i] = dt.score(X_train, y_train)
    scores[1, i] = dt.score(X_test, y_test)
    scores[2, i] = rf.score(X_train, y_train)
    scores[3, i] = rf.score(X_test, y_test)

    if i == num.shape[0] - 1:
        print("计算完毕！")


plt.figure(dpi=100)
plt.plot(num, scores[0, :], label="DecisionTree_Train")
plt.plot(num, scores[1, :], label="DecisionTree_Test")
plt.plot(num, scores[2, :], label="ForestClassifier_Train")
plt.plot(num, scores[3, :], label="ForestClassifier_Test")

plt.legend(loc='upper right')
plt.show()
