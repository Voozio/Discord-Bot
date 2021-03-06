import random

champion_list = [line[:-1] for line in open("txt_files/champions/champions.txt")]
items = [line[:-1] for line in open("txt_files/items/items.txt")]
items_starter = [line[:-1] for line in open("txt_files/items/items_starter.txt")]
items_shoes = [line[:-1] for line in open("txt_files/items/items_shoes.txt")]
items_jungle = [line[:-1] for line in open("txt_files/items/items_jungle.txt")]
items_support = [line[:-1] for line in open("txt_files/items/items_support.txt")]


class UB:
    def __init__(self, selection = 1):
        self.champion = ""
        self.starter = ""
        self.boots = ""
        self.item_list = []
        self.jungler = False
        self.support = False
        self.snake = False
        self.viktor = False

        self.determine_selection(selection)
        self.determine_champion()
        self.determine_items()

    def determine_selection(self, selection):
        if selection == 2:
            self.jungler = True
        elif selection == 3:
            self.support = True

    def determine_champion(self):
        self.champion = random.choice(champion_list)

        if self.champion == "Cassiopeia":
            self.snake = True
        elif self.champion == "Viktor":
            self.viktor = True

    def determine_items(self):
        """
        Starting Items
        """
        if self.jungler:
            self.starter = "Hunter's Machete or Hunter's Talisman"
        elif self.support:
            self.starter = random.choice(items_support)
        elif self.viktor:
            self.starter = "Hex Core MK-1"
        else:
            self.starter = random.choice(items_starter)

        """
        Boots
        """
        if not self.snake:
            self.boots = random.choice(items_shoes)

        """
        Items
        """
        if self.jungler:
            self.item_list.append(self.boots)
            self.item_list.append(random.choice(items_jungle))

            while len(self.item_list) < 6:
                item = random.choice(items)
                if item not in self.item_list:
                    self.item_list.append(item)
        elif self.support:
            self.item_list.append(self.boots)
            self.item_list.append(self.get_supp_item())

            while len(self.item_list) < 6:
                item = random.choice(items)
                if item not in self.item_list:
                    self.item_list.append(item)
        elif self.snake:
            while len(self.item_list) < 6:
                item = random.choice(items)
                if item not in self.item_list:
                    self.item_list.append(item)
        elif self.viktor:
            self.item_list.append(self.boots)
            self.item_list.append("Hex Core Item")

            while len(self.item_list) < 6:
                item = random.choice(items)
                if item not in self.item_list:
                    self.item_list.append(item)
        else:
            self.item_list.append(self.boots)

            while len(self.item_list) < 6:
                item = random.choice(items)
                if item not in self.item_list:
                    self.item_list.append(item)

    def get_supp_item(self):
        if self.starter == "Relic Shield":
            return "Targon's Buckler"
        elif self.starter == "Spectral Sickle":
            return "Harrowing Crescent"
        elif self.starter == "Spelltheif's Edge":
            return "Frostfang"
        elif self.starter == "Steel Shouldergaurds":
            return "Runesteel Spaulders"

    def display(self, ctx):
        result = f"{ctx.author.mention}\n" \
                 f"__**Champion**__\n" \
                 f"{self.champion}\n\n" \
                 f"__**Starting Item**__\n" \
                 f"{self.starter}\n\n" \
                 f"__**Items**__\n"

        for item in self.item_list:
            result += f"{item}\n"

        return result
