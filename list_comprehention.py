l = [100,200,300,400,500,600,700]
l1 = []

for value in l:
	l1.append(value * value)
print(l1)


# even no on list

a = [10,20,15,37,30,45,40,35,50]
a1 = [value for value in a if value % 2 == 0]
print(a1)

# to find length of each element

s = ['abc','abshf','whaa','gaurav']
s1 = [len(value) for value in s]
print(s1)

d = {x:x**2 for x in range(1,11)}
print(d)

s = {chr(x):x for x in range(97,123)}
print(s)

