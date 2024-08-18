n= int(input("enter a number:"))
# for i in range(n):
#     for j in range(n):
#         print(j+1,end=" ")
#     print()
#1 2 3
# 1 2 3
# 1 2 3
# for i in range(n):
#     for j in range(n):
#         print((n-j),end=" ")
#     print()
# 3 2 1
# 3 2 1
# 3 2 1
# for i in range(n):
#     for j in range(n):
#         print(chr(65+j),end=" ")
#     print()
#
# A B C D
# A B C D
# A B C D
# A B C D
for i in range(n):
    for j in range(n):
        print(chr(64+(n-j)),end=" ")
    print()



