# python is from monty python


# in python shell {
# type in cmd: py   -- to enter shell
# type exit() -- to exit shell
# press ctrl+L -- to clear shell
# }

import datetime

# print( 'The datetime now is',datetime.datetime.now())

aNumber = 10
aText = "ten"
aFloat = 10.10

# print(type(aNumber), type(aText), type(aFloat))
# int,
# str,
# float


student_grades = [9.8, 8, 4.9]
# print(type(student_grades))
# type list

listTillTen = list(range(1, 11))
# print(listTillTen)


listTill25_skipping_4 = list(range(1, 26, 4))
# print(listTill25_skipping_4)

# print(dir(list))
# every function of the type list

# print(dir(__builtins__))
# every non-type-specific functions

# print(help(list.count))
# return the description of the function of type

# print(sum(student_grades) / len(student_grades))

# max_value = max(student_grades)
# print(max_value)

# print(student_grades.count(9.8))
# how many items equals to 9.8


# print("UPPERCASE LETtErs".lower())

students_grades = {"Sin": 6.6, "Saint": 9.8, "Joshua": 8}
# print(students_grades)
# type dict -- print all

# print(students_grades.values())
# print only the values, without the names

# print(students_grades.keys())
# print only the names, without the values

# print(students_grades.items())
# print the item pair (key and value) -- as tuples

# for s_g in students_grades.keys():
#      print(f"Student: {s_g}\n Grade: {students_grades[s_g]}")
# ----------------------------------------------------------------
# for key, value in students_grades.items():
#      print( f"The student {key} has a grade of {value}" )


final_grades = (9.4, 5, 8.8, 10)

# print(final_grades)
# type- tuple
# list like but you cant change/add/remove the values inside

# a = {"b": 'teste', "c": 'aac', "d": 45}
# a.d -- do not work
# use -- print(a["d"])

# methods in list
# .append(item) -- insert new item
# .remove(item) -- remove item from list
# .clear() -- remove all items from list
# .index(item)
# -- return the index of that item. ex: a = [2.3, 4.4, 9], a.index(4.4) --- will return 1
# index can have other two args, start and stop.
# start is useful to skip some items of the list. Ex.: a.index(4.4, 2) -- it will skip the 0 and 1 index items and start search on the third item
# stop will limit search to that index, ex.: a.index(4.4, 0, 2) -- it will search the item between the indexes 0 and 2
# a[2] -- get the third item of list called a
# a[2:4] -- get the items of index 2 and 3 ----
# a[:3] -- get all items before index 3 (0,1,2)
# a[3:] -- get all items of index 3 and after
# a[-1] -- get last item of list
# list[:-1] -- everything but the last
# list[:-2] -- everything but the last two
# a[-2:] -- get the last two items from list

# !!!! --  index methods also works with strings ex.: "Hello"[-1] returns o  --


# functions in python
def average_grade(grades):
    if type(grades) == dict:
         return sum(grades.values()) / len(grades)
    return sum(grades) / len(grades)

# if operators: and / or

# if the function doesnt have a return, it will always return a None

#instead of {}/(), for functions, ifs, etc, python uses identation for scopes

# to check type you can use:   isinstance(3, int) or isinstance(student_grades, dict)

# def check_password(password):
#     return len(password) >= 8
# print(check_password('password'))

def check_temperature(temperature):
    if temperature > 25:
        return "Hot"
    elif temperature < 15:
        return "Cold"
    return "Warm"

# print( check_temperature( float( input( "a number: " ) ) ) ) 
# input("Enter a number") 

#string formating

# username = input("What's your name? ")
# messageOldFormat = "Hello %s!" % username.title() // works in python < 3
# messageInPython3 = f"Hello {username.title()}!" // added in python 3

# print(messageOldFormat)
# print(messageInPython3)

# first_name = input("What's your first name? ")
# last_name = input("What's your last name? ")
# messageOldFormat = "Hello %s %s!" % (first_name.title(), last_name.title() )
# messageInPython3 = f"Hello {first_name.title()} {last_name.title()}!"
# print(messageOldFormat)
# print(messageInPython3)


def greet(person):
    return "Hi %s" % person.title()

# print(greet(input("whats your name")))

for grade in students_grades.values():
     round(grade)
     
# for letter in "Andrew":
#      print(letter)


# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# for n in phone_numbers.values():
#      print(n.replace("+", "00"))

# for i in range(10):
#      print(i)

usernames = [ "Andrew", "Sussu", "Cardoso", "Akz" ]
# username = ""
# while usernames.count(username) == 0:
#      username = input("Login\nUsername: ") 

# better way to do the code above

# while True:
#      username = input("Username: ")
#      if usernames.count(username) == 1:
#           print("The username already exists")
#           continue
#      break

# while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
#     print(datetime.datetime.now())
#     print("It's not yet 19:30:20 of 2090.8.20")


# temps = [203, 300, 243, 286]
# print(temps)
# print([temp / 10 for temp in temps])

temps = [203, 300, 243, 286, -9999, 457.9]
# print([temp / 10 for temp in temps if temp != -9999])

#list comprehension
def get_ints(items):
    return [item for item in items if isinstance(item, int)]
def get_values(items):
    return [item if isinstance(item, (int, float)) else 0 for item in items ]
def get_sum(lst):
    return sum( [ float( n ) for n in lst ] )
def join_str(a, b):
    return a+b
    #return "".join([a,b])
def as_many_args_as_needed(*args):
    # args is a tuple
    return sum(args)
# print(as_many_args_as_needed(3,4,6,3,5))

def default_arg_values(a = 4, b = 9): #default values
    return a+b
# print(default_arg_values(a = 9, b = 3)) # named arguments - position doest matter

def to_upper_sorted(*args):
    return sorted([ arg.upper() for arg in args ])
# print(to_upper_sorted("a", "c", "r", "ab", "z", "t", "e"))

def as_many_args_as_needed_dict(**kwargs):
    return kwargs
# print(as_many_args_as_needed_dict(a = 4, b = 6, c = [1,3,5]))

def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
# print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))

