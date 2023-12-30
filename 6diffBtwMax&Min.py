# wap to read n float values and find the diffrence between highest and lowest element
n=[float(x) for x in input().split(",")]
minn=min(n)
maxx=max(n)
print(maxx-minn)
