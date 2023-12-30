# WAP to read input and find its average
n= [int(x) for x in input().split(",")]
len=len(n)
sum=0

for i in n:
    sum=i+sum

avg= sum/len
print(avg)