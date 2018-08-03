# You Only Look Once: Unified, Real-Time Object Detection **summary**

## Introduction.

### 기존연구 및 yolo의 장점.
1. `DPM(Deformable parts models)`
- sliding windows approach. 
- 각 윈도우마다 classifier를 적용하여 속도가 느림.

2. `R-CNN` 
- region proposal approach. 
- ‘selective search’를 이용하여 potential bounding box를 검출한 후 그 곳에 classifier를 적용함. 
- 후처리(post-processing)과정도 있어서 매우 복잡한 pipeline을 가진다. 
- 각 과정에 최적화가 개별로 이루어지기 때문에 속도가 느림..

3. `YOLO`: 
- **단일 CNN(single convolutional neural network)**으로 경계박스 및 클래스 스코어를 예측할 수 있음. 
- YOLO는 **전체** 이미지를 한번에 학습하기 때문에 일반화된 특징을 더 잘 추출함.
- 복잡한 pipeline을 하나로 통합(unified) 하였기 때문에 속도가 빠름.
- 

### Unified Detection
1. 전체 이미지를 `S * S` 개의 grid cell로 분할.

2. grid cell마다 클래스 개수만큼의 `class probability`와 `B`개의 경계박스를 가지고 있음. 각 경계박스는 object의 x, y, w, h, confidence를 포함함. 


3. 따라서 YOLO의 최종 아웃풋 사이즈는 `S * S * (B * 5 + #class)`