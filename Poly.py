from InputReader import InputReader
import sys

# Poly reads given polynomial and integral calculation bound from a textfile, given it's filename
# first two numbers are bounds of the calculation
# rest of the variables are increasing powers of the polynomial
# pValue - returns value of polynomial given *x*
class Poly:
	poly = None
	start = None
	end = None
	def __init__(self, filename):
		reader = InputReader()
		self.poly = reader.load(filename)
		self.start = self.poly.pop(0)
		self.end = self.poly.pop(0)
		
		print "Following polynomial was loaded: "
		counter = 0
		for i in self.poly:
			if counter == 0:
				sys.stdout.write(str(i))
			elif counter == 1:
				sys.stdout.write(" + " + str(i) + 'x')
			else:
				sys.stdout.write(" + " + str(i) + 'x^' + str(counter))
			counter += 1
		sys.stdout.write("\n")
		print 'Integral calculation starts:', self.start, 'ends:', self.end
		
	def pValue(self, x):
		value = 0
		counter = 0
		for i in self.poly:
			value += i * (x**counter)
			counter += 1
		
		return value
