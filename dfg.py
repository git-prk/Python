
listA = ["chinmay","deshpande",24,55]

info  = {
    # property   # value 
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":24,
    "rollNo":55,
    "age":54
}

# retrive
# print(info['age'])

# update
# info['rollno'] = 66

# property exist
#print("rollNo" in info)

#print(info["age"])
# vehicle = {
#     "color":"blue",
#     "type":"sedane"
# }
# print(type(vehicle))
# # does not stores value by index
# #print(vehicle[0])

# names = ["chinmay","sarika","poorva","amit","amol"]
# print(len(names))
# print(len(vehicle))

# program 1

student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":55
}

for key in student:
    print(key)

for prop in student:
    print(prop,student[prop])


