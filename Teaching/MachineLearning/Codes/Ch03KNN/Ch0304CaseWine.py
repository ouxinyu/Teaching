'''
@Author: Xin-Yu Ou (欧新宇)
@Description: K最近邻算法案例 —— 酒的分类
@LastEditorTime: 2020-01-16
'''
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
# 导入绘图工具箱 matplotlib
import matplotlib.pyplot as plt

# 1. 载入数据集
# 从sklearn的datasets模块中载入数据集
wine_dataset = load_wine()

# 2. 对数据集进行拆分（训练集+测试集）
# 导入数据集拆分工具

# 将数据集进行拆分，按照默认的比例进行拆分，其中训练集占75%，测试集占25%
X_train, X_test, y_train, y_test = train_test_split(wine_dataset['data'],
                                                    wine_dataset['target'],
                                                    random_state=0)

# 3. 使用KNN构建模型
# 引入KNN分类模型, 并配置KNN分类器，设置近邻数 = 1
knn = KNeighborsClassifier(n_neighbors=15, weights='distance')

knn.fit(X_train, y_train)

# 4. 预测与评分
score_train = knn.score(X_train, y_train)
score_test = knn.score(X_test, y_test)

print("训练集评分:{0:.2f}; 测试集评分:{1:.2f}".format(score_train, score_test))

# 查看样本特征集合属性
print("数据集中的样本总共有{}种特征，分别是：{}".format(
    len(wine_dataset['feature_names']), wine_dataset['feature_names']))

# 生成预测数据并进行预测
X_new = np.array([[32, 1, 3, 3, 3, 3, 3, 32, 1, 3, 3, 3, 3]])
prediction = knn.predict(X_new)
print("新酒的分类为{}".format(wine_dataset['target_names'][prediction]))

# 5. 进一步分析超参数对系统性能的影响
# 建立两个空列表，分别用于保存训练集和测试集的模型评分
training_score = []
test_score = []
neighbors_amount = range(1, 30)
for n_neighbors in neighbors_amount:
    clf3 = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf3.fit(X_train, y_train)

    score_train = clf3.score(X_train, y_train)
    score_test = clf3.score(X_test, y_test)
    # print("n_neighbors:{0}; train_score:{1:.2f}; test_score:{2:.2f}.\n".format(n_neighbors, score_train, score_test))

    # 把不同的n_neighbors数量对应的得分放进列表
    training_score.append(score_train)
    test_score.append(score_test)


# 下面用matplotlib将得分进行绘图
plt.plot(neighbors_amount, training_score, label="training score")
plt.plot(neighbors_amount, test_score, label="test score")
plt.ylabel("score")
plt.xlabel("n_neighbors")
plt.title("Learning Curve for the different number of neighbors")
plt.legend()
plt.show()
