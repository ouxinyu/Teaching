# TODO: 1. 导入必须库 以及 定义必要的函数
# 导入机器学习数据集处理工具
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn.model_selection import train_test_split

# TODO: 2. 创建/导入数据
cancer = datasets.load_breast_cancer()

# TODO: 3. 数据预处理，包括训练集、测试集划分，数据正则化，数据清洗等
X = cancer.data
y = cancer.target
X_trainval, X_test, y_trainval, y_test = train_test_split(
    X, y, train_size=0.7, random_state=8)
# X_train, X_val, y_train, y_val = train_test_split(X_trainval, y_trainval, train_size=0.7)

# TODO: 4. 用管道模型和网格搜索选择最优模型
SKF = StratifiedKFold(n_splits=3, random_state=8, shuffle=False)

params = [{'scaler': [StandardScaler(), MinMaxScaler()],
           'cls':[MLPClassifier(random_state=8, max_iter=2000)],
           'cls__alpha':[1e-6, 5e-5, 1e-5, 5e-4, 1e-4, 5e-3, 1e-3, 5e-2, 1e-2],
           'cls__hidden_layer_sizes':[[20], [50], [100], [150], [200], [10, 10], [20, 20], [50, 50]]},
          {'scaler': [StandardScaler(), MinMaxScaler()],
           'cls':[GaussianNB()],
           'cls__var_smoothing':np.logspace(-15, 10, 26)}]

pipe = Pipeline([('scaler', StandardScaler()), ('cls', MLPClassifier())])
grid = GridSearchCV(pipe, params, cv=SKF, verbose=1, n_jobs=-1)
grid.fit(X_trainval, y_trainval)

print('最佳模型是：\n{}'.format(grid.best_params_))
print('交叉验证平均分:{:.3f}'.format(grid.best_score_))

# 5. 保持参数不变，在训练验证集上重新训练，并输出结果
score_trainval = grid.score(X_trainval, y_trainval)
score_test = grid.score(X_test, y_test)

print('基于GridSearch方法的输出，训练集得分: {:.3f}, 测试集得分: {:.3f}'.format(
    score_trainval, score_test))
