# 加载 pandas库，并使用read_csv()函数读取糖尿病预测数据集diabetes
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split

data = pd.read_csv('datasets/diabetes.csv')

# 将数据中的特征和标签进行分离，其中第0位位索引号，第1-8位位特征，第9位为标签
X = data.iloc[:, 0:8]
y = data.iloc[:, 8]

# 以 70%:30%的比例对训练集和测试集进行拆分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

dt3 = tree.DecisionTreeClassifier(max_depth=3)
dt5 = tree.DecisionTreeClassifier(max_depth=5)
dt3.fit(X_train, y_train)
dt5.fit(X_train, y_train)

print("max_depth=3, 训练集评分:{0:.3f}；测试集评分:{1:.3f}".format(
    dt3.score(X_train, y_train), dt3.score(X_test, y_test)))
print("max_depth=5, 训练集评分:{0:.3f}；测试集评分:{1:.3f}".format(
    dt5.score(X_train, y_train), dt5.score(X_test, y_test)))
