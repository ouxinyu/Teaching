from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
# 导入数据预处理工具
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
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

# 3.使用管道模型进行模型选择
params = [{'reg': [RandomForestRegressor(random_state=26)],
           'scaler':[StandardScaler(), None],
           'reg__n_estimators':[100, 500, 1000]}]
pipe = Pipeline([('scaler', StandardScaler()), ('reg', MLPRegressor())])
grid = GridSearchCV(pipe, params, cv=3, verbose=1)
grid.fit(X_train, y_train)

print('最佳模型是：\n{}'.format(grid.best_params_))
print('交叉验证平均分:{:.2f}'.format(grid.best_score_))
print('测试集评分：{:.2f}'.format(grid.score(X_test, y_test)))
