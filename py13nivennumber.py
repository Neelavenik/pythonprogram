
# niv=input("enter a number:")
#
# sum=0
# for i in niv:
#     sum=sum+int(i)
# if int(niv)%sum==0:
#     print("given number is harshad or niven number")
# else:
#     print("given number is not harshad or niven number")
#
niv=int(input("enter a number:"))
sum=0
num=niv
while niv!=0:
    r=niv%10
    sum=sum+r
    niv=niv//10
if num%sum==0:
    print("given number is harshad niven")
else:
    print("given number is not niven")
