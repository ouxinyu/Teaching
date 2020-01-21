'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 朴素贝叶斯实战————肿瘤判断
@LastEditorTime: 2020-01-18
'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

# 1. 载入数据集
cancer = load_breast_cancer()

# 2. 数据集拆分（训练集+测试集）

X, y = cancer.data, cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=38)

# 3. 基于训练集构建贝叶斯模型

# 载入预处理，并对样本进行归一化
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)


bnb = BernoulliNB()
bnb_norm = BernoulliNB()
gnb = GaussianNB()
gnb_norm = GaussianNB()
mnb = MultinomialNB()

bnb.fit(X_train, y_train)
bnb_norm.fit(X_train_scaled, y_train)
gnb.fit(X_train, y_train)
gnb_norm.fit(X_train_scaled, y_train)
mnb.fit(X_train_scaled, y_train)

# 4. 输出各个模型的准确率
score_train_bnb = bnb.score(X_train, y_train)
score_train_gnb = gnb.score(X_train, y_train)
score_train_bnb_norm = bnb_norm.score(X_train_scaled, y_train)
score_train_gnb_norm = gnb_norm.score(X_train_scaled, y_train)
score_train_mnb_norm = mnb.score(X_train_scaled, y_train)
score_test_bnb = bnb_norm.score(X_test, y_test)
score_test_gnb = gnb.score(X_test, y_test)
score_test_bnb_norm = bnb.score(X_test_scaled, y_test)
score_test_gnb_norm = gnb_norm.score(X_test_scaled, y_test)
score_test_mnb_norm = mnb.score(X_test_scaled, y_test)

print("BernoulliNB模型，训练集评分: {0:.3f}, 测试集评分: {1:3f}".format(
    score_train_bnb, score_test_bnb))
print("BernoulliNB模型(归一化)，训练集评分: {0:.3f}, 测试集评分: {1:3f}".format(
    score_train_bnb_norm, score_test_bnb_norm))
print("GaussianNB模型，训练集评分: {0:.3f}, 测试集评分: {1:3f}".format(
    score_train_gnb, score_test_gnb))
print("GaussianNB模型，训练集评分(归一化): {0:.3f}, 测试集评分: {1:3f}".format(
    score_train_gnb_norm, score_test_gnb_norm))
print("MultinomialNB模型，训练集评分: {0:.3f}, 测试集评分: {1:3f}".format(
    score_train_mnb_norm, score_test_mnb_norm))

# 5 对单个样本进行性能评定

# 给定某个样本进行预测
data_id = 142

data_x = [X_test[data_id]]
data_y = y_test[data_id]

print("样本的正确分类为: {}".format(data_y))

print("BernoulliNB模型预测的分类是: {}".format(bnb.predict(data_x)[0]))
print("GaussianNB模型预测的分类是: {}".format(gnb.predict(data_x)[0]))
print("MultinomialNB模型预测的分类是: {}".format(mnb.predict(data_x)[0]))

# 输出每个预测分类的概率值
gnb.predict_proba(data_x)


# 6. 输出学习曲线
def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None,
                        n_jobs=1, train_sizes=np.linspace(.1, 1.0, 5)):
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    plt.grid()
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="lower right")
    return plt


title = "Learning Curves (Naive Bayes)"
cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)
estimator = GaussianNB()
plot_learning_curve(estimator, title, X, y, ylim=(0.9, 1.01), cv=cv, n_jobs=4)
plt.show()
