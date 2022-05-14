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

    def calculateP_n(self,n):
        ro = self.data['_Lambda'] / self.data['_Mu']
        k = self.data['_k']
        # n = self.data['_n']
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
        return round(self.calculateL() -(1 - self.calculateP_0()),4) if ro != 1 else round((k**2-k)/(2*k + 2),4)

    def avgLambda(self):
        ro = self.data['_Lambda'] / self.data['_Mu']
        return round(self.data['_Lambda']* (1 - self.calculateP_n(self.data['_k'])),4) if ro != 1 else (self.data['_k']*self.data['_Lambda'])/(self.data['_k']+1)

    def calculateW(self):
        return self.calculateL() / self.avgLambda()

    def calculateWq(self):
        return self.calculateLq() / self.avgLambda()

    def Display(self):
        n = self.data['_n']
        print('C_n:',self.calculateC_n())
        print(f'P_0: {self.calculateP_0()}')
        print(f'P_{n}: {self.calculateP_n(n)}')
        print(f'L: {self.calculateL()}')
        print(f'Lq: {self.calculateLq()}')
        print(f'W: {self.calculateW()}')
        print(f'Wq: {self.calculateWq()}')


    