class Armstrong:
	def __init__(self,n):
		self.n = n	
	def length_int(self):
		self.l = len(str(self.n))
	def backup(self):
		self.backup_n = self.n
		return self.backup_n
	def checkArm(self):
		arm = 0
		for i in str(self.n):
			arm += int(i)**len(str(self.n))
		if arm == self.num:
			return True
		else:
			return False

obj = Armstrong(153)
print(obj.length_int())
print(obj.backup)
print(obj.checkArm)		
		






