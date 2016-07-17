#!/usr/bin/python

# 闭包 closure
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print f1
print f2

print f1 == f2

print f1()

# 下面的结果全部是9 ， 原因在于返回的函数f引用了变量i，但它并非立刻执行。等到3个函数都返回时，他们所引用的变量已经变成了3
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3 = count()

print f1()
print f2()
print f3()

# 防止函数滥用引用，可以嵌套一层函数，将引用传入新的函数
def count2():
	fs = []
	for i in range(1,4):
		def f(j):
			def g():
				return j*j
			return g
		fs.append(f(i))
	return fs

f1,f2,f3 = count2()

print f1()
print f2()
print f3()

# 匿名函数
f = lambda x : x * x
print f(5)
# 
print map(lambda x: x*x,[1, 2, 3, 4, 5, 6, 7, 8, 9])
# 1-9 互相乘
print reduce(lambda x , y : x*y,[1, 2, 3, 4, 5, 6, 7, 8, 9])



