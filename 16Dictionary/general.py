# WAP to take input from user Name and marks then display it on the screen
rec={}
n=5
i=1
while i<=n:
    name=input("Enter The Name: ")
    marks=input("Enter Marks")
    rec[name]=marks
    i=i+1

print(rec)