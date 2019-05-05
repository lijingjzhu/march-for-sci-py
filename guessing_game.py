# Package for random number selection
import random 

# Pick the number to guess
n = random.randint(1, 99)

# Instructions for the guessing game
print ("Try to guess the number I am thinking about...")
guess = int(input("Enter an integer from 1 to 99: "))

while n != "guess":
  if guess < n:
    print ("Looks like that number is low...")
    guess = int(input("Enter an integer from 1 to 99: "))
  elif guess > n:
    print ("Too high! Chill the number down!")
    guess = int(input("Enter an integer from 1 to 99: "))
  else:
    print ("Spot on! That was an optimal guess.")
    break
