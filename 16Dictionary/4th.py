'''
create a dictionary dynamically by taking user input 
'''
Dict={}
while True:
   key=input("enter THE key: ")
   value=input("enter the value: ")
   Dict[key]=value
   print(Dict)
   exit=input('Enter ''E'' for exiting the program: ').upper()
   if exit=='E':
    break
# print(Dict)