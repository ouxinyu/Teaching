# **第04讲 矩阵的基础知识** `课堂互动`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

## **【课堂互动一】**

**1. 下列可以用来表达一个矩阵的符号是（）。**  
A. 加粗斜体小写英文字母    
B. 加粗小写英文字母  
C. 斜体小写英文字母  
D. 加粗斜体大写英文字母

<br/>

**2. 下列代码可以用于实现创建一个2×3维数组的Python代码是：(      )**  
A. A = np.array([1,2],[3,4],[5,6])      
B. A = np.array([1,2,3],[4,5,6])   
C. A = np.array([[1,2],[3,4],[5,6]])  
D. A = np.array([[1,2,3],[4,5,6]])

<br/>

**3. 如果矩阵A和矩阵B相等，则它们必为同型矩阵。**  
A. 对   
B. 错

<br/>

**4. 转置是矩阵的重要操作，它是以主对角线为轴的镜像，这条对角线从右上角到左下角。**  
A. 对  
B. 错

<br/>

**5. 代码np.array([5,6,7]).T 所定义的量是列向量。**  
A. 对  
B. 错

</br>

**6. 按照下列代码，输出的结果正确的一个是（         ）。**  

```python
import numpy as np

A=np.array([1,2,3,4]) 
print(A.T)
```

A. $[1, 2, 3, 4] (一维行向量)$       
B.  $ [1, \\ 2, \\ 3, \\ 4] \\ (一维列向量) $   
C. $[[1 2 3 4]]   (二维行向量) $  
D. $ [[1], \\ [2], \\ [3], \\ [4]] \\  (二维列向量)$ 

## **【课堂互动二】**

**1. 若矩阵A是一个对称矩阵，则矩阵A也必然为一个方阵。（      ）。**  
A. 对  
B. 错   

</br>

**2. 下列矩阵中，通常用来实现矩阵初始化的是哪一种？（      ）。**  
A. 单位矩阵  
B. 对角矩阵  
C. 零矩阵  
D. 方阵  
E. 对称矩阵  

</br>

**3. 所有的单位矩阵都是对角矩阵。**  
A. 对  
B. 错   

</br>

**4. 下列Python代码可以用来生成一个4阶单位矩阵的是（       ）。**  
A. np.eye(4)  
B. np.diag(4)  
C. np.zeros(4)  
D. np.ones(4)

</br>

**5. 使用numpy定义二阶方阵的时候，以下函数正确的是（       ）。**  
A. np.array((1, 2), (3, 4))  
B. np.array((1, 2, 3, 4))  
C. np.array([1,2,3,4])  
D. np.array([[1,2], [3,4]])

</br>

**6. 下列矩阵满足$A^{-1}=A^T$的是（       ）。**  
A. 逆矩阵  
B. 正定矩阵  
C. 正交矩阵  
D. 对称矩阵
