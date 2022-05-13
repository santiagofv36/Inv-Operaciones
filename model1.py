# Solving the model 1
#Add feature to know the ammount of clients in the system and the ammount of clients in the queue

class Model1:
    # Data is a dictionary with the following keys:
    #  '_Lambda'
    #  '_Mu'
    # '_n'

    def __init__(self, data):
        if data['_Lambda'] < data['_Mu']:
            print('Lambda must be greater than Mu')
            exit()
        self.data = data

    def calculateC_n(self):
        _lambda = self.data['_Lambda']
        _mu = self.data['_Mu']
        _n = self.data['_n']
        return (_lambda /_mu) ** _n

    def calculateP_0(self):
        return 1 - (self.data['_Lambda'] / self.data['_Mu'])
    
    def calculateP_n(self):
        return (1 - (self.data['_Lambda'] / self.data['_Mu'])) * self.calculateC_n()

    def calculateL(self):
        return self.data['_Lambda'] / (self.data['_Mu'] - self.data['_Lambda'])

    def calculateLq(self):
        return self.data['_Lambda']**2 / (self.data['_Mu']*(self.data['_Mu'] - self.data['_Lambda']))

    def calculateW(self):
        return self.calculateL() / self.data['_Lambda']

    def calculateWq(self):
        return self.calculateLq() / self.data['_Lambda']

    def probServerOcupied(self):
        return 1 - self.calculateP_0()

    def ClientsBeingAttended(self):
        return (self.calculateL() - self.calculateLq())

    def Display(self):
        n = self.data['_n']
        print()
        print(f'Probabilidad de que el servidor este ocupado: {self.probServerOcupied():.4f}')
        print(f'Numero esperado de elementos siendo atentidos {self.ClientsBeingAttended():.4f}')
        print(f'P_{n}: {self.calculateP_n():.4f}')
        print(f'L: {self.calculateL():.4f}')
        print(f'Lq: {self.calculateLq():.4f}')
        print(f'W: {self.calculateW():.4f}')
        print(f'Wq: {self.calculateWq():.4f}')
        print()




