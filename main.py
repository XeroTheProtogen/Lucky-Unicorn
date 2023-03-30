from start import start
from game_round import round_loop
from finish import finish_game

# Global variables & functions they are passed through
total_balance = start()
total_balance, money_gained, money_lost = round_loop(total_balance)
finish_game(total_balance, money_gained, money_lost)

