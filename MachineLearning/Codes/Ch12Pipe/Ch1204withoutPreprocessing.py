from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
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

# 3. 使用交叉验证进行训练和评分
scores = cross_val_score(MLPRegressor(random_state=26), X_train, y_train, cv=3)
print('交叉验证平均分：{:.2f}'.format(scores.mean()))
