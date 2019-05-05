# Package for random number selection
import random 

# Parameters
min_number = random.randint(-5, 1)
max_number = random.randint(2, 78)

# Pick the number to guess
n = random.randint(min_number, max_number)

# Instructions for the guessing game
print ("Try to guess the number I am thinking about...")
guess = int(input("Enter an integer from " + str(min_number) + " to "+ str(max_number) + ": "))

while n != guess:
  if guess < n:
    print ("Looks like that number is low...")
    guess = int(input("Enter an integer from " + str(min_number) + " to "+ str(max_number) + ": "))
  elif guess > n:
    print ("Too high! Chill the number down!")
    guess = int(input("Enter an integer from " + str(min_number) + " to "+ str(max_number) + ": "))
# Once the number is the same, we can quit out of the game
print ("Spot on! That was an optimal guess.")
