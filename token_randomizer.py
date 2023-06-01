import random as rand


def token_randomizer():
  """Generates a number, which is then used to 
     find the name of the generated token,
     before returning the name of the token & its value."""
  #Array containing token name & value
  tokens = [["unicorn", 5], ["zebra", 0.5], ["horse", 0.5], ["donkey", 0]]

  # Return a random number from 0 to last index of "tokens" list
  random = rand.randint(0, len(tokens) - 1)

  # Return both items in the 2d array
  return tokens[random][0], tokens[random][1]