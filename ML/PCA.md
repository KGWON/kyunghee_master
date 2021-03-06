**[terry님의 PCA 1](https://www.youtube.com/watch?v=9UggjVi9-9M&list=PL0oFI08O71gKEXITQ7OG2SCCXkrtid7Fq&index=27), [terry님의 PCA 2](https://www.youtube.com/watch?v=kMYRnyvtLC8&list=PL0oFI08O71gKEXITQ7OG2SCCXkrtid7Fq&index=28), [주재걸 교수님의 인공지능을 위한 선형대수학](https://www.edwith.org/linearalgebra4ai)을 참고하여 작성하였습니다.**



## PCA(Principal Component Analysis, 주성분분석)

대표적인 차원축소 기법 중 하나이다. 차원 축소 기법은 데이터의 시각화에 주로 이용되는데 근본적으로는 데이터들이 실제로 '살고 있는' 잠재공간(latent space)을 찾아내는 기법이라고 볼 수 있다. PCA는 철저히 선형대수학 개념을 바탕으로 설계되었고 다른 차원축소 기법들의 모태가 되기 때문에 잘 알아두면 머신러닝에 필요한 기본적인 수리적 지식을 쌓는데 도움이 될 것이다. 그러나 PCA는 몇 가지 가정을 바탕으로 하기 때문에 내가 가진 데이터가 PCA의 가정에 부합하지 않는다면 다른 차원축소 기법들을 고려해보아야하낟.



#### PCA의 기본가정 및 한계점.

- 선형성(linearity): 데이터들이 **선형관계**라고 가정하기 때문에 PCA가 찾은 새로운 축은 항상 **직선**이다. 내가 가진 데이터가 선형적인 특징을 보인다면 PCA가 답이 될 수도 있으나 굽은 좌표계가 더 적합하다면 PCA를 사용하지 말아야 한다.
- 분산이 큰 축이 가장 중요한 축이다:  데이터가 살고 있는 N차원 공간에서 분산이 가장 큰 축을 가장 먼저 찾은 다음 그 축과 직교하면서 두번째로 분산이 큰 축을 찾고 ... 이 과정을 반복하여 N개의 주성분을 찾는 과정이 PCA이다. 그러나 분산이 가장 크다고 해서 항상 그 축이 가장 중요한 축이라고는 할 수 없다. 예를들어 스케일의 크기가 다른 두 변수 A(10 ~ 1000)와 B(0.001 ~ 0.09)가 있을 때, 스케일의 차이에 의해서 A축의 분산이 **당연히** 크게 나타난다. 이것은 normalize의 중요성이라고도 볼 수 있다.
- 주성분은 서로 직교한다: PCA를 통해 찾은 새로운 축은 항상 직교한다는 가정이다. 하지만 데이터에 따라서 latent space가 반드시 직교이지 않을 수도 있다.



#### PCA의 과정

- 공분산행렬(covariance matrix)을 만든다.
- 대각화를 통해서 고유값과 고유벡터를 찾는다.
- 상위 N개의 고유값과 그에 상응하는 고유벡터를 찾아내고 고유벡터를 새로운 축으로 정의한다. 

### 





