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
  if playing_game != None:
    # Print out instructions
    print("""--------------------------
    Welcome to the Lucky Unicorn Game!
    --------------------------""")
    sleep(3)
    print("")
    print("""--------------------------
    You will need to pay one dollar before each round
    --------------------------""")
    sleep(2)
    print("")
    print("""--------------------------
    The rules are simple: You will receive a random token in each round, 
    and depending on the type of token, you will either win 5 dollars, 50 cents, or nothing.
    --------------------------""")
    sleep(5)
    print("")
    print("""--------------------------
    Here are the types of tokens you could get: 
    Unicorn - 5 dollars, Zebra - 50 cents, Horse - 50 cents, Donkey - 0 dollars.
    --------------------------""")
    sleep(3)
    print("")
    print("""--------------------------
    Before each round, you must bet some of your money. 
    Your winnings will be multiplied by how much money you bet.
    --------------------------""")
    sleep(5)
    print("")
    print("""--------------------------
    You may only keep playing if you still have money and haven't spent a total of 10 dollars on this game.
    --------------------------""")
    sleep(2)
    print("")
    print("""--------------------------
    Now, let's begin!
    --------------------------""")
  # Returns the player's balance for later use.
  return balance
