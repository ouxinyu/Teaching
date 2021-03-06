# 矩阵，让向量动起来

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---


```python
import numpy as np
a = np.array([[1,2,3,4]])
print("a={}".format(a))
print("b=\n{}".format(a.T))
```

    a=[[1 2 3 4]]
    b=
    [[1]
     [2]
     [3]
     [4]]
    

**【结果分析】**

从结果可以看到，我们使用一个二维数组来显示向量（两层中括号），这种方法基本上贯穿于整个计算机领域。其中 ***a*** 用来表示一个四维行向量，***b*** 表示一个四维列向量。

### 4. 矩阵的四则运算

#### 4.1.1 矩阵和标量的加法

【例1】设$A=\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$，且$b$=10，试求$A+b$。
解：  
$ A+b
=\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}+b
=\begin{bmatrix} 1+10 & 2+10 \\ 3+10 & 4+10 \end{bmatrix}
=\begin{bmatrix} 11 & 12 \\ 13 & 14 \end{bmatrix}$



```python
import numpy as np
A = np.array([[1,2],[3,4]])
b = 10

print(A+b)
```

    [[11 12]
     [13 14]]
    

#### 4.1.2 矩阵和向量的加法

【例1】设$A=\begin{bmatrix} 2 & 1 \\ 2 & 4 \end{bmatrix}$，且$b=[10, 20]^T$，试求$A+b$。
解：  
$ A+b
=\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}+b
=\begin{bmatrix} 1+10 & 2+10 \\ 3+10 & 4+10 \end{bmatrix}
=\begin{bmatrix} 11 & 12 \\ 13 & 14 \end{bmatrix}$



```python
import numpy as np
A = np.array([[2,1],[2,4]])
b = np.array([[10],[20]])
c = np.array([[10,20]])

print('A+b=\n{}'.format(A+b))
print('A+c=\n{}'.format(A+c))
```

    A+b=
    [[12 11]
     [22 24]]
    A+c=
    [[12 21]
     [12 24]]
    

#### 4.1 矩阵的加法运算

> **定义2** 设存在两个 m×n 的矩阵$A=a_{ij}, B=b_{ij}$，那么矩阵 ***A***与***B*** 的 ***和*** 记作 ***A***+***B*** ，规定为：

$A+B=\begin{bmatrix} 
    a_{11} & a_{12} & ... & a_{1n} \\ 
    a_{21} & a_{22} & ... & a_{2n} \\ 
    ... & ... & ... & ... \\ 
    a_{m1} & a_{m2} & ... & a_{mn}
\end{bmatrix}
+\begin{bmatrix} 
    b_{11} & b_{12} & ... & b_{1n} \\ 
    b_{21} & b_{22} & ... & b_{2n} \\ 
    ... & ... & ... & ... \\ 
    b_{m1} & b_{m2} & ... & b_{mn}
\end{bmatrix}
=\begin{bmatrix} 
    a_{11}+b_{11} & a_{12}+b_{12} & ... & a_{1n}+b_{1n} \\ 
    a_{21}+b_{21} & a_{22}+b_{22} & ... & a_{2n}+b_{2n} \\ 
    ... & ... & ... & ... \\ 
    a_{m1}+b_{m1} & a_{m2}+b_{m2} & ... & a_{mn}+b_{mn}
\end{bmatrix}$

应当注意，只有当两个矩阵是同型矩阵时，这两个矩阵才能进行加法运算。

矩阵加法满足下列运算规律（设***A***, ***B***, ***C***都是 m×n 的矩阵）：
1. ***A*** + ***B*** = ***B*** + ***A*** 
2. (***A*** + ***B***) + ***C*** = ***A*** + (***B*** + ***C***)

设矩阵 $A=a_{ij}$，记 $-A=-a_{ij}$，$-A$称为矩阵A的**负矩阵**，显然有 

***A*** + (***-A***) = ***O***。

由此规定矩阵的减法为：***A*** - ***B*** = ***A*** + (-***B***)

下面给出矩阵加法的Python代码


```python
import numpy as np
A = np.array([[1,2],[3,4],[5,6]])
B = np.array([[10,20],[30,40],[50,60]])
print("A=\n{},\n B=\n{},\n A+B=\n{}, \n B-A=\n{}".format(A,B,A+B,B-A))
```

    A=
    [[1 2]
     [3 4]
     [5 6]],
     B=
    [[10 20]
     [30 40]
     [50 60]],
     A+B=
    [[11 22]
     [33 44]
     [55 66]], 
     B-A=
    [[ 9 18]
     [27 36]
     [45 54]]
    

**【例1】超市年度销售总额** 

假设有四个超市，它们上半年和下半年的销售清单如下所示，试求这四个超市全年的销售清单。

|上半年销售表|大米|面粉|食油||下半年销售表|大米|面粉|食油|
:-:|:-:|:-:|:-:||:-:|:-:|:-:|:-:
超市一|150|250|50||超市一|180|350|60
超市二|250|500|100||超市二|300|550|120
超市三|300|700|120||超市三|350|850|150
超市四|450|850|80||超市四|500|850|100



