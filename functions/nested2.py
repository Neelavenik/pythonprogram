def Takeout(num1,num2):
    print("number",num1)
    print("number",num2)
    return num1,num2
# print(Takeout(num1=int(input("enter a number:")),num2=int(input("enter a number:"))))
v1,v2=Takeout(2,3)
print("number is:",v1)
print("number is:",v2)
#types of arguments
#positional: the arguments we passed while calling functons will be assigned based on the positions
#keyword:the arguments we pass at the time of calling function will be done by using parameters
#default:defining arguments at the time of defining parameters of a function
#variable length:passing multiple arguments at a time based on the requirement when we dont know the required number of
#arguments need to be passed prior