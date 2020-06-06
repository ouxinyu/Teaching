'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 给定天气特征预测晴雨
@LastEditorTime: 2020-01-17
'''
# 导入贝努利贝叶斯库
from sklearn.naive_bayes import BernoulliNB
import numpy as np

# 将X，y赋值为 np数组；X表示气候现象和预测的天气；y 表示实际的天气情况
X = np.array([[0, 1, 0, 1],
              [1, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 1],
              [0, 1, 1, 0],
              [0, 1, 0, 1],
              [1, 0, 0, 1]])

y = np.array([0, 1, 1, 0, 1, 0, 0])

# 定义一个贝努利贝叶斯分类器，用于实现数据拟合
clf = BernoulliNB()
clf.fit(X, y)

'''
条件一：假设天气预报为晴朗，但出现了多云的情况。试问真实的天气是什么？
'''

# 按照题设条件设定新数据
New_Day = [[0, 0, 1, 0]]
pred = clf.predict(New_Day)

# 输出预测结果
print("条件一：", end="")
if pred == [1]:
    print("要下雨了, 快收衣服啦！(y = 1)")
else:
    print("太阳出来了！(y = 0)")

'''
条件二：假设天气预报为有雨，但出现了刮北风，闷热，云量不多的情况。试问真实的天气是什么？
'''
# 按照题设条件设定新数据
New_Day2 = [[1, 1, 0, 1]]
pred2 = clf.predict(New_Day2)

# 输出预测结果
print("条件一：", end="")
if pred2 == [1]:
    print("要下雨了, 快收衣服啦！(y = 1)")
else:
    print("太阳出来了！(y = 0)")

'''
输出每个选项的预测概率
'''
prob1 = clf.predict_proba(New_Day)
prob2 = clf.predict_proba(New_Day2)

print("第一天的预测概率为: {}".format(prob1))
print("第二天的预测概率为: {}".format(prob2))
