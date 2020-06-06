# **第05讲 矩阵操作** `课堂互动`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

## **【课堂互动一】**

**1. 在使用numpy进行矩阵加法运算的时候，要求执行加法的两个元素必须具有相同的形态。**   
A. 对     
B. 错

<br/>

**2. 设存在矩阵$A = \begin{bmatrix} 1.2 & 3.4 & 5.6 \\ 7.8 & 9.1 & 0.7 \end{bmatrix}$, 和标量c=10，请使用*numpy*计算库求：*A* + $c$。**  
A. 无法直接对矩阵和标量进行计算    
B. $ \begin{bmatrix} 11.2 & 13.4 & 15.6 \\ 17.8 & 19.1 & 10.7 \end{bmatrix}$  
C. $ \begin{bmatrix} 11.2 & 13.4 & 15.6 \\ 7.8 & 9.1 & 0.7 \end{bmatrix}$  
D. $ \begin{bmatrix} 11.2 & 3.4 & 5.6 \\ 17.8 & 9.1 & 0.7 \end{bmatrix}$


## **【课堂互动二】**

**1.给定以下两个矩阵A和B，以下求"A的2倍与B的3倍的和"的Python描述正确的是（          ）。**  

$A = \begin{bmatrix} 150 & 250 & 50 \\ 250 & 500 & 100 \\ 300 & 700 & 120 \\ 450 & 850 & 80 \end{bmatrix},
B =  \begin{bmatrix} 180 & 350 & 60 \\ 300 & 550 & 120 \\ 350 & 850 & 150 \\ 500 & 850 & 100 \end{bmatrix}$

A. 2A+3B    
B. 2\*A+3\*B  
C. 2·A+3·B  
D. 2×A+3×B  
E. 2 $\odot$ A+3 $\odot$ B

<br/>

**2. 下列关于矩阵运算正确的包括（       ）。**  
A. $A^T+B^T=(A+B)^T$  
B. $(\alpha + \beta)A^T=\alpha A^T + \beta A^T$  
C. $(AB)^T=(BA)^T$  
D. $A^T+B^T=(AB)^T$

</br>

**3. 给定向量 *u, v*，及标量 $a, b$，下列运算规律正确的是（          ）。**  
A. **$a$($b$*u*)=$b$($a$*u*)**  
B. **$a$(*u+v*)=$a$*u*+$a$*v***  
C. **$a$(*uv*)=$a$(*vu*)**  
D. **$(a+b)$*v* = $a$*v* + $b$*v*** 

<br/>

**4. 按照下列代码，输出的结果正确的一个是（ ）。**

```python
import numpy as np

A=np.array([[1,2],[3,4]])
x=np.array([[1,1]]).T 
print(np.dot(A,x))
```

A. $[7, \\ 3]$     
B. $[[3] \\ [7]]$      
C. [[3, 7]]  
D. [3, 7]
