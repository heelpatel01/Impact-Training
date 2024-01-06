# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

n=int(input())
if n%2!=0 and 6<n<20:
    print("Weird")
elif 2<n<5 and n%2==0:
    print("Not Weird")
elif n>20 and n%2==0:
    print("Not Weird")
else:
    print("Weird")