'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 
@LastEditorTime: 
'''
'''
@Author: Xin-Yu Ou (欧新宇)
@Description:
@LastEditorTime:
'''
# 加载 pandas库，并使用read_csv()函数读取糖尿病预测数据集diabetes
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

data = pd.read_csv('Datasets/diabetes.csv')

# 将数据中的特征和标签进行分离，其中第0位位索引号，第1-8位位特征，第9位为标签

X = data.iloc[:, 0:8]
y = data.iloc[:, 8]

# 以 70%:30%的比例对训练集和测试集进行拆分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 引入KNN分类模型, 并配置KNN分类器，设置近邻数 = 2
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train, y_train)

train_score = knn.score(X_train, y_train)
test_score = knn.score(X_test, y_test)

print("训练集评分:{0:.2f}；测试集评分:{1:.2f}".format(train_score, test_score))


noStudent = 131
X_new = np.array([[noStudent//6, noStudent*3,
                   noStudent*2, noStudent, noStudent*4,
                   noStudent/7, noStudent/6, noStudent]])
prediction = knn.predict(X_new)
print("新样本的分类为：{}".format(prediction))
