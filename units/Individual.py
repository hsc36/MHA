class Individual(Unit):

	"An Individual Unit - soldier, airman, marine, trooper, etc."
	
	def __init__(self):
		super().__init__(self, "Individual")
		self.setSize(1)
		self.setChild(None)