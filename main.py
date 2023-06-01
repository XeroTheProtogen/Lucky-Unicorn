from start import start
from game_round import round_loop
from finish import finish_game

# Global variables & functions they are passed through
total_balance = start()
money_gained, total_balance = round_loop(total_balance)
finish_game(total_balance, money_gained)
