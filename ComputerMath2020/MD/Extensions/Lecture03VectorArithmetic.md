# **第03讲 向量的四则运算** `扩展练习`

<font color="blue">作者：欧新宇（Xinyu OU）</font>

<font color="red">本文档所展示的测试结果，均运行于：Intel Core i7-7700K CPU 4.2GHz</font>

---

#### **1.【计算题】**  
设 $v_1=(1,1,0)^T, v_2=(0,1,1)^T, v_3=(3,4,0)^T$, 使用Python实现 $a = v_1-v_2$ 及 $b = 3v_1 + 2v_2 - v_3$的求解。

- **Python实现**

```python
# 0. 载入运算库
import numpy as np

# 1. 定义已知量
v1 = ____(1)____
v2 = np.array([[0,1,1]]).T
v3 = ____(2)____

# 2. 计算和数据处理
print('a = {}'.format(v1-v2))
print('b = {}'.format(____(3)____))
```

##### **答案及解析**

```python
(1) np.array([[1,1,0]]).T
(2) np.array([[3,4,0]]).T
(3) 3*v1+2*v2-v3
```


```python
# 0. 载入运算库
import numpy as np

# 1. 定义已知量
v1 = np.array([[1,1,0]]).T
v2 = np.array([[0,1,1]]).T
v3 = np.array([[3,4,0]]).T

# 2. 计算和数据处理
print('a = {}'.format(v1-v2))
print('b = {}'.format(3*v1+2*v2-v3))
```

    a = [[ 1]
     [ 0]
     [-1]]
    b = [[0]
     [1]
     [2]]
    

#### **2.【计算题】**  

设 $3(a_1-a) + 2(a_2 + a) = 5(a_3 + a)$。其中, $a_1=(2,5,1,3)^T, a_2=(10,1,5,10)^T, a_3=(4,1,-1,1)^T$，求$a$。

- **基础推导**

> &emsp;&nbsp; $3(a_1-a) + 2(a_2 + a) = 5(a_3 + a)$  
> => $3a_1 - 3*a + 2a_2 + 2*a = 5a_3 + 5*a$  
> => $3a_1 + 2a_2 - 5a_3 = 6*a$  
> => $a = \frac{3}{6} a_1 + \frac{2}{6} a_2 - \frac{5}{6} a_3$

- **Python实现**

```python
import numpy as np
a1 = np.array([[2,5,1,3]]).T
a2 = (____(1)____)
a3 = np.array([[4,1,(-1),1]]).T

print(____(2)____)
```



##### **答案及解析**

```python
(1) np.array([[10,1,5,10]]).T
(2) 3/6*a1 + 2/6*a2 - 5/6*a3
```


```python
import numpy as np
a1=np.array([[2,5,1,3]]).T
a2=np.array([[10,1,5,10]]).T
a3=np.array([[4,1,(-1),1]]).T

print(3/6*a1 + 2/6*a2 - 5/6*a3)
```

    [[1.]
     [2.]
     [3.]
     [4.]]
    

#### **3.【计算题】**  

$u^T=(3,2,2), v^T=(5,3,1)$， 求 $u$ 和 $v$ 的内积（点乘）和外积（叉乘）。

- **Python实现**

```python
import numpy as np
u=np.array([[3,2,2]])
v=____(1)____

dot = ____(2)____  # 不是数学规则，而是程序的限制，大家只需要记住
cross = ____(3)____
print('点乘：{}，叉乘：{}'.format(dot, cross))
```


##### **答案及解析**

```python
(1) np.array([[5,3,1]])
(2) np.dot(u, v.T)
(3) np.cross(u, v)
```


```python
import numpy as np
u=np.array([[3,2,2]])
v=np.array([[5,3,1]])

dot = np.dot(u, v.T)  # 不是数学规则，而是程序的限制，大家只需要记住
cross = np.cross(u, v)
print('点乘：{}，叉乘：{}'.format(dot, cross))
```

    点乘：[[23]]，叉乘：[[-4  7 -1]]
    
