# **第03讲 向量的四则运算** `课堂互动答案`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

## **【课堂互动一】** `向量的加法和数乘`

**1. 已知 $a = [3, 7], b = [2, 2]$， 求$a+b$。**  
A. 14  
B. [10, 4]  
<font style='color:blue;font-weight:bold;'>C. [5, 9]</font>  
D. 无法计算

**答案及解析：** C


```python
import numpy as np
a = np.array([3,7])
b = np.array([2,2])

print(a+b)
```

    [5 9]
    

<br/>

**2. 已知 $a = [3, 3, 1], b = [5, 4]$， 求$a+b$。**  
A. $[8, 7, 1]$  
B. $[3, 5, 3, 4, 1]$  
C. $[3, 3, 1, 5, 4]$  
<font style='color:blue;font-weight:bold;'>D. 无法计算</font>  

**答案及解析：** D  
向量加法必须满足`同型`的前提。

<br/>

## **【课堂互动二】** `向量的内积和外积`

**1. 给定向量 $u = [1,2,3]，v = [4,5,6]$，求它们的内积 $u·v$。**  
A. [[32]]   
B. [[ 4  5  6]  
[ 8 10 12]  
[12 15 18]]  
<font style='color:blue;font-weight:bold;'>C. 32</font>  
D. 无法计算  

**答案及解析：** C  


```python
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6]).T

print(np.dot(a,b))
```

    32
    

<br/>

**2. 给定向量 $u = [1,2,3]，v = [4,5,6]$，求它们的外积$u × v$。**  
A. [4,5,6]  
<font style='color:blue;font-weight:bold;'>B. [-3, 6, -3]</font>    
C. [1, 2, 3]  
D. 无法计算

**答案及解析：** B


```python
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.cross(a,b))
```

    [-3  6 -3]
    

<br/>

**3. 下列与内积具有同等含义的一个是（      ）。**  
<font style='color:blue;font-weight:bold;'>A. 点乘</font>  
B. 向量积  
C. 外积  
D. 叉乘  

**答案及解析：** A  
向量的内积，又称为点乘；向量的外积，又称为叉乘、向量积。

<br/>

<br/>

**4. 下列哪一个几何意义，对应于向量 a 和 b 的内积？**  
<font style='color:blue;font-weight:bold;'>A. 向量 a 在向量 b 方向上的投影长度乘以向量 b 的模长</font>   
B. 向量 a 的模长乘以向量 b 的模长  
C. 向量 a 和向量 b  张成的平行四边形的面积。  
D. 向量 a 和向量 b  张成的平面的法向量，该向量垂直于 a 和 b  向量构成的平面。

**答案及解析：** A  

<br/>

## **【课堂互动三】** `向量的线性组合`

**1. 给定标量$\alpha=1, \beta=3, \gamma=5$，和向量$u=[1,2]^T, v=[2,3]^T, w=[3,4]^T$，试求：$\alpha u + \beta v + \gamma w$。**

A. [[22, 31]]  
<font style='color:blue;font-weight:bold;'>B. [[22]  
 [31]]</font>   
C. [[1, 2]  
[6, 9]  
[15, 20]]  
D. 无法计算

**答案及解析：** B  


```python
import numpy as np
a = 1
b = 3
c = 5
u = np.array([[1,2]]).T
v = np.array([[2,3]]).T
w = np.array([[3,4]]).T

print(a*u+b*v+c*w)
```

    [[22]
     [31]]
    
