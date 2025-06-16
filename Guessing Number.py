import random
guess_number=random.randint(1,100)
while True:
 try:
  guess = int(input("Guess a number between 1 and 100: "))
  if guess<guess_number:
     print("Guess is too low")
  elif guess>guess_number:
   print("Guess is too high")
  else:
    print("Guess is correct")
    break
 except ValueError:
  print("Sorry, that's not a number")