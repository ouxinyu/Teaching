'''
@Author: Xin-Yu Ou (欧新宇)
@Description: 
@LastEditorTime: 
'''
names = input("请输入各个同学行业名称，行业名称之间用空格间隔（回车结束输入）：")
t = names.split()
d = {}
for c in range(len(t)):
    d[t[c]] = d.get(t[c], 0)+1
    ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)
for k in range(len(ls)):
    zy, num = ls[k]
    print("{}:{}".format(zy, num))
