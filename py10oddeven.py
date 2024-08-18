l1=[1,2,3,4,5,6,7]
# for i in l1:
#     if i%2==0:
#         print("its a even number:",i)
#     else:
#         print("its a odd number:",i)
i=0
while i<=len(l1)-1:
    if l1[i]%2==0:
        print("even number:",
              l1[i])
    else:
        print("odd number:",l1[i])
    i=i+1
