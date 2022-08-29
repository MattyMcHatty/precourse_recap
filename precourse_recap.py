#This is a comment.

my_first_string = 'Hello There'
my_first_integer = 95
my_first_float = 3.14
my_first_boolean = False
my_first_list = ['red', 'blue', 'green']

def working_with_numbers():
    print(my_first_integer + my_first_float)
    print(my_first_integer * 45)
    print(my_first_float / 3)
    print(my_first_float - my_first_integer)

working_with_numbers()

print(my_first_string)
print(my_first_string + ' you lovely person!')
print(my_first_boolean)

if my_first_boolean == True:
    print('The Boolean is True!')
else:
    print('The Boolean is False')

for x in my_first_list:
    print(x)

while my_first_integer > 90:
    print(my_first_integer)
    my_first_integer -= 1
