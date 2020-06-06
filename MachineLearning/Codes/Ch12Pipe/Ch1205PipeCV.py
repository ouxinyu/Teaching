from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
# 导入数据预处理工具
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score
import pandas as pd

# 1. 数据载入
stocks = pd.read_excel('Datasets/stock.xls')
X = stocks.loc[:, '幅度%':'昨收']
y = stocks['涨跌']
print(X.shape, y.shape)

# 2.数据拆分
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=26, train_size=0.7)
print(X_train.shape, X_test.shape)

# 3.使用管道模型进行交叉验证和模型训练
# 方法一：
pipe = Pipeline([('scaler', StandardScaler()),
                 ('mlp', MLPRegressor(random_state=26, max_iter=800))])
print(pipe.steps)

# 方法二:
pipe = make_pipeline(StandardScaler(), MLPRegressor(
    random_state=16, max_iter=2000))
print(pipe.steps)

# 4. 输出结果
# 输出交叉验证评分
scores = cross_val_score(pipe, X_train, y_train, cv=3)
print('交叉验证平均分：{:.2f}'.format(scores.mean()))

# 使用训练集重新进行训练，并在测试集上进行评分
pipe.fit(X_train, y_train)
print('测试集评分：{:.2f}'.format(pipe.score(X_test, y_test)))
