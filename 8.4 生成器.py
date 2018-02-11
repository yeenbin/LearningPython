# 生成器

# 在Python中，一边循环一边计算的机制，成为生成器 generator

# 创建生成器的第一种方法 只要把一个列表生成式的[]改成() 就创建了一个generator

# generator保存的是算法 也是可迭代的对象

g = (x * x  for x in range(10))

for n in g:
	print(n)

# generator非常强大  

#斐波拉契数列用列表生成式写不出来，但是，用函数把他打印出来却很容易
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print(b)
		a,b = b, a + b
		n = n + 1
	return 'done'

fib(6)

#要把fib函数变成generator,只需要把print(b) 修改为yield b 就可以了
def g_fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b, a + b
		n = n + 1
	return 'done'

#最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# for n in g_fib(6):
# 	print(n)

#但是用for循环调用generator时，发选拿不到generator的return语句的返回值。如果想拿到返回值，必须
# 捕获 StopIteration 错误 返回值包含在StopIteration的value中
g = g_fib(6)
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value',e.value)
		break


# 杨辉三角
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1


# 把每一行看做一个list,试写一个generator, 不断输出下一行的list

# 方法一 用到了列表生成式， 理解起来比较困难
def triangles():
	L = [1]
	while True: 
		yield L
	
		L.append(0)
		L = [L[i - 1] + L[i] for i in range(len(L))]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
	print('测试失败!')