我们可以将上面的表单写成矩阵形式：

$A=\begin{bmatrix} 
    150 & 250 & 50 \\ 
    250 & 500 & 100 \\ 
    300 & 700 & 120 \\ 
    450 & 850 & 80
\end{bmatrix}，
B=\begin{bmatrix} 
    180 & 350 & 60 \\ 
    300 & 550 & 120 \\ 
    350 & 850 & 150 \\ 
    500 & 850 & 100
\end{bmatrix}$

则全年的销售情况可以用矩阵的加法来表示：

$C=A+B=\begin{bmatrix} 
    150+180 & 250+350 & 50+60 \\ 
    250+300 & 500+550 & 100+120 \\ 
    300+350 & 700+850 & 120+150 \\ 
    450+500 & 850+850 & 80+100
\end{bmatrix}$

下面给出Python代码的实现方法：


```python
import numpy as np

A = np.array([[150,250,50],[250,500,100],[300,700,120],[450,850,80]])
B = np.array([[180,350,60],[300,550,120],[350,850,150],[500,850,100]])
C = A + B
print("C=\n{}".format(C))
```

    C=
    [[ 330  600  110]
     [ 550 1050  220]
     [ 650 1550  270]
     [ 950 1700  180]]
    

**【结果分析】**

可见，基于numpy的矩阵加法也是按照按位相加的原理进行加法运算，而且运算过程也非常直观和简单。但需要注意的是numpy加法运算的两个元素也必须具有相同的形态。

#### 4.2 矩阵的数量乘法运算

> **定义3** 数 $\lambda$ 与矩阵A的乘积记作 $\lambda A$ 或 $A \lambda$，规定为：

$\lambda A = A \lambda =
\lambda \begin{bmatrix} 
a_{11} & a_{12} & ... & a_{1n} \\ 
a_{21} & a_{22} & ... & a_{2n} \\ 
... & ... & ... & ... \\ 
a_{m1} & a_{m2} & ... & a_{mn}
\end{bmatrix}
=\begin{bmatrix} 
\lambda a_{11} & \lambda a_{12} & ... & \lambda a_{1n} \\ 
\lambda a_{21} & \lambda a_{22} & ... & \lambda a_{2n} \\ 
... & ... & ... & ... \\ 
\lambda a_{m1} & \lambda a_{m2} & ... & \lambda a_{mn}
\end{bmatrix}$。

数乘矩阵满足下列运算规律（设 ***A***， ***B*** 为 m×n 矩阵，$\lambda, \mu$ 为标量）：
- $(\lambda \mu) A= \lambda (\mu A)$
- $(\lambda + \mu) A = \lambda A + \mu A$
- $\lambda(A + B) = \lambda A + \lambda B$

`矩阵相加`与`数乘`矩阵合起来，统称为矩阵的**线性运算**。

下面给出Python代码的实现方法。


```python
import numpy as np
A = np.array([[1,2],[3,4],[5,6]])
print(2*A)
```

    [[ 2  4]
     [ 6  8]
     [10 12]]
    

**【例2】计算期末总成绩**

甲、乙、丙三位同学在期末考试中，4门课程的成绩分别由矩阵A给出，而他们的平时成绩则由矩阵B给出，若期末考试成绩占总成绩的90％，而平时成绩占10％，请计算这三名同学的总成绩。

$A=\begin{bmatrix} 
    85 & 85 & 65 & 98 \\ 
    75 & 95 & 70 & 95 \\ 
    80 & 70 & 76 & 92
\end{bmatrix}，
B=\begin{bmatrix}
    90 & 70 & 80 & 92 \\ 
    80 & 90 & 82 & 92 \\ 
    85 & 75 & 90 & 90
\end{bmatrix}$

解：矩阵C表示总成绩，显然有：

$C = 0.9A + 0.1B = \begin{bmatrix} 
    85.5 & 83.5 & 66.5 & 97.4 \\ 
    75.5 & 94.5 & 71.2 & 94.7 \\  
    80.5 & 70.5 & 77.4 & 91.8 \\ 
\end{bmatrix}$


```python
import numpy as np

A = np.array([[85,85,65,98],[75,95,70,95],[80,70,76,92]])
B = np.array([[90,70,80,92],[80,90,82,92],[82,75,90,90]])
C = 0.9*A + 0.1*B
print("C=\n{}".format(C))
```

    C=
    [[85.5 83.5 66.5 97.4]
     [75.5 94.5 71.2 94.7]
     [80.2 70.5 77.4 91.8]]
    

#### 4.3 矩阵与矩阵的乘法

