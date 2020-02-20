from sklearn import preprocessing
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# TODO: 1.载入数据集
wine = datasets.load_wine()
X_train, X_test, y_train, y_test = train_test_split(
    wine.data, wine.target, random_state=62)
print(wine.data.shape, X_train.shape, X_test.shape)

# TODO: 2.基于原始数据训练模型，并输出得分
mlp = MLPClassifier(hidden_layer_sizes=[
                    100, 100], max_iter=2000, random_state=62)
# ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
mlp.fit(X_train, y_train)
print('原始数据，测试集得分：{:.4f}'.format(mlp.score(X_test, y_test)))

# 导入preprocessing预处理器

# TODO: 3.基于预处理数据训练模型，并输出得分
methods = ['StandardScaler', 'MinMaxScaler', 'MaxAbsScaler',
           'RobustScaler', 'Normalizer', 'Binarizer']

for str in methods:
    scaler = eval('preprocessing.' + str + '().fit(X_train)')
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    mlp.fit(X_train_scaled, y_train)
    print('预处理方法: {}, 测试集得分: {:.4f}'.format(
        str, mlp.score(X_test_scaled, y_test)))
