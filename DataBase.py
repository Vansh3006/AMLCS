class Artillery:
    def __init__(self, name, min_range, max_range, muzzle_velocity):
        self.name = name
        self.min_range = min_range
        self.max_range = max_range
        self.muzzle_velocity = muzzle_velocity


artillery_1 = Artillery('120 mm E1 Light Mortar', 7.2, 9.5, 305)
artillery_2 = Artillery('105 mm Indian Field Gun', 17.2, 20, 475)
artillery_3 = Artillery('122 mm D-30 Howitzer', 0, 21.9, 388)
artillery_4 = Artillery('130 mm M-46 Field Gun', 0, 38, 930)
artillery_5 = Artillery('155 mm Haubits FH77/B Howitzer', 0, 24, 770)
artillery_6 = Artillery('155 mm M777 howitzer', 0, 40, 827)
artillery_7 = Artillery('155 mm Dhanush (howitzer)', 0, 38, 610)
artillery_8 = Artillery("155 mm DRDO Advanced Towed Artillery Gun System (ATAGS)", 0, 52.074, 714)

artillery_directory = [artillery_1, artillery_2, artillery_3, artillery_4,
                       artillery_5, artillery_6, artillery_7, artillery_8]


class Missile:
    def __init__(self, name, min_range, max_range, speed):
        self.name = name
        self.min_range = min_range
        self.max_range = max_range
        self.speed = speed


missile_1 = Missile("Agni-I", 900, 1200, 7.5)
missile_2 = Missile("Agni-II", 2000, 3500, 12)
missile_3 = Missile("Agni-III", 3500, 5000, 14.5773)
missile_4 = Missile("Agni-IV", 0, 4000, 7)
missile_5 = Missile("Agni-V", 5500, 8000, 24)
missile_6 = Missile("K-15(Sagarika)", 0, 750, 7.5)
missile_7 = Missile("BrahMos Block I, II, III", 0, 290, 3)
missile_8 = Missile("Submarine launched BrahMos", 0, 290, 3)
missile_9 = Missile("Nirbhaya", 1000, 1500, 0.9)
missile_10 = Missile("Shaurya", 0, 700, 7.5)
missile_11 = Missile("Pinaka MkI", 0, 40, 4.7)
missile_12 = Missile("BM-21 Grad", 0, 45, 2.011)
missile_13 = Missile("Prithvi-I", 0, 150, 3)
missile_14 = Missile("Prithvi-II", 0, 350, 3)
missile_15 = Missile("Prithvi-III", 0, 600, 3)
missile_16 = Missile("Prithvi-III", 0, 750, 3)
missile_17 = Missile("Dhanush", 0, 750, 3)
missile_18 = Missile("BM-30 Smerch", 0, 850, 0.0485909)

missile_directory = [missile_1, missile_2, missile_3, missile_4, missile_5,
                     missile_6, missile_7, missile_8, missile_9,missile_10,
                     missile_11, missile_12, missile_13, missile_14, missile_15,
                     missile_16, missile_17, missile_18]