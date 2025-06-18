import random
set=['Rock', 'Paper', 'Scissor']
computer=random.choice(set)
while True:
 user=input('Rock,Paper, Scissor?')
 if user not in set:
     print('not valid choice')
 emojis={'Rock':'🪨', 'Paper':'📃', 'Scissor':'✂️'}
 print(f"user choice: {user}+{emojis[user]}")
 print(f"computer choice: {computer}+ {emojis[computer]}")

 if user == computer:
    print("Ties")
 elif ((user=="Rock" and computer=="Scissor")
      or (user=="Paper" and computer=="Rock") or
      (user=="Scissor" and computer=="Paper")):
    print("You win!")
 else:
    print("You lose!")

 should_continue=input("Would you like to play again? (y/n)")
 if should_continue == 'n':
  break


