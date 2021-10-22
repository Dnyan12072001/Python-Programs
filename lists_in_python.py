# LIST
# list are mutable : ADD , update and Delete
# ordared indexing and slicing
# heterogeneous datatype

l = [10,20,30,"Python","Java",[100,200,300]]
print(l)

# indexing and slicing : 
print(l[1])
print(l[1:3])
print(l[::-1])

l = [100,200,300,400,500]

for value in l[::2]:
	print(value)


#1 append
l.append(600)
print(l)

#2 extend
l.extend([500,600,700,800])
print(l)
l.extend("Python")
print(l)

#3 insert
l.insert(1,10000)
print(l)

l = [10,20,30]
l2 = l
print(l,l2)	

#4 Update
l = [10,20,30,40,50]
l[2] = 300
print(l)

#5 Delete , Pop , remove , clear
r = l.pop()
print(l)
print(l,r)

s = l.pop(2)
print(l)

# remove
s = [10,20,20,30,20,30,30,40]
s.remove(20)
print(s)
s.remove(40)
print(s)

s.clear()
print(s)

# sort
p = [200,300,400,500,600]
print(p.sort())
print(l[::-1])


# reverse
p.reverse()
print(p)

# Extend 
o = [0.0001]
print(o * 10)


































































