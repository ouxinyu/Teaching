from sklearn import preprocessing
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


# TODO: 4.测试预处理对性能的影响

methods = ['StandardScaler', 'MinMaxScaler', 'MaxAbsScaler',
           'RobustScaler', 'Normalizer', 'Binarizer']

for str in methods:
    scaler = eval('preprocessing.' + str + '().fit(X_train_lite)')
    X_train_scaled = scaler.transform(X_train_lite)
    X_test_scaled = scaler.transform(X_test_lite)
    mlp.fit(X_train_scaled, y_train_lite)
    print('预处理方法: {}, 测试集得分: {:.4f}，共计{:.2f}s'
          .format(str, mlp.score(X_test_scaled, y_test_lite), time.time() - start))
