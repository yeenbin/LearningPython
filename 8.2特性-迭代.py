#如果给定一个list或者tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代。
#在Python中，迭代是通过for...in 来完成的

d = {'a': 1,'b' : 2, 'c' : 3}

for key in d:   #默认情况下dict迭代的是key
	print(key)

#遍历value值
for value in d.values():
	print(value)


#同时遍历key和value

for k,v in d.items():
	print(k,v)


#字符串也是可迭代的对象
for c in 'ABCDEFG':
	print(c)

#所以 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而不太关心该对象究竟是list还是其他类型数据
#方法是通过collections模块的Iterable类型判断是否可迭代

from collections import Iterable

print(isinstance('abc', Iterable))  #str可迭代

print(isinstance(123,Iterable))  #整数不可迭代

# 如果要对list类似Java那样的下标循环  可以使用Python内置的enumerate函数 可以把一个list变成索引-元素对

for i, value in enumerate(['A','B','C']):
	print(i,value)


#--------------练习---------------
#请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
	min = None
	max = None

	for v in L:
		if min == None or min > v: min = v
		if max == None or max < v: max = v
		
	return(min,max)

		
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

