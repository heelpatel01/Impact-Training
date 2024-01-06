'''
SETDEFAULT():-->
'''
d={
    1:'google',
    2:'amazon',
    3:'Facebook',
    4:'Intel',
    5:'Tesla'
}
print(d.setdefault(999,'anjali'))
print(d)
print(d.setdefault(99)) #if we not passing any value it will print none.
print(d)
print(d.setdefault(1))