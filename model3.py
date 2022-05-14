from factorial import factorial

class Model3:

    def __init__(self, data):
        self.data = data

    def calculateC_n(self,n):
        Lambda = self.data['_Lambda']
        Mu = self.data['_Mu']
        N = self.data['_N']
        left = factorial(N)/(factorial(N-n))
        right = (Lambda/Mu)**n
        return left*right
    
    def calculateP_0(self):
        N = self.data['_N']
        return (sum(self.calculateC_n(n) for n in range(N+1)))**-1

    def calculateP_n(self,n):
        return self.calculateC_n(n)*self.calculateP_0()

    def calculateL(self):
        N = self.data['_N']
        return sum(n * self.calculateP_n(n) for n in range(N+1))

    def calculateLq(self):
        N = self.data['_N']
        return sum((n-1) * self.calculateP_n(n) for n in range(1,N+1))

    def calculateLambda_n(self,n):
        N = self.data['_N']
        return (factorial(N)/(factorial(N-n)))*(self.data['_Lambda'])
    
    def calculateAvgLambda(self):
        N = self.data['_N']
        return sum(self.calculateLambda_n(n) * self.calculateP_n(n) for n in range(N+1))

    def calculateW(self):
        return self.calculateL()/ self.calculateAvgLambda()

    def calculateWq(self):
        return self.calculateLq()/ self.calculateAvgLambda()

    def Display(self):
        print(f'P_0 = {self.calculateP_0():.4f}')
        print(f'L = {self.calculateL():.4f}')
        print(f'Lq = {self.calculateLq():.4f}')
        print(f'W = {self.calculateW():.4f}')
        print(f'Wq = {self.calculateWq():.4f}')
