class Model2:

    def __init__(self,data):
        self.data = data

    def calculateC_n(self):
        _lambda = self.data['_Lambda']
        _mu = self.data['_Mu']
        _n = self.data['_n']
        return (_lambda /_mu) ** _n

    def calculateP_0(self):
        ro = self.data['_Lambda'] / self.data['_Mu']
        k = self.data['_k']
        return round((1-ro)/(1-ro**(k+1)),4) if ro != 1 else round((k+1)**-1,4)

    def calculateP_n(self):
        ro = self.data['_Lambda'] / self.data['_Mu']
        k = self.data['_k']
        n = self.data['_n']
        return round(((1- ro)/(1- ro**(k+1))) * ro**n,4) if ro != 1 else round((k+1)**-1,4)

    def calculateL(self):
        ro = self.data['_Lambda'] / self.data['_Mu']
        k = self.data['_k']
        left = ro/(1-ro)
        right = ((k+1) * ro**(k+1))/(1-ro**(k+1))
        return round(left - right,4) if ro != 1 else round(k/2,4)

    def calculateLq(self):
        k = self.data['_k']
        ro = self.data['_Lambda'] / self.data['_Mu']
        return round((k*(k-1))/(2*(k+1)),4) if ro != 1 else round((k**2-k)/(2*k + 2),4)

    def calculateW(self):
        k = self.data['_k']
        Lambda = self.data['_Lambda']
        return round((k+1)/(2*(Lambda)),4) if self.data['_LambdaPromedio'] == 0 else round((self.calculateL())/(Lambda*(1- self.calculateP_n())),4)

    def calculateWq(self):
        k = self.data['_k']
        Lambda = self.data['_Lambda']
        return round((k-1)/(2*(Lambda)),4) if self.data['_LambdaPromedio'] == 0 else round((self.calculateLq())/(Lambda*(1- self.calculateP_n())),4)

    def Display(self):
        n = self.data['_n']
        print('C_n:',self.calculateC_n())
        print(f'P_0: {self.calculateP_0()}')
        print(f'P_{n}: {self.calculateP_n()}')
        print(f'L: {self.calculateL()}')
        print(f'Lq: {self.calculateLq()}')
        print(f'W: {self.calculateW()}')
        print(f'Wq: {self.calculateWq()}')


    