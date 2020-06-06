'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 岭回归基本方法（糖尿病数据集）
@Destination：训练集大小对模型性能的影响
@LastEditorTime: 2020-01-17
'''
# 0.导入数据集生成工具和拆分工具
from sklearn.datasets import load_diabetes
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import learning_curve, KFold
import matplotlib.pyplot as plt

# 配置参数使 matplotlib绘图工具可以显示中文
plt.rcParams['font.sans-serif'] = [u'Microsoft YaHei']

# 1. 载入糖尿病情数据集
X = load_diabetes().data
y = load_diabetes().target

# 定义一个用于绘制学习曲线的函数


def plot_learning_curve(est, X, y):
    # 将数据进行20次拆分来对模型进行评分
    training_set_size, train_scores, test_scores = learning_curve(est, X, y, train_sizes=np.linspace(0.1, 1, 20),
                                                                  cv=KFold(20, shuffle=True, random_state=1))
    estimator_name = est.__class__.__name__
    line = plt.plot(training_set_size, train_scores.mean(
        axis=1), '--', label="训练集 " + estimator_name)

    # plt.plot()参数解释：x轴，y轴，图标样式，图例（数组类型），色彩
    plt.plot(training_set_size, test_scores.mean(axis=1), '-',
             label="测试集 " + estimator_name, c=line[0].get_color())
    plt.xlabel("训练集样本数")
    plt.ylabel("模型评分")
    plt.ylim(0, 1.1)  # y轴坐标范围


plt.figure(dpi=120)  # 设置图形的尺度
plot_learning_curve(Ridge(alpha=1), X, y)
plot_learning_curve(LinearRegression(), X, y)
plt.legend(loc="best")
plt.show()
