## Variable Assignment
# In Python, you can use triple quotes, like above, or # pound signs to write comments: text that the computer doesn't
# use to decide what it's going to do 

# We can use = signs to assign variables. That means that we give them a name so that we can call them by name instead
# of having to type them out again. 

# Integer
x = 1

# Float
y = 2.34

# String
name = "Sam"

# List
zoo = ["dog","cat","banana"]

# Dictionary
test_grades = {"Alice": 98, "Catherine": 84, "Ahmad":10}

# Briefly talk about indexing
  # How to obtain values from a list 
  # Indexing starts at 0
  # example of indexing: animals[1] = ['dog', 'cat', 'banana'] = 'cat'

# For loops
# We use double equals signs to test whether two variables are equal
# Note that indentation and spacing is super particular in python! This code won't run properly unless you clean up your code.
for animal in zoo:
  # Conditionals
  print ("Currently dealing with the animal: " + animal)
  if animal == "dog":
    print ( "Dogs are the best!" )
  elif animal == "cat":
    print ( "Cats are friendly and get a bad rap!" )
  else:
    print ( "Ummm......why is a " +  animal + " in the zoo?" )

# Functions
def how_many_dogs_are_in_this_list(animal_list):
  count = 0
  for animal in animal_list:
    if animal == "dog":
      count += 1
    if count == 1:
      print ("There is " + str(count) + " dog in this list!")
    else:
      print ("There are " + str(count) + " dogs in this list!")

# Lists of animals
animal_list_1 = ["dog","dog","cat"]
animal_list_2 = ["cat","cat","cat"]
animal_list_3 = ["dog","","banana"]

# How many doggies!
how_many_dogs_are_in_this_list(animal_list_1)
how_many_dogs_are_in_this_list(animal_list_2)
how_many_dogs_are_in_this_list(animal_list_3)
