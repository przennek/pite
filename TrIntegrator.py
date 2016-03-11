# IntegralCalc is class for calculating integrals over Poly objects

class TrIntegrator:
	poly = None
	delta = None	

	def __init__(self, poly, delta):
		self.poly = poly
		self.delta = delta		
	
	def calculateIntegral(self):
		result = 0
		counter = self.poly.start + self.delta
		while counter < self.poly.end:
			counter += self.delta
			result += 0.5 * (self.poly.pValue(counter) + self.poly.pValue(counter + self.delta)) * self.delta
		return result