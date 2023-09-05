#!/usr/bin/env python
# coding: utf-8

# # Python Basics

# # Variables

# In[6]:


x = 22

print(x)


# In[7]:


type(x)


# In[8]:


y = "Mint Chocolate Chip"

print(y)


# In[9]:


type(y)


# In[13]:


y = "Chocolate"
Y = "Mint Chocolate Chip"


print(y)
print(Y)


# In[15]:


x,y,z = 4 , "apple", True


# In[16]:


print(x,y,z)


# In[18]:


x = y = z = "Nice"

print(x)


# In[23]:


#list
ice_cream = ["chocolate","Vanilla", "Rocky Road"]

print(ice_cream)

x,y,z = ice_cream

print(y)


# # Naming Variable

# In[27]:


# Camel Case

# Test variable case

testVariableCase = "Vanilla Swirl"


# In[26]:


# Pascal Case

# Test Variable Case

TestVariableCase = "Vanilla Swirl"


# In[25]:


# Snake Case

# Test Variable Case

test_variable_case = "Vanilla Swirl"


# In[ ]:


testvar = "Vanilla Swirl"
test_var = "Vanilla Swirl"
_test_var = "Vanilla Swirl"
testVar = "Vanilla Swirl"
TestVar = "Vanilla Swirl"
testvar2 = "Vanilla Swirl"


# In[30]:


# cant use

# 2testvar = "Vanilla Swirl"
# test-var = "Vanilla Swirl"
# test var = "Vanilla Swirl"
# test,var = "Vanilla Swirl"


# In[31]:


x = 'ice cream is my favorite' + "."

print(x)


# In[33]:


#  cant use
## x = 'ice cream is my favorite' + 2

## print(x)


# In[35]:


x = "ice cream"
y =" is"
z = " my favorite."

print(x+y+z)


# In[36]:


x = 1
y = 2
z = 3

print(x+y+z)


# # Data Types

# In[42]:


type(12)
type(-12 +23)


# In[43]:


type(-12 + 10.25)


# In[44]:


type(-12 + 3j)


# In[48]:


#Boolean

type(True)


# In[49]:


1 > 5


# In[51]:


1 == 1


# In[53]:


# Strings

'Single Quote'


# In[54]:


"Double Quote"


# In[62]:


"""
This is the multi line
quote triple quote.
"""


# In[63]:


multiline = """
This is the multi line
quote triple quote.
"""

print(multiline)


# In[64]:


type(multiline)


# In[65]:


a = "Hello World"


# In[73]:


print(a[0])


# In[66]:


print(a[:5])


# In[70]:


print(a[6])


# In[72]:


print(a[-1])


# In[74]:


print(a[2:5])


# In[75]:


a*3


# In[76]:


a + a


# In[81]:


#list

[1,2,3]

a = [1,2,3]
type(a)


# In[78]:


['Cookie Dough', 'Strawberry', ' Chocolate']


# In[79]:


['Vanilla', 3 , ['Scoops', 'Spoon'], True]


# In[83]:


#Manipulating List

ice_cream = ['Cookie Dough', 'Strawberry', ' Chocolate']
ice_cream.append('Salted Caramel')

ice_cream


# In[84]:


ice_cream[0] = 'Butter Pecan'


# In[85]:


ice_cream


# In[92]:


# Nested List

nested_list = ['Vanilla', 3 , ['Scoops', 'Spoon'], True]

nested_list[2][1]


# In[93]:


# Tuple

# it cannot be changed or modified after it created

tuple_scoops = (1,2,3,2,1)


# In[96]:


type(tuple_scoops)


# In[97]:


tuple_scoops[1]


# In[119]:


# sets

# cannot acces set through index

daily_pints = {1,2,3}


# In[116]:


type(daily_pints)


# In[118]:


print(daily_pints)


# In[110]:


daily_pints_logs = {1,2,32,4,5,7,44,33,44,5}
print(daily_pints_logs)


# In[113]:


wifes_daily_pints_logs = {1,2,4,5,55,4,33,69}


# In[114]:


print(daily_pints_logs | wifes_daily_pints_logs)


# In[120]:


print(daily_pints_logs & wifes_daily_pints_logs)


# In[121]:


print(daily_pints_logs - wifes_daily_pints_logs)


# In[122]:


print(daily_pints_logs ^ wifes_daily_pints_logs)


# In[123]:


#Dictionaries

# Key/ Value Pair

dict_cream = {'name': 'Alex', 'weekly intake': 5, 'favorite ice cream': ['MCC', 'Strawberry', 'Chocolate']}


# In[125]:


type(dict_cream)


# In[126]:


print(dict_cream)


# In[128]:


dict_cream.values()


# In[129]:


dict_cream.keys()


# In[130]:


dict_cream.items()


# In[140]:


dict_cream['favorite ice cream'][1]


# In[142]:


dict_cream['name'] = "Christian"

print(dict_cream)


# In[144]:


