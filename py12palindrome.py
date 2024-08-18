# num=int(input("enter a number:"))
# rev=0
# temp=num
# while num!=0:
#     r=num%10
#     rev=rev*10+r
#     num=num//10
# if rev==temp:
#     print(temp,"is a palindrome")
# else:
#     print(temp,'is not a palindrome')
# var=input("enter a value:")
# rev=var[-1::-1]
# if var==rev:
#     print("entered value is palindrome")
# else:
#     print("entered value is not palindrome")

value=input("enter a value:")
rev=0
temp=value
if type(value)==int:
    while value!=0:
        r=value%10
        rev=rev*10+r
        value=value//10
    if rev==temp:
        print("palindrome")
    else:
        print("not a plaindrome")
elif type(value)==str:
    srev=value[-1::-1]
    if srev==value:
        print("palindrome")
    else:
        print("not a palindrome")
