import discord


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
    if 'rock' in choice or 'r' == choice:
        return "Rock"
    if 'paper' in choice or 'p' == choice:
        return "Paper"
    if 'scissor' in choice or 's' == choice: # Scissor spelt singularly for better UX
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
    diff = abs(bot_choice - my_choice)
    if diff == 0:
        return "That's a tie!"
    if diff in [1, 3]:
        winner = max(bot_choice, my_choice)
    if diff in [2, 4]:
        winner = min(bot_choice, my_choice)
    if winner == my_choice:
        return "You won!"
    else:
        return "You lost \U0001F641"
