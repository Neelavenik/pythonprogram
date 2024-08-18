val=input("enter a value:")
new_string=""
new_string1=""
for i in val:
    if i.isalpha():
        new_string=new_string+i+" "
        new_string1=new_string1+" "
    else:
        new_string1=new_string1+i
x=new_string1.split()
y=new_string.split()
for i in range(len(x)):
    print(y[i]*int(x[i]))
