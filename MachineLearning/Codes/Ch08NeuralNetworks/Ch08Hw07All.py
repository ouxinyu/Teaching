# TODO: 1. 导入必须库 以及 定义必要的函数
import numpy as np
import matplotlib.pyplot as plt
# 导入数据集工具包
from sklearn import datasets
from sklearn.model_selection import train_test_split
# 导入MLP神经网络包
from sklearn.neural_network import MLPClassifier

# TODO: 2. 创建/导入数据
iris = datasets.load_iris()

# TODO: 3. 数据预处理，包括训练集、测试集划分，数据正则化，数据清洗等
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.1, random_state=10)

xticks = ['Baseline', 'Single', 'Multi', 'Logistic', 'Tanh', 'ReLU']
num = len(xticks)
scores_test = np.zeros([1, num])

# TODO: 4. 构建模型，并进行模型训练（或称为拟合数据）
mlp_Baseline = MLPClassifier(solver='lbfgs', random_state=10)
mlp_Baseline.fit(X_train, y_train)
scores_test[0, 0] = mlp_Baseline.score(X_test, y_test)

mlp_Single = MLPClassifier(
    solver='lbfgs', random_state=10, hidden_layer_sizes=[10])
mlp_Single.fit(X_train, y_train)
scores_test[0, 1] = mlp_Single.score(X_test, y_test)

mlp_Multi = MLPClassifier(solver='lbfgs', random_state=10,
                          hidden_layer_sizes=[32, 128, 128])
mlp_Multi.fit(X_train, y_train)
scores_test[0, 2] = mlp_Multi.score(X_test, y_test)


mlp_Logistic = MLPClassifier(solver='lbfgs', random_state=10,
                             activation='logistic', hidden_layer_sizes=[32, 128, 128])
mlp_Logistic.fit(X_train, y_train)
scores_test[0, 3] = mlp_Logistic.score(X_test, y_test)


mlp_Tanh = MLPClassifier(solver='lbfgs', random_state=10,
                         activation='tanh', hidden_layer_sizes=[32, 128, 128])
mlp_Tanh.fit(X_train, y_train)
scores_test[0, 4] = mlp_Tanh.score(X_test, y_test)


mlp_ReLU = MLPClassifier(solver='lbfgs', random_state=10,
                         activation='relu', hidden_layer_sizes=[32, 128, 128])
mlp_ReLU.fit(X_train, y_train)
scores_test[0, 5] = mlp_ReLU.score(X_test, y_test)

plt.figure(dpi=100)
plt.plot(scores_test[0, :], label='Test')
plt.legend(loc='best')
plt.savefig('Codes//Ch08NeuralNetworks//results//Ch08Hw01NN.png', dpi=150)
plt.show()
