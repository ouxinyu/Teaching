# 导入数据生成器
from sklearn.datasets import make_blobs
# 导入数据集拆分工具
from sklearn.model_selection import train_test_split
# 导入数据预处理工具
from sklearn.preprocessing import StandardScaler
# 导入多层感知机神经网络
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import GridSearchCV  # 导入管道模型
from sklearn.pipeline import Pipeline

# TODO: 1.生成数据集并进行数据划分
X, y = make_blobs(n_samples=200, centers=2, cluster_std=5, random_state=16)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=16)

# TODO: 2.创建管道模型，并创建预处理模块scaler和神经网络模块mlp
params = {'mlp__hidden_layer_sizes': [[50], [100], [100, 100]],
          'mlp__alpha': [0.0001, 0.001, 0.01, 0.1]}

pipeline = Pipeline(steps=[('scaler', StandardScaler()),
                           ('mlp', MLPClassifier(max_iter=1600, random_state=16))], verbose=0)

# TODO: 3.创建网格搜索模型，并输出预测结果
grid = GridSearchCV(pipeline, param_grid=params, cv=5,
                    iid=False, n_jobs=8, verbose=1)
grid.fit(X_train, y_train)
print('交叉验证评分:{:.2f}'.format(grid.best_score_))
print('模型最优参数：{}'.format(grid.best_params_))
print('测试集得分：{}'.format(grid.score(X_test, y_test)))

print(pipeline.steps)
