#for small strings you can use quotes
mystring="hi from janmay"
print(mystring)

#addind two strings
ourstring='hello' + 'hi'
print(ourstring)

#making long string
parastring="""Namaste 
hello
hi"""
print(parastring)

#length of string
string='Python for the beginners'
print(len(string))

#making upper case and lower case
course='Python for the beginners'
print(course.upper())
print(course.lower())

#indexing element
my_string='Python for the beginners'
print(my_string.find('f'))
print(my_string.replace('for','course'))
#finding element in string
print('Python' in my_string)

#string formatting
first_name='Janmay'
last_name='Bhatt'
#message=first_name+' '+last_name+' is a businessman'
message=f'{first_name} {last_name} is a businessman'#f''is for formatting the string
print(message)