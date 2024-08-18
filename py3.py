#string is also a data type .which allows us to store string based values . it is mutable  we can make changes for the string
v1="hello neelaveni"
print(str)
str1='''hello "world"'''
print(str1)
print(v1[0])
print(v1[1])

print(v1.index('h'))
print(v1.index('e'))
print(v1[-1])
v2=v1.replace('neelaveni','bhavya')
print(v2)
print(v1.upper())
print(v2.title())
v3="neelu"
print(v3.replace("neelu","thanu"))
v3='jaanu'
print(v3)
d="good morning folks"
print(d.split())

k=("-".join(d))
print(k)
for i in d:
    print(i)