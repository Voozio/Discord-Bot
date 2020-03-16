import random

champion_list = [line for line in open("txt_files/champions.txt")]
items = [line for line in open("txt_files/items/items.txt")]
items_starter = [line for line in open("txt_files/items/items_starter.txt")]
items_shoes = [line for line in open("txt_files/items/items_shoes.txt")]
items_jungle = [line for line in open("txt_files/items/items_jungle.txt")]
items_support = [line for line in open("txt_files/items/items_support.txt")]


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
            self.starter = "Your Choice"
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
            for i in range(4):
                self.item_list.append(random.choice(items))
        elif self.support:
            self.item_list.append(self.boots)
            self.item_list.append(self.get_supp_item())
            for i in range(4):
                self.item_list.append(random.choice(items))
        elif self.snake:
            for i in range(6):
                self.item_list.append(random.choice(items))
        elif self.viktor:
            self.item_list.append(self.boots)
            self.item_list.append("Hex Core Item")
            for i in range(4):
                self.item_list.append(random.choice(items))
        else:
            self.item_list.append(self.boots)
            for i in range(5):
                self.item_list.append(random.choice(items))

    def get_supp_item(self):
        if self.starter == "Relic Shield":
            return "Targon's Buckler"
        elif self.starter == "Spectral Sickle":
            return "Harrowing Crescent"
        elif self.starter == "Spelltheif's Edge":
            return "Frostfang"
        elif self.starter == "Steel Shouldergaurds":
            return "Runesteel Spaulders"
