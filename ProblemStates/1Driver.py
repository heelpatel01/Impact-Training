# //A company insures its drivers in the following cases
# //1. If the driver is married
# //2. If the driver is unmarried, male and above 30 years of age
# //3. If the driver is unmarried, female and above 25 years of age
# //In all other cases, the driver is not insured.
# //If the marital status, sex, age of the driver are the inputs.
# //write a program to determine whether the driver is insured or not. (use ‘nested-if’).

a = str(input("Enter your marital status (Married/Unmarried): "))
b = str(input("Enter your sex (Male/Female): "))
c = int(input("Enter your age: "))
if a == 'Married':
    print("Driver is insured")
elif a == 'Unmarried' and b == 'Male' and c > 30:
    print("Driver is insured")
elif a == 'Unmarried' and b == 'Female' and c > 25:
    print("Driver is insured")
else:
    print("Driver is not insured")