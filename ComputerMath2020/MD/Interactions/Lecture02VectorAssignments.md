# **第02讲 向量的基础知识** `课堂互动`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

## **【课堂互动一】**

**1. 下列量又可以被称为矢量的是（         ）。**  
A. 标量  
B. <font style='color:blue;font-weight:bold;'>向量</font>  
C. 矩阵  
D. 张量  

**2. 以下记法中，可以用来表示向量的有哪些？**  
A. <font style='color:blue;font-weight:bold;'>***a***</font>     
B. <font style='color:blue;font-weight:bold;'>$\vec{v}$</font>  
C. <font style='color:blue;font-weight:bold;'>$\vec{AB}$</font>   
D. <font style='color:blue;font-weight:bold;'>***A***</font>     

**3. 给定向量$a=[3,5,7]^T$ ，它可以用来表示（）。**  
A. 一个行向量  
<font style='color:blue;font-weight:bold;'>B. 一个列向量</font>  
C. 一个矩阵  
D. 矩阵在$x$方向上的分量

**4. 给出下列Python代码的运行结果（）：**  

>
```python
import numpy as np
A = np.array([2, 2, 3, 4])
C = A.T

print('a={}'.format(C))
```
>
          
A. *a* = [[2 2 3 4]]  
<font style='color:blue;font-weight:bold;font-style:italic'>B. a = [2 2 3 4]</font>  
C. *a* = [2  
2  
3  
4]  
D. *a* = [[2]  
[2]  
[3]  
[4]]  

**5. 下列代码，可以用来表示一个列向量的是（）。**  
A. A=np.array([5,6,7]).T  
<font style='color:blue;font-weight:bold;'>B. A=np.array([[5,6,7]]).T</font>    
C. A=np.array([[[5,6,7]]]).T  
D. A=[5;6;7]

## **【课堂互动二】**

**1. 下列范数可以用来衡量两个向量间距离的是（      ）。**  
A. p-范数  
B. L1范数   
<font style='color:blue;font-weight:bold;'>C. L2范数</font>  
D. 无穷范数

**2. 范数是数学中的一种基本概念，通常可以理解成一类特殊的函数。一个向量的范数通常满足以下哪些条件？（      ）。**  
<font style='color:blue;font-weight:bold;'>A. 非负性</font>  
<font style='color:blue;font-weight:bold;'>B. 齐次性</font>  
C. 不变性  
<font style='color:blue;font-weight:bold;'>D. 三角不等式</font>  

**3. 给定向量$a=[1,3,5,7,9]$，试求向量$a$的L1范数。**  
<font style='color:blue;font-weight:bold;'>A. 25</font>  
B. 12.8  
C. 1.0    
D. 9.0 

**4. 给定向量$a=[1,3,5,7,9]$，试求向量$a$的L2范数。**  
A. 25.0</font>  
<font style='color:blue;font-weight:bold;'>B. 12.8</font>  
C. 1.0   
D. 9.0

**5. 给定向量$a=[1,3,5,7,9]$，试求向量$a$的无穷范数。**  
A. 25.0  
B. 12.8  
C. 1.0   
<font style='color:blue;font-weight:bold;'>D. 9.0</font> 

## **【课堂互动三】**

**1. 下列代码，属于One-Hot向量的是哪一个？**  
A. $[0,3,0,0,0,1]$  
<font style='color:blue;font-weight:bold;'>B. $[0,1,0,0,0,0]$</font>   
C. $[0,1,0,1,0,1]$  
D. $[1,1,1,1,1,1]$

**2. 以下向量可以用来计算余弦相似性的特殊向量是哪一个？**  
A. 全0向量  
B. 全1向量   
C. One\-Hot向量  
<font style='color:blue;font-weight:bold;'>D. 单位向量</font>
