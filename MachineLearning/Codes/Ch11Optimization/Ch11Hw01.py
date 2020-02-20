# TODO: 1. 导入必须库 以及 定义必要的函数
# 导入机器学习数据集处理工具
import time
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn import datasets
from sklearn.model_selection import train_test_split

# TODO: 2. 创建/导入数据
iris = datasets.load_iris()

# TODO: 3. 数据预处理，包括训练集、测试集划分，数据正则化，数据清洗等
X = iris.data
y = iris.target
X_trainval, X_test, y_trainval, y_test = train_test_split(
    X, y, train_size=0.7, random_state=16)
# X_train, X_val, y_train, y_val = train_test_split(X_trainval, y_trainval, train_size=0.7)

# TODO: 4.使用分层k折交叉验证

start = time.time()

SKF = StratifiedKFold(n_splits=5, random_state=16, shuffle=False)
mlp = MLPClassifier(solver='lbfgs', activation='relu', random_state=16)

params = {'alpha': [5e-4, 1e-4, 5e-3, 1e-3, 5e-2, 1e-2],
          'hidden_layer_sizes': [[10], [20], [50], [100], [150], [10, 10], [20, 20], [50, 50]]}

# params = {'alpha':[1e-6, 5e-5, 1e-5, 5e-4, 1e-4, 5e-3, 1e-3, 5e-2, 1e-2],
#           'hidden_layer_sizes':[[10], [20], [50], [100], [150], [200], [10, 10],[20, 20],[50, 50],[100, 100],[150, 150],[200, 200]]}

grid_search = GridSearchCV(mlp, params, cv=SKF, iid=False)
grid_search.fit(X_trainval, y_trainval)
print("执行时间:{:.2f}s".format(time.time()-start))
print('最优参数：{}'.format(grid_search.best_params_))
print('最佳得分（验证集）：{:.4f}'.format(grid_search.best_score_))
print('最优模型：{}'.format(grid_search.best_estimator_))

# TODO: 5.保持参数不变，在训练验证集上重新训练，并输出结果
# 1).直接使用grid_search.score()进行输出
score_trainval = grid_search.score(X_trainval, y_trainval)
score_test = grid_search.score(X_test, y_test)

print('基于GridSearch方法的输出，训练集得分: {:.4f}, 测试集得分: {:.4f}'.format(
    score_trainval, score_test))
# 2).使用最优参数进行输出
best_params = grid_search.best_params_
mlp = MLPClassifier(solver='lbfgs', activation='relu',
                    random_state=16, **best_params)
mlp.fit(X_trainval, y_trainval)

score_trainval = mlp.score(X_trainval, y_trainval)
score_test = mlp.score(X_test, y_test)

print('基于最优参数的输出，训练集得分: {:.4f}, 测试集得分: {:.4f}'.format(
    score_trainval, score_test))


# 3).使用最优模型进行输出
model = grid_search.best_estimator_
score_trainval = model.score(X_trainval, y_trainval)
score_test = model.score(X_test, y_test)

print('基于最优模型的输出，训练集得分: {:.4f}, 测试集得分: {:.4f}'.format(score_trainval, score_test))
