# Despp: 评估PCA参数n_compponents对模型性能的影响，并可视化性能对比图
#
import numpy as np
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
# 定义一个MLP对数据进行拟合和分析
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

# TODO: 1. 载入数据集
wine = datasets.load_wine()
X = wine.data
y = wine.target

# TODO: 2. 数据预处理
# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=16)

scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

scoresA = np.zeros([3, 13])  # 创建一个数组用于存储得分，第一列是特征数量
scoresB = np.zeros([3, 13])
scoresA[0, :] = range(X.shape[1])
scoresB[0, :] = np.linspace(0.1, 0.99, num=13)

# 基于主成分个数
for i in range(X.shape[1]):
    # TODO: 3. 进行PCA降维
    pca = PCA(n_components=i + 1)
    pca.fit(X_train_scaled)
    X_train_pca = pca.transform(X_train_scaled)
    X_test_pca = pca.transform(X_test_scaled)

    # TODO: 4.训练MLP模型
    mlp = MLPClassifier(hidden_layer_sizes=[
                        100, 100], max_iter=2000, random_state=16)
    mlp.fit(X_train_pca, y_train)

    score_train = mlp.score(X_train_pca, y_train)
    score_test = mlp.score(X_test_pca, y_test)
    scoresA[1, i] = score_train
    scoresA[2, i] = score_test
    print("n_components={0}: 训练集得分 {1:.4f}，测试集得分 {2:.4f}".format(
        i+1, score_train, score_test))

print('')
# 基于信息量百分比
n = 0
for i in scoresB[0, :]:
    # TODO: 3. 进行PCA降维
    pca = PCA(n_components=i)
    pca.fit(X_train_scaled)
    X_train_pca = pca.transform(X_train_scaled)
    X_test_pca = pca.transform(X_test_scaled)

    # TODO: 4.训练MLP模型
    mlp = MLPClassifier(hidden_layer_sizes=[
                        100, 100], max_iter=2000, random_state=16)
    mlp.fit(X_train_pca, y_train)

    score_train = mlp.score(X_train_pca, y_train)
    score_test = mlp.score(X_test_pca, y_test)
    scoresB[1, n] = score_train
    scoresB[2, n] = score_test
    print("n_components={0:.2f}: 训练集得分 {1:.4f}，测试集得分 {2:.4f}".format(
        i, score_train, score_test))
    n = n + 1


plt.figure(figsize=(16, 4))
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

plt.subplot(121)
plt.plot(scoresA[0, :], scoresA[1, :], 'g-', label='训练集（个数）')
plt.plot(scoresA[0, :], scoresA[1, :], 'b-', label='测试集（个数）')
plt.legend(['训练集', '测试集'], loc='best')
plt.title('基于主成分个数的性能对比图')

plt.subplot(122)
plt.plot(scoresB[0, :], scoresB[1, :], 'g--', label='训练集（信息量）')
plt.plot(scoresB[0, :], scoresB[1, :], 'b--', label='测试集（信息量）')
plt.legend(['训练集', '测试集'], loc='best')
plt.title('基于信息量百分比的性能对比图')

plt.savefig('Codes//Ch09Preprocessing//results//Ch0908PCAEvalParameters.png', dpi=150)
plt.show()
