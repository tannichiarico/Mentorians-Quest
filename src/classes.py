#!python


class Player:
    max_hp = None
    strength = None
    attack_range = None
    position = None

    def __init__(self, name, class_name, position, current_hp=None):
        self.name = name
        self.class_name = class_name
        self.position = position
        if current_hp is not None:
            self.current_hp = current_hp
        else:
            self.current_hp = self.max_hp

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<{}> {} {} [{}hp] @ {}".format(self.__class__.__name__, self.name, self.class_name, self.current_hp, self.position)

    def move(self, new_position):
        print '{} moves from {} to {}'.format(self.name, self.position, new_position)
        self.position = new_position

    def attack(self, other_player):
        print '{0} attempts to attack {1} for {2} damage'.format(self.name, other_player.name, self.strength)
        if self._is_in_range(other_player):
            other_player.current_hp = other_player.current_hp - self.strength
            print 'Attack successful. {} now has {}hp'.format(other_player.name, other_player.current_hp)
        else:
            self._out_of_range(other_player)

    def _out_of_range(self, other_player):
        print '{0} is out of range.'.format(other_player.name)

    def _is_in_range(self, other_player):
        if abs(self.position - other_player.position) < self.attack_range:
            return True
        return False


class Warrior(Player):
    max_hp = 125
    strength = 25
    attack_range = 3


class Archer(Player):
    max_hp = 75
    strength = 10
    attack_range = 20


class Healer(Player):
    max_hp = 50
    strength = 1
    attack_range = 3
    heal_strength = 25

    def heal(self, other_player):
        if self._is_in_range(other_player):
            other_player.current_hp = other_player.current_hp + self.heal_strength
        else:
            self._out_of_range(other_player)


class Shaman(Player):
    max_hp = 60
    strength = 20
    attack_range = 10

    def attack(self, other_player):
        if self._is_in_range(other_player):
            super(Shaman, self).attack(other_player)
            self.current_hp = max(self.current_hp + self.strength, self.max_hp)
        else:
            self._out_of_range(other_player)
