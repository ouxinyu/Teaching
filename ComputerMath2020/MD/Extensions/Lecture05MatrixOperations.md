# **第05讲 矩阵操作** `扩展练习`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

#### **1.【计算题】**   
**已知 $A=[6,-3,2], B=[1,2,-4]^T$，求$AB$和$BA$。**

- **Python实现**

```python
import numpy as np
A = np.array([[6,-3,2]])
B = ____(1)____

print("AB=\n {}".format(np.dot(A,B)))
print("BA=\n {}".format(____(2)____))
```

##### **答案及解析**

```python
(1) np.array([[1],[2],[-4]])
(2) np.dot(B,A)
```


```python
import numpy as np
A = np.array([[6,-3,2]])
B = np.array([[1],[2],[-4]])

print("AB=\n {}".format(np.dot(A,B)))
print("BA=\n {}".format(np.dot(B,A)))
```

    AB=
     [[-8]]
    BA=
     [[  6  -3   2]
     [ 12  -6   4]
     [-24  12  -8]]
    

<br/>

#### **2.【计算题】**   
**求矩阵 $S = \begin{bmatrix}
2 & -1 & -6 & 0 \\
1 & -1 & 2 & -4 \\
\end{bmatrix}
\begin{bmatrix}
1 & 2 \\
0 & -1 \\
-1 & -3 \\
4 & 2 \\
\end{bmatrix}$ 的乘积。**

- **Python实现**

```python
import numpy as np
A = ____(1)____
B = np.array([[1,2],[0,-1],[-1,-3],[4,2]])

S = ____(2)____
print("A×B=\n {}".format(S))
```


##### **答案及解析**

```python
(1) np.array([[2,-1,-6,0],[1,-1,2,-4]])
(2) np.dot(A,B)
```


```python
import numpy as np
A = np.array([[2,-1,-6,0],[1,-1,2,-4]])
B = np.array([[1,2],[0,-1],[-1,-3],[4,2]])

S = np.dot(A,B)
print("A×B=\n {}".format(S))
```

    A×B=
     [[ -2  -7]
     [-17 -11]]
    

<br/>

#### **3.【计算题】**   
**设$A = \begin{bmatrix}
1 & -2 & 1 \\
4 & 1 & 0 \\
3 & -2 & 2
\end{bmatrix}$，
$B = \begin{bmatrix}
3 & 4 & 1 \\
3 & -1 & 2 \\
1 & 2 & 4
\end{bmatrix}$，求$M = 2A^2 + 5AB - 4BA+ 6B^2 + (AB)^T$。**

- **Python实现**

```python
import numpy as np
A = np.array([[1,2,1,0],[2,1,0,1],[3,-2,2,1],[1,2,4,3]])
B = np.array([[3,4,1,-2],[2,1,2,2],[2,-2,2,1],[1,2,-4,3]])

M = 2*np.dot(A,A)-5*np.dot(A,B)+4*np.dot(B,A)____(1)____
print("Result = \n {}".format(M))
```


##### **答案及解析**

```python
(1) -6*np.dot(B,B)+(np.dot(A,B).T)
```


```python
import numpy as np
A = np.array([[1,2,1,0],[2,1,0,1],[3,-2,2,1],[1,2,4,3]])
B = np.array([[3,4,1,-2],[2,1,2,2],[2,-2,2,1],[1,2,-4,3]])

M = 2*np.dot(A,A)+5*np.dot(A,B)-4*np.dot(B,A)+6*np.dot(B,B)+(np.dot(A,B).T)
print("Result = \n {}".format(M))
```

    Result = 
     [[124  77 189  25]
     [ 95 114 -36  17]
     [ 91  68 -36 -48]
     [161  73 -68 134]]
    

<br/>

#### **4.【计算题】**   
**矩阵的加法：设存在矩阵$A = \begin{bmatrix} -1.2 & 3.4 & -5.6 \\ 7.8 & -9.1 & 0.7 \end{bmatrix}$, 和向量$u = [30, 50]^T$。试求$(4A+2b)-(2A-3b)$。**

- **Python实现**

```python
import numpy as np
A = np.array([[-1.2,3.4,-5.6],[7.8,-9.1,0.7]])
u = ____(1)____

print(____(2)____)
```


##### **答案及解析**

```python
(1) np.array([[30,50]]).T
(2) (4*A+2*u)-(2*A-3*u)
```


```python
import numpy as np
A = np.array([[-1.2,3.4,-5.6],[7.8,-9.1,0.7]])
u = np.array([[30,50]]).T

print((4*A+2*u)-(2*A-3*u))
```

    [[147.6 156.8 138.8]
     [265.6 231.8 251.4]]
    
