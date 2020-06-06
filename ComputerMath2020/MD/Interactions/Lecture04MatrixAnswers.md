# **第04讲 矩阵的基础知识** `课堂互动答案`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

## **【课堂互动一】** `矩阵的定义及基本操作`

**1. 下列可以用来表达一个矩阵的符号是（）。**  
A. 加粗斜体小写英文字母    
B. 加粗小写英文字母  
C. 斜体小写英文字母  
<font style='color:blue;font-weight:bold;'>D. 加粗斜体大写英文字母</font>    

**答案及解析：** D 

<br/>

**2. 下列代码可以用于实现创建一个2×3维数组的Python代码是：(      )**  
A. A = np.array([1,2],[3,4],[5,6])      
B. A = np.array([1,2,3],[4,5,6])   
C. A = np.array([[1,2],[3,4],[5,6]])  
<font style='color:blue;font-weight:bold;'>D. A = np.array([[1,2,3],[4,5,6]])</font>     

**答案及解析：** D  

对于numpy数组，内层小方括号的数量等于数组的行数，小方括号内部的元素的个数等于数组的列数。

<br/>

**3. 如果矩阵A和矩阵B相等，则它们必为同型矩阵。**  
<font style='color:blue;font-weight:bold;'>A. 对</font>  
B. 错

**答案及解析：** A

矩阵相等的条件有两个：一是二者必须为同型矩阵；二是二者对应位置的元素必须相等。

<br/>

**4. 转置是矩阵的重要操作，它是以主对角线为轴的镜像，这条对角线从右上角到左下角。**  
A. 对  
<font style='color:blue;font-weight:bold;'>B. 错</font> 

**答案及解析：** B

在矩阵中，从左上角到右下角的对角线称为主对角线。

<br/>

**5. 代码np.array([5,6,7]).T 所定义的量是列向量。**  
A. 对  
<font style='color:blue;font-weight:bold;'>B. 错</font> 

**答案及解析：** B

在Python中，numpy所定义一维数组无法使用转置操作，因此np.array([]).T依然是一个一维行向量。


```python
import numpy as np
np.array([5,6,7]).T 
```




    array([5, 6, 7])



</br>

**6. 按照下列代码，输出的结果正确的一个是（         ）。**  

```python
import numpy as np

A=np.array([1,2,3,4]) 
print(A.T)
```

<font style='color:blue;font-weight:bold;'>A. $[1, 2, 3, 4]  (一维行向量)$</font>      
B.  $ [1, \\ 2, \\ 3, \\ 4] \\ (一维列向量) $   
C. $[[1, 2, 3, 4]]  (二维行向量) $  
D. $ [[1], \\ [2], \\ [3], \\ [4]] \\  (二维列向量)$ 

**答案及解析：** A

在numpy中，一维向量无法进行转置操作。


```python
import numpy as np

A=np.array([1,2,3,4]) 
print(A.T)
```

    [1 2 3 4]
    

## **【课堂互动二】** `特殊形态的矩阵`

**1. 若矩阵A是一个对称矩阵，则矩阵A也必然为一个方阵。（      ）。**  
<font style='color:blue;font-weight:bold;'>A. 对</font>    
B. 错   

**答案及解析：** A

</br>

**2. 下列矩阵中，通常用来实现矩阵初始化的是哪一种？（      ）。**  
A. 单位矩阵  
B. 对角矩阵  
<font style='color:blue;font-weight:bold;'>C. 零矩阵</font>    
D. 方阵  
E. 对称矩阵  

**答案及解析：** C

零矩阵可以初始化为和目标矩阵同型，同时占用空间最小的优点，因此经常被用来做矩阵初始化和内存空间申请使用。

</br>

**3. 所有的单位矩阵都是对角矩阵。**  
<font style='color:blue;font-weight:bold;'>A. 对</font>    
B. 错   

**答案及解析：** A

</br>

**4. 下列Python代码可以用来生成一个4阶单位矩阵的是（       ）。**  
<font style='color:blue;font-weight:bold;'>A. np.eye(4)</font>  
B. np.diag(4)  
C. np.zeros(4)  
D. np.ones(4)

**答案及解析：** A

A选项生成一个4阶单位矩阵；B选项无法生成任何形态的矩阵，但可通过修改后生成4阶对角矩阵；C选项生成一个全0向量；D选项生成一个全1向量。


```python
import numpy as np

print(np.eye(4))
print(np.diag([4,4,4,4]))
print(np.zeros(4))
print(np.ones(4))

```

    [[1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]
     [0. 0. 0. 1.]]
    [[4 0 0 0]
     [0 4 0 0]
     [0 0 4 0]
     [0 0 0 4]]
    [0. 0. 0. 0.]
    [1. 1. 1. 1.]
    

</br>

**5. 使用numpy定义二阶方阵的时候，以下函数正确的是（       ）。**  
A. np.array((1, 2), (3, 4))  
B. np.array((1, 2, 3, 4))  
C. np.array([1,2,3,4])  
<font style='color:blue;font-weight:bold;'>D. np.array([[1,2], [3,4]])</font> 

**答案及解析：** D

A选项不符合语法规范；B选项首先创建了一个元组，其次使用np.array()方法将元组转换为一个一阶行向量；C选项创建一个一阶行向量；D选项创建了一个二阶方阵。


```python
print('A={}'.format(np.array((1, 2, 3, 4))))
print('B={}'.format(np.array([1,2,3,4])))
print('C={}'.format(np.array([[1,2], [3,4]])))
```

    A=[1 2 3 4]
    B=[1 2 3 4]
    C=[[1 2]
     [3 4]]
    

</br>

**6. 下列矩阵满足$A^{-1}=A^T$的是（       ）。**  
A. 逆矩阵  
B. 正定矩阵  
<font style='color:blue;font-weight:bold;'>C. 正交矩阵</font>  
D. 对称矩阵  

**答案及解析：** C

</br>
