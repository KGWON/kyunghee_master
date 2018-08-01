## 주요 파일 설명

- **/yolov3.weights**: yolov3에 pre-trained된 가중치.


- **/data/train.txt**: 학습에 사용 할 이미지 리스트. 개행으로 구분.


- **/data/test.txt**: 테스트에 사용 할 이미지 리스트. 개행으로 구분.


- **/data/imgs**: 학습 및 테스트에 사용할 모든 이미지(class, x, y, width, height).


- **/data/cus_obj.data**: 클래스 개수, 클래스 이름이 담긴 파일의 경로, 학습 이미지 폴더 경로 지정, 학습 진행시 가중치 파일이 저장될 경로 등 지정.
~~~
classes = <클래스 개수>
train = <train.txt 파일경로> 예) data/train.txt
valid = <test.txt 파일경로> 예) data/test.txt
names = <.names 파일경로> 예) data/cus_obj.names
backup = <학습시 가중치가 저장되는 폴더경로>
~~~

- **/data/cus_obj.names**: 클래스 목록. 개행으로 구분.


- **/darknet53.conv.74**: 처음으로 학습시킬 때 사용하는 가중치.


- **/data/makeTrainTest.py**: 사용자가 지정한 폴더에 있는 이미지를 일정 비율로 분할하여 train.txt와 test.txt 파일을 생성하는 파이썬 스크립트.

## 학습 및 테스트 코드


**학습**
- 코드: ./darknet detector train <.data 파일경로> <.cfg 파일경로> <초기 가중치파일 경로>
- 예시: ./darknet detector train data/cus_obj.data cfg/cus_yolov3.cfg darknet53.conv.74


**테스트**
- 코드: ./darknet detector test <.data 파일경로> <.cfg 파일경로> <.weights 파일경로> <.jpg 파일경로>
- 예시: ./darknet detector test data/cus_obj.data  cfg/cus_yolov3.cfg backup/cus_yolov3_10000.weights data/imgs/dal_t0.jpg
참고) 테스트 시 .data파일을 명시해 주지 않으면 coco.data파일을 사용하게 되므로 주의가 필요함.
