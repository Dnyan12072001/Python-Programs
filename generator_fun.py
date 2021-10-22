
def printval(l):
	for value in l:
		print(value)

l = [10,20,30,40,50]
printval(l)

def fibo():
	first_num = 0
	second_num = 1
	while(True):
		next_val = first_num + second_num
		yield next_val
		first_num,second_num = second_num, next_val

g = fibo()
#print(g)

print(next(g))
print(next(g))
print(next(g))
print(next(g))


for value in range(10):
	print(next(g))

for value in range(2,20):
	print(next(g))



l = [100,200,30,400,50]

l2 = [value * value for value in l]

print(l2)

l2 = (value * value for value in l)

print(next(l2))
print(next(l2))
print(next(l2))































