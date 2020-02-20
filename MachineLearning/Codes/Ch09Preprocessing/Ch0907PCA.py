import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
# 定义一个MLP对数据进行拟合和分析
from sklearn.neural_network import MLPClassifier

# TODO: 1.载入数据集
wine = datasets.load_wine()
X = wine.data
y = wine.target

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=16)

# 定义不同的输出名称
Xtrain = ['X_train', 'X_train_scaled', 'X_train_pca']
Xtest = ['X_test', 'X_test_scaled', 'X_test_pca']
model = ['原始数据', '预处理数据', 'PCA数据']

# TODO: 2.对原始数据进行预处理
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("原始数据的形态：训练集{}测试集{}".format(X_train.shape, X_test.shape))
print("预处理数据的形态：训练集{}测试集{}".format(X_train_scaled.shape, X_test_scaled.shape))
print("标签的形态：训练集{}测试集{}".format(y_train.shape, y_test.shape))

# TODO: 3.基于预处理数据进行PCA降维，设置主成分数量为2以便我们进行可视化
pca = PCA(n_components=2)
pca.fit(X_train_scaled)
X_train_pca = pca.transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)
print("PCA数据的形态, 训练集: {}, 测试集: {}".format(X_train_pca.shape, X_test_pca.shape))


# TODO: 4. 使用MLP在三种数据上进行训练，并输出评分

mlp = MLPClassifier(hidden_layer_sizes=[100,100], max_iter=2000, random_state=16)

for i in range(3):
    mlp.fit(eval(Xtrain[i]), y_train)
    score_train = mlp.score(eval(Xtrain[i]), y_train)
    score_test = mlp.score(eval(Xtest[i]), y_test)
    print("{0}: 训练集得分 {1:.4f}，测试集得分 {2:.4f}".format(model[i], score_train, score_test))


# TODO: 5. 可视化输出

plt.figure(figsize=(12, 4))

for i in range(np.size(model)):
    # 酒数据集总共有三个类别，分别用0，1，2表示
    Class0 = eval(Xtrain[i] + '[y_train==0]')
    Class1 = eval(Xtrain[i] + '[y_train==1]')
    Class2 = eval(Xtrain[i] + '[y_train==2]')

    plt.subplot(1, 3, i+1)
    plt.scatter(Class0[:, 0], Class0[:, 1], c='b', s=60, edgecolor='k')
    plt.scatter(Class1[:, 0], Class1[:, 1], c='c', s=60, edgecolor='k')
    plt.scatter(Class2[:, 0], Class2[:, 1], c='r', s=60, edgecolor='k')

    plt.legend(wine.target_names, loc='best')
    plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']
    plt.xlabel('特征一')
    plt.ylabel('特征二')
    plt.title('图' + str(i) + '：' + model[i])

plt.savefig('Codes//Ch09Preprocessing//results//Ch0907PCA.png', dpi=150)
plt.show()
