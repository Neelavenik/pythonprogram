n=int(input("enter a number"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
print(sum)
if sum==n:
    print("its a perfect number")
else:
    print("its not a perfect number")