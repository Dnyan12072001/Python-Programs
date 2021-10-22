import re


# \s - space

# [a-zA-Z] - char class a or b or c.... or z A or B or ... z
# [0-9] - digit class 0 or 1 ... or 9

# + - atleast one [a-z]+
# * - zero or more

# ^ - start string
# $ - end of string

# ? - optional

# [a-z]{2,4}


# pan no check

s = "ABCDE1234A"
r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
l = re.findall(r,s)
print(l)

# 10 digit mob no valid or not

s = "7835789009"
r = re.compile("[6-9][0-9]{9}")
l = re.findall(r,s)
print(l)


# dd-mm-yyyy
s = "12-05-2018"
r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l = re.findall(r,s)
print(l)


# re module groups

s = "12-05-2018"
r = re.compile("^([0-9]{2})-([0-9]{2})-([0-9]{4})$")

m = re.search(r,s)
if m:
	print(m.group())  # 1, 2 ,3 
else:
	print("pattern not found")

# [0-9] - \d
# [^0-9] - \D
# [a-zA-Z] - \w

# space \s

















