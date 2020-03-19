import random

# Locations
castaways = [line[:-1] for line in open("txt_files/champions/groups/location/bandle_city_and_bilgewater.txt")]
demacia = [line[:-1] for line in open("txt_files/champions/groups/location/demacia.txt")]
freljord = [line[:-1] for line in open("txt_files/champions/groups/location/freljord.txt")]
ionia = [line[:-1] for line in open("txt_files/champions/groups/location/ionia.txt")]
heaven_and_earth = [line[:-1] for line in open("txt_files/champions/groups/location/ixtal_and_targon.txt")]
noxus = [line[:-1] for line in open("txt_files/champions/groups/location/noxus.txt")]
piltover = [line[:-1] for line in open("txt_files/champions/groups/location/piltover_and_zaun.txt")]
dark = [line[:-1] for line in open("txt_files/champions/groups/location/shadow_isles_and_void.txt")]
sand_land = [line[:-1] for line in open("txt_files/champions/groups/location/shurima.txt")]

# Fun
assassins = [line[:-1] for line in open("txt_files/champions/groups/fun/assassins.txt")]
big_beefy_boiz = [line[:-1] for line in open("txt_files/champions/groups/fun/big_beefy_boiz.txt")]
britney_spears = [line[:-1] for line in open("txt_files/champions/groups/fun/britney_spears.txt")]
global_offensive = [line[:-1] for line in open("txt_files/champions/groups/fun/global.txt")]
guns = [line[:-1] for line in open("txt_files/champions/groups/fun/guns.txt")]
immortals = [line[:-1] for line in open("txt_files/champions/groups/fun/immortals.txt")]
katniss = [line[:-1] for line in open("txt_files/champions/groups/fun/katniss_everdeen.txt")]
machines = [line[:-1] for line in open("txt_files/champions/groups/fun/machines.txt")]
magicians = [line[:-1] for line in open("txt_files/champions/groups/fun/magicians.txt")]
mana = [line[:-1] for line in open("txt_files/champions/groups/fun/mana.txt")]
music = [line[:-1] for line in open("txt_files/champions/groups/fun/music.txt")]
hooks = [line[:-1] for line in open("txt_files/champions/groups/fun/off_the_hook.txt")]
summoners = [line[:-1] for line in open("txt_files/champions/groups/fun/summoner.txt")]
transformers = [line[:-1] for line in open("txt_files/champions/groups/fun/transformers.txt")]
unappreciated = [line[:-1] for line in open("txt_files/champions/groups/fun/unappreciated.txt")]
zoom_x2 = [line[:-1] for line in open("txt_files/champions/groups/fun/zoom_x2.txt")]


class Team:
    def __init__(self):
        self.locations = [castaways,
                          demacia,
                          freljord,
                          heaven_and_earth,
                          ionia,
                          noxus,
                          piltover,
                          dark,
                          sand_land]
        self.fun = [assassins,
                    big_beefy_boiz,
                    britney_spears,
                    global_offensive,
                    guns,
                    immortals,
                    katniss,
                    machines,
                    mana,
                    music,
                    hooks,
                    summoners,
                    transformers,
                    unappreciated,
                    zoom_x2]
        self.group_names_loc = [castaways[0],
                                demacia[0],
                                freljord[0],
                                heaven_and_earth[0],
                                ionia[0],
                                noxus[0],
                                piltover[0],
                                dark[0],
                                sand_land[0]]
        self.group_names_fun = [assassins[0],
                                big_beefy_boiz[0],
                                britney_spears[0],
                                global_offensive[0],
                                guns[0],
                                immortals[0],
                                katniss[0],
                                machines[0],
                                mana[0],
                                music[0],
                                hooks[0],
                                summoners[0],
                                transformers[0],
                                unappreciated[0],
                                zoom_x2[0]]

    def generate_team(self, group_num = 0):
        if group_num == 1:
            location_group = random.choice(self.locations)
            return self.generate_team_helper(location_group, group_num)
        elif group_num == 2:
            fun_group = random.choice(self.fun)
            return self.generate_team_helper(fun_group, group_num)
        else:
            combined = [self.locations, self.fun]
            group_type = random.choice(combined)
            group_num = combined.index(group_type) + 1
            chosen_group = random.choice(group_type)
            return self.generate_team_helper(chosen_group, group_num)

    def generate_team_helper(self, group, group_num):
        count = 0
        if group_num == 1:
            team = [self.determine_group_name_loc(group)]
        else:
            team = [self.determine_group_name_fun(group)]

        while count < 5:
            champion = random.choice(group)
            if champion not in team and (champion not in self.group_names_loc or champion not in self.group_names_fun):
                team.append(champion)
                count += 1

        return team

    def determine_group_name_loc(self, group):
        for i in range(len(self.locations)):
            if group == self.locations[i]:
                return self.group_names_loc[i]

    def determine_group_name_fun(self, group):
        for i in range(len(self.fun)):
            if group == self.fun[i]:
                return self.group_names_fun[i]
