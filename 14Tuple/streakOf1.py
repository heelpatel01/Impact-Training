list=[1,0,1,1,1,0]

count=0
maxx=0

for index,value in enumerate(list):
    if(list[index]==1):
        count=count+1
        if(count>maxx):
            maxx=count+maxx
    else:
        count=0
print(maxx)
        
