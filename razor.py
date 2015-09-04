class Razor(object):

	def __init__(self, numPhases=4, usesPerPhase=1):
		self.phases = numPhases
		self.usesPerPhase = usesPerPhase
		self.currentPhase = 1
		self.phaseDescriptions = []

	def definePhases(self, phaseNum, description):
		self.phaseDescriptions[phaseNum] = description


	def shave(self):
		pass
			