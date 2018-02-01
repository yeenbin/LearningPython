# 循环语句
names = ['abb','city','Tracy']
for name in names:
	print(name)

#如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：


l = list(range(101))
sum = 0
for x in l:
	sum += x
print(sum)


#在循环中，break语句可以提前退出循环。

n = 1
while n<= 100:
	if n > 10: #dang de
		break  #
	print(n) 
	n = n + 1	
print('END')


# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
n = 0
while n < 10:
	n += 1
	if n % 2  == 0 : #如果是偶数 就跳过这一次的循环 执行下一次的循环
		continue
	print(n)


#要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

#有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。

#下面这个是死循环
n = 1
while n > 0:
	n += 1
	print(n)






