# **第04讲 矩阵的基础知识** `扩展练习`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

#### **1.【计算题】**  
编写Python代码，实现以下矩阵的创建，并显示（打印）到屏幕。

$A=\begin{bmatrix}
1 & 3 & 5 & 7\\
-2 & -4 & -6 & -8 \\
\end{bmatrix}$


- **Python实现**

```python
import numpy as np
A = ____(1)____([[1,3,5,7],____(2)____])

print('A= \n{}'.format(A))
```

##### **答案及解析**

```python
(1) np.array
(2) [-2,-4,-6,-8]
```


```python
import numpy as np
A = np.array([[1,3,5,7],[-2,-4,-6,-8]])

print('A= \n{}'.format(A))
```

    A= 
    [[ 1  3  5  7]
     [-2 -4 -6 -8]]
    

#### **2.【计算题】**  
给定以下两个矩阵A和B，试求线性组合S=1.1A+2.2B，并将结果显示（打印）到屏幕。

$A=\begin{bmatrix}
1.2 & -0.5 & 3.4 \\
2.4 & -1.7 & -2.1 \\
\end{bmatrix},
B=\begin{bmatrix}
1.2 & -2 & 0 \\
0 & -1.8 & -2.3 \\
\end{bmatrix}$

- **Python实现**

```python
import numpy as np
A = np.array([[1.2,-0.5,3.4],[2.4,-1.7,-2.1]])
B = ____(1)____

S = ____(2)____

print('S = \n{}'.format(S))
```

##### **答案及解析**

```python
(1) np.array([[1.2,-2,0],[0,-1.8,-2.3]])
(2) 1.1*A + 2.2*B
```


```python
import numpy as np
A = np.array([[1.2,-0.5,3.4],[2.4,-1.7,-2.1]])
B = np.array([[1.2,-2,0],[0,-1.8,-2.3]])

S = 1.1*A+2.2*B

print('S = \n{}'.format(S))
```

    S = 
    [[ 3.96 -4.95  3.74]
     [ 2.64 -5.83 -7.37]]
    
