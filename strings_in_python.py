# String : '', " "
#1 strings are immutable
#2 string is orderd data structure

s = "Python sample string"
print(type(s))
print(s)
# Indexing
print(s[0])
print(s[-1])
print(s[-3])

# Slicing
print(s[0:5])
print(s[7:])
print(s[7:16])
print(s[:5])

# stride
print(s[::2])  #skip one char
print(s[::-1]) #reverse string

for value in s:
	print(value)

for value in s[::2]:
	print(value)


# help(str)


#1 Format
num1 = 100
num2 = 200
print("Value of num1 is {} value of num2 {}".format(num1,num2))

print("Value of num1 is {1} value of num2 {0} ".format(num1,num2))
print("Value of num1 is {} value of num2 {}".format(num1,num2))

s = "python sample string"

s1 = s.capitalize()
print(s1)
print(id(s1))

#2 Upper , lower , title
print(s.upper())
print(s.lower())
print(s.title())
#3 isupper , islower , istitle
print(s.isupper())
print(s.islower())

# 4 split , join
s = "HTML,CSS,PYTHON,JAVA,Django"
l = s.split(",")
print(l)

s1 = (" ").join(l)
print(s1)

#maketrans
# translate
s1 = "abcd"
s2 = "1234"
s3 = "Python Sample string abcd"
table = str.maketrans(s1,s2)
result = s3.translate(table)
print(result)

# Index , Find , rfind function
s = "HTML,CSS,PYTHON,JAVA"
print("PYTHON" in s)
print(s.index("PYTHON"))
print(s.find("PYTHON"))
print(s.find("python"))
print(s.rfind("PYTHON"))


s = "      ********This is sample string*******   "
s1 = s.strip(" ")
print(s1)
s1 = s.strip("*")
print(s1)


s = "python"
s1 = s.center(20,"*")
print(s1)

s = "python"
s1 = s.ljust(20,"*")
print(s1)

s = "html,css,python,html"
s1 = s.replace("html","HTML5")
print(s1)






















