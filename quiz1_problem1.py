# write a Python program to find those numbers which are divisible by 7 and 5, between 1500 and 2700 (both included)
for i in range(1500,2701):

    if i%5==0 and i%7==0:

        print(i)


# problem 2
# write a program to count number of even and odd number from a series of number

series = [1,2,3,5,4,7,6,8,9]

even_count=0

odd_count=0

for i in series:

    if i%2==0:

        even_count+=1

    else:

        odd_count+=1

print(even_count, odd_count)
