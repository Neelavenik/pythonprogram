#list is also a data structure used to store sequence of values
#it is immutable data type
x=[10,20,30,"radha","krishna",20+10j,True]
print(x)
print(type(x))
x.append(40)#adds a single value at the end of the list
print(x)
print(x+[2,3,4])
x.extend([9,10,11])#adds multiple values at the end of the existing list
print(x)
y=x.copy()#makes a copy of the existing list
print(y)
y.remove(9)#removes value we passed
print(y)
print(x.count(10))
y.clear()
print(y)
del(y)
x.insert(3,"seetha")
print(x)
x.reverse()
print(x)
print(x)
x[0]="neelu"
print(x)
x.pop()
print(x)
x.pop(0)
print(x)

A=[1,3,10,4,16,4,18,9,20]
A.sort()
print(A)
A.sort(reverse=True)
print(A)
print(max(A))
print(min(A))
print(any(A))
print(all(A))
print(sum(A))