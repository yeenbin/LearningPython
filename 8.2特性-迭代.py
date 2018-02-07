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
