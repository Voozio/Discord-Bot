import random

# Emojis
CACTUS = "🌵"
CAMEL = "🐪"
DESERT = "🏜️"
ORANGE_DIAMOND = "🔸"
THUMBS_UP = "👍"
THUMBS_DOWN = "👎"


class Poll:
    def __init__(self, context, poll_list):
        self.ctx = context
        self.owner = context.message.author
        self.initial_prompt = f"{self.ctx.author.mention} You seek opinions. React to the option you desire.\n"\
                              f"{CAMEL} - Yes/No Question (Why though?)\n"\
                              f"{DESERT}  - Multiple Choice"
        self.poll_type = None
        self.poll_number = self.get_poll_num(poll_list)
        self.question_prompt = ""
        self.question = ""
        self.options_prompt = ""
        self.options = []

    def get_poll_num(self, poll_list):
        poll_num = 1
        for poll in poll_list:
            if self.ctx.author == poll.owner:
                poll_num += 1

        return poll_num

    async def prompt_poll_type(self):
        message = await self.ctx.send(self.initial_prompt)
        await message.add_reaction(CAMEL)
        await message.add_reaction(DESERT)

    def get_poll_type(self, reaction):
        if reaction.emoji == CAMEL:
            self.question_prompt = f"{self.ctx.author.mention} You've chosen the majestic camel. Type in your question."
            self.options.append(THUMBS_UP)
            self.options.append(THUMBS_DOWN)
            self.poll_type = CAMEL
        elif reaction.emoji == DESERT:
            self.question_prompt = f"{self.ctx.author.mention} You've chosen the bountiful desert. " \
                                   f"Type in your question."
            self.options_prompt = "You will be prompted to react an emoji and pair it with an answer. Repeat this " \
                                  "as many times as you'd like. Please react your first emoji."
            self.poll_type = DESERT

    async def prompt_question(self):
        return await self.ctx.send(self.question_prompt)

    async def prompt_options(self):
        responses = [
            "A curious traveler, aren't you? ",
            "Great questions deserve great answers. ",
            "A difficult question to answer... ",
            "Why would you need to know such a thing? "
        ]
        return await self.ctx.send(f"{self.ctx.author.mention} " + random.choice(responses) + self.options_prompt)

    async def prompt_option_reaction(self):
        message = await self.ctx.send("React the next emoji you'd like to use or the orange diamond "
                                      "when you're finished.")
        await message.add_reaction(ORANGE_DIAMOND)
        return message

    async def prompt_option_message(self, reaction):
        await self.ctx.send(f"Enter a description for:  {reaction}")

    def add_option(self, reaction):
        self.options.append(reaction)

    def contains(self, reaction):
        for element in self.options:
            if reaction == element[0]:
                return True
        return False

    async def ask(self, current_ctx):
        if self.poll_type == CAMEL:
            message = await current_ctx.send(f"{self.ctx.author.mention} asks: {self.question}")
            for emoji in self.options:
                await message.add_reaction(emoji)
        elif self.poll_type == DESERT:
            m_string = f"{self.ctx.author.mention} asks: {self.question}"
            for element in self.options:
                m_string += f"\n{element[0].emoji} : {element[1].content}"
            m_string += "\nPlease select one."

            message = await current_ctx.send(m_string)
            for element in self.options:
                await message.add_reaction(element[0].emoji)
