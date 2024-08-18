
+n=int(input("enter a number:"))
for i in range(n):
    for j in range(n-i):
        print(chr(64+n-j),end=" ")
    print()
# C B A
# C B
# C
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()
# 1
# 1 2
# 1 2 3
# for i in range(n):
#     for j in range(n-i):
#         print(n-j,end=" ")
#     print()
# 3 2 1
# 3 2
# 3
