from sklearn import datasets
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

# TODO: 1.载入数据集
# 载入wine数据集
wine = datasets.load_wine()

# TODO: 2.拆分数据集：按照 7:1:2 的比例来进行划分训练集、验证机和测试集
X_trainval, X_test, y_trainval, y_test = train_test_split(
    wine.data, wine.target, train_size=0.8, random_state=38)
X_train, X_val, y_train, y_val = train_test_split(
    X_trainval, y_trainval, train_size=0.875,  random_state=38)

params = {'alpha': [0.01, 0.1, 1.0, 10.0],
          'max_iter': [100, 1000, 5000, 10000]}

lasso = Lasso()
grid_search = GridSearchCV(lasso, params, cv=6, iid=False)
grid_search.fit(X_train, y_train)
print('网格搜素评分(验证集)：{:.4f}.'.format(grid_search.score(X_val, y_val)))
print('最优参数：{}'.format(grid_search.best_params_))

# 在GridSearchCV类中包含一个best_score_属性，可以实现交叉验证中最优性能的输出
print('模型最高分(验证集)为：{:.4f}'.format(grid_search.best_score_))
