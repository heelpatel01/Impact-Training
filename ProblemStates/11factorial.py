# wap to find factorial of given number using function

n= int(input("Enter Number"))
def fact(n):
    fact =1
    for x in range(2,n+1,1):
        fact=fact*x
    print(fact)

fact(n)

