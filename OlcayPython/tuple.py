# list = [1, 2 ,3]

# tuple = (1, "iki", 3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))


list = ["ali","veli"]
tuple = ("damla","ayşe")

list[0] = "ahmet"
#tuple[0] = "deniz"          #tuple a bir eleman atadıktan sonra onu bu şekilde değiştiremiyoruz.

print(tuple.count("ayşe"))
print(tuple.index("ayşe"))

print(list) 
print(tuple)

tuple = ("damla","ayşe")
names = ("demet","emel","ayşe") + tuple
print(names)