class PrimeORnot:
	def __init__(self,n):
		self.n = n
	def Primecheck(self):
		if self.n in [1,2,3,5]:
			return True
		elif self.n in [4,6]:
			return False
		else:
			for i in range(2, self.n//2):
				if self.n == 0:
					return False
				else:
					return True

If __name__ == "__main__":
	x = int(input("Enter a Number: "))
	obj = PrimeORnot(x)
	print(obj.primeORnot())			
		
