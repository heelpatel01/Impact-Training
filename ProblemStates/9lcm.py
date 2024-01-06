a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
max= a if a>b else b
while 1:
    if(max%a==0 and  max%b==0):
        print(max)
        break
    max=max+1