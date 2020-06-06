# **第07讲 向量空间** `课堂互动答案`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

## **【课堂互动一】** `向量与向量组`

**1. 下列符号中可以用来表示 n 维向量的是（ ）。**  

A. 小写正体英文字母  
<font style='color:blue;font-weight:bold;'>B. 小写加粗斜体英文字母</font>     
C. 小写斜体英文字母  
D. 大写加粗斜体英文字母  
E. 大写斜体英文字母

**答案及解析：** B

</br>

**2. 把 $n$ 个无序的数排列在一起形成一个集合，这个集合就称为 $n$ 维向量。**  

A. 对    
<font style='color:blue;font-weight:bold;'>B. 错</font>

**答案及解析：** B

<br/>

**3. 在计算机领域，默认情况下，向量 $a$ 表示一个（ ）。**  

A. 行向量    
<font style='color:blue;font-weight:bold;'>B. 列向量</font>  
C. 以上都可以  
D. 以上都不对

**答案及解析：** B

<br/>

**4. 向量 $u^T$ 通常用来表示一个（ ）。**  

<font style='color:blue;font-weight:bold;'>A. 行向量</font>  
B. 列向量  
C. 若无特殊说明，以上均可以  
D. 一般不用来表示向量  

**答案及解析：** A

</br>

**5. 所有的 n 维向量都可以理解为（ ）张量。**  

A. 零阶  
<font style='color:blue;font-weight:bold;'>B. 一阶</font>     
C. 二阶  
D. n 阶

**答案及解析：** B

</br>

## **【课堂互动二】** `向量空间和子空间`

**1. 在$n$维空间$V_n$中，如果存在一个超平面，那么该超平面的维度为（）。**  

<font style='color:blue;font-weight:bold;'>A. n-1</font>  
B. n     
C. n+1    
D. 无法确定

**答案及解析：** A

</br>

**2. 若$V$为一向量空间，则它满足加法和标量乘法的完备性，这意味着以下（）公理是成立的。**  

<font style='color:blue;font-weight:bold;'>A. 𝒙+𝒚=𝒚+𝒙</font>  
<font style='color:blue;font-weight:bold;'>B. (𝒙+𝒚)+𝒛=𝒙+(𝒚+𝒛)</font>       
<font style='color:blue;font-weight:bold;'>C. (𝑎+𝑏)𝒙=𝑎𝒙+𝑏𝒙</font>     
<font style='color:blue;font-weight:bold;'>D. 𝒙+(−𝒙)=𝟎</font> 

**答案及解析：** ABCD

</br>

**3. 若空间S是空间V的子空间，则（）。**  

<font style='color:blue;font-weight:bold;'>A. 标量乘法运算是封闭的</font>  
B. 乘法运算是封闭的       
C. 除法运算时封闭的      
<font style='color:blue;font-weight:bold;'>D. 加法运算是封闭的</font> 

**答案及解析：** AD

</br>

## **【课堂互动三】** `线性相关性`

**1. 假设存在向量组 $B={b_1, b_2, ..., b_m}$，请问B中各向量是线性无关的的条件是什么？**  

A. 由向量组B所形成的矩阵的秩 < 向量组B中向量的个数  
<font style='color:blue;font-weight:bold;'>B. 由向量组B所形成的矩阵的秩 = 向量组B中向量的个数</font>     
C. 由向量组B所形成的矩阵的秩 > 向量组B中向量的个数    
D. 无法判断向量组的线性无关

**答案及解析：** B

</br>

**2. 向量组中的两个向量，如果他们是线性相关的，那么在空间中，它们将确定（      ）。**  

A. 一个点（即两个向量的交点）  
<font style='color:blue;font-weight:bold;'>B. 一条直线</font>  
C. 一个平面    
D. 一个三维空间

**答案及解析：** B

</br>

**3. 当方程组中的某个方程式可以由其他方程式通过线性组合得到，那么可以说这个方程式是多余的。**  
<font style='color:blue;font-weight:bold;'>A. 对</font>   
B. 错

**答案及解析：** A

</br>

**4. 如果一个向量组包含5个列向量，那么我们将这5个列向量排成一行所组成的矩阵，可以被称为矩阵的行向量组。**  

A. 对  
<font style='color:blue;font-weight:bold;'>B. 错</font>   

**答案及解析：** B

</br>

**5. 下列表达式，可以用来表达一个 n 维向量空间的是（ ）。**  

A. $\pi=\{x=(x_1,x_2,...,x_n)^T|a_1x_1+a_2x_2+...+a_nx_n=b\}$  
B. $b=\lambda_1a_1+\lambda_2a_2+...+\lambda_m a_m$  
<font style='color:blue;font-weight:bold;'>C. $R_n=\{x=(x_1,x_2,...,x_n)^T|x_1,x_2,...,x_n \in R \}$</font>  
D. $k_1a_1+k_2a_2+...+k_ma_m=0$  
E. $A:a_1,a_2,...,a_m$

**答案及解析：** C

选项A表示平面，

</br>

## **【课堂互动四】** `空间的张成`

**1. 判断如下向量所张成的空间的形态（ ）。**  

$u_1=\begin{bmatrix} 1 \\ 1.5 \end{bmatrix}, u_2=\begin{bmatrix} 0.5 \\ 1 \end{bmatrix}$

A. 一条直线  
<font style='color:blue;font-weight:bold;'>B. 一个平面</font>    
C. 整个三维空间  
D. 无法张成空间

**答案及解析：** B

</br>

**2. 判断如下向量所张成的空间的形态（ ）。**  

$u_1=\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}, u_2=\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$

A. 一条直线  
<font style='color:blue;font-weight:bold;'>B. 一个平面</font>    
C. 整个三维空间  
D. 无法张成空间

**答案及解析：** B

</br>

**3. 判断如下向量所张成的空间的形态（ ）。**  

$u_1=\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, u_2=\begin{bmatrix} -2 \\ -2 \\ -2 \end{bmatrix}, u_2=\begin{bmatrix} 3 \\ 3 \\ 3 \end{bmatrix}$

<font style='color:blue;font-weight:bold;'>A. 一条直线</font>      
B. 一个平面  
C. 整个三维空间  
D. 无法张成空间

**答案及解析：** A

</br>

**4. 判断如下向量所张成的空间的形态（ ）。**  

$u_1=\begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix}, 
u_2=\begin{bmatrix} 2 \\ 1 \\ 5 \end{bmatrix}, 
u_3=\begin{bmatrix} 4 \\ 3 \\ 2 \end{bmatrix},
u_4=\begin{bmatrix} 4 \\ 2 \\ 10 \end{bmatrix}$

A. 一条直线    
B. 一个平面  
<font style='color:blue;font-weight:bold;'>C. 整个三维空间</font>  
D. 整个四维空间  
E. 无法张成空间

**答案及解析：** C

</br>

**5. 判断如下向量所张成的空间的形态（ ）。**  

$u_1=\begin{bmatrix} 1 \\ 2 \end{bmatrix}, 
u_2=\begin{bmatrix} -1 \\ -2 \end{bmatrix}$

<font style='color:blue;font-weight:bold;'>A. 一条直线</font>     
B. 一个平面  
C. 整个三维空间  
D. 无法张成空间

**答案及解析：** A

</br>
