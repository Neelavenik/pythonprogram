se={1,2,3,4,5,6,7,9,8,10,20}
print(se)
se1={2,4,5,6,7,8,9}
print(se1)
print(se is se1)
print(se.issuperset(se1))
print(se1.issubset((se)))
print(se.isdisjoint(se1))
print(se1.isdisjoint(se))
print(se.union(se1))#displays all the values from both sets except common values
print(se1.intersection(se)) #displays only common values from both sets
print(se.difference(se1))
print(se.symmetric_difference(se1))