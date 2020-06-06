'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 贝努利朴素贝叶斯
@LastEditorTime:2020-01-17
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import BernoulliNB
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

# 1. 载入数据及数据初始化
# 生成样本数为 50000， 分类数为 2的数据集，并按照 75%:25% 的比例进行拆分
X, y = make_blobs(n_samples=500, centers=5, random_state=8)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)

# 2. 模型评分
# 导入贝努利贝叶斯库

# 使用贝努利贝叶斯拟合数据
# 默认情况下，二值化参数binarize = 0, 通过调整二值化参数可以优化模型
nb = BernoulliNB()
# nb = BernoulliNB(binarize = 4)
nb.fit(X_train, y_train)

# 输出模型评分，即正确率
score = nb.score(X_test, y_test)
print("模型评分：{:.3f}".format(score))

# 3. 可视化分析
# 导入绘图工具

# 配置参数使 matplotlib绘图工具可以显示中文
# 设置图的分辨率为 100像素
plt.figure(dpi=100)
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

# 设置坐标轴的范围
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

# 用不同背景颜色表示不同的类别
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

z = nb.predict(np.c_[(xx.ravel(), yy.ravel())]).reshape(xx.shape)
plt.pcolormesh(xx, yy, z, cmap=plt.cm.Pastel1)

# 将训练集和测试集用散点图表示出来
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train,
            cmap=plt.cm.cool, edgecolor="k")
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=plt.cm.cool, marker="*")

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

# 设置图标题
plt.title("分类器：贝努利朴素贝叶斯 (BernoulliNB)")
plt.show()
