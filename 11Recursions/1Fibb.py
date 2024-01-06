def fibb(number):
    if number==1:
        return 0
    elif number==2:
        return 1
    return fibb(number-1)+fibb(number-2)

print(fibb(10))


# wap to print n to 1 using recursion
def oneToN(n):
    if n==1:
        print(n)
        return n
    
    print(n)
    oneToN(n-1)


print(oneToN(5))