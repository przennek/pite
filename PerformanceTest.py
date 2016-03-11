import unittest
import time
from TrIntegrator import TrIntegrator
from Poly import Poly
import scipy.integrate as integrate

class PerformanceTest(unittest.TestCase):
    def setUp(self):
        datafile = "test.dat"
        self.polygon = Poly(datafile)
        self.delta = 1e-3

    def runTest(self):
        calc = TrIntegrator(self.polygon, self.delta)
        start_time_selfmade = time.time()
        mine_res = calc.calculateIntegral()
        print "Self time:", time.time() - start_time_selfmade
        g = lambda x: 0.5 * (self.polygon.pValue(x) + self.polygon.pValue(x + self.delta)) * self.delta
        start_time_scipy = time.time()
        scipy_res = integrate.quad(g, self.polygon.start, self.polygon.end, epsrel=1e-3, epsabs = 0)
        print "Scipy time:", time.time() - start_time_scipy

        print mine_res
        print scipy_res[0] * 1000

if __name__ == '__main__':
    unittest.main()

# As you may see my code lost to the scipy's, not only it's faster but also more precise
# (except for part where scipy returns values 1000 times too small i tried to google that without luck)