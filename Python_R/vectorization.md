## R과 파이썬의 대표적인 차이점- 내장함수의 '벡터연산' 지원

- R은 내장함수가 기본적으로 벡터연산을 지원하도록 되어 있다. 아래 코드를 살펴보자.

  ~~~R
  a <- c(1, 2, 3)
  b <- c(4, 5, 6)
  print(a+b) # 결과는 (5, 7, 9)
  ~~~

- 파이썬은 내장함수가 기본적으로 지원하지 않는다. 아래 코드를 살펴보자. R에 익숙한 사용자는 파이썬 결과가 당황스럽다.

  ~~~python
  a = [1, 2, 3]
  b = [4, 5, 6]
  print(a+b) # 결과는 [1, 2, 3, 4, 5, 6]
  ~~~

- 파이썬에서 벡터연산을 하는 방법은 3가지로 생각해 볼 수 있다.

  - 리스트, 튜플 등을 numpy 모듈의 ndarray형으로 변환: ndarray는 벡터연산을 지원한다.

  - 리스트, 튜플 등을 pandan 모듈의 series형으로 변환: series는 벡터연산을 지원한다.

  - list comprehension 이나 map, filter 함수를 이용

    ~~~python
    a = [1, 2, 3]
    b = [4, 5, 6]
    
    # 아래 코드는 같은 결과를 리턴한다. 그러나 map으로 구현한 것이 좀더 속도가 빠를 것 같다...
    list(map(lambda x, y: x + y, a, b)) # [5, 7, 9]
    [x + y for x, y in zip(a,b)] # [5, 7, 9]
    ~~~

- (추가사항) a, b 두개의 리스트가 있을 때, a 리스트의 item이 b원소에 속해 있는지 여부를 True, False로 반환하는 방법

  ~~~python
  a = ['a', 'b', 'c', 'd', 'e', 'f']
  b = ['d', 'e', 'f']
  
  # 아래 코드는 같은 결과를 리턴한다.
  list(map(lambda item: item in b, a)) # [False, False, False, True, True, True]
  [item in b for item in a] # [False, False, False, True, True, True]
  ~~~
