import os
import numpy as np
import time
# 导入多层感知机MLP神经网络
from PIL import Image
import joblib

# TODO: 1: 载入模型
start = time.time()

ModelPath = os.path.join(os.getcwd(), 'Models', 'Ch08MNIST_lbfgs.pkl')
model = joblib.load(ModelPath)

print("载入模型共耗时: {:.3f}s".format(time.time() - start))


# TODO: 2. 预测给定图像
# 此处我们属于自己的手写字体进行测试

filename = 'mydigital09.png'
filepath = os.path.join(os.getcwd(), 'Attachments', filename)
image = Image.open(filepath).convert('F')
image = image.resize((28, 28))


# 将PIL的Image图像转换为numpy的数组
img = np.asarray(image)
# 将二维矩阵转换为一维向量以便于预测
im = img.reshape(1, 28*28)

# 输出预测结果
pred = model.predict(im)[0]
print('预测结果是:{:.0f}'.format(pred))

# 显示图像
image.show()
