# **第06讲 矩阵的应用** `课后习题`

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


**1. 给定矩阵$M=\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\end{bmatrix}$，分别求它的行空间形式和列空间形式。其中，向量组的系数以$a,b,c,d$进行表示。** 

**2. 设存在矩阵
$A = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix},
B = \begin{bmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \end{bmatrix}$, 向量
$u = \begin{bmatrix} 10 \\ 20 \end{bmatrix}, 
v = \begin{bmatrix} 100\\ 200 \\300 \end{bmatrix}$。
请将乘法$Au$和$Bv$分解成列的视角。**

<br/>

**3. 【应用题】冠状病毒感染人员预测**

冠状病毒的感染是非常快速的，某城市有800万人，在1月15日有2000人确诊感染了冠状病毒。假设每天新增确诊病例为未感染人口的0.4%，每天的治愈率为确诊人群的5%。假设在没有找到有效的抑制病例增加手段和防感染疫苗的情况下，2天，10天，20天，50天，100天后分别有多少确诊病例。

**【进阶问题】** <font color="blue">按照当前的设定，多少天以后达到峰值，即：新增确诊病例和新增治愈人数基本一致。</font>

**【扩展问题】** <font color="red">有兴趣的同学可以考虑，如何利用Python获取，当治愈率上升到一定的程度，或感染率降低到一定的程度后，出现拐点的日期。</font>


<br/>

**4.【应用题】 网络的矩阵分割和连接**

给出如下电路图，同时已知输入电流$i_{in}=25A$和输入电压$u_{in}=220V$，假设并联电路的电阻$R_{并}=200$欧姆，串联电路的电阻$R_{串}=4$欧姆，求输出电流$i_{out}$和输出电压$u_{out}$。（输出结果保留2位小数）

> 在Python实现的时候，注意使用合理维度的数组存储数据。

![L0601-hw201](../../Attachments/L0601-hw201.png)



```python

```