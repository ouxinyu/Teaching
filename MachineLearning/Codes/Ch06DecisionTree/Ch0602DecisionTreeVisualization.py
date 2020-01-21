'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 决策树的基本使用
@LastEditorTime: 2020-01-18
'''
# 载入graphviz绘图工具包
import graphviz
import os
# 导入决策树中输出graphiviz的接口
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split

# 导入tree树模型和数据集加载工具
from sklearn import tree
from sklearn import datasets

'''
设置超参数max_depth
'''
_max_depth = 3


# 导入数据拆分工具
wine = datasets.load_wine()

# 1. 载入Wine数据集
# 设置X, y的值。此处为了便于可视化，仅选取前两个特征
X = wine.data[:, :2]
# X = wine.data
y = wine.target
# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y)


# 2. 配置决策树，并拟合训练集
# 设置决策树的分类器的最大深度为 1
clf = tree.DecisionTreeClassifier(max_depth=_max_depth)
# 拟合训练数据集
clf.fit(X_train, y_train)

# 3. 输出预测准确率
# 输出模型评分，即正确率
score_train = clf.score(X_train, y_train)
score_test = clf.score(X_test, y_test)

print("树深 = {0}：训练集准确率：{1:.3f}，测试集准确率：{2:.3f}".format(
    _max_depth, score_train, score_test))


filePath = os.path.join(os.getcwd() + '\\Codes\\Ch06DecisionTree\\tmp\\')
fileName = os.path.join(filePath + 'Wine.dot')

# 选择分类模型
export_graphviz(clf, out_file=fileName,
                class_names=wine.target_names,
                feature_names=wine.feature_names[:2],
                impurity=False, filled=True)
# 打开dot文件
with open(fileName) as f:
    dot_graph = f.read()

# 显示dot文件中的图形
graph = graphviz.Source(dot_graph)
graph.render(filePath + 'tree')
