
#def add(a,b):
#    return a+b

#add=lambda a,b:a+b
#print(add(2,3))

myList=[lambda a, b: a+b, lambda a, b: a*b]

print(myList[1](1,2))