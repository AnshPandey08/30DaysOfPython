#1 Declare your age as integer variable
age = 20
print(age)

#2 Declare your height as a float variable
height = 175.5
print('height')

#3 Declare a variable that store a complex number
complex_number = 4 +4j
print(complex_number)

#4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#base = float(input('Enter the base of triangle: '))
#height = float(input('Enter the height of triangle: '))
#Calc_triangle = 0.5 *base * height
#print(Calc_triangle)

#5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = 5
b = 4
c = 3
perimeter_of_triangle = (a+b+c)
print(perimeter_of_triangle)

#6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
#length =int(input('Enter the length of rectangele: '))
#breadth = int(input('Enter the breadth of rectangle: '))
#area_of_rectangle = 2 * length * breadth
#print(area_of_rectangle)

#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') == len('dragon'))

#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on in Python','on' in 'Python')
print('on in dragon','on' in 'dragon')

#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('i Hope this course is not full of jargon','jargon' in 'I hope this course is not full of jargon')

#21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#hours = int(input('Enter the hours:'))
#rate_per_hour = int(input('Enter the rate per hour: '))
#weekly_earning = hours * rate_per_hour
#print(weekly_earning)

#15 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years_lived = int(input('Enter number of years you have lived : '))
seconds = int(years_lived * (365*24*60*60))
print('you have lived for ',seconds ,'seconds')