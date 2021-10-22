#1 map

def sqr(num):
	return num**2

l = [10,20,30,40,50]
result = list(map(sqr,l))
print(result)

for value in result:
	print(value)


def add(a,b):
	return a + b

l1 = [100,200,300,400,500]
l2 = [10,20,30,40,50]
result = list(map(add,l1,l2))
print(result)


def check_num(num):
	if num % 2== 0:
		return True
	else:
		return False
l = [100,115,200,117,402,408]

result = list(map(check_num,l))
print(result)



#2 filter
def check_num(num):
	if num % 2== 0:
		return True
	else:
		return False
l = [100,115,200,117,402,408]

result = list(filter(check_num,l))
print(result)

#3 lambda

l = [10,20,30,40,50]
result = list(map(lambda num1:num1**2,l))
print(result)


l = [100,115,200,117,402,408]
result = list(filter(lambda num:num % 2== 0,l))
print(result)


d = {1:50,2:40,3:30,4:20,5:50}
l = sorted(d.items())
print(l)

d = {8:50,3:40,2:30,1:20,5:10}
l = dict(sorted(d.items(),key = lambda x: x[1]))
print(l)