> **【定义4】**设***A***=$(a_{ij})$ 是一个m×s矩阵，***B***=$(b_{ij})$ 是一个s×n矩阵，那么矩阵A与矩阵B的乘积是一个m×n矩阵$C$=$(c_{ij})$，其中 $c_{ij} = a_{i1} b_{1j} + a_{i2} b_{2j} + ... + a_{is} b_{sj} = \sum^s_{k=1} a_{ik} b_{kj}$
$(i = 1, 2, ..., m; j = 1, 2, ..., n)，$并把此乘积记作 $C=AB$。

为了更清楚，下面给出一个示例：

$C = A × B =\begin{bmatrix} 
    a_{11} & a_{12} \\
    a_{21} & a_{22} \\ 
    a_{31} & a_{32}
\end{bmatrix}
\begin{bmatrix} 
    b_{11} &  b_{12} &  b_{13} \\
    b_{21} &  b_{22} &  b_{23} 
\end{bmatrix}
=\begin{bmatrix} 
    a_{11} b_{11} + a_{12} b_{21} & a_{11} b_{12} + a_{12} b_{22} & a_{11} b_{13} + a_{12} b_{23} \\ 
    a_{21} b_{11} + a_{22} b_{21} & a_{21} b_{12} + a_{22} b_{22} & a_{21} b_{13} + a_{22} b_{23} \\ 
    a_{31} b_{11} + a_{32} b_{21} & a_{31} b_{12} + a_{32} b_{22} & a_{31} b_{13} + a_{32} b_{23}
\end{bmatrix}$

通过观察上面的计算公式，可以总结出矩阵乘法 `C=AB` 的三个要点：
1. AB可乘的条件：A的列数 = B的行数
2. AB乘积C的形状：A的行 × B的列
3. AB乘积C的元素构成：A的行与B的列的内积

下面给出一个例子：

**【例3】** 求矩阵 $A = \begin{bmatrix} 
1 & 2 & 3 \\
4 & 5 & 6 \\
1 & 1 & 1
\end{bmatrix}，
B=\begin{bmatrix} 
1 & 7 \\
2 & 8 \\
3 & 9 
\end{bmatrix}$ 的乘积AB。

解：因为A是3×3矩阵，B是3×2矩阵，A的列数等于B的行数，所以矩阵A与B可以相乘，其乘积AB=C是一个3×2矩阵。按定理可得：
$C=AB=\begin{bmatrix} 
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    1 & 1 & 1
\end{bmatrix}
\begin{bmatrix} 
    1 & 7 \\
    2 & 8 \\
    3 & 9 \\
\end{bmatrix}
=\begin{bmatrix} 
    1*1+2*2+3*3 & 1*7+2*8+3*9 \\
    4*1+5*2+6*3 & 4*7+5*8+6*9 \\
    1*1+1*2+1*3 & 1*7+1*8+1*9 
\end{bmatrix}
=\begin{bmatrix} 
    14 & 50 \\
    32 & 122 \\
    6 & 24 \\
\end{bmatrix}
$

下面给出该乘积的Python代码。注意我们使用`np.dot(A,B)`实现矩阵乘法。


```python
import numpy as np

A = np.array([[1,2,3],[4,5,6],[1,1,1]])
B = np.array([[1,7],[2,8],[3,9]])
C = np.dot(A,B)
print("C=\n{}".format(C))
```

    C=
    [[ 14  50]
     [ 32 122]
     [  6  24]]
    

**【结果分析】**

值得注意的是矩阵乘法是不符合交换律的，换句话说，上例中的BA是没有意义的。


```python
import numpy as np

A = np.array([[1,2,3],[4,5,6],[1,1,1]])
B = np.array([[1,7],[2,8],[3,9]])
C = np.dot(B,A)
print("C=\n{}".format(C))
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-19-4de9c015f434> in <module>
          3 A = np.array([[1,2,3],[4,5,6],[1,1,1]])
          4 B = np.array([[1,7],[2,8],[3,9]])
    ----> 5 C = np.dot(B,A)
          6 print("C=\n{}".format(C))
    

    ValueError: shapes (3,2) and (3,3) not aligned: 2 (dim 1) != 3 (dim 0)


**【例4】** 下面再给出一个例子：求矩阵 
$A = \begin{bmatrix} 
    -2 & 4 \\
    1 & -2 \\
\end{bmatrix}，
B = \begin{bmatrix} 
    2 & 4 \\
    -3 & -6 \\
\end{bmatrix}$ 的乘积AB及BA。

解：按定义有

$AB= \begin{bmatrix} 
    -2 & 4 \\
    1 & -2 \\
\end{bmatrix}
\begin{bmatrix} 
    2 & 4 \\
    -3 & -6 \\
\end{bmatrix}
=\begin{bmatrix} 
    -16 & -32 \\
    8 & 16 \\
\end{bmatrix}$

$BA= 
\begin{bmatrix} 
    2 & 4 \\
    -3 & -6 \\
\end{bmatrix}
\begin{bmatrix} 
    -2 & 4 \\
    1 & -2 \\
\end{bmatrix}
=\begin{bmatrix} 
    0 & 0 \\
    0 & 0 \\
\end{bmatrix}$

下面同样给出Python的代码


```python
import numpy as np

