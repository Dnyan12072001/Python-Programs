# Conditional statements

#1 if_else :
#if [condition]:
#    statements
#else :
#    statements

a = 100
b = 200

if a > b:
	print("a is greater")
elif b > a:
	print("b is greater")
else:
	print("both equal")


#2 For loop
# Iterable datatypes : str , list , tuple , dict

# for [variable_name] in [Iterable datatype]:
 
l = [10,20,30,40,50]

for value in l:
	print(value)

# for counting sum
sum = 0
for value in l:
	sum = sum + value
print(sum)

# for sum of 1st 20 num : 1-20
# by using range function 

sum = 0
for value in range(1,20):
	print(value)


for value in range(20,1000,20):
    print(value)


#break
#continue
l = [1,2,3,4,5,6]
key = 4

for value in l:
	if value == key:
		print("element found")
		break
	else:
		continue
else: 
	print ("Element not found")

print("Gaurav")

# enumerate
# pass
for index,value in enumerate(l):
	print(index,value)
	if value == key:
		print("element found")
		break
	else:
		pass
		print("Gaurav")
else: 
	print ("Element not found")


# 3 While loops in python

# while [condition]:
#     [statments]
#else

# sum of 1-20 num
count = 1
sum = 0

while count <= 20:
	sum = sum +count
	count = count +1

print(sum)