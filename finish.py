from time import sleep


def finish_game(balance, gained, lost):
  sleep(3)
  print("""--------------------------
  Thanks for playing Lucky Unicorn.
  --------------------------""")
  sleep(3)
  print(f"""--------------------------
  Your total balance is: ${balance:.2f}.
  --------------------------""")
  sleep(4)
  if not gained <= 0:
    print(f"""--------------------------
    You have {gained:.2f} more dollars then you originally had.
    --------------------------""")
  elif not lost <= 0:
    print(f"""--------------------------
    You lost a total of ${lost:.2f}.
    --------------------------""")
  sleep(4)
  print("""--------------------------
  See you later!
  --------------------------""")