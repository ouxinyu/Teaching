# **第06讲 矩阵的应用** `扩展练习`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

#### **1.【计算题】**   
**给定矩阵$M=\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\end{bmatrix}$，分别求它的行空间形式和列空间形式。其中，向量组的系数以$a,b,c,d$进行表示。注意列向量组的顺序。** 

**解：**  
(1) 矩阵M的`行空间`形式为：  
```python
a(1,0,0,0)+____(1)____(0,1,0,0)+c(0,0,1,0)=(a,b,c,0)
```

(2) 矩阵M的`列空间`形式为：  
$x_1\begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
+\underline{\quad(2)\quad}\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
+x_3\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
+x_4\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
=\begin{bmatrix} a \\ b \\ c \end{bmatrix}$


<br/>

##### **答案及解析**

```python
(1) b(0,1,0,0)
(2) c
```

#### **2.【计算题】**   
**设存在矩阵
$A = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$, 向量
$u = \begin{bmatrix} 10 \\ 20 \end{bmatrix}$。
请将乘法$Au$分解成列的视角。**

**解：**  
$Au=\underline{\quad(1)\quad}\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
+\underline{\quad(2)\quad}\begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$

##### **答案及解析**

```python
(1) 10
(2) 20
```

$Au=\begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix} 
\begin{bmatrix} 10 \\ 20 \end{bmatrix}
=10\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
+20\begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$

<br/>

#### **3.【应用题】冠状病毒感染人员预测**

冠状病毒的感染是非常快速的，某城市有50万人，在1月15日有3000人确诊感染了冠状病毒。假设每天新增确诊病例为未感染人口的0.7%，每天的治愈率为确诊人群的8%。假设在没有找到有效的抑制病例增加手段和防感染疫苗的情况下，2天，5天，8天，20天，50天后分别有多少确诊病例。

```python
import numpy as np
A = np.array(____(1)____)
x = np.array(____(2)____)
n = [2, 5, 8, 20, 50] 
person = x

for i in n:
    for j in range(i):
        person = ____(3)____

    print("{:3d}天后，未感染人数为{:.0f}，确诊人数为{:.0f}".format(i, person[0][0], person[1][0]))
```

##### **答案及解析**

```python
(1) [[0.996, 0.05],[0.004,0.95]]
(2) [[7998000],[2000]]
(3) np.dot(A, person)
```

**解**：我们可以用如下思路构建传染矩阵X。
1. 矩阵X的第一行第一个元素为一天后仍然没有被感染的人占前一天没有被感染人群的百分比; 第一行第二个元素为前一天被治愈的人群占前一天确诊感染人群的百分比。。
2. 矩阵A的第二行第一个元素为一天后被感染确诊的人占前一天没有被感染人群的百分比；第二行第二个元素为前一天确诊的同时没有被治愈的人占前一天确诊人群的百分比。

则有:
$A=\begin{bmatrix}
99.3/100 & 8/100 \\
0.7/100 & 92/100 \\
\end{bmatrix}$

若令 $x=\begin{bmatrix} 500000-3000 \\ 3000 \end{bmatrix}$，则1天后确诊感染人数和正常人数可以用$A$乘以$x$计算，即$Ax$。其中`(500000-3000)*(99.3/100)`表示原来正常人群中仍然没有被感染的人数，`3000*(8/100)`表示一天后被治愈的人数，两者相加就是1天后正常人群的总数；`(500000-3000)*(0.7/100)`表示新增确诊病例，`3000*(92/100)`表示一天后仍然没有被治愈的确诊人数，两者相加就是1天后处于确诊状态的被感染人群。

$Ax=\begin{bmatrix}
99.6/100 & 5/100 \\
0.4/100 & 95/100 \\
\end{bmatrix}$

一般地说，n天后，感染冠状病毒的人数和正常人数，可由$A^n x$求得。


```python
import numpy as np
A = np.array([[0.996, 0.05],[0.004,0.95]])
x = np.array([[7998000],[2000]])
n = [2, 5, 8, 20, 50] 
person = x

for i in n:
    for j in range(i):
        person = np.dot(A, person)

    print("{:3d}天后，未感染人数为{:.0f}，确诊人数为{:.0f}".format(i, person[0][0], person[1][0]))
```

      2天后，未感染人数为7935938，确诊人数为64062
      5天后，未感染人数为7807837，确诊人数为192163
      8天后，未感染人数为7664243，确诊人数为335757
     20天后，未感染人数为7492028，确诊人数为507972
     50天后，未感染人数为7412680，确诊人数为587320
    