A = np.array([[-2,4],[1,-2]])
B = np.array([[2,4],[-3,-6]])
AB = np.dot(A,B)
BA = np.dot(B,A)
print("AB=\n{}".format(AB))
print("BA=\n{}".format(BA))
```

    AB=
    [[-16 -32]
     [  8  16]]
    BA=
    [[0 0]
     [0 0]]
    

**【结果分析】**

在 **【例3】** 中$A$是3×3矩阵，$B$是2×3矩阵，乘积$AB$有意义，而$BA$却没有意义。由此可知，在矩阵的乘法中必须注意矩阵相乘的`顺序`。$AB$是$A$`左乘`$B$（$B$被$A$左乘）的乘积，$BA$是$A$`右乘`$B$的乘积，$AB$有意义时，$BA$可以没有意义。

又若$A$是 m×n 矩阵，$B$是 n×m 矩阵，则$AB$与$BA$都有意义，但$AB$是m阶方阵，$BA$是n阶方阵，
- 当$m \neq n$时$AB \neq BA$。
- 即使 m=n,即$A、B$是同阶方阵。如 **【例4】** ，$A$与$B$都是2阶方阵，从而$AB$与$BA$也都是2阶方阵，但$AB$与$BA$仍然可以不相等。

总之，矩阵乘法不满足交换律，即在一般情况下，$AB \neq BA$。

**【例4】** 还表明，矩阵 $A \neq O, B \neq O$，但却有 $BA \neq O$。因此要特别注意：若有两个矩阵$A、B$满足$AB=O$，不能得出$A=O$或$B=O$的结论；若$A \neq O$而 $A(X-Y)=O$，也不能得出$X=Y$的结论。

矩阵乘法虽然不满足交换律，但仍满足下列结合律和分配率（假设运算时可行的）
1. 结合律：$(AB)C = A(BC)$
2. $\lambda (AB) = (\lambda A)B = A(\lambda B)$，其中$\lambda$是标量
3. 分配律：$A(B+C) = AB + AC, (B+C)A = BA + CA$

对于单位矩阵 ***I***，不难得出结论：$I_m A_{m×n} = A_{m×n}， A_{m×n} I_n = A_{m×n}$，

或简写成：$IA=AI=A$，

可见单位矩阵 ***I*** 在矩阵乘法中的作用类似于标量 1。

下面给出一个关于线性组合的例子：

**【例5】服装厂的生产量**

有甲、乙、丙、丁4个服装厂，一个月的产量情况由下表给出，若甲厂生产8个月，乙厂生产10个月，丙厂生产5个月，而丁厂生产9个月，则共生产帽子、衣服、裤子各多少？用矩阵来描述。

品种|甲|乙|丙|丁
:-:|:-:|:-:|:-:|:-:
帽|20|4|2|7
衣|10|18|5|6
裤|5|7|16|3

解：上表可以矩阵化为:
$A=\begin{bmatrix} 
    20 & 4 & 2 & 7 \\ 
    10 & 18 & 5 & 6 \\ 
    5 & 7 & 16 & 3
\end{bmatrix}，
b=\begin{bmatrix}
    8 \\
    10 \\ 
    5 \\
    9
\end{bmatrix}$

则，总产量可以表示为：
$C = A × b = \begin{bmatrix} 
    8×20 & 10×4 & 5×2 & 9×7 \\ 
    8×10 & 10×18 & 5×5 & 9×6 \\ 
    8×5 & 10×7 & 5×16 & 9×3
\end{bmatrix}
= \begin{bmatrix}
    273 \\
    339 \\ 
    217
\end{bmatrix}$


```python
import numpy as np

