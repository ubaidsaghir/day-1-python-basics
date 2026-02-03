dic = {
    1: "Ubaid",
    2: "Ahsan",
    344:"ali",
    56:"Hassan"
}
print(dic.values())
for key in dic.keys():
 print(f"the value corresponding to the key {key} is{dic[key]}")
print(dic.items())

name = "Ubaid"
for i in name:
    print(i)
    if(i =="b"):
        print("this is something special")
        
        
colors = ["Red","Green","Blue"]
for color in colors:
    print(color)
    for i in color:
        print(i)    
        
        
students = [
    {"name":"Ali","gpa":3.6},
    {"name":"Ahsan","gpa":3.8},
    {"name":"Umer","gpa":2.6},
    {"name":"Adeel","gpa":2.9},
    {"name":"hassan","gpa":3.4},
]

for student in students:
    if student["gpa"] > 3.0:
        print(student["name"])
        
        
students = [
    {"name":"Ubaid","marks":90},
    {"name":"Ali","marks":50},
    {"name":"Ahmad","marks":77},
    {"name":"Umer","marks":88},
    {"name":"Usman","marks":60},
]

for student in students:
    if student ["marks"] > 70:
        print(student["name"])
        
        
products = [
    
    {"name":"laptop", "price":70000,"quantity":5},
    {"name":"mouse", "price":4000,"quantity":10},
    {"name":"keyboard", "price":10000,"quantity":0},
]

for product in products:
    if product["price"] <50000:
        print(product["name"],"Out of Stock")
    else:
        print(product["name"],"In Stock") 
        
        
employees = [
    {"name":"ubaid","salary":20000},
    {"name":"umer","salary":40000},
    {"name":"usman","salary":50000},
    {"name":"Faizan","salary":60000},
]

for emp in employees:
    if emp ["salary"]> 50000:
     print(emp["name"])                           