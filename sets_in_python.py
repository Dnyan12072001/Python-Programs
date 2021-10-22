# sets
# sets are mutable
# only add immutable elements in the set : str , int , tuple , float
# unorderd

s = {10,20,30,40,40,50,20,50}
print(s,type(s))

r = {100,200,300,20,400,400,200,600}
r.add(600)
print(r)

f = s.union(r)
print(f)

h = s.intersection(r)
print(h)

t = s.difference(r)
print(t)

t2 = r.difference(s)
print(t2)

c = s.symmetric_difference(r)
print(c)

s.intersection_update(r)
print(s)

s.difference_update(r)
print(r)

s.symmetric_difference_update(r)
print(s)

print(s.issubset(r))
print(s.issuperset(r))

l = [100,200,300,400]
s = set(l)
print(s)

l = [100,200,300,400,400,500,6089]
h = [388,679,279,20495,59,739,4637]

s1 = set(l)
s2 = set(h)

s3 = s1.union(s2)
print(s3)

l3 = list(s3)
print(l3)

l3.sort()
print(l3)

# pop , remove , clear , discerd , del

s = {100,200,300,400}

r = s.pop()
print(r)

s.remove(100)
print(s)

s.clear()
print(s)








