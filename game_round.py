from token_randomizer import token_randomizer as token_rand
from time import sleep
from debug import force_range


def round_loop(start_bal):
  """Starts each round, and asks for the player"""
  money_spent = 0
  #Variable to calculate money gained
  money_gained = 0
  money_lost = 0
  #Loop condition
  loop = True
  #Replay condition
  first_round = True
  #Different possible answers to play_round
  yes = ["yes", "y", "yeah", "sure"]
  no = ["no", "n", "nope", "nah"]
  # Rounds happen here
  while loop:
    play_round = ""
    # If the player has spent more then 10 dollars or their balance is less then 1$, tell them & end loop.
    if money_spent >= 10 or start_bal < 1:
      if money_spent >= 10:
        print("""--------------------------
        You have spent the maximum amount of money allowed.
        --------------------------""")
      elif start_bal < 1:
        print("""--------------------------
        Insufficient funds to continue.
        --------------------------""")
      loop = False
      continue
    # Ask player if they would like to play another round
    if money_spent > 0 and money_spent <= 10 and not first_round:
      play_round = input("""--------------------------
      Would you like to play another round?
      --------------------------""").strip().lower()
    if play_round in yes or first_round:  
      money_betted = force_range("""--------------------------
      How much money would you like to bet?
      --------------------------""", 1, 10)
    # Ensure that the amount betted doesn't exceed $10, or that it plus money_spent doesn't exceed $10\
    if money_betted + money_spent > 10:
      valid = False
      print("""--------------------------
      Too high of a bet, you are only allowed to spend up to 10 dollars in total.
      --------------------------""")
      while not valid:
        money_betted = force_range("""--------------------------
        How much money would you like to bet?
        --------------------------""", 1, 10)
        if money_betted + money_spent > 10:
          print("""--------------------------
            Too high of a bet, you are only allowed to spend up to 10 dollars in total.
            --------------------------""")
        else:
          valid = True
    money_spent += money_betted
    if play_round in yes or first_round:
      start_bal -= money_betted
      # Generate token
      print("""--------------------------
      Generating token....
      --------------------------""")
      token, token_value = token_rand()
      print("""--------------------------
      Token Generation complete!
      --------------------------""")
      print("""--------------------------
      The token you won is...
      --------------------------""")
      sleep(3)
      if token == "unicorn":
        print("""--------------------------
        Congratulations, you won the Unicorn token,
        which means that you get 5 dollars!
        --------------------------""")
      elif token == "zebra":
        print("""--------------------------
        You won the Zebra token, which means you get 50 cents!
        --------------------------""")
      elif token == "horse":
        print("""--------------------------
        You won the Horse token, which means you get 50 cents!
        --------------------------""")
      elif token == "donkey":
        print("""--------------------------
        Sorry to say, but you got the donkey token, which means you don't win.
        But hey, there's always next time!
        --------------------------""")
      start_bal += money_gained
      money_gained += (token_value * money_betted)
      if money_gained + (token_value * money_betted) > money_lost:
        while money_lost > 0:
          money_lost -= 1
      first_round = False
    elif play_round in no or money_spent >= 10:
      loop = False
    else:
      print("""--------------------------
      That isn't an answer, please ask again
      --------------------------""")
      continue
    if play_round in yes:
      print(play_round + "is a yes")
    elif play_round in no:
      print(play_round + "is a no")
    else:
      print(play_round + "is not a yes, or a no")
  else:
    return start_bal, money_gained, money_lost
