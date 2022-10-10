# Built in Functions - type(),float(),str(),input(),list(),dict(),min(),max(),file()
# Variables - It store data in computer memory.A variable refers to a memory address in  which data is stored.

#Variables in Python

firstname = 'Ansh'
lastname = 'Pandey'
country = "India"
City = "Chandigarh"
age = 20
is_married = False
skills = ['Python' , 'C++' , 'Machine Learning' , 'C']
person_info = {
    'firstname':'Ansh',
    'lastname':'Pandey',
    'country':'India',
    'city':'Chandigarh'
} 


print('Hello,World!')  #The text Hello,World! is an argument
print('Hello',',','World','!') #it can take multiple arguments, four arguments have been passed
print(len('Hello,World!')) #it takes only one argument

#Printing the values stored in the variables

print('First name:', firstname)
print('First name Length :', len(firstname))
print('Last name :',lastname)
print('Last name length: ',len(lastname))
print('Country: ' , country)
print('City: ',City)
print('Age: ',age)
print('Married: ',is_married)
print('Skills: ',skills)
print('Person information: ', person_info)

#Declaring Multiple Variable in a Line
#Multiple variables can also be declared in one line:

from tempfile import _TemporaryFileWrapper


firstname , lastname , country , age , is_married = 'Ansh' , 'Pandey' , 'India',20,False

print(firstname , lastname , country, age, is_married)
print('First name: ',firstname)
print('Last name: ',lastname)
print('Country: ',country)
print('Age: ',age)
print('Married: ',is_married)


#Getting user input using the input() built_in function.

firstname = input('What is your name: ')
age = input('How old are you?: ')

print(firstname)
print(age)

# Data Types - Baiscally , Data types are actually classes and variables are instance(object) of these classes.
#It tells that the variable is of which type whether it is int , float , string, bool , list, etc.

#Different Python data types
#Lets declare variables with varioud data types

firstname  = 'Ansh'      #str
lastname = 'Pandey'      #str
country = 'India'        #str
city = 'Chandigarh'      #str
age = 20                 #int

#Printing out types  
print(type('Ansh'))                 #str
print(type(firstname))              #str
print(type(10))                     #int              
print(type(3.14))                   #float
print(type(1 + 1j))                 #complex
print(type(True))                   #bool
print(type([1,2,3,4]))              #list
print(type({'name':'Ansh','age':20,'is_married':20}))        #dict
print(type((1,2)))                            #tupple 
print(type(zip([1,2],[3,4])))               #set



# Casting - Converting one data type to another data type.
#Use int() , float() , str(),list,set.
#When we do arithmetic operations string numbers should be first converted to int or floar otherwise it will return an error.

#int to float
num_int = 10
print('num_int',num_int)           #10
num_float = float(num_int) 
print('num_float:',num_float)      #10.0

#float to int
gravity = 9.81
print(int(gravity))               #9

#int to str
num_int =10
print(num_int)                    #10
num_str = str(num_int)
print(num_str)                    #'10'

#String to float
num_str = '10.6'
print('num_int' , int(num_str))    #10
print('num_float',float(num_str))  #10.6

#string to list
firstname = 'Ansh'
print(firstname)                       #Ansh
first_name_to_list = list(firstname)
print(first_name_to_list)              #['A','n','s','h']
