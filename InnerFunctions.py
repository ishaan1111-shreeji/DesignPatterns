def func():
    print("Parent Function")

    def func1():
        print("First Child Function")

    def func2():
        print("Second Child Function")

    func2()
    func1()
func()
print("*"*20,"Another_Example","*"*20)
def function(n):
    def function1():
        return "softvan"
    def function2():
        return "ssl"
    if n==1:
        return function1
    else:
        return function2
a=function(1)
b=function(2)
print(a())
print(a)
print(b())