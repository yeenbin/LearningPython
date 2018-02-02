#dict

#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

d = {'Michael' : 95 , 'Bob' : 75 , 'Tracy' : 85}
print(d['Bob'])

d['Jack'] = 88
print(d)
print(d['Jack'])

#避免key不存在 会报错的结  有两种办法
#1.通过in判断key是否存在
#2.通过dict提供的get()方法 可以返回None 或者自己指定的value

print('tomas' in d)
print(d.get('tomas'))
print(d.get('tomas', -1))

#删除一个key 用pop(key)方法 对应的value也会从dict中删除

d.pop('Bob')
print(d)



#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：

# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。


#需要牢记的第一条就是dict的key必须是不可变对象。
#这个通过key计算位置的算法称为哈希算法（Hash）。



#-----------------------------------------

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

s = set([1,2,3,2,3,4])

print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加 但是不会有效果
s.add(5)
s.add(5)
s.add(5)
s.add(5)
s.add(8)
s.add(False)
s.add('string')
print(s)


#通过remove()方法可以删除元素
s.remove(4)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

s2 = set([2, 3, 5, 8, 9,10])

print(s & s2) #交集
print(s | s2) #并集


#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”

# s.add([1,2]) #添加可变对象会报错

s.add((1,2))  #没包含可变对象的元组可以加入
print(s)

#s.add((1,[2,3]))  # 包含了可变对象的元组加入会报错



######不可变对象

#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a = ['c','b','a']
a.sort()
print(a)
