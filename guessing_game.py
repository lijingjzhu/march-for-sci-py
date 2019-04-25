import random
n = random.randint(1, 99)
guess = int(input("Enter an integer from 1 to 99: "))

while n != "guess":
  print
  if guess < n:
    print ("Looks like that number is low...")
    guess = int(input("Enter an integer from 1 to 99: "))
  elif guess > n:
    print ("Too high! Chill the number down!")
    guess = int(input("Enter an integer from 1 to 99: "))
  else:
    print ("Spot on! That was an optimal guess.")
    break
  print