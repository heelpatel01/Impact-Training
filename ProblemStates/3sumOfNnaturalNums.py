# Wap to find sum of natural numbers 
n = int(input("Enter your range: "))
summ = 0
counter = 1

while counter <= n:
    summ = summ + counter
    counter = counter + 1

print("Sum of natural numbers up to", n, "is:", summ)
