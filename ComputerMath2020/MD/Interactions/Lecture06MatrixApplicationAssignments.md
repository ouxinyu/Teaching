# **第06讲 矩阵的应用** `课堂互动`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

## **【课堂互动一】** `从线性变换的角度看矩阵与向量的乘法`

**1. 在矩阵与向量的乘法运算中，矩阵可以被理解为向量从原始空间到目标空间的映射矩阵。**  

A. 对  
B. 错


**2. 在进行向量与矩阵乘法的时候，通常写成矩阵在左，向量在右的形式，即：y=Ax；同样的写成y=xA也是等价的。**  
A. 对    
B. 错


## **【课堂互动二】** `从向量的角度看矩阵乘法`

**1. 如果矩阵M是一个5×6的矩阵，那么该矩阵包含（ ）个行向量和（ ）个列向量。**  
A. 5 5   
B. 5 6  
C. 6 5  
D. 6 6 

<br/>

**2. 只要是同一个向量，无论基底（坐标系）如何变换，其坐标值都不会变化。**  
A. 对    
B. 错

<br/>

**3. 给定一个矩阵$M=\begin{bmatrix} 
2 & 5 & 1 \\ 
3 & 2 & 4 \\ 
1 & 2 & 3 \\ 
\end{bmatrix}$，它的行空间矩阵为：（ ）。**  


A. $a(2,5,1)+b(3,2,4)+c(1,2,3)=(a,b,c)$  
B. $a \begin{bmatrix} 2 \\ 3 \\ 1 \end{bmatrix}
+b \begin{bmatrix} 5 \\ 2 \\ 2 \end{bmatrix}
+c \begin{bmatrix} 1 \\ 4 \\ 3 \end{bmatrix}
=\begin{bmatrix} a \\ b \\ c \end{bmatrix}$  
C. $a(2,3,1)+b(5,2,2)+c(1,4,3)=(a,b,c)$  
D. $a \begin{bmatrix} 2 \\ 5 \\ 1 \end{bmatrix}
+b \begin{bmatrix} 3 \\ 2 \\ 4 \end{bmatrix}
+c \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
=\begin{bmatrix} a \\ b \\ c \end{bmatrix}$

<br/>

**4. 从行的角度审视矩阵与向量的乘法可以理解为（ ），从列的角度审视矩阵乘法可以理解为（ ）。**  

A. 原矩阵的各行分别与向量进行点乘的过程 原矩阵的各行分别与向量进行点乘的过程  
B. 原矩阵各列与向量对应位置的线性组合 原矩阵各列与向量对应位置的线性组合  
C. 原矩阵的各行分别与向量进行点乘的过程 原矩阵各列与向量对应位置的线性组合  
D. 原矩阵各列与向量对应位置的线性组合 原矩阵的各行分别与向量进行点乘的过程


<br/>

**5. 给出矩阵乘法*Ax*，可以得到其列向量的表示方法为（ ）。**  
$Ax=\begin{bmatrix} 2 & 3 \\ 4 & 5 \end{bmatrix} \begin{bmatrix} 5 \\ 6 \end{bmatrix}$

A. $5 \begin{bmatrix} 2 \\ 4 \end{bmatrix} + 6 \begin{bmatrix} 3 \\ 5 \end{bmatrix}$  
B. $5 \begin{bmatrix} 2 \\ 3 \end{bmatrix} + 6 \begin{bmatrix} 4 \\ 5 \end{bmatrix}$  
C. $6 \begin{bmatrix} 2 \\ 4 \end{bmatrix} + 5 \begin{bmatrix} 3 \\ 5 \end{bmatrix}$  
D. $6 \begin{bmatrix} 2 \\ 3 \end{bmatrix} + 5 \begin{bmatrix} 4 \\ 5 \end{bmatrix}$

<br/>

**6. 给出以下矩阵和向量相乘的表达，下列选项中理解不正确的是（ ）。**  
$Au=\begin{bmatrix} 1 & 2 \\ 3 & 4\end{bmatrix} \begin{bmatrix} 3 \\ 5 \end{bmatrix}
=3\begin{bmatrix} 1 \\ 3 \end{bmatrix}
+5\begin{bmatrix} 2 \\ 4 \end{bmatrix}$

A. 列向量$[1, 3]^T$是空间$A$中的一个基向量  
B. 坐标$[3,5]^T$可以理解为在空间A中的两个基的上的分量分别是3和5.  
C. 向量$[3,5]^T$分别表示向量u在空间$A$中，y方向上有3个分量，x方向上有5个分量  
D. 矩阵$[[1,2],[3,4]]$可以理解为向量$[3,5]^T$的基


**7. 以下代码中，可以用来表示$A^{10}$的一项是（ ）。**  

```python
import numpy as np
n = 10
A = np.array([[1]])
```

A.  
```python
for i in range(n):    
    res = np.dot(2, res)
    print('n={}: res={}'.format(i, res))
```

B.
```python
for i in range(n):    
    res = np.dot(2, res)
    print('n={}: res={}'.format(i+1, res))
```

C.
```python
for i in range(n+1):    
    res = np.dot(2, res)
    print('n={}: res={}'.format(i+1, res))
```

D.
```python
for i in range(n+1):    
    res = np.dot(2, res)
    print('n={}: res={}'.format(i, res))
```
