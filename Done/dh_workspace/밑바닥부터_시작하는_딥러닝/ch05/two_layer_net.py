# TwoLayerNet
import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.layers import *
from common.gradient import numerical_gradient
from collections import OrderedDict


class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std = 0.01):
        # 가중치 초기화
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size) 
        self.params['b2'] = np.zeros(output_size)

        # 계층 생성
        self.layers = OrderedDict()
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])

        self.lastLayer = SoftmaxWithLoss()
        
    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
        
        return x
        
    # x : 입력 데이터, t : 정답 레이블
    def loss(self, x, t):
        y = self.predict(x)
        return self.lastLayer.forward(y, t)
    
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)                                        #인덱스를 반환
        if t.ndim != 1 : t = np.argmax(t, axis=1)                       #인덱스를 반환
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
        
    # x : 입력 데이터, t : 정답 레이블
    def numerical_gradient(self, x, t):                                 #수치적 미분을 이용
        loss_W = lambda W: self.loss(x, t)
        
        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
        
        return grads
        
    def gradient(self, x, t):                                           #back propagation을 이용.
        # forward
        self.loss(x, t)

        # backward
        dout = 1
        dout = self.lastLayer.backward(dout)
        
        layers = list(self.layers.values())                             #forward한 결과들이 리스트에 저장된다. Affine1->Relu1->Affine2 이런 순으로 저장된다.
        layers.reverse()                                                #Affine2->Relu1->Affine1 이렇게 리스트가 바뀐다.
        for layer in layers:
            dout = layer.backward(dout)                                 #Affine2에 dout이 기본적으로 1이기 때문에 굳이 dout을 초기화 할 필요는 없다.
                                                                        #return값들을 dout에 저장해서 연쇄적으로 계산가능.

        # 결과 저장
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Affine1'].dW, self.layers['Affine1'].db     #backward함수에 dw와 db를 저장했었는데 그걸 grads의 'W1'과' 'b1'에 저장
        grads['W2'], grads['b2'] = self.layers['Affine2'].dW, self.layers['Affine2'].db     #backward함수에 dw와 db를 저장했었는데 그걸 grads의 'W2'과' 'b2'에 저장

        return grads