A = np.array([[20,4,2,7],[10,18,5,6],[5,7,16,3]])
b = np.array([[8],[10],[5],[9]])
C = np.dot(A, b)
print("C=\n{}".format(C))
```

    C=
    [[273]
     [339]
     [217]]
    

#### 4.4 矩阵的幂

根据矩阵的乘法法则，可以定义**矩阵的幂**。设A是n阶方阵，定义：

$A^1 = A, A^2 = A^1 A^1,..., A^{k+1} = A^k A^1$，

其中 $k$ 为正整数。也就是说，$A^k$ 就是 $k$个$A$连乘。显然只有方阵满足条件，**幂**运算才有意义。

由于矩阵的乘法适合结合律，所以矩阵的幂满足以下运算规律：

$A^k A^l = A^{k+l}, (A^k)^l = A^{kl}$

其中 $k、l$为正整数。又因矩阵乘法一般不满组交换律，所以对于两个 n 阶矩阵 $A$与$B$，一般来说 $(AB)^k \neq A^k B^k$。

下面看一个例子：

**【例6】四个城市间的单向航线**

若四个城市的航向图如下所示：

![Image](http://ouxinyu.cn/Teaching/ComputerMath/Attachments/04-Case06-Airline.png)

令$a_{ij}=\left\{
\begin{aligned}
1 &, 从i市到j市有1条单向航线 \\
0 &, 从i市到j市没有单项航线 \\
\end{aligned}
\right.$

则上图可以表示为：

$A=(a_{ij})=\begin{bmatrix} 
    0 & 1 & 1 & 1 \\ 
    1 & 0 & 0 & 0 \\ 
    0 & 1 & 0 & 0 \\
    1 & 0 & 1 & 0
\end{bmatrix}$，

若记 $A^2=b_{ij}$，则 $b_{ij}$ 为从i市经过一次中转到j市的单向航线条数。有：
$A=(a_{ij})=\begin{bmatrix} 
    0 & 1 & 1 & 1 \\ 
    1 & 0 & 0 & 0 \\ 
    0 & 1 & 0 & 0 \\
    1 & 0 & 1 & 0
\end{bmatrix}，
有A^2=\begin{bmatrix} 
    2 & 1 & 1 & 0 \\ 
    0 & 1 & 1 & 1 \\ 
    1 & 0 & 0 & 0 \\
    0 & 2 & 1 & 1
\end{bmatrix}$.

例如：
- $b_{23}=1$，显示从(2)经过一次中转后到达(3)市的单项航线有一条：(2)->(1)->(3);
- $b_{42}=2$，显示从(4)经过一次中转后到达(2)市的单项航线有2条：(4)->(1)->(2)，(4)->(3)->(2)；
- $b_{11}=2$，显示过(1)市的双向航线有2条：(1)->(2)->(1)，(1)->(4)->(1)；
- $b_{33}=0$，显示(3)市没有双向航线。


**【例7】** 假设给定上面的航线矩阵 $A$，试求从(4)市到(2)市，最多经过4次转机，有几种到达方法。下面我们使用Python代码来完成这个例子。


```python
import numpy as np
A = np.array([[0,1,1,1],[1,0,0,0],[0,1,0,0],[1,0,1,0]])
A2 = np.dot(A,A)
A3 = np.dot(A2,A)
A4 = np.dot(A3,A)
A5 = np.dot(A4,A)
print(A[3,1] + A2[3,1] + A3[3,1] + A4[3,1] + A5[3,1])
```

    11
    

**【结果分析】**

需要注意的是矩阵乘法的代码语法，不能使用 `A*A`(元素乘)，而要使用点乘 `.dot(A,B)`。


```python
A=np.array([[1,2],[1,1]])
B=np.array([[2,3],[4,5]])
A*B
```




    array([[2, 6],
           [4, 5]])



### 5. 矩阵的转置

> **【定义5】** 给定矩阵 $A_{m×n}$, 若将其行和列的元素进行位置互换，可以得到一个新的矩阵 $B_{n×m}$。那么矩阵B就称为矩阵A的**转置矩阵**，并记作 $B=A^T$。同时，矩阵A也称为矩阵B的**转置矩阵**。行和列的互换操作就称为矩阵的**转置**。

下列给出矩阵转置的Python代码。


```python
import numpy as np
A = np.array([[1,2,3,4],[5,6,7,8]])

