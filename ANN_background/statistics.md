## MLE(Maximum Likelihood Estimation, 최대우도추정법)

- 데이터 X가 **주어져** 있을 때(확률변수가 아니라 **상수**) 그 데이터 X가 발생할 확률을 최대로 하는 theta(parameter, 모수, **확률변수**)를 추정하는 방법.
- p(x|theta) = p(theta|x)*p(x) / p(theta)
- 예를 들어 어떤 데이터 X=1이 주어져 있고 σ2(분산) =1임을 안다고 할 때, 데이터 X가 발생할 확률을 최대로 하는 μ는 어떤 것인가? 문제를 푸는 것이 최대우도추정법임.
- log-likelhood는 concave 하므로 최적의 theta를 미분해서 한번에 구할 수 있음.
- 인공신경망에서 theta는 모든 상황에 다 들어맞는 가중치(weight)일 것인데, 가중치에 대한 loss함수는 한번에 편미분하여 최적의 값을 계산 할 수 있는 형태가 아님. 따라서 경사하강법 등의 방법을 통해서 점진적으로 최적의 가중치를 찾아나가는 것. 결국 인공신경망 알고리즘은 응용 통계임을 알 수 있음.
- 그래프로 이해하면 편하므로 아래 두 레퍼런스를 꼭 참조할 것!!



## Reference

[최대우도추정 - 데이터사이언스스쿨](https://datascienceschool.net/view-notebook/79140e6a9e364bcbb04cb8e525b9dba4/)

[최대우도추정 - ratsgo](https://ratsgo.github.io/statistics/2017/09/23/MLE/)