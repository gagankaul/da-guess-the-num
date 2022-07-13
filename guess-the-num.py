#Guess the number App

from math import *

#Print welcome message
print("Welcome to Guess the Number App")
print("\nI will try to guess your number between a range that you provide.")
input("Press enter when you are ready! ")

state = True

while state == True:
  #Get user input to define the range
  lower = int(input("\nEnter the lower end of the range: "))
  upper = int(input("Enter the upper end of the range: "))
  print("\nI think I will be able to guess your number within " + str(round(log(upper, 2))) + " tries.")
  count = 0

  #Main program loop using binary sort
  for i in range(lower,upper):
      num = (lower+upper) // 2
      guess = input(f"\nIs your number: {num}? Press 'y' for yes, 'h' for too high or 'l' for too low: ")
      
      if ((guess != "h") and (guess != "l") and (guess != "y")):
          print("That's an invalid response. Please try again.")
      else:
          count += 1
          if guess == "h":
              upper = num
          elif guess == "l":
              lower = num
          else:
              print(f"\nYay! I guessed your number {num} in {count} tries. ")
              break

  choice = input("\nWould you like to play another game (y/n): ").lower().strip()
  if choice == "n":
    state = False