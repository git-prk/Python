names  = ["chinmay","shirish","ram","satish"]
print(type(names))

info = ["chinmay","deshpande",40,45]

info  = {
    # property:value
    # key:value
    "first_name":"chinmay",
    "last_name":"deshpande",
    "age":40,
    "rollNo":45
}
print(info)
print(type(info))


# program 2
#          0           1        2      3
names = ["chinmay","shirish","rahul","raj"]
# retrive
print(names[0])

# update
# names[0] = "ram"
# print(names)

# # add 
# names.append("sarika")
# print(names)

# delete
# names.pop()
# names.pop(2)
# names.remove("chinmay")

# retrive , update, delete , add
print("chinmay"  in names)

#          0           1        2      3
names = ["chinmay","shirish","rahul","raj"]

# range()
for x in range(len(names)):
    print(x)
    print(names[x])

# without range()

for item in names:
    print(item)


student = {
    "first_name":"sarika",
    "last_name":"pansare",
    "age":23,
    "rollNo":45
}

# student
# retrive
print(student['first_name'])

#update
student['last_name'] = "dani" 
print(student)

# add
student['city'] = "pune"
print(student)
student['city'] = "nagpur"
print(student)

# del
student.pop("first_name")
student.popitem()