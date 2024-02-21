#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Control flow

# loops
    # for 
    # while 



#for i in range(5):
 #   print(" I Love Python!!!")


i = 0
while i < 6:
    print(" I Love Python!")
    i = i + 1

i = 0
while i < 6:
    i = i + 1
    print(" I Love Python!!")


i = 0
while i < 1:
    i = i + 1
    print(" I Love Python!!!")


#  for loop vs while loop 
#  controlled | uncontrolled
#  count known | based on condition


# # while loop


valid_input = False
while not valid_input:
    value = input("Enter a number !!")
    if value.isdigit():
        valid_input = True
        print(value)
    else:
        print("Enter the number in numeric form! Please")




valid_input = False

while not valid_input:
    value = input("Enter a number in numeric!!!")
    if value.isdigit():
        valid_input =  True
        print(value)
    else:
        print("Enter in NUmeric only")


# # break , continue,pass

# break

num_list = [1,2,3,4,5,6,7,8,9]
for i in num_list:
    if i ==4:
        break
    print(i)


#  continue
num_list = [1,2,3,4,5,6,7,8,9]
for i in num_list:
    if i ==4:
        continue
    print(i)

# pass

a = 100
if a < 300:
#     code is required
    pass