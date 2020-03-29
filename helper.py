class Helper:
    def __init__(self):
        self.commands = ["help",
                         "lottery",
                         "poll",
                         "polling",
                         "prophecy",
                         "roll",
                         "team",
                         "ub"]
        self.commands_full = ["help [command]",
                              "lottery [seconds]",
                              "poll",
                              "polling [poll number]",
                              "prophecy",
                              "roll [number]",
                              "team [type]",
                              "ub [role]"]
        self.command_dict = {}
        self.init_command_info()

    # noinspection PyMethodMayBeStatic
    def display_help(self):
        result = "Help has been requested?\n\n" \
                 "__**Syntax to Summon Me**__\n" \
                 "Arise! [command] [options (optional)]\n\n" \
                 "__**Available Commands**__\n"
        for com in self.commands_full:
            result += f"{com}\n"

        result += "\nIf you want more info on a specific command, " \
                  "use the command \"help\" followed by a command of your choice. " \
                  "**For example: Arise! help roll**" \
                  "\nI'm sure Azir will be glad to help you out... I love him so much..."

        return result

    # noinspection PyMethodMayBeStatic
    def display_command(self, command):
        if command not in self.commands:
            return "That command doesn't exist :/"
        result = f"__**Command: {command[0].upper()}{command[1:]}**__\n\n"
        result += self.command_dict[command]
        return result

    # noinspection PyMethodMayBeStatic
    def init_command_info(self):
        self.command_dict["help"] = "Did somebody say recursion?"
        self.command_dict["lottery"] = "**Syntax:** Arise! lottery [seconds]\n\n" \
                                       "__**Description**__\n" \
                                       "Azir's lottery selects one lucky winner from a pool. To enter the pool, " \
                                       "react to the lottery message with ***any*** emoji. I do not discriminate. " \
                                       "The default timer is **60 seconds**. Upon request, a different number of " \
                                       "seconds may be allowed."
        self.command_dict["poll"] = "**Syntax:** Arise! poll\n\n" \
                                    "__**Description**__\n" \
                                    "You have questions and I'll help you set them up. Follow the step-by-step " \
                                    "instructions. When you have finished them all, use the polling command to " \
                                    "ask away."
        self.command_dict["polling"] = "**Syntax:** Arise! polling [poll number]\n\n" \
                                       "__**Description**__\n" \
                                       "This command allows you to use the poll you've created. If you have multiple " \
                                       "polls, you may enter a number to specify which poll. The default is the first."
        self.command_dict["prophecy"] = "Prepare yourself."
        self.command_dict["roll"] = "**Syntax:** Arise! roll [number]\n\n" \
                                    "__**Description**__\n" \
                                    "Azir needs random numbers *all* the time so he thought you may need some too. " \
                                    "This command produces a random number from 1 to the default value of **10**. " \
                                    "If you want to roll up to a different number, let me know."
        self.command_dict["team"] = "**Syntax:** Arise! team [type]\n\n" \
                                    "__**Description**__\n" \
                                    "Do you want to play a team with a theme? The Shuriman Empire has just the " \
                                    "solution for you! With 25 different groupings (wow. Wow! WOW!!), you'll be " \
                                    "having fun forever :) The default value for [type] is **0** in which you'd " \
                                    "get any random team. To select a team based on location, use **1**. To select " \
                                    "a *funner* team, use **2**."
        self.command_dict["ub"] = "**Syntax:** Arise! ub [role]\n\n" \
                                  "__**Description**__\n" \
                                  "Oh, how I love Ultimate Bravery. No one is as good at this game mode as Azir. " \
                                  "**NO ONE!**... Ahem... So basically, you are given a random champion and a build. " \
                                  "Here are the general guidelines:\n\n" \
                                  "1. Don't play this alone. Azir forbids it.\n" \
                                  "2. No rerolling if the champion or build is undesirable.\n" \
                                  "3. Okay, rerolling is allowed is the majority of the group agrees.\n" \
                                  "4. Feel free to use any rune page. Choose wisely.\n" \
                                  "5.a) Build the items in the order that they've been delivered.\n" \
                                  "5.b) The first two items are interchangeable.\n" \
                                  "6. Try your best to win. That's the whole point of this game.\n\n" \
                                  "The default value for [role] is **1**. To select a jungle specific build, " \
                                  "use **2**. To select a support specific build, use **3**."
