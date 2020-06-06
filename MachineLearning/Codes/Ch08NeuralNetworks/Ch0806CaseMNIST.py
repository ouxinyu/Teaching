import sys
import os
import numpy as np
import time
# 导入多层感知机MLP神经网络
from sklearn.neural_network import MLPClassifier
from PIL import Image
from sklearn.externals import joblib
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

mlp = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[
                    100, 100], activation='relu', alpha=1e-5, random_state=62)
mlp.fit(X_train_lite, y_train_lite)

# 保存mlp神经网络模型
ModelPath = os.path.join(os.getcwd(), 'Models', 'Ch08MNIST_lbfgs.pkl')
joblib.dump(mlp, ModelPath)

print('训练结束，用时{:.2f}s.'.format(time.time() - start))
print('训练集得分: {:.4f}, 测试集得分: {:.4f}'.format(
    mlp.score(X_train_lite, y_train_lite), mlp.score(X_test_lite, y_test_lite)))

# TODO: 4. 预测给定图像
'''
此处我们尝试将测试集中的图像进行直接进行输出并预测
'''
id = 342
# 将numpy数组转换为PIL图像
img = Image.fromarray(np.uint8(test_images[id]))

# 保存PIL图像到磁盘指定路径
filename = 'mnist' + str(id) + '.png'
filepath = os.path.join(os.getcwd(), 'Codes', 'Ch08NeuralNetworks', 'tmp', filename)
img.save(filepath)

image = Image.open(filepath).convert('F')
image = image.resize((28, 28))

# 显示图像
# image.show()

# 将PIL的Image图像转换为numpy的数组
img = np.asarray(image)
# 将二维矩阵转换为一维向量以便于预测
im = img.reshape(1, 28*28)

# 输出预测结果
pred = mlp.predict(im)[0]
print('图片的GrandTruth标签是: {}, 预测结果是:{:.0f}'.format(int(test_labels[id]), pred))
