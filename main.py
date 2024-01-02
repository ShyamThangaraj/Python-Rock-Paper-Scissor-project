import random
UserChoice = ""

def RPS(choice):
  Options = ["r", "p", "s"]
  RobotChoice = random.choice(Options)
  if UserChoice == RobotChoice:
    print("It's a tie!")
    Intro()
  elif UserChoice



def Intro():
  Global UserChoice
  while True:
    choice = input("Enter 'r' for rock, 'p' for paper, 's' scissor: ")
    choice = choice.lower()
    if choice == "r" or "p" or "s":
      break
    else:
      print("Wrong choice! Please input again!")
  RPS(choice)
  