from discord.ext import commands
import asyncio
import random

BOT_PREFIX = "Arise! "
TOKEN = "MzUxMDc1NTMxODk2MjU4NTYy.XluEfA.86oDql-V6ULyhrRVYB2PVJCeOJo"

client = commands.Bot(command_prefix = BOT_PREFIX)


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
    elif "azir" in ctx.content.lower():
        responses = [
            "Did somebody say His name?",
            "Don't speak His name with your peasant mouth.",
            "SHURIMAAAAAAAAAAAAA!"
        ]
        await ctx.channel.send(random.choice(responses))

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
    return


@client.command()
async def quote(ctx):
    print(f"{ctx.message.author} invoked the quote command")
    return


client.run(TOKEN)
