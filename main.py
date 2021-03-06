# P_n Probability of n clients in the system
# L Expected number of clients in the system
# Lq Expected length of the queue
# W Expected Residence time in the system 
# Wq Expected Residence time in the queue
#  S Number of servers in the system

from model1 import Model1
from model2 import Model2
from model3 import Model3

def model1():
    print()
    print('Solving the model 1')
    print()
    Lambda = float(input('Lambda: '))
    Mu = float(input('Mu: '))
    n = int(input('n: '))
    exceed = int(input('exceso: '))
    data = {'_Lambda': Lambda, '_Mu': Mu, '_n': n,'_N': exceed}
    model = Model1(data)
    model.Display()

def model2():
    print()
    print('Solving the model 2')
    print()
    Lambda = float(input('Lambda: '))
    Mu = float(input('Mu: '))
    n = int(input('n: '))
    k = int(input('k: '))
    data = {'_Lambda': Lambda, '_Mu': Mu, '_n': n, '_k': k}
    model = Model2(data)
    model.Display()

def model3():
    print()
    print('Solving the model 3')
    print()
    Lambda = float(input('Lambda: '))
    Mu = float(input('Mu: '))
    N = int(input('N: '))
    data = {'_Lambda': Lambda, '_Mu': Mu, '_N': N}
    model = Model3(data)
    model.Display()

def main():
    op = ''
    while op != '0':
        print('1.- Solve the model 1')
        print('2.- Solve the model 2')
        print('3.- Solve the model 3')
        print('0.- Exit')
        op = input('Choose an option: ')
        if op == '1':
            model1()
        elif op == '2':
            model2()
        elif op == '3':
            model3()
        elif op == '0':
            print('Exiting...')
        else:
            print('Invalid option')

if __name__ == "__main__":
    main()