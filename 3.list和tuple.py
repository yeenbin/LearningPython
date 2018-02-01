# list是一种有序的列表数据集合 元素的数据类型可以不同 可随时添加和删除其中的数据
classmates = ['Michael',2,'Tracy']
print(classmates)

# 获取list长度的函数 len
print(len(classmates))

#通过索引获取list元素 前提要确保索引不越界
print(classmates[1])



#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
print(t)

#可变的tuple 其实变的不是tuple 而是改变tuple中的List元素
t1 = ('a','b',['A','B'])
print(t1)


t1[2][0] = 'C'
print(t1)