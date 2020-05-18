from discord.ext import commands
import asyncio
import random
import helper
import poll_manager
import ultimate_bravery
import team_generator

BOT_PREFIX = ("Arise! ", "arise! ")
TOKEN = [token]

client = commands.Bot(command_prefix = BOT_PREFIX)
client.remove_command("help")
helper = helper.Helper()
team_gen = team_generator.Team()
quote_list = [line[:-1] for line in open("txt_files/quotes.txt")]
recent_quotes = [line[:-1] for line in open("txt_files/quotes_recent.txt")]
champion_list = [line[:-1] for line in open("txt_files/champions/champions.txt")]
poll_list = []

# Emojis
CACTUS = "🌵"
CAMEL = "🐪"
DESERT = "🏜️"
ORANGE_DIAMOND = "🔸"
THUMBS_UP = "👍"
THUMBS_DOWN = "👎"


# Events
@client.event
async def on_ready():
    print("------------")
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------------")


@client.event
async def on_message(ctx):
    if ctx.author.id == client.user.id:
        return
    # elif "azir" in ctx.content.lower():
    #     responses = [
    #         "Did somebody say his name?",
    #         "Don't speak his name with your peasant mouth.",
    #         "SHURIMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"
    #     ]
    #     await ctx.channel.send(random.choice(responses))

    await client.process_commands(ctx)


# no decimals
# Commands
@client.command()
async def roll(ctx, num = 10):
    print(f"{ctx.message.author} invoked the Roll command")
    if int(num) >= 1:
        await ctx.send(f"{ctx.author.mention} rolled a {random.randint(1, int(num))}")
    else:
        await ctx.send("Azir has no time for insolence. Roll a number greater than 0...")


@client.command()
@commands.cooldown(1, 15)
async def lottery(ctx, wait_time = 60):
    print(f"{ctx.message.author} invoked the Lottery command")
    if 0 > wait_time > 60:
        wait_time = 60

    users = []
    message = await ctx.send(f"{ctx.author.mention} started a lottery. React to this message to enter. "
                             f"Soon, a lucky soldier will be selected to fight in Azir's war.")

    await asyncio.sleep(wait_time)
    cache_message = await ctx.fetch_message(message.id)
    for reaction in cache_message.reactions:
        async for user in reaction.users():
            if user not in users:
                users.append(user)

    winner = random.choice(users)
    await ctx.send(f"{winner.mention} has won the lottery!")


@client.command()
async def poll(ctx):
    print(f"{ctx.message.author} invoked the Poll command")

    if ctx.message.channel.id != 693662780988850206:
        await ctx.send("This command can only be used in the polling creation text channel. Out of all people, "
                       "I thought you would've known...")
        return
    user_poll = poll_manager.Poll(ctx, poll_list)

    await user_poll.prompt_poll_type()

    def check1(user_reaction, user):
        return user == ctx.message.author and (user_reaction.emoji == CAMEL or user_reaction.emoji == DESERT)

    try:
        poll_type_reaction, _ = await client.wait_for("reaction_add", check = check1, timeout = 60)
    except asyncio.TimeoutError:
        await ctx.send(f"{ctx.author.mention} You mustn't make me wait. Come back when you're ready.")
        return

    user_poll.get_poll_type(poll_type_reaction)

    prompt_question_m = await user_poll.prompt_question()

    def check2(m):
        return m.author == ctx.message.author and not m.content.startswith("arise!", 0) \
               and m.channel == prompt_question_m.channel

    try:
        question = await client.wait_for("message", check = check2, timeout = 60)
    except asyncio.TimeoutError:
        await ctx.send(f"{ctx.author.mention} You mustn't make me wait. Come back when you're ready.")
        return
    else:
        user_poll.question = question.content
        if poll_type_reaction.emoji == CAMEL:
            await ctx.send("Well, you're all set. Use the \"polling\" command to ask away.\n")
            poll_list.append(user_poll)
            return
        else:
            prompt_options_m = await user_poll.prompt_options()

    def check3(user_reaction, user):
        return user == ctx.message.author and user_reaction.message.id == prompt_options_m.id

    while True:
        option = []
        try:
            reaction, _ = await client.wait_for("reaction_add", check = check3, timeout = 60)
        except asyncio.TimeoutError:
            await ctx.send(f"{ctx.author.mention} You mustn't make me wait. Come back when you're ready.")
            return
        else:
            if reaction.emoji == ORANGE_DIAMOND:
                await ctx.send("Well, you're all set. Use the \"polling\" command to ask away.\n")
                poll_list.append(user_poll)
                return
            elif user_poll.contains(reaction):
                await ctx.send("This emoji is already an option. Did you forget?")
                prompt_options_m = await user_poll.prompt_option_reaction()
                continue
            else:
                option.append(reaction)

        await user_poll.prompt_option_message(reaction)

        try:
            option_m = await client.wait_for("message", check = check2, timeout = 60)
        except asyncio.TimeoutError:
            await ctx.send(f"{ctx.author.mention} You mustn't make me wait. Come back when you're ready.")
            return
        else:
            option.append(option_m)

        user_poll.add_option(option)
        prompt_options_m = await user_poll.prompt_option_reaction()


@client.command()
async def polling(ctx, poll_number = 1):
    print(f"{ctx.message.author} invoked the Polling command")
    temp = 1
    for p in poll_list:
        if ctx.message.author == p.owner:
            if poll_number == temp:
                await p.ask(ctx)
                poll_list.remove(p)
                return
            else:
                temp += 1
    await ctx.send("You don't have that many polls. Can you even count?")


@client.command()
async def prophecy(ctx):
    print(f"{ctx.message.author} invoked the Prophecy command")

    repeated = True
    while repeated:
        quote = random.choice(quote_list)
        try:
            recent_quotes.index(quote)
        except ValueError:
            await ctx.send(quote)
            for i in range(len(recent_quotes) - 1):
                recent_quotes[i] = recent_quotes[i+1]
            recent_quotes[len(recent_quotes) - 1] = quote
            with open("txt_files/quotes_recent.txt", "w") as f:
                for line in recent_quotes:
                    f.write(f"{line}\n")
            repeated = False


@client.command()
async def ub(ctx, selection = 1):
    print(f"{ctx.message.author} invoked the Ultimate Bravery command")
    player = ultimate_bravery.UB(selection)
    await ctx.send(player.display(ctx))


@client.command()
async def team(ctx, group = 0):
    team_list = team_gen.generate_team(group)
    result = f"__**{team_list[0]}**__"
    for i in range(1, 6):
        result += f"\n{team_list[i]}"
    await ctx.send(result)


@client.command()
async def help(ctx, command = None):
    print(f"{ctx.message.author} invoked the Help command")
    if command is None:
        await ctx.send(helper.display_help())
    else:
        await ctx.send(helper.display_command(command))


client.run(TOKEN)
