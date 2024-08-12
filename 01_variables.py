my_string_variable = 'My variable'
print (my_string_variable)

my_int_variable = 8
print (my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print (my_bool_variable)
'''
Python it's interpreter function
'''
# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print('Este es el valor de: ', my_bool_variable)

#some functions of system 
print(len(my_string_variable))

#Variables in one line. There is not recommended to use
name, surname, alias, age = 'Aldo', 'Casas', 'ACA', 23
print('Me llamo:', name, surname, 'Mi edad es:', age, 'y mi alias es:', alias, 'con edad de: ', age)

# Inputs
'''
name = input('what is your name? ')
age = input('how old are you? ')
print(name)
print(age)
'''

#change type
name = 123
age = 'aldo'
print(name)
print(age)