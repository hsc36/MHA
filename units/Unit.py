class Unit:

	"A generic Unit class"

	def __init__(self, type):
		"""
		ID				: str - Object ID
		type			: str - This Unit's Type
		name			: str - Name of this Unit
		size			: int - Number of Individual people in this Unit
		auth_size		: int - Number of Individual people authorized to be in this Unit
		act_date		: datetime - Date and Time of this Unit's Activation
		act_location	: Location - Location of Unit Activation
		inact_date		: datetime - Date and Time of this Unit's Inactivation
		inact_location	: Location - Location of Unit Inactivation
		parent_unit		: Unit - This Unit's commanding Unit
		child_unit		: list(Unit) - List of Units under this Unit's command
		"""
		self.ID = assignUnitID()
		self.type = None
		self.name = None
		self.size = None
		self.auth_size = None
		self.act_date = None
		self.act_location = None
		self.inact_date = None
		self.inact_location = None
		self.parent_unit = None
		self.child_unit = None

	# ID Generation
	def assignUnitID():
		"Sets self.ID for Unit"
		return generateUnitID()

	def generateUnitID(self, type):
		"Generates a random alphanumeric ID, given the self.type"
		"@TODO: Random number + type"
		return generated_unit_id

	def setUnitID(self, unit_id):
		self.unit_id = unit_id

	def getUnitID(self):
		return self.unit_id

	# Type
	def setType(self, type):
		self.type = type

	def getType(self):
		return self.type

	# Name
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	# Current Size (Number of Individuals)
	def setSize(self, size):
		self.size = size

	def getSize(self):
		return self.size

	# Authorized Size (Number of Individuals)
	def setAuthSize(self, auth_size):
		self.auth_size = auth_size

	def getAuthSize(self):
		return self.auth_size

	# Date Activated 
	def setActivationDate(self, act_date):
		self.act_date = act_date

	def getActivationDate(self):
		return self.act_date

	# Location Activated 
	def setActivationDate(self, act_location):
		self.act_location = act_location

	def getActivationDate(self):
		return self.act_location

	# Date Inactivated 
	def setActivationDate(self, inact_date):
		self.inact_date = inact_date

	def getActivationDate(self):
		return self.inact_date

	# Location Inactivated 
	def setActivationDate(self, inact_location):
		self.inact_location = inact_location

	def getActivationDate(self):
		return self.inact_location

	# Parent Unit
	def setParentUnit(self, parent_unit):
		self.parent_unit = parent_unit

	def getParentUnit(self):
		return self.parent_unit

	# Child Unit
	def setChildUnit(self, child_unit):
		self.child_unit = child_unit

	def getChildUnit(self):
		return self.child_unit