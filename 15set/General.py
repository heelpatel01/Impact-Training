# creations of set in diff way
# creation of empty set
# s = {}
# print(s)
# print(type(s))

# way of creating empty set using set()
# s = set()
# print(s)
# print(type(s))

# # creation of set with multiple elements
# s = {23, 33, 43, 53, 63}
# print(s)
# print(type(s))


# creation of set with heterognous elements
# s = {23, 33, 43, 53, 63, 'surendra', 4.5, True}
# print(s)
# print(type(s))

# crations of set using set()
# craetion of set from list
# l = [23, 33, 43, 53, 63]
# s = set(l)
# print(s)
# print(type(s))

# craetion of set from tuple
# t = (23, 33, 43, 53, 63)
# s = set(t)
# print(s)
# print(type(s))

# creation of set from range()
# s=set(range(10))
# print(s)
# print(type(s))

# creation of set from str
# name = "surendra kumar panda"
# s = set(name)
# print(s)
# print(type(s))


# name = "surendra kumar panda"
# s = set(name.split())
# print(s)
# print(type(s))


# s = set("surendra kumar panda")
# print(s)
# print(type(s))

# s = {23, 33, 43, 53, 63}
# print(s[2])
# print(s[::])

# in and not in

# s = {23, 33, 'surendra', 'rahul', 43, 53, 63}
# print('surendra' in s)
# print('priyanka' in s)
# print('surendra' not in s)
# print('priyanka' not in s)



# Set comprehensions
# without set comprehensions

# create a set from list
# l = [23, 33, 43, 53, 63]
# s = set()

# for i in l:
#     s.add(i)

# print(s)

# with set comprehensions
# create a set from list

# l = [23, 33, 43, 53, 63]

# s = {i for i in l}
# print(s)


# ex

# l = [23, 33, 43, 53, 63]

# s = {i*2 for i in l}
# print(s)


# work with range


# s = {i for i in range(100, 111)}
# print(s)


# s = {i**2 for i in range(11)}
# print(s)


# craete a set by adding all the elemenet from 20 to 40 which is divisible by 4

# s = {i for i in range(20, 41) if i % 4 == 0}
# print(s)


# create a set from list called as names by adding the first char of each element
# names = ['surendra', 'priyanka', 'rahul', 'zini']

# s = {i[0] for i in names}
# print(s)


# names = ['surendra', 'priyanka', 'rahul', 'zini']

# s = {i[0].upper() for i in names}
# print(s)


# craete a set from a list (names) by adding all the elements but if the elmenet is priyanka then instread of priyanka add anjali

# names = ['surendra', 'priyanka', 'rahul', 'zini']

# s = {i if i != 'priyanka' else 'anjali' for i in names}
# print(s)


a= {10,20,30}
b={40,50,60}
print(a&b)