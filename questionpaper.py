

# var='Mango is a sweet fruit'
# count=0
# for i in var:
#     if i not in 'aeiou':
#         print(i)
#         count=count+1
# print(count)
# x="Good morning son"
# y=x.split()
#
# for i in y:
#     k=i[-1::-1]
#
#     print(k,end=" ")
#13th
# d1={'Name':'suresh','age':21,'salary':20000,'location':'india'}
# d1['country']=d1.pop('location')
# print(d1)
#14th
# sampleDict={
#     "class":{
#         "student":{"name":"Mike","marks":{
#             "physics":70,
#             "history":80
#         }
#                    }
#     }
# }
#
# print(sampleDict["class"]["student"]["marks"]["history"])
#16th

# n=20
# ans=format(n,'b')
# print(ans)
#sum of prime numbers
# sum=0
# for i in range(2,20):
#     for j in range(2,i):
#        if ((i%j)==0):
#          break
#     else:
#       sum=sum+i
#
# print(sum)
#sum of natural numbers
# num=int(input("enter a number:"))
# sum=0
# if num<0:
#
#     print("enter a non negative number")
# elif num==0:
#     print("zero is not considered")
#
# else:
#     while num<=9:
#         sum=sum+num
#         num=int(input("enter a number"))
#     print(sum)
# sum=0
# for i in range (1,10):
#     sum=sum+i
# print(sum)

##15th.duck number
# n=input("enter a number:")
# if  str(n[0])!='0':
#     print("duck number")
# else:
#     print("not a duck number")




# n=str(input("enter a number:"))
# print('duck number' if n[0]!='0' else 'not a duck number')
#16...binary number for integer without using bin()
n=int(input("enter a number:"))
st=" "
while n!=0:
    r=n%2
    st=st+str(r)

    n=n//2
print(st[-1::-1])









