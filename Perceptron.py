from math import exp
import numpy

class Perceptron:
    eta = 0.0001
    epochs = 100
    b = 0.0001
    w = [-b, 0, 0]
    ## constant for feature index in dataset
    fi = 0
    fj = 1
    ## constant for classes to test only ignore rest
    ci = 0
    cj = 1
    def __init__(self, eta, epochs):
        self.eta = eta
        self.epochs = epochs
        self.b = 0.001
        ## INITIAL WEGHTS
        self.w = [self.b, 0, 0]
        
    def sigmoid(self, V):
        return 1 / 1 + exp(V)

    def signum(self, PHI):
            if PHI > 0:
                return 0
            else:
                return 1 
    
    def activation(self, PHI):
        if PHI > 0:
            return +1
        else:
            return -1
    
    def train(self, data):
        for epo_i in range(0, self.epochs):
            counter = 0
            for T in data:
                X = T[0] ## Input
                d = T[1] ## Desired Response
                ## SKIPS CLASSES TO LIMIT PROBLEM TO ONLY TWO CLASSES ##
                if d != self.ci and d != self.cj:
                    counter = counter + 1
                    continue
                ## END SKIP ##
                X = [1 ,X[self.fj], X[self.fj]] ## Inputs only two features
                V = numpy.inner(self.w, X)
                Y = self.signum(V)
               # Y = self.activation(Y)
                self.w = self.w + self.eta * (d - Y) * numpy.array(X)
                print 'W(n+1) = ', self.w
                counter = counter + 1
        
    def test(self, data):
        print 'Testing:'
        correct = 0
        wrong = 0
        counter = 0
        for T in data:
            X = T[0] ## Input
            d = T[1] ## Desired Response            
            ## SKIPS CLASSES TO LIMIT PROBLEM TO ONLY TWO CLASSES ##
            if d != self.ci and d != self.cj:
                counter = counter + 1
                continue
            ## END SKIP ##
            X = [1 ,X[self.fj], X[self.fj]] ## Inputs only two features
            print 'X = ', X

            V = numpy.inner(self.w, X)
            #print 'V = ', V
            Y = self.signum(V)
            #Y = self.activation(Y)
            print 'Y = ', Y
            print 'd = ', d
            if Y == d:
                correct = correct + 1
            else:
                wrong = wrong + 1
            counter = counter + 1
        print 'correct=', correct
        print 'wrong=', wrong