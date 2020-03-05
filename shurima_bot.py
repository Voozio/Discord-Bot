from discord.ext import commands
import asyncio
import random
import poll_manager

BOT_PREFIX = "Arise! "
TOKEN = [token]

client = commands.Bot(command_prefix = BOT_PREFIX)
quote_list = [line for line in open("quotes.txt")]
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
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------------")


@client.event
async def on_message(ctx):
    if ctx.author.id == client.user.id:
        return
    elif ctx.content.startswith('!hello'):
        await ctx.channel.send(f"Hello {ctx.author.mention}")
    # elif "azir" in ctx.content.lower():
    #     responses = [
    #         "Did somebody say his name?",
    #         "Don't speak his name with your peasant mouth.",
    #         "SHURIMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"
    #     ]
    #     await ctx.channel.send(random.choice(responses))

    await client.process_commands(ctx)


# Commands
@client.command()
async def roll(ctx, num = 10):
    print(f"{ctx.message.author} invoked the roll command")
    if int(num) >= 1:
        await ctx.send(f"{ctx.author.mention} rolled a {random.randint(1, int(num))}")
    else:
        await ctx.send("Stop wasting my time and roll a number greater than 0...")


@client.command()
@commands.cooldown(1, 15)
async def lottery(ctx, wait_time = 60):
    print(f"{ctx.message.author} invoked the lottery command")
    if 0 > wait_time > 60:
        wait_time = 60

    users = [ctx.message.author]
    message = await ctx.send(f"{ctx.author.mention} started a lottery. React to this message to enter. "
                             f"Soon, a lucky soldier will be selected to fight in Azir's war. @here")

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
    print(f"{ctx.message.author} invoked the poll command")
    user_poll = poll_manager.Poll(ctx)

    await user_poll.prompt_poll_type()

    def check1(user_reaction, user):
        return user == ctx.message.author and (user_reaction.emoji == CAMEL or user_reaction.emoji == DESERT)

    try:
        poll_type_reaction, _ = await client.wait_for("reaction_add", check = check1, timeout = 60)
    except asyncio.TimeoutError:
        await ctx.send(f"{ctx.author.mention} You mustn't make me wait. Come back when you're ready.")
        return

    user_poll.get_poll_type(poll_type_reaction)

    await user_poll.prompt_question()

    def check2(m):
        return m.author == ctx.message.author

    try:
        question = await client.wait_for("message", check = check2, timeout=60)
    except asyncio.TimeoutError:
        await ctx.send(f"{ctx.author.mention} You mustn't make me wait. Come back when you're ready.")
        return
    else:
        if poll_type_reaction.emoji == CAMEL:
            user_poll.question = question.content
            await ctx.send(f"{ctx.author.mention} Simple, I like it. Well, you're all set. "
                           f"Use the \"polling\" command to interrogate friends and strangers alike.")
        else:
            await user_poll.prompt_options()

    # def check3(user_reaction, user):
    #     return user == ctx.message.author and user_reaction.emoji is not None

    # if poll_type_reaction.emoji == CAMEL:
    #     try:
    #         reaction_1, _ = await client.wait_for("reaction_add", check = check3, timeout = 60)
    #     except asyncio.TimeoutError:
    #         await ctx.send(f"{ctx.author.mention} You mustn't make me wait. Come back when you're ready.")
    #         return
    #     else:
    #         if reaction_1.emoji == ORANGE_DIAMOND:
    #             user_poll.add_option(THUMBS_UP)
    #             user_poll.add_option(THUMBS_DOWN)
    #         else:
    #             user_poll.add_option(reaction_1)
    #             try:
    #                 reaction_2, _ = await client.wait_for("reaction_add", check = check3, timeout = 60)
    #             except asyncio.TimeoutError:
    #                 await ctx.send(f"{ctx.author.mention} You mustn't make me wait. Come back when you're ready.")
    #                 return
    #             else:
    #                 if reaction_2.emoji == ORANGE_DIAMOND:
    #                     user_poll.add_option(THUMBS_UP)
    #                     user_poll.add_option(THUMBS_DOWN)
    #                 else:
    #                     user_poll.add_option(reaction_2)

    poll_list.append(user_poll)


@client.command()
async def polling(ctx):
    for p in poll_list:
        if ctx.message.author == p.owner:
            await p.ask()


@client.command()
async def prophecy(ctx):
    print(f"{ctx.message.author} invoked the prophecy command")
    await ctx.send(random.choice(quote_list))


client.run(TOKEN)
