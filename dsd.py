students  = [
    {
        "firstName":"chinmay",
        "lastName":"deshpande",
        "age":19,
        "vehicle":True
    },
    {
        "firstName":"sarika",
        "lastName":"pansare",
        "age":4,
        "vehicle":True
    },
    {
        "firstName":"pranali",
        "lastName":"pansare",
        "age":19,
        "vehicle":False

    },

    {
        "firstName":"tavish",
        "lastName":"anade",
        "age":39,
        "vehicle":True
    }

]

#q4 = [ x['firstName'+": can drive"] if x['age'] > 18 and x['vehicle'] else 'firstName'+": cant drive"] for x in students]
#print(q4)

q4 = {x['firstName']: "can drive" if x['age'] > 18 and x['vehicle'] else "can't drive" for x in students}
print(q4)


#["chinmay":'candrive',"sarika":"cannot drive","pranali":"cannot","tavish":"candrive"]