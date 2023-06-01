from token_randomizer import token_randomizer as token_rand
from time import sleep
from debug import force_range


def round_loop(start_bal: float):
  """Starts each round, and asks for the player"""
  #Variable to calculate money gained
  money_gained = 0
  #Variable to check the total amount of money that has been betted
  money_betted = 0
  #Loop condition
  loop = True
  while loop:
    if money_betted > 10:
      loop = False
      print("""--------------------------
      You've betted the maximum amount of money, time to see your winnings
      --------------------------""")
      continue
    # Ask player for their bet
    betting_amount = request_bet(money_betted, start_bal)
    # Update money gained, balance, and amount betted
    money_gained -= betting_amount
    start_bal -= betting_amount
    money_betted += betting_amount
    # Generate a reward
    reward = reward_player(betting_amount)
    # Update money gained & balance
    money_gained += reward
    start_bal += reward
    # Ask player if they want to continue playing
    loop = continue_game()
  else:
    return money_gained, start_bal


def reward_player(money_bet: float) -> float:
  # Generate Token
  print("""--------------------------
  Generating Token...
  --------------------------""")
  # Start token generation
  token, token_value = token_rand()
  print("""--------------------------
  Token Generation complete!
  --------------------------""")
  print("""--------------------------
  The token you won is...
  --------------------------""")
  sleep(3)
  # Provide feedback
  if token == "unicorn":
    print(f"""--------------------------
    Congratulations, you won the Unicorn token, which means that you get ${token_value * money_bet:.2f}!
    --------------------------""")
  elif token == "horse":
    print(f"""--------------------------
    You won the Horse token, which means you get ${token_value * money_bet:.2f}!
    --------------------------""")
  elif token == "zebra":
    print(f"""--------------------------
    You won the Zebra token, which means you get ${token_value * money_bet:.2f}!
    --------------------------""")
  elif token == "donkey":
    print("""--------------------------
    Sorry to say, but you got the donkey token, which means you don't win.
    But hey, there's always next time!
    --------------------------""")
  # Return the money won
  return token_value * money_bet


def request_bet(money_spent: float, balance: float) -> float:
  loop = True
  while loop:
    # Ask player how much money they want to bet
    betting_amount = force_range("""--------------------------
    How much would you like to bet?
    --------------------------""", 1, 10)
    # If the player bets more then $10, or more then the total amount of money spent,
    # ask for a lower bet
    if balance < betting_amount or betting_amount > (10 - money_spent):
      print("""--------------------------
      Too high of a bet, please try again.
      --------------------------""")
      continue
    # If the player bets less then $1, ask for a higher bet
    elif betting_amount < 1:
      print("""--------------------------
      Too low of a bet, please try again
      --------------------------""")
    else:
      loop = False
  return betting_amount


def continue_game() -> bool:
  #Lists of possible responses
  yes = ["yes", "yeah", "y"]
  no = ["no", "nah", "n"]
  loop = True
  while loop:
    # Ask player if they would like to continue playing
    response = input("""--------------------------
    would you like to play another round? Y/N
    --------------------------""").lower().strip()
    # If yes, continue playing the game
    if response in yes:
      loop = False
      return True
    # Else if no, stop playing
    elif response in no:
      loop = False
      return False
    # If response matches none of the possible responses, ask again
    else:
      print("""--------------------------
      That isn't an answer, please try again.
      --------------------------""")
