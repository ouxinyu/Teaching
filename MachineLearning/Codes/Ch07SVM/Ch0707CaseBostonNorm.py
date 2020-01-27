# TODO: 1. 导入必须库 以及 定义必要的函数
# 导入数据预处理工具
from sklearn.preprocessing import StandardScaler
# 导入 Boston波士顿房价数据集
from sklearn import datasets
from sklearn.model_selection import train_test_split
# 导入支持向量机SVM
from sklearn import svm
# 或使用 from sklearn.svm import SVR, 直接使用 SVR() 进行调用

# TODO: 2. 创建/导入数据
boston = datasets.load_boston()

# TODO: 3. 数据预处理，包括训练集、测试集划分，数据正则化，数据清洗等
X, y = boston.data, boston.target

X_train, X_test, y_train, y_test = train_test_split(X, y)

# TODO: 4. 构建模型，并进行模型训练（或称为拟合数据）
for kernel in ['linear', 'rbf', 'sigmoid']:
    svr = svm.SVR(kernel=kernel, gamma='auto')
    svr.fit(X_train, y_train)
    print(kernel, '核函数的模型训练集得分:{:.3f}, 测试集得分:{:.3f}'.format(
        svr.score(X_train, y_train), svr.score(X_test, y_test)))

# TODO: 5. 模型优化：数据归一化

# 对训练集合测试集进行数据预处理：归一化
# 创建预处理训练器
scaler = StandardScaler()
# 提取训练集超参数
scaler.fit(X_train)
# 用预训练超参数拟合训练集和测试集
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

for kernel in ['linear', 'rbf', 'sigmoid']:
    svr = svm.SVR(kernel=kernel)
    svr.fit(X_train_scaled, y_train)
    print('数据预处理后', kernel, '核函数的模型训练集得分: {:.3f}, 测试集得分：{:.3f}'.format(
        svr.score(X_train_scaled, y_train), svr.score(X_test_scaled, y_test)))
