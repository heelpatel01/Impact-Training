arr= [1,5,3,4,2]
tgt= 2
count=0
arr=sorted(arr)
for x in range(len(arr)):
    for i in range(len(arr)):
        if(arr[x]-arr[i]==tgt):
            count=count+1

print(count)