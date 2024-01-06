# # WAP to check whether the given string is palindrom or not

# name= "HKH"
# start=0
# end=len(name)

# if(name[start:end]==name[-1:-(end-1)]) 
#     print(True)
#     else
#     print(False)

name = "KAMAK"
start = 0
end = len(name)

if name[start:end] == name[::-1]:
    print(True)
else:
    print(False)
