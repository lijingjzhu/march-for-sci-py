import random 

# Pick the number to guess
n = random.randint(1, 10)

# Instructions for the guessing game
print ("Try to guess the number I am thinking about...")
guess = int(input("Enter an integer from 1 to 10: "))

while n != guess:
  if guess < n:
    print ("Looks like that number is low...")
    guess = int(input("Enter an integer from 1 to 10: "))
  elif guess > n:
    print ("Too high! Chill the number down!")
    guess = int(input("Enter an integer from 1 to 10: "))
# Once the number is the same, we can quit out of the game
print ("Spot on! That was an optimal guess.")