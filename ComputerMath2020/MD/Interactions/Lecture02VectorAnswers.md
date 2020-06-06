# **第02讲 向量的基础知识** `课堂互动答案`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

## **【课堂互动一】** `向量的基本知识和列向量`

**1. 下列量又可以被称为矢量的是（         ）。**  
A. 标量  
B. <font style='color:blue;font-weight:bold;'>向量</font>  
C. 矩阵  
D. 张量  

**答案及解析：** B  

向量称欧几里得向量、几何向量、矢量，它指具有大小和方向的量。它可以形象化地表示为带箭头的线段。

<br/>

**2. 以下记法中，可以用来表示向量的有哪些？**  
A. <font style='color:blue;font-weight:bold;'>a</font>     
B. <font style='color:blue;font-weight:bold;'>$\vec{v}$</font>  
C. <font style='color:blue;font-weight:bold;'>$\vec{AB}$</font>   
D. <font style='color:blue;font-weight:bold;'>A</font>     

**答案及解析：** ABCD  
A，向量的标准表达方式，小写粗斜体英文字母；B，单向量有向线段表达法；C，起点-终点有向线段表达法；D，张量表达法。

<br/>

**3. 给定向量$a=[3,5,7]^T$ ，它可以用来表示（）。**  
A. 一个行向量  
<font style='color:blue;font-weight:bold;'>B. 一个列向量</font>  
C. 一个矩阵  
D. 矩阵在$x$方向上的分量

**答案及解析：** B  
默认情况，可以使用$a$表达一个列向量；而对于列举法，通常在元素列表的右上角增加一个转置符号用于表达一个列向量。

<br/>

**4. 给出下列Python代码的运行结果（）：**  


```python
import numpy as np
A = np.array([2, 2, 3, 4])
C = A.T

print('a={}'.format(C))
```
           
A. *a* = [[2 2 3 4]]  (二阶行向量)  
<font style='color:blue;font-weight:bold;font-style:italic'>B. a = [2 2 3 4]  (一阶行向量)</font>  
C. *a* = [2,  
2,  
3,  
4]  
(一阶列向量)  
D. *a* = [[2],  
[2],  
[3],  
[4]]  
(二阶列向量)

**答案及解析：** B


```python
import numpy as np
A = np.array([2, 2, 3, 4])
C = A.T

print('a={}'.format(C))
```

    a=[2 2 3 4]
    

<br/>

**5. 下列代码，可以用来表示一个列向量的是（）。**  
A. A=np.array([5,6,7]).T  
<font style='color:blue;font-weight:bold;'>B. A=np.array([[5,6,7]]).T</font>    
C. A=np.array([[[5,6,7]]]).T  
D. A=[5;6;7]

**答案及解析：** B 


```python
print('选项A = {}'.format(np.array([5,6,7]).T))
print('选项B = {}'.format(np.array([[5,6,7]]).T))
print('选项C = {}'.format(np.array([[[5,6,7]]]).T))
```

    选项A = [5 6 7]
    选项B = [[5]
     [6]
     [7]]
    选项C = [[[5]]
    
     [[6]]
    
     [[7]]]
    

## **【课堂互动二】** `范数`

**1. 下列范数可以用来衡量两个向量间距离的是（      ）。**  
A. p-范数  
B. L1范数   
<font style='color:blue;font-weight:bold;'>C. L2范数</font>  
D. 无穷范数

**答案及解析：** C

<br/>

**2. 范数是数学中的一种基本概念，通常可以理解成一类特殊的函数。一个向量的范数通常满足以下哪些条件？（      ）。**  
<font style='color:blue;font-weight:bold;'>A. 非负性</font>  
<font style='color:blue;font-weight:bold;'>B. 齐次性</font>  
C. 不变性  
<font style='color:blue;font-weight:bold;'>D. 三角不等式</font>  

**答案及解析：** ABD

<br/>

**3. 给定向量$a=[1,3,5,7,9]$，试求向量$a$的L1范数。**  
<font style='color:blue;font-weight:bold;'>A. 25</font>  
B. 12.8  
C. 1.0    
D. 9.0 

**答案及解析：** A  

`L1范数`求的是向量每个元素的绝对值的累加和，即：$||v_1||=\sum^n_{i=1} |v_i|$。

<br/>

**4. 给定向量$a=[1,3,5,7,9]$，试求向量$a$的L2范数。**  
A. 25.0</font>  
<font style='color:blue;font-weight:bold;'>B. 12.8</font>  
C. 1.0   
D. 9.0

**答案及解析：** B

`L2范数`求的是向量的长度，也被称为欧几里得距离，简称欧氏距离。即：$||v_2||=(\sum^n_{i=1} |v_i|^2)^{1/2}$。

<br/>

**5. 给定向量$a=[1,3,5,7,9]$，试求向量$a$的无穷范数。**  
A. 25.0  
B. 12.8  
C. 1.0   
<font style='color:blue;font-weight:bold;'>D. 9.0</font> 

**答案及解析：** D

$L_{\infty}$ `范数` 表示向量中最大分量的绝对值，即：$||v_{\infty}||=\max \limits_{i} |v_i|$。

<br/>

习题3~5的Python描述


```python
import numpy as np
a = np.array([1,3,5,7,9])

print('L1范数:{:.1f}'.format(np.linalg.norm(a,ord=1)))
print('L2范数:{:.1f}'.format(np.linalg.norm(a,ord=2)))
print('无穷范数:{:.1f}'.format(np.linalg.norm(a,ord=np.inf)))
```

    L1范数:25.0
    L2范数:12.8
    无穷范数:9.0
    

## **【课堂互动三】**

**1. 下列代码，属于One-Hot向量的是哪一个？**  
A. $[0,3,0,0,0,1]$  
<font style='color:blue;font-weight:bold;'>B. $[0,1,0,0,0,0]$</font>   
C. $[0,1,0,1,0,1]$  
D. $[1,1,1,1,1,1]$

**答案及解析：** B 

有且仅有一个分量为1，其它分量都为0的向量称为One-Hot向量，又称为独热码。

**2. 以下向量可以用来计算余弦相似性的特殊向量是哪一个？**  
A. 全0向量  
B. 全1向量   
C. One\-Hot向量  
<font style='color:blue;font-weight:bold;'>D. 单位向量</font>

**答案及解析：** B 

单位向量将向量的长度约束为1，这样可以很好地屏蔽模长（向量大小）带来的影响，仅用于表达向量的方向。而余弦相似性就是一种只关心向量间夹角大小的相似性计算方法。
