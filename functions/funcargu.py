#positional arguments
# def call(x,y):
#     print(x)
#     print(y)
# call(10,20)
#keyword arguments
# def call(Name,Age,Salary):
#     print(Name)
#     print(Age)
#     print(Salary)
# name='neelu'
# age=25
# salary=30000
#
# call(Name=age,Age=salary,Salary=name)
#Default arguments
# def call(name='neelu',age=25,salary=20000):
#     print(name)
#     print(age)
#     print(salary)
# call()
#vla
def sum(*args):
    sum=0
    t1=args
    print(t1)
    for i in t1:
        sum=sum+i
    return sum
print(sum(1,2,3,4,5))