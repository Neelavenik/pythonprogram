# num=str(input("enter a number:"))
# rev=num[-1::-1]
# print(rev)
num=int(input("enter a number"))
rev=0

while num!=0:
    r=num%10
    rev=rev*10+r
    num=num//10
print("reverse of a number is:",rev)