dict_cream.update({'name': 'Christian', 'weekly intake': 5, 'weight': 300})

print(dict_cream)

#update wont delete or replace the dict// it will just update 


# In[150]:


#delete

del dict_cream['weight']
print(dict_cream)


# # Comparison Operators

# In[1]:


10 == 10


# In[2]:


10 == 50


# In[3]:


10 != 50


# In[4]:


'Vanilla ' == "Chocolate"


# In[5]:


10 < 50


# In[6]:


10 <= 10


# # logical Operators

# In[8]:


(10 > 50) and (50 > 10)


# In[9]:


(70 > 50) and (50 > 10)


# In[10]:


(10 > 50) or (50 > 10)


# In[11]:


not(50 > 10)


# # Membership Operators

# In[12]:


ice_cream = "I love Chocolate ice cream"

'love' in ice_cream


# In[16]:


scoops = [1,2,3,4,5]

wanted_scoops = 8

2 in scoops


# In[14]:


6 not in scoops


# In[17]:


wanted_scoops in scoops


# # If - Elif-  Else Statemet 

# In[18]:


if 25 > 10:
    print("it worked!")


# In[23]:


if 25 < 10:
    print("it worked!")
elif 25 < 30:
    print('elif worked')
elif 25 < 32:
    print('elif 2 worked')
else:
    print("it did not worked")


# In[24]:


print('It Worked') if 10>30 else print ("it doesnot")


# In[27]:


# nested if

if 25 > 10:
    print("it worked!")
    if 10 > 5:
        print("nested if")
elif 25 < 30:
    print('elif 1 worked')
elif 25 < 32:
    print('elif 2 worked')
else:
    print("it did not worked")


# # for loop

# In[28]:


integers = [1,2,3,4,5]


# In[30]:


for number in integers:
    print(number)


# In[38]:


integers = [1,2,3,4,5]


# In[39]:


for i in integers:
    print(i+i)
    


# In[40]:


ice_cream_dict = {'name': 'Alex', 'weekely intake': 5, 'favorite ice creams': ['MCC', 'Chocolate']}


# In[41]:


ice_cream_dict


# In[48]:


for cream in ice_cream_dict.values():
    print(cream)


# In[49]:


for key, values in ice_cream_dict.items():
    print(key, '->','values')


# # Nested For Loops

# In[52]:


flavors = ['Vanilla', 'Chocolate', "MCC"]
toppings = ['Hot fudge', 'Marshmallows', 'Oreos']


# In[53]:


for one in flavors:
    for two in toppings:
        print(one, 'topped with', two)


# # while loop

# In[57]:


number = 0

while number < 5 :
    print(number)
    number = number + 1
    


# In[63]:


# using break to exit from the loop
number = 0

while number < 5 :
    print(number)
    if number == 3:
        break
    number = number + 1


# In[60]:


number = 0

while number < 5 :
    print(number)
    if number == 3:
        break
    number = number + 1
else:
    print("no longer less than 5")


# In[62]:


# using continue to stop the current loop at that point and run for next item 
# it stops working the code below the continue
number = 0

while number < 5 :
    number = number + 1
    if number == 3:
        continue
    print(number)
else:
    print("no longer less than 5")


# # Functions

# In[64]:


def function():
    print("My first Function")


# In[65]:


function()


# In[69]:


def func(a):
    print(a, "banana")


# In[70]:


func("apple")


# In[75]:


def num_square(num,power):
    print(num**power)


# In[77]:


num_square(5,3)


# In[82]:


#arbetary Argument

arg_tuple = (5,6,1,2)
def number_arg(*number):
    print(number[0]*number[1])
    


# In[85]:


number_arg(*arg_tuple)


# In[88]:


def num_square(number,power):
    print(number**power)


# In[91]:


num_square(power = 5,number = 3)


# In[99]:


#keyboard Argument

def number_kwarg(**number):
    print('My number is:' + number['integer'] + ' My other number:' + number['integer2'])
    


# In[100]:


number_kwarg(integer = '2309', integer2 = "1234")


# # converting Data Types

# In[102]:


num_int = 7

type(num_int)


# In[ ]:





# In[109]:


num_str ='7'

type(num_str)


# In[112]:


num_str_conv = int(num_str)

type(num_str_conv)


# In[115]:


num_sum = num_int + num_str_conv

print(num_sum)


# In[116]:


list_type = [1,2,3]

type(list_type)


# In[117]:


tuple(list_type)


# In[118]:


list_type = [1,2,3,3,4,5,6,1]

set(list_type)


# In[119]:


type(set(list_type))


# In[120]:


dict_type = {'name' : 'Alex', 'age': 28, 'hair': 'N/A'}


# In[121]:


type(dict_type)


# In[124]:


dict_type.items()


# In[125]:


dict_type.keys()


# In[126]:


dict_type.values()


# In[127]:


list(dict_type.keys())


# In[128]:


type(list(dict_type.keys()))


# In[131]:


long_str = "I like to Party"

list(long_str)


# # The End
