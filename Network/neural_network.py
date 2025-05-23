import numpy as np

class Neural_network:
    def __init__(self, loss_f, optimizer, *layers, regularization=None):
        self.loss_f = loss_f
        self.optimizer = optimizer
        self.regularization = regularization if regularization else Null()
        self.layers = list(layers)
        
    def forward_pass(self, x):
        self.x = x
        for i in range(len(self.layers)):
            self.x = self.layers[i].forward(self.x)
        return self.x

    def loss(self, x_pred, x_true):
        self.x_pred = x_pred
        self.x_true = x_true
        return self.loss_f.forward(self.x_pred, self.x_true) + self.regularization.forward(self.layers)
    
    def backpropagation(self):
        self.delta = self.loss_f.backward()
        for i in range(len(self.layers) - 1, -1, -1):
            if i == len(self.layers) - 1:
                self.layers[i].backward(np.ones((self.delta.shape[0], self.delta.shape[0])), self.delta, self.regularization)
                
            else:
                self.layers[i].backward(self.layers[i+1].w, self.layers[i+1].delta, self.regularization)

    def optimize(self):
        self.optimizer.optimize(self.layers)