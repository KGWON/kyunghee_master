# Papers Summary

## Introduction.

### 기존연구 요약 및 YOLO의 장점.

1. **`DPM(Deformable parts models)`**
- sliding windows approach. 
- 각 윈도우마다 classifier를 적용하여 속도가 느림.

2. **`R-CNN`** 
- region proposal approach. 
- ‘selective search’를 이용하여 potential bounding box를 검출한 후 그 곳에 classifier를 적용함. 
- 후처리(post-processing)과정도 있어서 매우 복잡한 pipeline을 가진다. 
- 각 과정에 최적화가 개별로 이루어지기 때문에 속도가 느림.

3. **`YOLO`**
- 단일 CNN(single convolutional neural network)으로 경계박스(bounding box) 및 클래스 스코어를 예측할 수 있음. 

- YOLO는 전체 이미지를 한번에 학습하기 때문에 일반화된 특징을 더 잘 추출함.

- 복잡한 pipeline을 하나로 통합(unified) 하였기 때문에 속도가 빠름.

  

### Unified Detection.

1. 전체 이미지를 `S * S` 개의 grid cell로 분할.

2. grid cell마다 클래스 개수만큼의 `class probability`와 `B`개의 경계박스를 가지고 있음. 각 경계박스는 object의 `x, y, w, h, confidence score`를 포함함. 

   - _confidence score_ = ![](/Users/ku/kyunghee_master/miscellaneous/yolo_confidence.svg), obeject가 없으면  __'0'__
   - _class probability_ = ![](/Users/ku/kyunghee_master/miscellaneous/yolo_class_probability.svg)
   - _class specific confidence_ = _confidence score * class probability_

   > *confidence score*: 모델이 예측한 bbox가 얼마나 신뢰도 있게 object를 포함하는지, 그 예측이 얼마나 정확한지를 나타내는 지표.


3. 따라서 YOLO의 최종 아웃풋 사이즈는 `S * S * (B * 5 + #class)`



#### Network design

<img src = "~/miscellaneous/yolo_v1_network.png">

- input size: 448 * 448 (다른 크기의 사진을 인풋 시켜도 자동으로 448 * 448로 `resize`한다.)
- activation function: leaky relu
- loss function: sum-squared error(it is easy to optimize)
- <img src = "~/miscellaneous/yolo_loss_function.png">
- ![](/Users/ku/kyunghee_master/miscellaneous/lambda.svg): confidence score가 대부분 '0'이어서 object를 포함한 셀의 gradient가 과대평가 될 우려가 있기 때문에 object가 포함된 셀에는 페널티를 많이 주고, object가 없는 셀에는 페널티를 적게 주기 위함.             

  - <img src = "~/miscellaneous/lambda_coord.svg"> = 5 (최적화 시 object가 있는 셀에 더욱 집중 하게 된다.)
  - <img src = "~/miscellaneous/lambda_noobj.svg"> = 0.5(최적화 시 object가 없는 셀은 덜 집중 하게 된다.)



#### LImitations of YOLO

1. `Spatial constraint`: 각 그리드 셀은 오직 B개의 bbox를 가질 수 있고 각 bbox는 하나의 클래스만 예측할 수 있음.

2. `struggle swith small object`: 크기가 작은 object는 잘 탐지하지 못함.

3. `loss function`: 큰 bbox에서 발생하는 에러와 작은 bbox에서 발생하는 에러의 절대적인 수치가 같으면 이를 동일하게 취급함.

   > A small error in a large box is generally benign but a small error in a small box has a much greater effect on IOU



## 더욱 자세한 YOLO bounding box 원리는… 아래 슬라이드를 참조!

[YOLO 슬라이드](https://docs.google.com/presentation/d/1aeRvtKG21KHdD5lg6Hgyhx5rPq_ZOsGjG5rJ1HP7BbA/pub?start=false&loop=false&delayms=3000&slide=id.p)

