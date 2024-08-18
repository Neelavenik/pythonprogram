# num=int(input("enter a number:"))
# sum=0
# prod=1
# temp=num
# while num!=0:
#     r=num%10
#     sum=sum+r
#     prod=prod*r
#     num=num//10
# if sum==prod:
#     print("given number is spy number")
# else:
#     print("given number is not a spy number")
num=input("enter a number:")
sum=0
prod=1
for i in num:
    sum=sum+int(i)
    prod=prod*int(i)
if sum==prod:
    print("given number is spy number")
else:
    print("given number is not a spy number")