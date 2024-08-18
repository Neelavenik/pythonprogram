# name=input("enter your name:")
# list=[]
# for i in name:
#     if i not in list:
#         list.append(i)
#
# print(list)
#1st sum of all natural numbers
sum=0
# for i in range(1,10):
#     print(i)
#     sum=sum+i
# print(sum)
# num=int(input("enter a number:"))
# if num==0:
#     print("please enter a non zero number")
# elif num<0:
#     print("please enter a non negative number")
# else:
#     while num<=9 and num!=0:
#         sum=sum+num
#         num=int(input("enter a number"))
#     print(sum)
#2.count of non-vowels from the given string
# var="Be the way you actually want to be"
# count=0
# for i in var:
#     if i in 'aeiouAEIOU':
#         continue
#     else:
#         print(i)
#         count+=1
# print(count)
#3.display numbers from -10 t0 -1
# for i in range(-10,0):
#     print(i)
# num=-10
# while num!=0:
#     print(num)
#     num=num+1
#4.. factorial of a number
# from math import *
# def factorial(num):
#     if num==1 or num==0:
#         return 1
#     else:
#       return ( num * factorial(num-1))
# print(factorial(5))
#5..program to display all prime numbers with in a range
# sum=0
# for i in range(2,20):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         sum=sum+i
# print(sum)
#7..sum of prime numbers in a given number
var=576874397
sum=0
while var!=0:
    r=var%10
    for j in range(2,r):
        if r%j==0:
            break
    else:
        sum=sum+r

    var=var//10
print(sum)


