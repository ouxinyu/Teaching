# **第05讲 矩阵操作** `课后习题答案`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

- ### **作业要求及提交**

1. 将所有运行结果保存为一个`word`文档（特别推荐保存为`pdf`文档进行提交）
2. 要求：使用编程环境完成下列习题，并按题目顺序进行排版，每个题目要求按如下顺序组织（若存在）:  
`0).`题目(将题目完整Copy到作业文档中，可以通过公式编辑器编辑或截图方式）；  
`1).`需要手工书写的部分，请尽量在word文档中进行编辑（迫不得已时，可书写在纸上并拍照）；  
`2).`代码（尽量通过从编程环境截图粘贴）；  
`3).`运行结果贴于文档中。 （复制运行结果到文档或通过截图粘贴）  
`x). ` **如果熟悉本编程环境'Jupyter Notebook'也可以直接在本环境中编写所有文稿及代码，并打印成pdf文档进行提交。**
3. 将文档上传至 `课堂派` 平台

> 注意：截图只需要截取必要部分。此外，请确保截图清晰可见。


-  ### **答案及解析**

**【计算题】使用Python代码，求解以下矩阵运算**

**1. 已知 $A=[1,2,3], B=[4,5,6]^T$，求$AB$和$BA$。**

**解**：  
$ AB = [1,2,3] \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}
= 1 \times 4 + 2 \times 5 + 3 \times 6 
= 32 $

$ BA = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix} [1,2,3]
= \begin{bmatrix} 4 \times 1 & 4 \times 2 & 4 \times 3 \\
5 \times 1 & 5 \times 2 & 5 \times 3 \\
6 \times 1 & 6 \times 2 & 6 \times 3 \end{bmatrix}
= \begin{bmatrix} 4 & 8 & 12 \\ 5 & 10 & 15 \\ 6 & 12 & 18\end{bmatrix}$


```python
import numpy as np
A = np.array([[1,2,3]])
B = np.array([[4],[5],[6]])

print("AB=\n {}".format(np.dot(A,B)))
print("BA=\n {}".format(np.dot(B,A)))
```

    AB=
     [[32]]
    BA=
     [[ 4  8 12]
     [ 5 10 15]
     [ 6 12 18]]
    

<br/>

**2. 求矩阵 $S = \begin{bmatrix}
2 & 1 & 4 & 0 \\
1 & -1 & 3 & 4 \\
\end{bmatrix}
\begin{bmatrix}
1 & 3 & 1 \\
0 & -1 & 2 \\
1 & -3 & 1 \\
4 & 0 & -2 \\
\end{bmatrix}$ 的乘积。**

**解：**


```python
import numpy as np
A = np.array([[2,1,4,0],[1,-1,3,4]])
B = np.array([[1,3,1],[0,-1,2],[1,-3,1],[4,0,-2]])

S = np.dot(A,B)
print("A×B=\n {}".format(S))
```

    A×B=
     [[ 6 -7  8]
     [20 -5 -6]]
    

<br/>

**3. 设$A = \begin{bmatrix}
1 & 2 & 1 & 0 \\
2 & 1 & 0 & 1 \\
3 & -2 & 2 & 1 \\
1 & 2 & 4 & 3 \\
\end{bmatrix}$，
$B = \begin{bmatrix}
3 & 4 & 1 & -2 \\
2 & 1 & 2 & 2 \\
2 & -2 & 2 & 1 \\
1 & 2 & -4 & 3 \\
\end{bmatrix}$，求$M = 4A^2 + 3AB - 2BA+ 5B^2 + (AB)^T$。**

**解:**


```python
import numpy as np
A = np.array([[1,2,1,0],[2,1,0,1],[3,-2,2,1],[1,2,4,3]])
B = np.array([[3,4,1,-2],[2,1,2,2],[2,-2,2,1],[1,2,-4,3]])

M = 4*np.dot(A,A)+3*np.dot(A,B)-2*np.dot(B,A)+5*np.dot(B,B)+(np.dot(A,B).T)
print("Result = \n {}".format(M))
```

    Result = 
     [[129  71 154  26]
     [ 97 107   4  35]
     [ 86  52  10 -23]
     [155  85  -3 141]]
    

<br/>

**4. 矩阵的加法：设存在矩阵$A = \begin{bmatrix} 1.2 & 3.4 & 5.6 \\ 7.8 & 9.1 & 0.7 \end{bmatrix}$, 和向量$u = [100, 200]^T$。试求$(2A+3b)-(3A-2b)$。**

**解：**


```python
import numpy as np
A = np.array([[1.2,3.4,5.6],[7.8,9.1,0.7]])
u = np.array([[100,200]]).T

print((2*A+3*u)-(3*A-2*u))
```

    [[498.8 496.6 494.4]
     [992.2 990.9 999.3]]
    