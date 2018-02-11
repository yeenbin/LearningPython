#列表生成式即List Comprehensions

#生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 可以用list(range(1, 11))

print(list(range(1,11)))

#如果需要生成[1x1,2x2,3x3,...,10x10] 需要怎么做呢？

l = [x * x for x in range(1,11)]
print(l)

# 写列表生成式时，把要生成的元素x*x放到前面，后面跟for循环， 就可以把list创建出来，十分有用，多些几次就可以很快熟悉这种语法

#for循环后面还可以加上if判断，这样我们可以筛选出仅偶数的平方
l1 = [x * x for x in range(1,11) if x % 2 == 0]

print(l1)


# 还可以使用两层循环，可以生成全排列

l2 = [m + n for m in 'ABC' for n in 'XYZ']
print(l2)

# 运用列表生成式，可以写出非常简洁的代码 例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现

import os # 导入os模块
l3 = [d for d in os.listdir('.')]
print(l3)


# 由于for循环可以使用2个甚至多个变量，因此，列表生成页可以使用两个变量来生成list
d = {'x' : 'A', 'y' : 'B', 'z' : 'C'}
l4 = [k + ' = ' + v for k,v in d.items()]
print(l4)


# 最后把一个list中所有的字符串变成小写
l5 = [s.lower() for s in ['Hello', 'World', 'IBM', 'Apple']]
print(l5)

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s,str)] # 过滤只是字符串的元素
print(L2)

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

