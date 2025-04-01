# 질문 리스트

1. 활성화 함수는 왜 하는가?
> 비선형성을 위해, 선형 함수 자체가 심층 신경망에 도움이 되지 않는다.(선형함수를 여러개를 사용했을 때 어차피 그 함수는 선형함수가 된다. y=a*x->3times->y=a^3*x )<br>
또한 층을 깊게 해서 표현력을 높이기 위해 활성화 함수를 사용한다.

2. back propagation의 원리
> (역전파 왜함? gradient를 계산하기 위해 )<br>
> chain -rule을 이용. <br>
> 곱셈의 경우 위아래를 바꾸고 덧셈의 경우 이전의 결과값이 그대로 통과.<br>
> df/(d가중치)를 구하는 것이 목적<br>

3. forward 원리
>Linear -> activation -> BatchNorm(option), dropout(while training)->...<br>
>CNN의 경우: Conv2d->activation->pooling->...->fully connected layer

4. 데이터의 종류에는 무엇이 있는가?
> train(0.8), test(0.1-0.2), validation(0-0.1)

5. 매개변수가 괜찮은지 어떻게 판단?
> by loss function<br> 
> & <br>
> accuracy <br>
> & <br>
> loss 값이 training set은 떨어지는데 test set 또는 validation set은 떨어지다가 높아지면 overfitting이 되는중인 것임. 
> <br><br>
> 따라서 매개변수 초기화 xavier initialization, uniform initialization을 쓰거나 ,
dropout을 하거나,
regularization(weight deca!!y, batch_normali!!zation, early stopping) 을 한다.
><br><br>
>가중치 감소란, 가중치가 높을수록 훈련모델에 잘 맞는다는 소리임.(가중치가 높다는 것은 그 입력특성이 모델의 출력에 끼치는 영향력이 크다는 것이므로.) 그 모델에 잘 맞는다는 소리는 오버피팅이 될 가능성이 높다는 것이고 이를 방지하기 위해 가중치 값을 감소시켜서 오버피팅을 방지. how? 
loss=original_loss+1/2*lambda*sigma(w_i^2) 여기서 lambda는 가중치 감소의 강도를 결정 하는데 클수록 가중치 감소가 커지고 작을수록 가중치 감소가 작아져서 적절한 람다를 설정하는 것이 중요.
<br><br>
>batch normalization은 internal covariate shift가 일어나는 것을 방지하기 위해, 오버피팅을 방지하기 위해 사용.. 그리고 평균과 분산은 학습가능한 것이 아니고, 감마와 베타 값이 학습가능한 값이다. sample mean 과 sample variance를 평균내어서 learning mean 과 learning vairance를 만든다. 

6. 분류, 회귀가 무엇인지. 그리고 어떤 함수가 쓰이는지(mse, cse->loss function)
> * 1. 분류(개 고양이)- 특정 클래스에 속하는지 판단(이산적인 출력값), CrossEntropyLoss함수(softmax함수와 NegativeLogLikelihoodLoss함수를 합친거, 주로 여러개를 분류할 때 사용. 1/N sigma(-y*log(y^)),  여기의 y^은 소프트맥스로 예측한 값, y는 정답이면 1이고 정답이 아니면 0)
Binary cross entropy함수(두 클래스 중 하나를 예측하는거, -1/N*sigma(y*log(H(x))+(1-y)*log(1-H(x)))
여기의 H(x)함수는 주로 sigmoid) 
>  * 2. 회귀(키에 따른 몸무게) - 연속적인 숫자를 예측.
MSE함수: 1/m*sigma((H(x)-y)^2). H(x)는 예측 값으로 Linear regression한 값, y는 실제값.

7. 오버피팅 
> train의 학습률과 test의 학습률의 차이가 적을수록 좋은거다. train의 학습률만 높다고 좋은 것이 아니다.

8. 합성곱에서 왜 필터를 쓰는가.
> 가중치에서의 fully connected layer에서의 가중치를 생각하면 된다. 이미지의 특징을 찾아내는 것이 목적.

9. 가중치 감소의 norm은 손실함수에 더해준다. 하지만 손실함수는 적을수록 좋다. 그럼 왜 이짓을 할까?
> (위에 나와있다.)
참고로 L1 regularization이 따로 있는데, L1 정규화 수학적 표현으로는<br> Loss=original_loss + lambda*sigma(|w_i|)이다. 얘도 오버피팅을 방지하는데 도움이 된다. 
<br>
또 참고로, elastic net이라고 L1정규화와 L2정규화를 결합하는 방식이 있는데 수학적 표현으로는<br>
loss=original_loss+lambda1*sigma(|w_i|)+lambda2*sigma(w_i^2)이 있다.

10. 참고로 cnn은 image classification에 잘 쓰인다. 그 외로 object detection, image segmentation등이 있다.

11. 참고로 학습 관련 기술들로는 
>* 1) 매개변수 갱신을 위한 최적화(optimization-최적화와 관련된 공식은 따로 잘 보도록 하자....또 참고로 ada grad의 경우 학습이 많이 할수록 점차 학습률을 줄여나간다.)<br>
>* 2) 가중치의 초기값-xavier 초기화(n_in+n_out), he 초기화(n_in) normal은 sqrt(2), uniform sqrt(6)<br>
>* 3) batch normalization(오버피팅 억제, internal shift covariate 억제)<br>
>* 4) 가중치 감소(오버피팅 억제)<br>
>* 5) 드롭아웃(오버피팅 억제)<br>

12. CNN에서 마지막에 왜 fully connected layer를 넣는가?
> CNN(합성곱 신경망)에서 마지막에 Fully Connected Layer(FC Layer)를 사용하는 이유는 주로 특징을 분류하는 역할을 하기 때문입니다.<br>
><br>
>CNN은 주로 입력 이미지에서 다양한 수준의 특징을 추출합니다. 초기 계층에서는 이미지의 엣지, 텍스처, 색상과 같은 저수준 특징을 추출하고, 점점 더 높은 계층으로 갈수록 더 복잡한 패턴과 형태를 인식하게 됩니다. 그러나 이 과정은 이미지의 공간적인 정보를 그대로 유지하면서 추출된 특징들만을 반환하게 됩니다. <br>
> <br>
>이때, Fully Connected Layer(FC Layer)는 이미지를 클래스별로 분류할 수 있는 최종 결정 단계입니다. FC Layer는 입력 데이터를 **일반적인 1D 벡터로 평탄화(flatten)**한 뒤, 각 노드가 모든 이전 노드와 연결되어 있어, 이미지를 각 클래스의 확률로 변환할 수 있습니다. 이 단계에서 최종 출력은 보통 소프트맥스 함수 등을 사용해 분류 결과가 됩니다.<br>
><br>
>따라서 FC Layer는 CNN의 특징 추출과 분류 과정을 이어주는 중요한 역할을 합니다. 이 계층을 통해 CNN은 고차원적으로 추출된 특징을 바탕으로 정확한 분류를 할 수 있게 됩니다.
