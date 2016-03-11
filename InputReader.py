from numpy import loadtxt

class InputReader:
    def load(self, filename):
        try:
            input = loadtxt(filename, comments="#", delimiter=" ", unpack=False)
        except IOError:
            print "No such file."
            exit()
        except Exception:
            print "Corrupted data file."
            exit()

        poly = []
        for i in input:
            poly.append(float(i))

        return poly
