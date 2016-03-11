import glob
from Poly import Poly
from TrIntegrator import TrIntegrator

class ApplicationMgr:
    def firstMenu(self):
        mode = None
        firstMenuTrap = True
        while firstMenuTrap:
            print "Integral calculator:"
            print "1) Calculate integral."
            print "2) Exit."
            try:
                mode = int(raw_input(': '))
            except ValueError:
                print "Not a number!"
            if mode == 1 or mode == 2:
                firstMenuTrap = False
            else:
                print "Wrong response."
        return mode

    def inputMenu(self):
        option = ApplicationMgr.chooseInputMenu(self)
        mode = None
        inputMenuTrap = True
        while inputMenuTrap:
            if option == 1:
                print "Input file number: "
                files = glob.glob("*.dat")
                counter = 0
                for file in files:
                    print str(counter) + ') ' + file
                try:
                    mode = int(raw_input(': '))
                except ValueError:
                    print "Not a number!"
                if mode <= counter:
                    inputMenuTrap = False
                else:
                    print "Wrong response."
                    continue
                datafile = files.pop(mode)

            elif option == 2:
                datafile = raw_input(': ')
                inputMenuTrap = False

            print "Insert delta: "
            try:
                delta = float(raw_input(': '))
            except ValueError:
                print "Not a number!"

            polygon = Poly(datafile)
            calc = TrIntegrator(polygon, delta)
            print "----------------------------"
            print "Result:", calc.calculateIntegral()
            print "----------------------------"

    def chooseInputMenu(self):
        mode = None
        chooseInputMenuTrap = True
        while chooseInputMenuTrap:
            print "Read options: "
            print "1) Read polynomial from listed file from script directory."
            print "2) Read polynomial from datafile, given it's full file path."
            try:
                mode = int(raw_input(': '))
            except ValueError:
                print "Not a number!"
            if mode == 1 or mode == 2:
                chooseInputMenuTrap = False
            else:
                print "Wrong response."
        return mode

    def run(self):
        while True:
                response = self.firstMenu()
                if response == 1:
                    ApplicationMgr.inputMenu(self)
                elif response == 2:
                    break
                else:
                    print "Wrong response."