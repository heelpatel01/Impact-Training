num = int(input("Enter a number: "))

reversed_num = 0
m=num
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print(reversed_num == num )
print(f"Original Number: {num}")
print(f"Reversed Number: {reversed_num}")
