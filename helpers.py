import discord


def find_user(author, users, pat) -> discord.Member:
    pat = str(pat).lower()
    for u in users:
        if u.name.lower().startswith(pat):
            return u
        if pat.lower() in u.display_name.lower():
            return u
        if str(u.id) in pat:
            return u
    raise Exception('User Not Found')