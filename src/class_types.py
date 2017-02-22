#!python


class Player(object):
	"""Base Player Class and Subclasses"""
	max_productivity = None
	impact = None
	influence = None
	location = None
	creativity = None
	reorg_productivity = 5

	def __init__(self, name, location, current_productivity=None):
		self.name = name
		self.location = location
		if current_productivity is not None
			self.current_productivity = current_productivity
		else: 
			self.current_productivity = self.max_productivity

	def reorg(self, new_location):
		print "{0} initiates a reorg of the teams. Everyone loses {1} productivity".format(self.name, reorg_productivity)
		Player.current_productivity = Player.current_productivity - reorg_productivity
		self.location = new_location
		print "{0} has move from {1} to {2}".format(self.name, self.location, new_location)
		

	def context_switch(self, other_player):
		print "{0} attempts to distract {1} with random questions about an API {1} never worked on for a reduction of {2} productivity".format(self.name, other_player, self.impact)
		if self.in_circle_of_influence(other_player):
			other_player.current_productivity = other_player.current_productivity - self.impact
			print "{0} Successfully distracted {1}! {1} pretends to know all about the API and has had his/her productivity drop to {2}, SHAME!".format(self.name, other_player.name, other_player.current_productivity)
		else:
			self.outside_circle_of_influence(other_player)
			print "Diverting the conversation to another team member, {1} remains focused despite {0}'s efforts.".format(self.name, other_player.name)


	def in_circle_of_influence(self, other_player):
		if abs(self.location - other_player.location) < self.influence:
			return True
		return False

	def outside_circle_of_influence(self, other_player):
		print "{0} is outside of {1}'s circle of influence!".format(other_player.name, self.name)