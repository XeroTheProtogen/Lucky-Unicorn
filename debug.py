def force_float(msg):
  """Checks if the player has inputted a number, and if not,
     catches the ValueError given & instead asks for a valid number"""
  valid = False
  while not valid:
    try:
      number = float(input(msg))
      valid = True
    except ValueError:
      print("Please input a valid number")
  else:
    return number


def force_range(msg, min: float, max: float):
  """A modified version of the function 'force_float'.
  In addition to error catching, this function ensures the player inputs a number
  inbetween the variables min & max"""
  valid = False
  while not valid:
    try:
      numb = float(input(msg))
      if numb >= min and numb <= max:
        valid = True
      else:
        print(f"Number must be within the range of {min}-{max}.")
    except ValueError:
      print(f"Please input a valid number from {min}-{max}.")
  else:
    return numb


