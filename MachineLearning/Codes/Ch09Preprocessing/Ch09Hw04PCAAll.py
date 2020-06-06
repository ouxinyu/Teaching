import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA  # 导入多层感知机MLP神经网络
from sklearn.neural_network import MLPClassifier
import time
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'Modules'))
import load_MNIST

# TODO: 1.载入数据

start = time.time()

train_images = load_MNIST.load_train_images()
train_labels = load_MNIST.load_train_labels()
test_images = load_MNIST.load_test_images()
test_labels = load_MNIST.load_test_labels()

print("载入数据集共耗时: {:.3f}s".format(time.time() - start))

# TODO: 2.数据划分及预处理I
# 标准调整形态的方法
# X_train = train_images.reshape(train_images.shape[0], train_images.shape[1]*train_images.shape[2])/255
# 此处，因为我们已经知道的样本的形态，所以可以直接书写值

X_train = train_images.reshape(60000, 28*28)/255
y_train = train_labels
X_test = test_images.reshape(10000, 28*28)/255
y_test = test_labels

# 为了提高训练速度，我们只提取10%的样本进行演示
X_train_lite = X_train[0:5999, :]
y_train_lite = y_train[0:5999]
X_test_lite = X_test[0:999, :]
y_test_lite = y_test[0:999]

# TODO: 3.使用原始数据进行预测
# 导入多层感知机MLP神经网络

start = time.time()

mlp = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[
                    100, 100], activation='relu', alpha=1e-5, random_state=62, verbose=0)
mlp.fit(X_train_lite, y_train_lite)

score_ori_train = mlp.score(X_train_lite, y_train_lite)
score_ori_test = mlp.score(X_test_lite, y_test_lite)

# TODO: 4.按要求计算范围内的PCA降维后的性能
num = 20
scores = np.zeros([3, num])
scores[0, :] = np.linspace(0.40, 0.99, num)

start = time.time()

# 基于信息量百分比
n = 0
for i in scores[0, :]:
    # TODO: 3. 进行PCA降维
    pca = PCA(n_components=i)
    pca.fit(X_train_lite)
    X_train_pca = pca.transform(X_train_lite)
    X_test_pca = pca.transform(X_test_lite)

    # TODO: 4.训练MLP模型
    mlp = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[
                        100, 100], activation='relu', alpha=1e-5, random_state=62, verbose=0)
    mlp.fit(X_train_pca, y_train_lite)

    score_train = mlp.score(X_train_pca, y_train_lite)
    score_test = mlp.score(X_test_pca, y_test_lite)
    scores[1, n] = score_train
    scores[2, n] = score_test

    t = time.time() - start
    print("n_components={0:.2f}: 训练集得分 {1:.4f}，测试集得分 {2:.4f}，t = {3:.2f}".format(
        i, score_train, score_test, t))

    n = n + 1

# TODO: 5.可视化性能
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

plt.plot(scores[0, :], scores[1, :], 'g--^', label='训练集（信息量）')
plt.plot(scores[0, :], scores[2, :], 'b--o', label='测试集（信息量）')
plt.legend(['训练集', '测试集'], loc='best')
plt.title('基于信息量百分比的性能对比图')

max_y = np.round(np.max(scores[2, :]), 4)
max_index = np.where(scores[2, :] == np.max(scores[2, :]))
max_x = scores[0, max_index]

score_ori_test_y = np.round(score_ori_test, 4)
score_ori_text_x = 1

plt.plot(max_x, max_y, 'ks')
plt.annotate(max_y,
             xy=(max_x, max_y),
             xytext=(max_x+0.01, max_y))
plt.plot(score_ori_text_x, score_ori_test_y, 'ks')
plt.annotate(score_ori_test_y,
             xy=(score_ori_text_x, score_ori_test_y),
             xytext=(score_ori_text_x+0.01, score_ori_test_y))
plt.show()
