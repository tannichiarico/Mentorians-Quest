#!python
from classes import *
import pdb


def main():
	players = []
	setup_status = 'n'
	while setup_status != 'y':
		add_player(players)
		setup_status = raw_input("Are you ready to begin, y/n?>> ")
	print players


def add_player(players):
	player_name = raw_input("What is your character's name?>> ")
	print "Player setup done, welcome %s!" % player_name
	player_class = get_class(players)
	player = player_class(player_name, player_class, 10)
	players.append(player)


def get_class(players):
	choice_to_class = {
		'1':Warrior,
		'2':Archer,
		'3':Healer,
		'4':Shaman
	}

	user_class = None
	while user_class is None:
		pick_class = raw_input('Pick your Class:\n\t1.Warrior\n\t2.Archer\n\t3.Healer\n\t4.Shaman\n ')
		try:
			user_class = choice_to_class[pick_class]
			print ('you have selected', user_class)
		except KeyError:
			print 'Pick a valid option'
	return user_class
if __name__ == '__main__':
	main()




	# warrior_1 = Warrior('troy',10)
	# warrior_2 = Warrior('ari',15)
	# print warrior_1.name
