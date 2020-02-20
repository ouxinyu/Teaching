import sys
import os
import time
# 导入多层感知机MLP神经网络
from sklearn.neural_network import MLPClassifier
import joblib
sys.path.append(os.path.join(os.getcwd(), 'Modules'))
import load_MNIST

# TODO: 1: 载入数据集
start = time.time()

train_images = load_MNIST.load_train_images()
train_labels = load_MNIST.load_train_labels()
test_images = load_MNIST.load_test_images()
test_labels = load_MNIST.load_test_labels()

print("载入数据集共耗时: {:.3f}s".format(time.time() - start))


# TODO: 2. 数据预处理
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


# TODO: 3.训练MLP神经网络并输出预测结果
start = time.time()

print('开始训练模型，请稍等...', end='')
mlp = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[
                    100, 100], activation='relu', alpha=1e-5, random_state=62)
mlp.fit(X_train_lite, y_train_lite)

# 保存mlp神经网络模型
ModelPath = os.path.join(os.getcwd(), 'Models', 'Ch08MNIST_lbfgs.pkl')
joblib.dump(mlp, ModelPath)

print('训练结束，用时{:.2f}s.'.format(time.time() - start))
print('训练集得分: {:.4f}, 测试集得分: {:.4f}'.format(
    mlp.score(X_train, y_train), mlp.score(X_test, y_test)))
