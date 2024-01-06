'''
🙋‍♂️ Program to find out the number of occurrences of a char present in a string
'''
# choice=input('If You Want To Count Upper And Lower both Character So Enter UL, and if upper than enter U and For Lower L.')
# if choice=='UL':
#     print(Name)
# elif choice=='U':
#     print(Name1)
# else:
#     print(Name2)


'''Name1=input('Enter Any Thing That you Want to check which character is present how many times:- \n').upper()
Name2=input('Enter Any Thing That you Want to check which character is present how many times:- \n').lower()'''
#===============================================
Name=input('Enter Any Thing That you Want to check which character is present how many times:- \n')
d={}
for i in Name:
    d[i]=d.get(i,0)+1
print(d)
for i,j in d.items():
    print(f'{i} Is Present {j} times')