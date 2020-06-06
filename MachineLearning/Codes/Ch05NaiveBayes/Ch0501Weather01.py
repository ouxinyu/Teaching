'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 统计气候现象、预测的天气与实际天气之间的关系
@LastEditorTime: 2020-01-17
'''
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

# 对不同分类计算每个特征为 1的数量，并使用字典类型进行保存 {气候现象: 出现的次数}
counts = {}
for label in np.unique(y):
    counts[label] = X[y == label].sum(axis=0)  # 将多维数组中的数值，按列进行相加

print("下雨的天数:{0}天，天晴(不下雨)的天数:{1}天\n".format(sum(y == 1), sum(y == 0)))
print("下雨与气候的关系:\n {}".format(counts))
