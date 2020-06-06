# **第06讲 矩阵的应用** `课堂互动答案`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

## **【课堂互动一】** `从线性变换的角度看矩阵与向量的乘法`

**1. 在矩阵与向量的乘法运算中，矩阵可以被理解为向量从原始空间到目标空间的映射矩阵。**  
 
<font style='color:blue;font-weight:bold;'>A. 对</font>     
B. 错

**答案及解析：** A  

**2. 在进行向量与矩阵乘法的时候，通常写成矩阵在左，向量在右的形式，即：y=Ax；同样的写成y=xA也是等价的。**  
A. 对    
<font style='color:blue;font-weight:bold;'>B. 错</font>

**答案及解析：** B

在矩阵和向量的乘法运算中，我们通常将向量看成是一个矩阵，因此运算将变为两个矩阵的相乘。一般情况下矩阵的乘法是不满足交换律的，即$AB \neq BA$

## **【课堂互动二】** `从向量的角度看矩阵乘法`

**1. 如果矩阵M是一个5×6的矩阵，那么该矩阵包含（ ）个行向量和（ ）个列向量。**  
A. 5 5   
<font style='color:blue;font-weight:bold;'>B. 5 6</font>  
C. 6 5  
D. 6 6 

**答案及解析：** B

对于一个矩阵来说，其包含的行向量的个数等于其原始行数，其列向量的个数等于其原始的列数。

**2. 只要是同一个向量，无论基底（坐标系）如何变换，其坐标值都不会变化。**  
A. 对    
<font style='color:blue;font-weight:bold;'>B. 错</font>  

**答案及解析：** B

对于一个向量来说，一旦进行了基底（坐标系）变换，则坐标的值就会发生变换。唯一不变的是空间中多个对象的相对关系。

<br/>

**3. 给定一个矩阵$M=\begin{bmatrix} 
2 & 5 & 1 \\ 
3 & 2 & 4 \\ 
1 & 2 & 3 \\ 
\end{bmatrix}$，它的行空间矩阵为：（ ）。**  

<font style='color:blue;font-weight:bold;'>
A. $a(2,5,1)+b(3,2,4)+c(1,2,3)=(a,b,c)$</font>

B. $a \begin{bmatrix} 2 \\ 3 \\ 1 \end{bmatrix}
+b \begin{bmatrix} 5 \\ 2 \\ 2 \end{bmatrix}
+c \begin{bmatrix} 1 \\ 4 \\ 3 \end{bmatrix}
=\begin{bmatrix} a \\ b \\ c \end{bmatrix}$

C. $a(2,3,1)+b(5,2,2)+c(1,4,3)=(a,b,c)$

D. $a \begin{bmatrix} 2 \\ 5 \\ 1 \end{bmatrix}
+b \begin{bmatrix} 3 \\ 2 \\ 4 \end{bmatrix}
+c \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
=\begin{bmatrix} a \\ b \\ c \end{bmatrix}$

**答案及解析：** A

对于矩阵$A$来说，其行空间矩阵是指它的各个行向量所张成的$R^{1 \times n}$的子空间。一般来说，矩阵$A$包含多少行，则它就又多少个行空间矩阵。

<br/>

**4. 从行的角度审视矩阵与向量的乘法可以理解为（ ），从列的角度审视矩阵乘法可以理解为（ ）。**  

A. 原矩阵的各行分别与向量进行点乘的过程 原矩阵的各行分别与向量进行点乘的过程  
B. 原矩阵各列与向量对应位置的线性组合 原矩阵各列与向量对应位置的线性组合  
<font style='color:blue;font-weight:bold;'>C. 原矩阵的各行分别与向量进行点乘的过程 原矩阵各列与向量对应位置的线性组合</font>  
D. 原矩阵各列与向量对应位置的线性组合 原矩阵的各行分别与向量进行点乘的过程

**答案及解析：** C

<br/>

**5. 给出矩阵乘法*Ax*，可以得到其列向量的表示方法为（ ）。**

$Ax=\begin{bmatrix} 2 & 3 \\ 4 & 5 \end{bmatrix} \begin{bmatrix} 5 \\ 6 \end{bmatrix}$

<font style='color:blue;font-weight:bold;'>A. $5 \begin{bmatrix} 2 \\ 4 \end{bmatrix} + 6 \begin{bmatrix} 3 \\ 5 \end{bmatrix}$</font>

B. $5 \begin{bmatrix} 2 \\ 3 \end{bmatrix} + 6 \begin{bmatrix} 4 \\ 5 \end{bmatrix}$

C. $6 \begin{bmatrix} 2 \\ 4 \end{bmatrix} + 5 \begin{bmatrix} 3 \\ 5 \end{bmatrix}$

D. $6 \begin{bmatrix} 2 \\ 3 \end{bmatrix} + 5 \begin{bmatrix} 4 \\ 5 \end{bmatrix}$

**答案及解析：** A

列向量表达方式为矩阵列和向量的线性组合，具体等于矩阵的各列分别与向量的对应位置进行数乘，之后再进行相加。

<br/>

**6. 给出以下矩阵和向量相乘的表达，下列选项中理解不正确的是（ ）。**  
$Au=\begin{bmatrix} 1 & 2 \\ 3 & 4\end{bmatrix} \begin{bmatrix} 3 \\ 5 \end{bmatrix}
=3\begin{bmatrix} 1 \\ 3 \end{bmatrix}
+5\begin{bmatrix} 2 \\ 4 \end{bmatrix}$

A. 列向量$[1, 3]^T$是空间$A$中的一个基向量  
B. 坐标$[3,5]^T$可以理解为在空间A中的两个基的上的分量分别是3和5.  
<font style='color:blue;font-weight:bold;'>C. 向量$[3,5]^T$分别表示向量u在空间$A$中，y方向上有3个分量，x方向上有5个分量</font>  
D. 矩阵$[[1,2],[3,4]]$可以理解为向量$[3,5]^T$的基

**答案及解析：** A

向量$[3,5]^T$分别表示向量u在空间$A$中，x方向上有3个分量，y方向上有5个分量。

<br/>

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

<font style='color:blue;font-weight:bold;'>B.</font>  
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

**答案及解析：** B


```python
import numpy as np
n = 10
res = np.array([[1]])

for i in range(n):    
    res = np.dot(2, res)
    print('n={}: res={}'.format(i+1, res))
```

    n=1: res=[[2]]
    n=2: res=[[4]]
    n=3: res=[[8]]
    n=4: res=[[16]]
    n=5: res=[[32]]
    n=6: res=[[64]]
    n=7: res=[[128]]
    n=8: res=[[256]]
    n=9: res=[[512]]
    n=10: res=[[1024]]
    
