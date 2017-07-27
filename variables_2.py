# First scenario using variable
# f = "Mohan"
# print f

# def myFun():
#     f = "Nitin is learning"
#     print f

# myFun()
# print f


#  Second scenario using global variable
f = "123"
print f

def someFunc():
    global f
    print f
    f = "456"

someFunc()
print f