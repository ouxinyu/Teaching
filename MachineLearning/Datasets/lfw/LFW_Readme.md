下面我们使用一个非常著名的人脸识别数据库LFW来完成后续的实验。

基本方法如下第3步所示，但是由于`lfw人脸识别数据集`服务器在国外，因此下载速度可能会很慢（甚至中断），所以建议按照如下步骤进行操作：
1. 下载数据集

> 方法一：链接：https://pan.baidu.com/s/1eySjV_1K2XYD5YYKCxiVEw   提取码：3wut

    或者
    
> 方法二：链接：https://ndownloader.figshare.com/files/5976015   
    
2. 将下载好的文件 `lfw-funneled.tgz`，复制到默认存储文件夹路径：

> C:\Users\用户名\scikit_learn_data\fw_home

如果文件夹不存在，可以先执行第三步一次

3. 使用以下语句载入和使用`lfw人脸识别数据集`
        
```python
from sklearn.datasets import fetch_lfw_people
faces = fetch_lfw_people(min_faces_per_person=20, resize=0.8)