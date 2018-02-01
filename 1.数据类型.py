#注释
a = -100
if a >= 0:
	print(a)
else:
	print(-a)


print('I\'m ok')

#为了简化，Python还允许用r''表示''内部的字符串默认不转义
print('\\\t\\')

print(r'\\\t\\')

#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容

print('''line
line2
line3''')

#布尔值
print(True)
print(False)
print('-------------------------')
print(True and True)
print(True and False)
print(False and False)
print('-------------------------')
print(True or True)
print(True or False)
print(False or False)
print('-------------------------')
print(not True)
print(not False)

#空值
#空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

print(None)

# 变量
#在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
print('-------------------------')
a = 123
print(a)
a = '字符串'
print(a)

#这种变量本身类型不固定的语言称之为动态语言

#在Python中，通常用全部大写的变量名表示常量
PI = 3.14159265359

#事实上PI也是一个变量的 用全部大写的变量名表示常量只是一个习惯上的写法

#除法/ 地板除//  取余%
print('-------------------------')
print(10 / 3)
print(9 / 3)
