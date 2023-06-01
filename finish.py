from time import sleep


def finish_game(balance, gained):
  sleep(3)
  print("""--------------------------
  Thanks for playing Lucky Unicorn.
  --------------------------""")
  sleep(3)
  print(f"""--------------------------
  Your total balance is: ${balance:.2f}.
  --------------------------""")
  sleep(4)
  if gained > 0:
    print(f"""--------------------------
    Congratulations, you won ${gained:.2f} total
    --------------------------""")
  elif gained < 0:
    print(f"""--------------------------
    Shame, you lost a total of ${gained * -1:.2f}
    --------------------------""")
  else:
    print("""--------------------------
    You somehow managed to not lose nor gain any money...
    I'm not sure if you're lucky or unlucky...
    --------------------------""")
  sleep(4)
  print("""--------------------------
  See you later!
  --------------------------""")