print("矩阵A=\n{}\n".format(A))
print("矩阵A的转置=\n{}".format(A.T))
```

    矩阵A=
    [[1 2 3 4]
     [5 6 7 8]]
    
    矩阵A的转置=
    [[1 5]
     [2 6]
     [3 7]
     [4 8]]
    

矩阵的转置也是一种运算，满足下述运算规律（假设运算都是可行的）：
1. $(A^T)^T = A$
2. $(A + B)^T = A^T + B^T$
3. $(\lambda A)^T = \lambda A^T$
4. $(AB)^T = B^T A^T$

**【例8】** 已知 
$A = \begin{bmatrix} 
    2 & 0 & -1 \\
    1 & 3 & 2 \\
\end{bmatrix}，
B = \begin{bmatrix} 
    1 & 7 & -1\\
    4 & 2 & 3 \\
    2 & 0 & 1 
\end{bmatrix}$，求$(AB)^T$。

此处只给出Python代码的实现方法：


```python
import numpy as np
A = np.array([[2,0,-1],[1,3,2]])
B = np.array([[1,7,-1],[4,2,3],[2,0,1]])
print(np.dot(A,B).T)
```

    [[ 0 17]
     [14 13]
     [-3 10]]
    

### 张量的常用操作

在机器学习和深度学习中，我们常常将需要处理的数据规范化为特定维度的张量。例如，在不进行批处理的时候，

- 彩色图像可以看成是一个三维张量，分别是图像的高，图像的宽，图像的颜色通道（RGB），即，[C,H,W]。
- 视频可以看成是一个四维张量，分别是视频的时间帧方向、每一帧的颜色通道、高和宽，即，[T,C,H,W]
- 三维场景也可以看成是四维张量，分别是每一个像素的信息编码轴、场景的高、宽和深度，即：[C,H,W,D]

事实上，从前面的学习中我们已经知道包括标量、向量、矩阵在内的所有数据类型都可以统一成张量，这为我们进行数据处理提供了方便。在Python中，我们可以使用numpy数组来表示张量。


值得注意的是，数据的维度并非一成不变。以图象为例，如果输入的是灰度图，那么只需要二维张量即可，而如果是彩色图那么还需要一个单独的颜色通道。不过，对于张量的操作我们其实可以归结出一些常用的操作，例如：索引(indexing)、切片(slicing)、链接(joining)、换位(mutating)等。其中，张量的索引、切片和链接和矩阵操作基本一致。下面，我们简单介绍一下换位操作。
**换位（mutating）**：张量的换位操作类似于矩阵的转置操作。矩阵的转置是交换行和列，使得索引的次序改变。对于张量来讲，这种索引的改变，将涉及多个维度的交换。在此期间，换位操作要求只能调整索引的顺序，而每个维度内部的元素不能改变。换位操作可公式化为(仅一种)：
A(c, i, j, k) = B(i, j, k, c) 

例如，处理连续视频序列时，
1. 输入视频张量A大小为(10, 3, 800, 600)，分别表示10帧，每帧图像是3通道彩色图像，图像大小为800×600像素。
2. 经过卷积神经网络提取特征后，张量A的大小变为B (10, 128, 64, 64)。
3. 接下来需要使用循环神经网络对时间轴进行编码，我们需要先将张量的各个维度进行换位，得到张量C(128, 64, 64, 10) ，再进行处理。


### 6. 矩阵与向量的乘法的新视角：改变向量在空间中的位置

矩阵与向量的乘法通常可以理解成向量 $x$ 到向量 $y$ 的线性变换。

> **【定义6】** 对于向量 $y=[y_1, y_2, ..., y_m]^T$，若它能由向量 $x=[x_1, x_2,...,x_n]^T$ 线性表示，即有：

$\left\{
\begin{aligned}
& y_1 = a_{11} x_{1} + a_{12} x_{2} + ... + a_{1n} x_{n} \\
& y_2 = a_{21} x_{1} + a_{22} x_{2} + ... + a_{2n} x_{n} \\
& ... \\
& y_m = a_{m1} x_{1} + a_{m2} x_{2} + ... + a_{mn} x_{n} \\
\end{aligned}
\right.$

则称此关系式为向量$x$到向量$y$的线性变换，可以写成输出向量 $y$ 等于系数矩阵$A$左乘输入向量$x$：

$y=\begin{bmatrix} 
    y_1 \\ 
    y_2 \\ 
    ... \\ 
    y_m \\
\end{bmatrix}
=\begin{bmatrix} 
    a_{11} & a_{12} & ... & a_{1n} \\ 
    a_{21} & a_{22} & ... & a_{2n} \\ 
    ... & ... & ... & ... \\ 
    a_{m1} & a_{m2} & ... & a_{mn} \\
\end{bmatrix}
\begin{bmatrix} 
    x_1 \\ 
    x_2 \\ 
    ... \\ 
    x_n \\
\end{bmatrix}
=\begin{bmatrix} 
    a_{11} x_{1} + a_{12} x_{2} + ... + a_{1n} x_{n} \\ 
    a_{21} x_{1} + a_{22} x_{2} + ... + a_{2n} x_{n} \\ 
    ...  \\ 
    a_{m1} x_{1} + a_{m2} x_{2} + ... + a_{mn} x_{n} \\
\end{bmatrix}
=AX$

*注意 m 不一定等于 n.* 一般而言，$y=Ax$ 的形式是便于描述向量x的空间位置在矩阵A的作用下进行变换的过程。此时需要特别注意的是，在进行乘法的时候，**矩阵A在左，列向量x在右**，即Ax的顺序不能变。正如前面所讲，`矩阵与向量`的*乘法*可以看作是`矩阵与矩阵`的*乘法*第一种特征形式，只不过位于后面的矩阵是一个列数为1的特殊矩阵。

对照矩阵与矩阵的乘法规则，我们可以总结矩阵与向量的乘法规则：当把列向量看作是一个列数为1的特殊矩阵时，那么运算过程就变得比较简单了。
1. 矩阵在左，列向量在右，矩阵的列数和列向量的维数必须相等；
2. 矩阵和列向量相乘的结果也是一个列向量；
3. 矩阵的行数就是结果向量的维数；
4. 乘法运算的实施过程就是矩阵的每行和列向量的对应元素分别相乘后,再进行相加。

**【例8】** 给出一个矩阵与向量相乘的例子：$\begin{bmatrix} 
    1 & 2  \\
    4 & 5  \\
    7 & 8  \\  
\end{bmatrix}
\begin{bmatrix} 
    3 \\
    4 \\ 
\end{bmatrix}
=\begin{bmatrix} 
    1*3+2*4 \\
    4*3+5*4 \\
    7*3+8*4 \\
\end{bmatrix}
=\begin{bmatrix} 
    11 \\
    32 \\
    53 \\
\end{bmatrix}$.

下面给出Python描述：


```python

