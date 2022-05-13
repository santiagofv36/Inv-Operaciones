# Solving the model 1

class Model1:
    # Data is a dictionary with the following keys:
    #  '_Lambda'
    #  '_Mu'
    # '_n'

    def __init__(self, data):
        self.data = data

    def calculateC_n(self):
        _lambda = self.data['_Lambda']
        _mu = self.data['_Mu']
        _n = self.data['_n']
        return (_lambda /_mu) ** _n

    def calculateP_n(self):
        ro = self.data['_Lambda'] / self.data['_Mu']
        # print(ro)
         
        return (1 - (self.data['_Lambda'] / self.data['_Mu'])) * self.calculateC_n()

    def calculateL(self):
        return self.data['_Lambda'] / (self.data['_Mu'] - self.data['_Lambda'])

    def calculateLq(self):
        return self.data['_Lambda']**2 / (self.data['_Mu']*(self.data['_Mu'] - self.data['_Lambda']))

    def calculateW(self):
        return self.calculateL() / self.data['_Lambda']

    def calculateWq(self):
        return self.calculateLq() / self.data['_Lambda'] /60

    def Display(self):
        n = self.data['_n']
        print('C_n :', self.calculateC_n())
        print(f'P_{n}: {self.calculateP_n()}')
        print('L:', self.calculateL())
        print('Lq:', self.calculateLq())
        print('W:', self.calculateW())
        print('Wq:', self.calculateWq())




