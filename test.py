#/usr/bin/python

# filter function
def not_empty(s):
	return s and s.strip()

print filter(not_empty , ['A' , '' , 'B' , None , '   ']);

# 删除1-100的素数
def is_prime(s):
	if s == 1:
		return False
	for i in range(2,s):
		if s % i == 0 :
			return False
	return True

print filter(is_prime , range(1,101))

# 排序算法	冒泡，快速 默认顺序排列
print sorted([36, 5, 12, 9, 21])
# sorted也是高阶函数，支持传入自定义函数
def reversed_cmp(x , y):
	if x > y :
		return -1
	if x < y :
		return 1
	return 0

print sorted([36, 5, 12, 9, 21] , reversed_cmp)

# 练习：字符串忽略大小写顺序排列
def cmp_ignore_case(s1 , s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	if u1 > u2:
		return 1

print sorted(['bob', 'about', 'Zoo', 'Credit'] , cmp_ignore_case)



