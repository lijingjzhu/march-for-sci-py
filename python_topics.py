'''
Variable Assignment:
In Python, you can use triple quotes, like above,
or # pound signs to write comments: text that the computer doesn't
use to decide what it's going to do. 

We can use = signs to assign variables. 
That means we give them a name so that we can call them by name instead
of having to type them out again. 
'''

# Variable Assignment of common data types:

# Integer
x = 1

# Float
y = 2.34

# String
name = "Sam"
science = "JuLie$562 9183!!"

# List
pets = ["dog","cat","python"]

# Dictionary
test_grades = {"Alice": 98, "Catherine": 84, "Ahmad":10}

''' 
For loops:

These loops allow you to repeat tasks FOR either a range of values
or for elements in a set (like a list or dictionary).
Note that indentation is super particular in python! 
This code won't run unless you have proper formatting.
'''
for animal in pets:
  # Adding strings with a + joins them together
  # This allows us to see where we are in our loop
  print ("Currently dealing with the animal: " + animal)

  ''' 
  Conditional (if / elif / else):
  Allows you to write different behavior for different cases
  '''
  # Compare if two things are equivalent with the == sign
  if animal == "dog":
    print ( "Dogs are the best!" )
  elif animal == "cat":
    print ( "Cats are friendly and get a bad rap!" )
  else:
    print ( "Uhh...who brought a " +  animal + " in my house?" )

'''
Functions:
Functions allow us to reuse code for different inputs. 
In the example below, I made a function to count the number of dogs in
a list of animals.
'''
def how_many_dogs_are_in_this_list(animal_list):
  count = 0
  # Loop over each animal in the list
  for animal in animal_list:
    # Check to see if the animal is a dog
    if animal == "dog":
      # Add to our count variable each loop
      count += 1

  # After looping, print out the number of dogs
  if count == 1:
    print ("There is " + str(count) + " dog in this list!")
  else:
    print ("There are " + str(count) + " dogs in this list!")

## Code to run 
# Lists of animals
animal_list_1 = ["dog","DOG","cAt"]
animal_list_2 = ["cat","cat","@llig@tor"]
animal_list_3 = ["dog","","banana"]

# How many dogs!
# Notice the output for the first list. Is this correct? Hint: Yes. Why?
how_many_dogs_are_in_this_list(animal_list_1)
how_many_dogs_are_in_this_list(animal_list_2)
how_many_dogs_are_in_this_list(animal_list_3)
