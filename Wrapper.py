def function1(function):
    def wrapper():
        print("hello1")
        function()
        print("....welcome to python softvan tutorial")
    return wrapper
# def function2():
#     print("Innoventa")
# #     wrapp syntax
# function2=function1(function2)
# function2()
# Alternative of above using pi syntax
@function1
def function2():
    print("Innoventa")
function2()