## mAP 계산 방법

- object = `apple`
- \# ground truth 'apple' boxes = `5`
- \# predicted 'apple' boxes = `10`
- Rank: sorted by `confidence score`
- `IoU`>0.5(threshold), correct.
- `precision` = \# correct / \# detected boxes
- `recall` = \# correct / \# ground truth boxes

| Rank | correct? | precision  |  recall   |
| :--: | :------: | :--------: | :-------: |
|  1   |    T     | 1/1 = 1.0  | 1/5 = 0.2 |
|  2   |    T     | 2/2 = 1.0  | 2/5 = 0.4 |
|  3   |    F     | 2/3 = 0.67 | 2/5 = 0.4 |
|  4   |    F     | 2/4 = 0.5  | 2/5 = 0.4 |
|  5   |    F     | 2/5 = 0.4  | 2/5 = 0.4 |
|  6   |    T     | 3/6 = 0.5  | 3/5 = 0.6 |
|  7   |    T     | 4/7 = 0.57 | 4/5 = 0.8 |
|  8   |    F     | 4/8 = 0.5  | 4/5 = 0.8 |
|  9   |    F     | 4/9 = 0.45 | 4/5 = 0.8 |
|  10  |    T     | 5/10 = 0.2 | 5/5 = 1.0 |

- 그러나 이를 그대로 적용하면 아래와 같은 지그재그 모양의 그래프를 얻는다.

![mAP_no_smooth](/miscellaneous/mAP_no_smooth.png)



- `AP`는 precision-recall curve의 *아래 영역의 넓이*를 뜻한다. 보통 recall 포인트 11개(0.1, 0.2, 0.3, … 1.0)를 기준으로 smooth하게 그래프를 바꾼 후 근사적으로 `AP`를 구한다.
- `mAP`는 클래스마다의 `AP`를 구하여 평균을 내면 된다. 0<=`AP`<=1 이므로 0<= `mAP`<=1이다. 1에 가까울수록 detection 알고리즘의 성능이 좋다고 볼 수 있다.

### [레퍼런스]

[mAP 계산 방법](https://medium.com/@jonathan_hui/map-mean-average-precision-for-object-detection-45c121a31173)



## IoU(Intersection of Union) 계산 방법

![IoU](/miscellaneous/IoU.jpg)

### [레퍼런스]

[IoU 계산 방법](http://nooverfit.com/wp/david9%E7%9A%84%E6%99%AE%E5%8F%8A%E8%B4%B4%EF%BC%9A%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89%E4%B8%AD%E7%9A%84%E5%B9%B3%E5%9D%87%E7%B2%BE%E5%BA%A6ap-%E5%B9%B3%E5%9D%87%E7%B2%BE%E5%BA%A6%E5%9D%87/jlhnn/)