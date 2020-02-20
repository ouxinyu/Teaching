# 导入数据生成器
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_blobs
# 导入数据集拆分工具
from sklearn.model_selection import train_test_split
# 导入数据预处理工具
from sklearn.preprocessing import StandardScaler
# 导入多层感知机神经网络
from sklearn.neural_network import MLPClassifier
# 导入画图工具
import matplotlib.pyplot as plt

# TODO: 1.生成数据集并进行数据划分
X, y = make_blobs(n_samples=200, centers=2, cluster_std=5, random_state=16)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=16)

# TODO: 2.数据预处理
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("训练集形态：{}，测试集形态：{}".format(X_train_scaled.shape, X_test_scaled.shape))

# TODO: 3.数据可视化
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

plt.scatter(X_train[:, 0], X_train[:, 1], label='原始数据')
plt.scatter(X_train_scaled[:, 0], X_train_scaled[:, 1],
            marker='^', edgecolor='k', label='预处理后数据')

plt.title('预处理前后训练集的分布情况图')
plt.legend(loc='best')
plt.show()

# TODO: 4.使用网格搜索输出评分
# 导入网格搜索类
# 设定网格搜索的目标参数字典
params = {'hidden_layer_sizes': [[50], [100], [100, 100]],
          'alpha': [0.0001, 0.001, 0.01, 0.1]}
# 建立网格搜索模型
mlp = MLPClassifier(max_iter=1600, random_state=16)
grid = GridSearchCV(mlp, param_grid=params, cv=3,
                    iid=False, verbose=1, n_jobs=8)
# 使用网格搜索拟合数据
grid.fit(X_train_scaled, y_train)
# 输出结果
print('模型最佳得分：{:.2f}'.format(grid.best_score_))
print('模型最佳参数：{}'.format(grid.best_params_))

print('测试集得分：{}'.format(grid.score(X_test_scaled, y_test)))
