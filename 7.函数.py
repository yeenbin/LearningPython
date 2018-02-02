#Python 内置了很多有用的函数 我们可以直接调用。
print(abs(-20))

# abs(1,2) #TypeError: abs() takes exactly one argument

# abs('a') #TypeError: bad operand type for abs(): 'str'


#而max函数max()可以接收任意多个参数，并返回最大的那个
print(max(1,2,3,10,-3))


#数据类型的转换
print(int('123'))
print(int(12.34))

print(float('33.45'))

print(str(12.34))


#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

a = abs #变量a指向abs函数

print(a(-10))



#-------------定义函数-----------------
print('-------------定义函数-----------------')

#在Python ，定义一个函数要使用def语句、依次写出函数名、括号、括号中的参数和冒号：
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(11))
print(my_abs(-11))


#请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。



# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名

# 定义一个什么事页不做的空函数
def nop():
	pass

#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。


# 传入错误的参数
# my_abs('a')

#我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。



# 返回多个值的函数
#比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标

import math

def move(x,y,step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny


r = move(100, 100, 60, math.pi / 6)
print(r)

# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

# 小结

# 定义函数时，需要确定函数名和参数个数；

# 如果有必要，可以先对参数的数据类型做检查；

# 函数体内部可以用return随时返回函数结果；

# 函数执行完毕也没有return语句时，自动return None。

# 函数可以同时返回多个值，但其实就是一个tuple。


#-------------函数的参数-----------------
print('-------------函数的参数-----------------')

#Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码

# 位置参数
#定义一个函数power(x, n) 用来计算x的n次方
def power(x,n):
	s = 1
	while n > 0:
		n -= 1
		s = s * x
	return s

print(power(5,2))
print(power(5,3))

