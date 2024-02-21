# loop 
print(1)
print(2)
print(3)
print(4)
print(5)


# for loop   # while loop

#range(startIndex,endIndex(not include),step)
for x in range(4):
    print(x)
    
for x in range(1,4):
    print(x)

for x in range(1,4):
    print("hello")
    
for x in range(1,11,2):
    print(x)
    
# 1 2 3 4 5 6 7 8 9 10

for x in range(2,21,2):
    print(x)

for x in range(3,31,3):
    print(x)

for x in range(50,4,-5):
    print(x)
    

# while loop 
# intialization 
#while(condition):
    #statement
    # increment / decrement


i1 = 1
while(i1 <= 3):
    print(i1)  # 1 # 2 # 3
    i1 = i1 + 1 # 2 # 3 # 4
    
    
i2 = 1
while(i2 <= 3):
    print("hello")  # "hello" # "hello" # "hello"
    i2 = i2 + 1  # 2 # 3 # 4