def niven(number):
    sum=0
    temp=number
    while number!=0:
        r=number%10
        sum=sum+r
        number=number//10
    if temp%sum==0:
        print("given number is niven")
    else:
        print("given number is not niven")
a=niven
# print(a(number=int(input("enter a number:"))))
a(number=int(input("enter a number:")))

