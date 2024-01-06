d={}
while True:
       key=input('Enter a boy friend name:- ')
       value=input('Enter a Girl friend name:- ')
       d[key]=value
       choice=input('Do you Want to add more items? ')
       if choice=='n':
        break
print(d)
while True:
    key=input('Enter bf name to search his gf name:- ')
    value=d.get(key,'Single')
    print(f'Hey {key} your gf is {value} 😍😘🥰')
    choice=input('Do you Want to add more items?[yes/no] ')
    if choice=='no':
        break