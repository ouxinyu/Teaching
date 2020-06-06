# 导入数据生成器
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_blobs
# 导入数据集拆分工具
from sklearn.model_selection import train_test_split
# 导入数据预处理工具
from sklearn.preprocessing import StandardScaler
# 导入多层感知机神经网络
from sklearn.neural_network import MLPClassifier

# TODO: 1.生成数据集并进行数据划分
X, y = make_blobs(n_samples=200, centers=2, cluster_std=5, random_state=16)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=16)

# TODO: 2.数据预处理
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("训练集形态：{}，测试集形态：{}".format(X_train_scaled.shape, X_test_scaled.shape))

# TODO: 3.使用管道模型进行训练和评估
# 导入管道模型
# 建立包含预处理和神经网络的管道模型
pipeline = Pipeline([('scaler', StandardScaler()),
                     ('mlp', MLPClassifier(max_iter=1600, random_state=38))])
# 使用管道模型对训练集进行拟合
pipeline.fit(X_train, y_train)
print('使用管道模型的MLP模型评分：{:.2f}'.format(pipeline.score(X_test, y_test)))
