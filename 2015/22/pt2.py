class Effect:
    def __init__(self, turns, armor, damage, mana):
        self.turns = turns
        self.armor = armor
        self.damage = damage
        self.mana = mana
    
    def copy(self):
        return Effect(self.turns, self.armor, self.damage, self.mana)

class Fighter:
    def __init__(self, hp, damage, mana):
        self.hp = hp
        self.damage = damage
        self.armor = 0
        self.mana = mana
        self.effects = set()
    
    def get_hit(self, damage):
        self.hp -= max(1, damage - self.armor)

    def heal(self, health):
        self.hp += health

    def get_current_effect(self, effect):
        for e in self.effects:
            if e.armor == effect.armor and e.damage == effect.damage and e.mana == effect.mana:
                return e
        return None

    def add_effect(self, effect):
        current_effect = self.get_current_effect(effect)
        if current_effect is not None:
            current_effect.turns = effect.turns
        else:
            self.effects.add(effect)
            self.armor += effect.armor
    
    def do_effects(self):
        new_effects = self.effects.copy()
        for effect in self.effects:
            self.hp -= effect.damage
            self.mana += effect.mana
            effect.turns -= 1
            if effect.turns == 0:
                self.armor -= effect.armor
                new_effects.remove(effect)
        self.effects = new_effects
    
    def copy(self):
        fighter = Fighter(self.hp, self.damage, self.mana)
        for effect in self.effects:
            fighter.add_effect(effect.copy())
        return fighter
    
def magic_missile(player: Fighter, boss: Fighter):
    boss.get_hit(4)
def drain(player: Fighter, boss: Fighter):
    boss.get_hit(2)
    player.heal(2)
def shield(player: Fighter, boss: Fighter):
    player.add_effect(Effect(6, 7, 0, 0))
def poison(player: Fighter, boss: Fighter):
    boss.add_effect(Effect(6, 0, 3, 0))
def recharge(player: Fighter, boss: Fighter):
    player.add_effect(Effect(5, 0, 0, 101))

spells = {
    53: magic_missile,
    73: drain,
    113: shield,
    173: poison,
    229: recharge
}

class Game:
    def __init__(self, player: Fighter, boss: Fighter):
        self.player = player
        self.boss = boss
        self.mana_spent = 0
        self.spell_log = []
    
    def copy(self):
        game = Game(self.player.copy(), self.boss.copy())
        game.mana_spent = self.mana_spent
        game.spell_log = self.spell_log.copy()
        return game
    
    def get_winner(self):
        if self.player.hp <= 0:
            return self.boss
        if self.boss.hp <= 0:
            return self.player
        return None
    
    def get_available_spells(self):
        return sorted([spell for spell in spells.keys() if self.player.mana >= spell])

    def cast_spell(self, spell):
        self.spell_log.append(spells[spell].__name__)
        spells[spell](self.player, self.boss)
        self.player.mana -= spell
        self.mana_spent += spell
    
    def do_effects(self):
        self.player.do_effects()
        self.boss.do_effects()
    
    def attack_player(self):
        self.player.get_hit(self.boss.damage)

# print(do_player_turn(Fighter(50, 0, 500), Fighter(58, 9, 0)))
games = [Game(Fighter(50, 0, 500), Fighter(58, 9, 0))]
min_mana = 99999999999999

def check_game_over(game: Game):
    global min_mana
    winner = game.get_winner()
    if winner == game.player:
        min_mana = min(min_mana, game.mana_spent)
        print(game.mana_spent, game.spell_log)
    return winner is not None

while len(games) > 0:
    new_games = []
    # Player turn
    for game in games:
        if game.mana_spent > min_mana:
            continue
        game.player.hp -= 1
        if check_game_over(game):
            continue
        game.do_effects()
        if check_game_over(game):
            continue
        available_spells = game.get_available_spells()
        for spell in available_spells:
            new_game = game.copy()
            new_game.cast_spell(spell)
            if not check_game_over(new_game):
                new_games.append(new_game)
    games = new_games
    print(len(games), 'game scenarios')
    new_games = []
    # Boss turn
    for game in games:
        game.do_effects()
        if check_game_over(game):
            continue
        game.attack_player()
        if not check_game_over(game):
            new_games.append(game)
    games = new_games
    print(len(games), 'game scenarios')

print('min mana:', min_mana)