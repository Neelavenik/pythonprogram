#local variable is a variable that is defined within a function and used within that function only
# def call():
#     a=10
#     print(a)
# call()
#enclosing variable is a variable that is defined in a innerfunction and can be used in the outer function
# def outer():
#     b=20
#     def inner():
#         a=10
#         print(a)
#         print(b)
#     inner()
#     print(b)
# outer()
#global variable is a variable that is defined outside of the function and used anywhere.
a=10
print(a)
def outer():
    print(a)
    def inner():
        b=20
        print(b)
        print(a)
    inner()
    print(a)

outer()
print(a)


