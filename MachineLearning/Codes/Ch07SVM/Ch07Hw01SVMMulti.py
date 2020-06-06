'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 鸢尾花数据集上不同核的SVM性能对比
@LastEditorTime: 2020-01-26
'''
# TODO: 1. 导入必须库 以及 定义必要的函数
# 导入机器学习数据集处理工具
from sklearn import datasets
from sklearn.model_selection import train_test_split
# 导入支持向量机SVM
from sklearn import svm

# TODO: 2. 创建/导入数据
iris = datasets.load_iris()

# TODO: 3. 数据预处理，包括训练集、测试集划分，数据正则化，数据清洗等
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6)


# TODO: 4. 构建模型，并进行模型训练（或称为拟合数据）
C = 1.0
models = (svm.LinearSVC(C=C, max_iter=5000),
          svm.SVC(kernel='linear', C=C, gamma='auto'),
          svm.SVC(kernel='rbf', gamma=0.7, C=C),
          svm.SVC(kernel='sigmoid', C=C, gamma='auto'),
          svm.SVC(kernel='poly', degree=3, C=C, gamma='auto'))
# TODO:考虑输出变量models
models = (clf.fit(X_train, y_train) for clf in models)

titles = ('LinearSVC (linear kernel)',
          'SVC with linear kernel',
          'SVC with RBF kernel',
          'SVC with sigmoid kernel',
          'SVC with ploy(degree=3) kernel')


# TODO: 5. 输出模型准确率
for model, title in zip(models, titles):
    print("{0}, 训练集准确率: {1:.3f}, 测试集准确率: {2:.3f}".format(
        title, model.score(X_train, y_train), model.score(X_test, y_test)))
