import random

# Emojis
CACTUS = "🌵"
CAMEL = "🐪"
DESERT = "🏜️"
ORANGE_DIAMOND = "🔸"
THUMBS_UP = "👍"
THUMBS_DOWN = "👎"


class Poll:
    def __init__(self, context):
        self.ctx = context
        self.owner = context.message.author
        self.initial_prompt = f"{self.ctx.author.mention} You seek opinions. React to the option you desire.\n"\
                              f"{CAMEL} - Yes/No Question\n"\
                              f"{DESERT}  - Multiple Choice (Coming Soon)"
        self.question_prompt = ""
        self.question = ""
        self.options_prompt = ""
        self.reaction_options = []

    async def prompt_poll_type(self):
        message = await self.ctx.send(self.initial_prompt)
        await message.add_reaction(CAMEL)
        await message.add_reaction(DESERT)

    def get_poll_type(self, reaction):
        if reaction.emoji == CAMEL:
            self.question_prompt = f"{self.ctx.author.mention} You've chosen the majestic camel. Type in your question."
            self.reaction_options.append(THUMBS_UP)
            self.reaction_options.append(THUMBS_DOWN)
        elif reaction.emoji == DESERT:
            self.question_prompt = f"{self.ctx.author.mention} You've chosen the bountiful desert. " \
                                   f"Please type in your question."
            self.options_prompt = "React to this message with the emojis you'd like to use."

    async def prompt_question(self):
        await self.ctx.send(self.question_prompt)

    async def prompt_options(self):
        responses = [
            "A curious traveler, aren't you? ",
            "Great questions deserve great answers. ",
            "A difficult question to answer... ",
            "Why would you need to know such a thing? "
        ]
        message = await self.ctx.send(f"{self.ctx.author.mention} " + random.choice(responses) + self.options_prompt)
        await message.add_reaction(ORANGE_DIAMOND)

    def add_option(self, reaction):
        self.reaction_options.append(reaction)

    async def ask(self):
        message = await self.ctx.send(f"{self.ctx.author.mention} asks: " + self.question)
        for emoji in self.reaction_options:
            await message.add_reaction(emoji)
