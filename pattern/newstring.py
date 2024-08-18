inname=input("enter a string and value:")
name1=""
name2=""
for i in inname:

    if i.isalpha():
        name1=name1+i+" "
        name2=name2+" "
    else:
        name2=name2+i

x=name1.split()
y=name2.split()

print(x)
print(y)
for i in range(len(x)):
    print(x[i]*int(y[i]))