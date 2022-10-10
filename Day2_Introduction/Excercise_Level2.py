#1 Check the data type of all variables using type() build-in function

from cmath import pi


print(type(10))              #int
print(type(3.14))            #float
print(type('Ansh'))          #string
print(type(4 + 4j))          #complex
print(type(True))            #bool
print(type([1,2,3,4]))       #list
print(type({'name':'Ansh','age':20 , 'is_married':False}))  #dict
print(type((5,6)))                   #tuple
print(type(zip([5,6],[3,4])))        #zip


#2 Using the len() built-in function, find the length of first name
firstname = 'Ansh'
print(len(firstname))

#3 Compate the length of first name and last name
firstname = 'Ansh'
lastname = 'Pandey'
print(len(firstname))
print(len(lastname))


#4  Declare 5 as num_one and 4 as num_two
#i Add num_one and num_two and assign the value to a variable total
#ii Subtract num_two from num_one and assign the value to a variable diff
#iii Multiply num_two and num_one and assign the value to a variable product
#iv Divide num_one by num_two and assign the value to a variable division
# Calculate num_one to the power of num_two and assign the value to a variable exp
#vi Find floor division of num_one by num_two and assign the value to a variable floor_division

num_one = 5
num_two = 4

#i
total = (num_one + num_two)
print(total)

#ii
diff = (num_one - num_two)
print(diff)

#iii
product = (num_one * num_two)
print(product)

#iv 
division  =  (num_one / num_two)
print(division)

#v
remainder = (num_one % num_two)
print(remainder)

#vi 
exp = (num_one**num_two)
print(exp)

#vii
floor_division  = (num_one//num_two)
print(floor_division)

#5 The radius of a circle is 30 meters.
#i Calculate the area of a circle and assign the value to a variable name of area_of_circle
#ii Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#iii Take radius as user input and calculate the area.

radius = 30 

#i 
area_of_circle = 3.14 * 30 * 30
print(area_of_circle)

#ii
circum_of_circle = 2 * 3.14 * 30
print(circum_of_circle)

#iii
rad = float(input('Enter the radius: '))
area = 3.14 * rad **2
print(area)

#6 Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
firstname = input("Enter the First Name: ")
country  = input('Enter your Country: ')
age = input('Enter the age: ')

print('First name is ' , firstname)
print('Country is ',country)
print('The age is ',age)
