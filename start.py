from time import sleep
from debug import force_range


def start():
  """The beginning of Lucky Unicorn, gets player balance
  & prints out instructions for the game."""
  print("Lucky Unicorn Game.")
  sleep(3)
  # Too lazy to type question as argument, so I set a variable to it instead.
  question = """Please provide a starting balance. 
  Must be higher then or equal to 1 dollar, and lower then or equal to 10 dollars."""
  # Make the player input a number from 1-10
  balance = force_range(question, 1, 10)
  # Simply checks for a input from the keyboard
  playing_game = input("Press <enter> to begin.")
  read_instructions = input("Do you know the rules to Lucky Unicorn? Y/N").lower().strip()
  yes = ["yes", "y", "yeah"]
  no = ["no", "n", "nah"]
  loop = True
  
  while loop:
    if read_instructions not in yes and read_instructions not in no:
      print("\033[1;37;41mError, please try again")
      read_instructions = input("\033[0;37mDo you know the rules to Lucky Unicorn? Y/N").lower().strip()
      if read_instructions in yes or read_instructions in no:
        loop = False;
        break;
  if playing_game != None and read_instructions in no:
      # Print out instructions
      print("""\033[0;37m--------------------------
      \033[33mWelcome to the Lucky Unicorn Game!
      \033[37m--------------------------""")
      sleep(3)
      print("")
      print("""--------------------------
      The rules are simple: You will bet some of your money, then receive a token.
      --------------------------""")
      sleep(4)
      print("")
      print("""--------------------------
      The token you receive will add it's value, multiplied by your bet, to your balance.
      --------------------------""")
      sleep(3)
      print("")
      print("""--------------------------
      Here are the rewards:
      \033[37mDonkey - $0
      \033[36mHorse - $0.5
      \033[36mZebra - $0.5
      \033[35mUnicorn - $5
      \033[37m--------------------------""")
      sleep(5)
      print("")
      print("""--------------------------
      Now, let's begin!
      --------------------------""")
  elif read_instructions in yes:
      print("""\033[0;37m--------------------------
      Well then, let's get started!
      --------------------------""")
  # Returns the player's balance for later use.
  return balance