```


```python
import numpy as np
A = np.array([[1,2],
              [4,5],
              [7,8]])
x = np.array([[3,4]]).T
print(np.dot(A,x))
```

    [[11]
     [32]
     [53]]
    

**【结果分析】**

从程序运行的结果来看，原始向量 $u=\begin{bmatrix} 3 \\ 4 \end{bmatrix}$ 表示二维平面的一个点，其在二维平面中的坐标为 A(3, 4)，经过与矩阵 $A=\begin{bmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \end{bmatrix}$ 的乘法运算后，最终将原始点 A 转换为新的目标点B，其空间坐标为B(11,32,53)。

从以上的例子可以总结出矩阵所发挥的重要作用：在指定矩阵的作用下，原始空间中的向量被**映射**转换到了目标空间的新坐标，向量的空间`位置`由此发生了变化，甚至在映射后，目标空间的维数想较于原始空间都有可能发生改变。

### 7. 矩阵的应用案例

矩阵的应用非常广泛，下面仅举两例。

**【例9】** 生产成本核算问题

某厂生产三种产品，它的成本分为三类。每一类成本中，给出生产单个产品时估计需要的量。同时给出每季度生产每种产品数量的估计。该公司希望在股东会上用一个表格展示出每一季度三类成本的数量：原料费、工资和管理费。

成本（元）|产品A|产品B|产品C||产品|夏|秋|冬|春
:-:|:-:|:-:|:-:||:-:|:-:|:-:|:-:|:-:
原材料|0.1|0.3|0.15||A|4000|4500|4500|4000
劳动|0.3|0.4|0.25||B|2000|2600|2400|2200
企业管理费|0.1|0.2|0.15||C|5800|6200|6000|6000

解：我们用矩阵的方法来考虑此问题，设产品分类成本矩阵为M，季度产量矩阵为P，则有：

$M=\begin{bmatrix} 
0.1 & 0.3 & 0.15 \\
0.3 & 0.4 & 0.25 \\
0.1 & 0.2 & 0.15 
\end{bmatrix}，P=\begin{bmatrix} 
4000 & 4500 & 4500 & 4000 \\
2000 & 2600 & 2400 & 2200 \\
5800 & 6200 & 6000 & 6000 \\
\end{bmatrix}.$

- 如果按 $Q=M*P$ 构造乘积，则MP的第一列表示夏季的成本。
    - 原料费：$0.1*4000+0.3*2000+0.15*5800=1870$
    - 工资：$0.3*4000+0.4*2000+0.25*5800=3450$
    - 管理费和其他：$0.1*4000+0.2*2000+0.15*5800=1670$
- MP的第二列表示秋季的成本。
    - 原料费：$0.1*4500+0.3*2600+0.15*6200=2100$
    - 工资: $0.3*4500+0.4*2600+0.25*6200$
    - 管理费和其他: $0.1*4500+0.2*2600+0.15*6200$
- MP的第三列和第四列表示冬季和秋季的成本。

MP第一行的元素表示四个季度原料的总成本，第二和第三行的元素分别表示四个季度中每一季度工资和管理的成本。每一类成本的年度总成本可由矩阵的每一行元素相加得到。每一列元素相加，即可得到每一季度的总成本。下表汇总了总成本。

成本（元）|夏|秋|冬|春|全年
:-:|:-:|:-:|:-:|:-:|:-:
原材料|1870|2160|2070|1960|8060
劳动|3450|3940|3810|3580|14780
企业管理费|1670|1900|1830|1740|7140
总成本|6990|8000|7710|7280|29980

下面给出Python的计算方法。


```python
import numpy as np
import pandas as pd

M = np.array([[0.1,0.3,0.15],[0.3,0.4,0.25],[0.1,0.2,0.15]])
P = np.array([[4000,4500,4500,4000],[2000,2600,2400,2200],[5800,6200,6000,6000]])
Q = np.dot(M,P)

# 将numpy数组转换为DataFrame
df = pd.DataFrame(Q)
# 添加行列的标题
df.columns = ['夏','秋','东','春']
df.index = ['原材料','劳动','企业管理费']
# 计算各列数据总和并作为新列添加到末尾
df['全年'] = df.apply(lambda x:x.sum(), axis=1)
# 计算各列数据总和并作为新行添加到末尾
df.loc['总成本'] = df.apply(lambda x:x.sum())

