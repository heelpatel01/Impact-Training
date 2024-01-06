#==================LIST__MERGING=====================
a=[1,2,3,4,'Ganpati No Jay JayKar']
b=['ganpati bappa','moriya',5,6,7,8]
c=a+b
print('List Merging Method 1:- ',c)
c=[*a,*b]
print('List Merging Method 2:- ',c)
#=================TUPLE__MERGING=====================
a=(1,2,3,4,'Ganpati No Jay JayKar')
b=('ganpati bappa','moriya',5,6,7,8)
c=a+b
print('Tuple Merginng Method 1:- ',c)
c=(*a,*b)
print('Tuple Merging Method 2:- ',c)
#=================SET__MERGING========================
# ----------------1st.method⛔-----------------
# a={1,2,3,4,'Ganpati No Jay JayKar'}
# b={'ganpati bappa','moriya',5,6,7,8}
# c=a+b#concatination is not applicable in set.
# print(c)
a={1,2,3,4,'Ganpati No Jay JayKar'}
b={'ganpati bappa','moriya',5,6,7,8}
c={*a,*b}
print('Set Merging Method "1":- ',c)

#==============DICTIONARY__MERGING=====================
'''
1ST METHOD OF CONCATINATE NOT APPLICABLE
2ND METHOD OF MERGING IS NOT SUCCSESFULL
3RD METHOD IS INTRODUCING:-
'''

a={1:'HEEL',2:'PURV',3:'HARSH',4:'DEEP',5:'DARSH'}
b={6:'AVADH',7:'BABA',8:'DIPENDRA',9:'JAY'}
# C={A+B}
# print(C)
# c={*a,*b}# it will point to only keys
# print(c)# and will print only keys
#for printingg value we have to use double star**
c={**a,**b}
print(c) #perfect mering solution