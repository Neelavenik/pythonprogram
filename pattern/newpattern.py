n=input("enter a value:")#program
mid=len(n)//2
imp=n[mid:]+n[:mid]
print(imp)
for i in range(len(n)+1):
    print('\t'*(len(n)-i),imp[0:i])
