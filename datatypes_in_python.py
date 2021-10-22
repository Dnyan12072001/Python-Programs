a = 10
b =20
add = a + b
print(add)

#list
i = (1,2,3,4)
print(i) 

#id functions 
#type

print(type(a))
print(type(b))

print(id(a))
print(id(b))

a = 10
b = 10
#object intering
print(id(a),id(b))

#Data types

#1 int
num1 = 100
print(type(num1))

#2 float
num2 = 1.37
print(type(num2))

num1 = 100
print(id(num1))  
num1 = 105
print(id(num1))

#3 str('',"")
s = "Gaurav"
print(type(s))
print(s)

s = "'Gaurav' Sanjay Narkhede"
print(id(s))
print(s)

#4 list[]   mutable data type

l = [10,20,30,40,50,"Gaurav","Python"]
print(l,id(l))
l.append(60)  #add no
print(l,id(l))

#5 Tuple : immutable datatype
t = (10,20,10,30)
print(t)

#6 Dict : mutable datatype
d = {"name": "Gaurav","email":"dnyanadeonarkhede@gmail.com"}
print(d,type(d))

#7 sets : mutable data type   
s = {10,20,30,40} 
print(s)

#8 boolean : true or false

#9 complex : 4 + 3i