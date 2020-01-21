# 加载 pandas库，并使用read_csv()函数读取糖尿病预测数据集diabetes
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
data = pd.read_csv('datasets/diabetes.csv')

# 将数据中的特征和标签进行分离，其中第0位位索引号，第1-8位位特征，第9位为标签
X = data.iloc[:, 0:8]
y = data.iloc[:, 8]

# 以 70%:30%的比例对训练集和测试集进行拆分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 引入KNN分类模型, 并配置KNN分类器，设置近邻数 = 2
gnb = GaussianNB()
gnb.fit(X_train, y_train)


data_id = 39
data_x = [np.array(X_test)[data_id]]
data_y = np.array(y_test)[data_id]

print("样本的正确分类为: {}".format(data_y))

print("GaussianNB模型预测的分类是: {}".format(gnb.predict(data_x)[0]))
print("+ 属于分类0的概率值是：{:.5f}".format(gnb.predict_proba(data_x)[0][0]))
print("+ 属于分类1的概率值是：{:.5f}".format(gnb.predict_proba(data_x)[0][1]))