# 输出pandas数据
display(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>夏</th>
      <th>秋</th>
      <th>东</th>
      <th>春</th>
      <th>全年</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>原材料</td>
      <td>1870.0</td>
      <td>2160.0</td>
      <td>2070.0</td>
      <td>1960.0</td>
      <td>8060.0</td>
    </tr>
    <tr>
      <td>劳动</td>
      <td>3450.0</td>
      <td>3940.0</td>
      <td>3810.0</td>
      <td>3580.0</td>
      <td>14780.0</td>
    </tr>
    <tr>
      <td>企业管理费</td>
      <td>1670.0</td>
      <td>1900.0</td>
      <td>1830.0</td>
      <td>1740.0</td>
      <td>7140.0</td>
    </tr>
    <tr>
      <td>总成本</td>
      <td>6990.0</td>
      <td>8000.0</td>
      <td>7710.0</td>
      <td>7280.0</td>
      <td>29980.0</td>
    </tr>
  </tbody>
</table>
</div>


**【例10】** 婚姻状况计算模型

某城镇中，有8000位已婚女性和2000位单身女性，假设每年有30%的已婚女性离婚，20%的单身女性结婚。假设所有女性的总数为一常数，试求1年后有多少已婚女性和单身女性？2年后呢？10年后呢？

解：我们可以用如下的思路构建矩阵A。1).矩阵A的第一行元素分别为1年后仍处于婚姻状态的已婚女性和已婚的单身女性百分比;2).第二行元素分别为1年后离婚的已婚女性和未婚的单身女性的百分比。则：

$A=\begin{bmatrix} 
0.7 & 0.2 \\
0.3 & 0.8 \\ 
\end{bmatrix}$

若令 $x=\begin{bmatrix} 8000 \\ 2000 \end{bmatrix}$，则1年后已婚女性和单身女性人数可以用$A$乘以$x$计算. 其中`8000*0.7`表示仍然在婚姻状态的已婚女性，`2000*0.2`为转变为已婚的单身女性，两者相加就是1年后已婚女性的总人数；`8000*0.3`表示1年后离婚的已婚女性，`2000*0.8`表示仍然未婚的未婚女性，两者相加就是1年后未婚女性的总人数。

$Ax=\begin{bmatrix} 
0.7 & 0.2 \\
0.3 & 0.8 \\ 
\end{bmatrix}
\begin{bmatrix} 
8000 \\
2000 \\ 
\end{bmatrix}
=\begin{bmatrix} 
6000 \\
4000 \\ 
\end{bmatrix}$

1年后将有6000位已婚女性，4000位单身女性。

要求2年后已婚女性和单身女性的数量，计算

$A^2 x = A(Ax) =\begin{bmatrix} 
0.7 & 0.2 \\
0.3 & 0.8 \\ 
\end{bmatrix}
\begin{bmatrix} 
6000 \\
4000 \\ 
\end{bmatrix}
=\begin{bmatrix} 
5000 \\
5000 \\ 
\end{bmatrix}$

2年后，一半的女性将为未婚，一般的女性将为单身。

一般地，n年后已婚女性和单身女性的数量可由$A^n x$求得。

按照以上的分析，我们将使用Python代码实现后续的计算，求解10年后的已婚女性和单身女性的数量。


```python
import numpy as np
A = np.array([[0.7,0.2],[0.3,0.8]])
x = np.array([[8000],[2000]])

n = 8 # n=1:A^2; n=2:A^3
product = np.dot(A,x)

for i in range(n-1):
    product = np.dot(A, product)
    
print(product)
```

    [[4015.625]
     [5984.375]]
    

**【结果分析】**

由程序的输出结果可知，10年后已婚女性和诞生女性的数量分别为：4016人和5984人。


**【例6.4】网络的矩阵分割和连接**  
在电路设计中，经常要把复杂的电路分割为局部电路，每一个电路都用一个网络“黑盒子”来表示。“黑盒子”的输入为$u_1, i_1$，输出为$u_2, i_2$，都有两个变量，因此其输入输出关系用2×2矩阵$A$来表示（如下图）, $A$被称为该电路的**传输矩阵**。

![](../Attachments/L0601-ex0101.png)

`传输矩阵`的元素可以用理论计算，也可用实验测试的方法取得。把复杂的电路分成许多串接局部电路，分别求出或测出它们的传输矩阵，再相乘起来，得到总的传输矩阵，可以使分析和测量电路的工作简化。 



```python
import numpy as np
R1 = Symbol('R1', real=True)
R2 = Symbol('R2', real=True)
u1 = Symbol('u1', real=True)
i1 = Symbol('i1', real=True)

A1 = np.array([[1, -R1],[0, 1]])
A2 = np.array([[1,0],[-1/R2,1]])
A = np.dot(A2, A1)

IN = np.array([[u1],[i1]])
OUT = np.dot(A,IN)


print('A = \n {} \n'.format(A))

print('OUT = \n {}'.format(OUT))
```

    A = 
     [[1 -R1]
     [-1/R2 R1/R2 + 1]] 
    
    OUT = 
     [[-R1*i1 + u1]
     [i1*(R1/R2 + 1) - u1/R2]]
    


```python

```
