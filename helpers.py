import discord
from datetime import timedelta, datetime


def find_user(author: discord.Member, users: list, pat: str) -> discord.Member:
    pat = str(pat).lower()
    for u in users:
        if u.name.lower().startswith(pat):
            return u
        if pat.lower() in u.display_name.lower():
            return u
        if str(u.id) in pat:
            return u
    raise Exception('User Not Found')


def get_rps(choice: str) -> str:
    choice = choice.lower().strip()
    if choice.startswith('r'):
        return "Rock"
    if choice.startswith('p'):
        return "Paper"
    if choice.startswith('s'):
        return "Scissors"
    raise Exception('Invalid Choice')


def play_rps(my_choice: str, bot_choice: str) -> str:
    if my_choice == "Rock" and bot_choice == "Scissors":
        return "You Won!"
    if my_choice == "Paper" and bot_choice == "Rock":
        return "You Won!"
    if my_choice == "Scissors" and bot_choice == "Paper":
        return "You Won!"
    if my_choice == bot_choice:
        return "That's a tie!"
    return "You lost \U0001F641"


def get_rpssl(choice: str) -> int:
    choice = choice.lower().strip()
    if choice.startswith('r'): return 0
    if choice.startswith('p'): return 1
    if choice.startswith('sc'): return 2
    if choice.startswith('sp'): return 3
    if choice.startswith('l'): return 4
    raise Exception('Invalid Choice')


def play_rpssl(my_choice: int, bot_choice: int) -> str:
    rpssl_inflection = {
        0: ["crushes", "crushes"],
        1: ["covers", "disproves"],
        2: ["cuts", "decapitates"],
        3: ["smashes", "vapourises"],
        4: ["poisons", "eats"],
    }

    choices = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]

    diff = abs(bot_choice - my_choice)

    if diff == 0: return "That's a tie!"
    if diff in [1, 3]: winner = max(bot_choice, my_choice)
    else: winner = min(bot_choice, my_choice)

    loser = my_choice + bot_choice - winner

    if winner == my_choice:
        position = "You won \U0001F38A"
    else:
        position = "You lost \U0001F641"

    if diff > 1: diff = diff % 2
    else: diff = diff - 1

    return f"{choices[winner]} {rpssl_inflection[winner][diff]} {choices[loser].lower()}. " + position