# l1=[1,2,3,4,5,6,7]
# for i,j in enumerate(l1):
#     print(f'{i} is index of:{j}')
# old_list=[11,22,[32,23,43],[54,64,76],'python','java','sql']
# new_list=[]
# for i in old_list:
#     if isinstance(i,list):
#         new_list.extend(i)
#     else:
#         new_list.append(i)
# print(new_list)
# l1=[12,22,31,42,54,19,20,39]
# print(list(map((lambda x:x+2),l1)))
# print(list(filter((lambda x:x%2),l1)))
l1=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# print(list(map((lambda y:y**2),(list(filter((lambda x: x%2==0 ),l1))))))
from functools import reduce
print(reduce((lambda x,y:x+y),l1))


