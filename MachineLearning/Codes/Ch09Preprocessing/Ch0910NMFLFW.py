# 导入数据集获取工具
from sklearn.datasets import fetch_lfw_people
# 导入MLP神经网络模型
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.decomposition import NMF
import time

# TODO: 1.载入LFW数据集, 并进行可视化
faces = fetch_lfw_people(min_faces_per_person=20, resize=0.8)
# 获取图像的尺寸
image_shape = faces.images[0].shape

# TODO: 2.输出基于原始图像的识别准确率
start = time.time()

# faces.data/255将图像数据转换成[0,1]之间浮点数
X_train, X_test, y_train, y_test = train_test_split(
    faces.data/255, faces.target, random_state=62)
mlp = MLPClassifier(hidden_layer_sizes=[
                    100, 100], random_state=62, max_iter=400, verbose=2)
mlp.fit(X_train, y_train)
print('模型识别准确率:{0:.2f} ({1:.2f}s)'.format(
    mlp.score(X_test, y_test), time.time()-start))

# TODO: 3.使用NMF处理人脸数据，并保留90%的信息
start = time.time()
nmf = NMF(n_components=105, random_state=62, verbose=0).fit(X_train)
X_train_nmf = nmf.transform(X_train)
X_test_nmf = nmf.transform(X_test)
print('NMF处理后数据形态：{0}(执行时间：{1:.2f}s)'.format(
    X_train_nmf.shape, time.time() - start))

# TODO: 4.输出白化后的批评分
start = time.time()
mlp = MLPClassifier(hidden_layer_sizes=[
                    100, 100], random_state=62, max_iter=800, verbose=0)
mlp.fit(X_train_nmf, y_train)
print('nmf处理后模型准确率：{0:.2f}({1:.2f}s)'.format(
    mlp.score(X_test_nmf, y_test), time.time() - start))
