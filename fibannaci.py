n=int(input("enter a number:"))
start=0
stop=1
sum=0
count=0
while count<n:
    print(sum)
    start=stop
    stop=sum
    sum=start+stop
    count+=1
