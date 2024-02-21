# Set in Python
# unhashable i.e can be changed , we can edit SETS
# empty set is a dictionary
# set is an unorderd collection * of unique object **
# duplicates are not allowed
# indexing cant be used to acce the elements inside a set


# Creating a set

s1 = {11,22,33,44}
print(s1)
print(type(s1))

# Properties of SETS

# s2 = {11,22,33,44,[11,22,33]}
# print(s2)


s3 = {11,22,33,44,'one','two'}
print(s3)


# s4 = {11,22,33,44,'one','two',{99,88,77}}
# print(s4)

#  comparing the sets with differnt orders

s1 = {11,22,33,44}
print(s1)
print(type(s1))
print(id(s1))


s2 = {22,33,44,11}
print(s2)
print(type(s2))


print(s1==s2)


list_num1 = [11,22,33,44]
list_num2 = [11,22,33,44]

print(list_num2 ==list_num1)
#  HW
#  chekc the ID of each set and compare
print (id(list_num1))
print (id(list_num1)==id(list_num2))
#print(2128612020608==2128612342080)
# 

s5 = {10}
print(s5)
print(type(s5))


s6 = {}
print(s6)
print(type(s6)) #empty set is a dictionary

t1 = (10,11,12)
print(type(t1))

t2 = (99,)
print(type(t2))



# INdexing is not there in SETS

s7 = {22,33,44,11,22,33,44,11,22,33,44,11}
s8 = {22,33,44,11}

print(s7)
print(s8)
# print(s8[0]) #'set' object is not subscriptable

# HW :  find the meaning of  : subscriptable

# accessing the elements in a SET
s8 = {22,33,44,11,22,33,44,11}
print(s8)


# using for loop

for i in s8:
  print(i)

# Doubts in dictionary Methods
# update

d1= {
  'sameer' : 75,
  'saket': 89
}


d1.update({'sanket': 99})
print(d1)


# setdefault
# setdefault : get()  +  update()

print(d1.setdefault('sameer'))
print(d1.setdefault('suraj'))
print(d1)