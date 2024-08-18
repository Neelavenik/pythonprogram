#for loop is used t iterate values and displays the iterables of all  data types
var="Hello my world:"
# for i in var:
#     if i not in "a,e,i,o,u":
#         print(i)
#while loop is used to execue the output till the condition is true . once the condition becomes false the loop terminates
i=0
while i<=len(var)-1:
    if var[i] not in "a,e,i,o,u":
        print(var[i])

    i=i+1
