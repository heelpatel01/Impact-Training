def palindrome(string):

    if string == string[::-1]:
        print("it's palindrome")
        return
    print("not palindrome")

palindrome("HKH")
    