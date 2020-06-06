import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import numpy as np
from sklearn.cluster import KMeans

# TODO: 1.生成数据
blobs = make_blobs(random_state=1, centers=1)
X_blobs = blobs[0]
plt.scatter(X_blobs[:, 0], X_blobs[:, 1], c='r', edgecolor='k')
plt.show()

# TODO: 2.使用KMeans实现聚类
kmeans = KMeans(n_clusters=3)
kmeans.fit(X_blobs)

# 打印KMeans聚类标签
print("K均值的聚类标签:\n{}".format(kmeans.labels_))

# TODO: 3.可视化聚类结果
# 下面是用来画图的代码
x_min, x_max = X_blobs[:, 0].min()-0.5, X_blobs[:, 0].max()+0.5
y_min, y_max = X_blobs[:, 1].min()-0.5, X_blobs[:, 1].max()+0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))

Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

Z = Z.reshape(xx.shape)
# 绘制背景底色
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.summer,
           aspect='auto', origin='lower')
# 绘制离散点
plt.plot(X_blobs[:, 0], X_blobs[:, 1], 'r.', markersize=5)

# 绘制用蓝色叉号代表的聚类中心
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x',
            s=150, linewidths=3, color='b', zorder=10)
plt.savefig('Codes//Ch09Preprocessing//results//Ch0911KMeans.png', dpi=150)
plt.show()
