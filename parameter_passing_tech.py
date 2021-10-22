#1 Position arguments
#2 Default argument
#3 keyword argument
#4 variable length positional args
#5 varibale length keyword args   


# LINEAR SEARCH :

def linear_search(l,key):
	for value in l:
		if value == key:
			return True
	else:
	    	return False


l = [100,200,300,400,500]
key = 400
result = linear_search(l,key)
print(result)



# password gen

import random
def gen_password():
	l = ['@','#','$','&']

	upper = chr(random.randint(65,90))
	lower = chr(random.randint(97,122))
	special = random.choice(l)
	digit = random.randint(10000,99999)
	password = upper + lower + special + str(digit)
	return password

result = gen_password()
print(result)


def gen_password(length = 8):
	l = ['@','#','$','&']

	upper = chr(random.randint(65,90))
	lower = chr(random.randint(97,122))
	special = random.choice(l)
	digit = random.randint(10000,99999)
	password = upper + lower + special + str(digit)
	l = random.sample(password,length)
	password = ("").join(l)
	return password

result = gen_password(5)
print(result)


# keyword argument

def validate(username,password):
	if username == "ABC" and password == "Abc@123":
		print("Valid password")
	else:
		print("invalid password")

validate("ABC","Abc@123")
validate(password = "Abc@123",username="ABC")

help(print)
print(100,200,sep=",",end=" ")
print("HIs")

#4 variable length argument in py

def add_value(*args):
	l = []
	for value in args:
		l.append(value)

	return l

result = add_value(100,200,300,400,500)
print(result)
result = add_value(100,200,300,400,500,39904,435363,6,54546)
print(result)


#5 
def get_details(**l):
	print(l)

get_details(name="Gaurav",email = "gaurav@gmail.com",mob_no= 7875239235,dob = "12-07-2001")

get_details(name="Gaurav",email = "gaurav@gmail.com",mob_no= 7875239235)

get_details(name="Gaurav",mob_no= 7875239235)

















































































