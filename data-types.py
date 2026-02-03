a = 50
b = 5
print("The value of",a,"+",5,'is',a+b)
print("The value of",a,"-",5,'is',a-b)
print("The value of",a,"*",5,'is',a*b)
print("The value of",a,"/",5,'is',a/b)

marks = [3,5,6,"Ubaid",True,6,7,2,32]
print(marks)
print(type(marks))
print(marks[len(marks)-2])

if 3 in marks:
    print("yes")
else:
    print("No")    
print(marks)
print(marks[1:-1])
print(marks[1:4:2])