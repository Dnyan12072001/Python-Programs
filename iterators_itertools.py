l = [100,200,300,400,500]
i = iter(l)
# print(i)

# print(next(i))
# print(next(i))

for value in i:
	print(value)


import itertools

l1 = [10,20,30,40,50]
l2 = [100,200,300,400,500]
l3 = [1000,2000,3000,4000,5000]

i = itertools.chain(l1,l2,l3)

# print(next(i))

for value in i:
	print(value)


count = 0
for value in itertools.cycle(l1):
	if count < 20:
		print(value)
	else:
		break

	count+=1


count = 0
for value in itertools.repeat(l1):
	if count < 20:
		print(value)
	else:
		break

	count+=1


count = 0
for value in itertools.count(10,5):
	if count > 20:
		break
	else:
		print(value)
	count+=1
    

# permutaion and cobination

l = [1,2,3,4,5,6]
print(list(itertools.permutations(l,2)))
print(list(itertools.combinations(l,2)))










