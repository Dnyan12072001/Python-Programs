# dist

d = {"Name" : "gaurav", "email_id": 12345666}
print(d)

d["contact_no"] = 12345678
print(d)

# get
# setdefault

print(d.get("Name"))
print(d.setdefault("email_id"))


for x in d:
	print(x)


d = {}
for value in range(1,11):
    d[value] = value * value
print(d)


a = [1,2,3,4,5]
b = [1,4,9,16,25]

c = dict(zip(a,b))
print(c)

d = dict.fromkeys(a)
print(d)

g = {1:8, 2:3, 3:4}
h = {5:5,6:7, 9:0,3:6}
g.update(h)
print(g)

# pop, popitem , clear , del

f = g.pop(2)
print(g)

















