list = [i*i for i in range (4)]
print(list)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

names = ["milo","Sarah","Bruno","Anastasia","Rosa"]
namewith_o = [item for item in names if "o" in item]
print(namewith_o)

names = ["milo","Sarah","Bruno","Anastasia","Rosa"]
namewith_o = [item for item in names if (len(item)>4)]
print(namewith_o)

list1 = [2,4,6,8,10,12]

for lst in list1:
    if lst > 10:
        print(lst) 

products = [
    
    {"name":"laptop", "price":70000,"quantity":5},
    {"name":"mouse", "price":4000,"quantity":10},
    {"name":"keyboard", "price":10000,"quantity":0},
]
