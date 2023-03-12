# The sceptix bot
A Discord bot made for The sceptix club, an open source club at SJEC.

## Video Demo: https://www.youtube.com/watch?v=o4vlN9eUMKQ
## Description:
    The sceptix bot is a minimalistic Discord bot built with the discord.py API that serves as a management tool for The sceptix club Discord server. It has funcationality for both the server moderators as well as the server users.

### Utility Commands:

    This set of commands deals with "utility functions". The prime example being the "!ping" command. It returns the latency of the bot in millisenconds. It is often used to check if the bot is live and functioning correctly. The second of utlity functions is the "!av" command. It simply returns the profile icon of the user provided (or yours if you don't provide any arguement). The best part is that it does not rely on Discord.py's user resolution. As I wanted the bot to identify a user simply by a subset of their username / nickname, I had to manually intervene and implement a function called "find_user()". All such "helper" functions are in an aptly named "helpers.py" file. The final of utilitiy commands implemented is "!joined". Like av, it relies on the find_user function. This command returns the join-date of a given user (ie, the date and time that particular user joined the server).

### Games:

    This section was arguably the hardest and best to build. It has implementations of many common games like "Rock Paper Scissors", as well as some commands that flip a coin, and choose between a given list of strings. The most interesting of all of these was "Rock Paper Scissors Spock Lizard". It is an extension to the standard world of RPS that introduces two new entities with their own set of matchings against the existing Rock, Paper, and Scissors. It was implemented with a mathematical approach as guided by [this](https://eduherminio.github.io/blog/rock-paper-scissors/) article.

### Moderation:

    In this final set of bot commands, functionality in regards to priviledged moderation was added to the bot. This includes a "!purge" command that by default deletes a 100 of the previous messages (that are not pinned) on a channel. "!kick" simply kicks the user. "!roleadd" and "!roleremove" adds a given role to all the non-bot members of the server, and removes a role from all the non-bot users of the server respectively. This is useful in cases where setting up for an event with a default role is required. "!rename" which allows the moderators to fix the server nickname of any given user. Last of all the most interesting commands in this section are "!kill" and "!revive". Kill serves as the middle ground between muting and kicking. Where-in the user is stripped-of of all roles and isolated to a designated channel where only the moderators can send messages. This helps moderate spam, resolve conflicts, and in some essence, punish a user for violating agreed-upon terms. Revive is the complementary function that undoes Kill and regains the user access to all other channels.