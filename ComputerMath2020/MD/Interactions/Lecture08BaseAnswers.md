# **第08讲 维数、基底与坐标** `课堂互动答案`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

## **【课堂互动一】** `维数、基底与坐标`

**1. 若一个线性空间V中存在一个包含10个元素的基底，那么我们可以说这个线性空间V的维数为10。**  

<font style='color:blue;font-x-:bold;'>A. 对</font>  
B. 错  

**答案及解析：** A

<br/>

**2. 若向量组$a_1, a_2,...,a_n$是线性空间$V$的一组基底，则要求该向量组必须（   ）。**  

<font style='color:blue;font-x-:bold;'>A. 线性无关</font>  
B. 线性相关  
C. 存在不为0的元素  
D. 不存在为0的元素

**答案及解析：** A

<br/>

**3. 设二维向量$u$在标准基环境中的坐标是（3，4），则在新基底 $E_x= [0.5, 0], E_y=[0, 2]$中，向量$u$ 的坐标为（     ）。**  

A. (3, 4)  
<font style='color:blue;font-x-:bold;'>B. (6, 2)</font>  
C. (1.5, 8)  
D. (6, 8)  
E. (1.5, 2)

**答案及解析：** B

<br/>

**4. 以下矩阵能够作为标准基的是（     ）。**  

<font style='color:blue;font-x-:bold;'>A. $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$</font>  
B. $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$  
<font style='color:blue;font-x-:bold;'>C. $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$</font>    
<font style='color:blue;font-x-:bold;'>D. $\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$</font>

**答案及解析：** ACD

<br/>

**5. 设$𝑎_1,𝑎_2,...,𝑎_n$是线性空间$𝑉_𝑛$的一个基，对于任意元素$𝑎∈𝑉_𝑛$，总有且仅有一组有序数$𝑥_1,𝑥_2,...,𝑥_𝑛$，使$𝑎=𝑥_1𝑎_1+𝑥_2𝑎_2+...+𝑥_n𝑎_n$ 。则（        ）称为元素$𝑎$在空间$𝑉_𝑛$中的坐标。**  

A. 有序数$1, 2, ..., n$  
<font style='color:blue;font-x-:bold;'>B. 有序数$x_1,x_2,...,x_n$</font>  
C. 有序向量组$a_1,a_2,...,a_n$    
D. 有序线性组合$x_1a_1, x_2a_2, ...,x_na_n $

**答案及解析：** B

<br/>

## **【课堂互动二】** `构成基底的条件`

**1. 任何向量组都可以作为基底。**  

A. 对  
<font style='color:blue;font-x-:bold;'>B. 错</font>  

**答案及解析：** B

<br/>

**2. 给定一共2维空间$V_2$，如果存在向量组 $a = ([1,1]^T, [2,2]^T)$，请问向量组$a$是否能成为这个二维空间的基底？**  

A. 不可以，因为它违背了向量完备性的要求  
<font style='color:blue;font-x-:bold;'>B. 不可以，因为它违背了线性无关的要求</font>  
C. 不可以，因为它违背了线性相关的要求   
D. 可以作为这个二维空间的基底

**答案及解析：** B

<br/>

**3. 在判断一个向量组是否能成为基底的条件时，有一个充分必要条件是空间中的任意一个向量都可以由向量组a的线性组合构成，并且这种组合具有唯一性。那么请问，唯一性等价于什么？**  

A. 向量组 $a$ 线性相关  
<font style='color:blue;font-x-:bold;'>B. 向量组 $a$ 线性无关</font>  
C. 向量组 $a$ 数量完备   
D. 向量组 $a$ 维数完备

**答案及解析：** B

<br/>

**4. 给定两个向量 $a,b ≠0$ 和标量$i, j∈R$，它们的线性组合 $i*a + j*b$ 可能存在以下哪种情况？**  

A. 确定一个点  
<font style='color:blue;font-x-:bold;'>B. 确定一条直线</font>  
<font style='color:blue;font-x-:bold;'>C. 确定一个平面</font>     
D. 确定一个三维空间

**答案及解析：** BC

$a,b$为两个不为零的向量，当$a,b$不共线，则线性组合确定一个平面；当$a,b$共线，则线性组合只能确定一条直线。

<br/>

**5. 给定两个向量 $u,v,w \neq 0$和标量$a,b,c \in R$，它们的线性组合 $au+bv+cw$ 可能存在以下哪种情况？**  

A. 确定一个点  
<font style='color:blue;font-x-:bold;'>B. 确定一条直线</font>  
<font style='color:blue;font-x-:bold;'>C. 确定一个平面</font>   
<font style='color:blue;font-x-:bold;'>D. 确定一个三维空间</font>

**答案及解析：** BCD

对于不为0的三个向量，在空间R中，可能存在三种不同的关系。  
1.三者共线，确定一条直线  
2.任意两者共线，确定一个平面  
3.三者均不共线（线性无关），确定整个三维空间

<br/>


```python

```
