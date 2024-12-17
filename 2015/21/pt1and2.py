class Item:
    def __init__(self, cost, damage, armor):
        self.cost = cost
        self.damage = damage
        self.armor = armor

weapons = [
    Item(8, 4, 0),
    Item(10, 5, 0),
    Item(25, 6, 0),
    Item(40, 7, 0),
    Item(74, 8, 0)
]

armors = [
    Item(13, 0, 1),
    Item(31, 0, 2),
    Item(53, 0, 3),
    Item(75, 0, 4),
    Item(102, 0, 5)
]

rings = [
    Item(25, 1, 0),
    Item(50, 2, 0),
    Item(100, 3, 0),
    Item(20, 0, 1),
    Item(40, 0, 2),
    Item(80, 0, 3)
]

class Fighter:
    def __init__(self, hp, damage, armor):
        self.hp = hp
        self.damage = damage
        self.armor = armor
    
    def get_hit(self, damage):
        self.hp -= max(1, damage - self.armor)

def fight(player: Fighter, boss: Fighter):
    while True:
        boss.get_hit(player.damage)
        if boss.hp <= 0:
            return True
        player.get_hit(boss.damage)
        if player.hp <= 0:
            return False

weapon_options = [0, 1, 2, 3, 4]
armor_options = [-1, 0, 1, 2, 3, 4]
ring_options = [[], [0], [1], [2], [3], [4], [5], [0,1], [0,2], [0,3], [0,4], [0,5], [1,2], [1,3], [1,4], [1,5], [2,3], [2,4], [2,5], [3,4], [3,5], [4,5]]

min_gold_win = 99999999
max_gold_lose = 0
for weapon in weapon_options:
    for armor in armor_options:
        for ring_indices in ring_options:
            damage_stat = weapons[weapon].damage
            armor_stat = armors[armor].armor if armor != -1 else 0
            for ring in ring_indices:
                damage_stat += rings[ring].damage
                armor_stat += rings[ring].armor
            player = Fighter(100, damage_stat, armor_stat)
            boss = Fighter(109, 8, 2)
            cost = weapons[weapon].cost
            cost += armors[armor].cost if armor != -1 else 0
            for ring in ring_indices:
                cost += rings[ring].cost
            if fight(player, boss):
                min_gold_win = min(min_gold_win, cost)
            else:
                max_gold_lose = max(max_gold_lose, cost)
print('min gold to win', min_gold_win)
print('max gold to lose', max_gold_lose)