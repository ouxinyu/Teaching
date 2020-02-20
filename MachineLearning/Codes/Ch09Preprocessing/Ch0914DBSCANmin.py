import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
# 导入DBSCAN
from sklearn.cluster import DBSCAN

# TODO: 1. 生成数据集，并用散点图显示
blobs = make_blobs(n_samples=300, random_state=1, centers=4)
X_blobs = blobs[0]

# TODO: 2. 训练DBSCAN
db = DBSCAN(min_samples=15)
clusters = db.fit_predict(X_blobs)

# TODO: 3.绘制聚类后的散点样本图
plt.figure(figsize=(12, 4))

plt.subplot(121)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
plt.scatter(X_blobs[:, 0], X_blobs[:, 1], c='r', edgecolor='k')

plt.subplot(122)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
plt.scatter(X_blobs[:, 0], X_blobs[:, 1], c=clusters,
            cmap=plt.cm.spring, s=40, edgecolor='k')
plt.savefig('Codes//Ch09Preprocessing//results//Ch0914DBSCANmin.png', dpi=150)
plt.show()

# TODO: 4.输出聚类标签和类别数
print("经过DBSCAN聚类后，总共有{}个类别".format(np.unique(clusters).size - 1))
print('聚类标签为：\n{}'.format(clusters))
