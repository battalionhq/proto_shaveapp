class Razor(object):

	def __init__(self, numPhases=4, usesPerPhase=1):
		self.phases = numPhases
		self.usesPerPhase = usesPerPhase
		self.currentPhase = 0
		self.phaseDescriptions = []

	def definePhases(self, phaseNum, description):
		self.phaseDescriptions[phaseNum] = description


	def shave(self):
		if self.currentPhase ==0:
			print "Choose a side to be side A."
		elif self.currentPhase == 1:
			print "Use side B of razor"
		elif self.currentPhase ==2:
			print "flip blade and use side A"
		elif self.currentPhase ==3:
			print "Use side B of razor"
		elif self.currentPhase ==4:
			self.currentPhase = 0
			print "change blade and start with side A"
		self.currentPhase +=1


			