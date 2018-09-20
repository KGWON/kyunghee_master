## 주요 파일 설명

**`/yolov3.weights`**: yolov3에 pre-trained된 가중치.


**`/data/train.txt`**: 학습에 사용 할 이미지 리스트. 개행으로 구분.


**`/data/test.txt`**: 테스트에 사용 할 이미지 리스트. 개행으로 구분.


**`/data/imgs`**: 학습 및 테스트에 사용할 모든 이미지(class, x, y, width, height).


**`/data/cus_obj.data`**: 클래스 개수, 클래스 이름이 담긴 파일의 경로, 학습 이미지 폴더 경로 지정, 학습 진행시 가중치 파일이 저장될 경로 등 지정.
~~~
classes = <클래스 개수>
train = <train.txt 파일경로> 예) data/train.txt
valid = <test.txt 파일경로> 예) data/test.txt
names = <.names 파일경로> 예) data/cus_obj.names
backup = <학습시 가중치가 저장되는 폴더경로>
~~~

**`/data/cus_obj.names`**: 클래스 목록. 개행으로 구분.


**`/darknet53.conv.74`**: 처음으로 학습시킬 때 사용하는 가중치.


**`/data/makeTrainTest.py`**: 사용자가 지정한 폴더에 있는 이미지를 일정 비율로 분할하여 train.txt와 test.txt 파일을 생성하는 파이썬 스크립트.

## 학습 및 테스트 코드


**학습**
~~~
./darknet detector train <.data 파일경로> <.cfg 파일경로> <초기 가중치파일 경로>
./darknet detector train data/cus_obj.data cfg/cus_yolov3.cfg darknet53.conv.74
~~~


**테스트**
~~~
./darknet detector test <.data 파일경로> <.cfg 파일경로> <.weights 파일경로> <.jpg 파일경로>
./darknet detector test data/cus_obj.data  cfg/cus_yolov3.cfg backup/cus_yolov3_10000.weights data/imgs/dal_t0.jpg

./darknet detector test <.data 파일경로> <.cfg 파일경로> <.weights 파일경로> <<test.txt파일 경로>> <결과가 출력 될 파일 경로>
./darknet detector test data/cus_obj.data cfg/cus_yolov3.cfg backup/cus_yolov3_10000.weights <data/test.txt> result.txt
~~~


참고) 테스트 시 `.data`파일을 명시해 주지 않으면 `coco.data`파일을 사용하게 되므로 주의가 필요함.



## 레퍼런스

[yolo_v1 슬라이드](https://docs.google.com/presentation/d/1aeRvtKG21KHdD5lg6Hgyhx5rPq_ZOsGjG5rJ1HP7BbA/pub?start=false&loop=false&delayms=3000&slide=id.p)

[yolo_v1 슬라이드 해석 블로그](http://blog.naver.com/PostView.nhn?blogId=sogangori&logNo=220993971883&parentCategoryNo=6&categoryNo=&viewDate=&isShowPopularPosts=true&from=search)

[yolo_v1 논문](https://arxiv.org/abs/1506.02640)

[mAP 계산 방법](https://medium.com/@jonathan_hui/map-mean-average-precision-for-object-detection-45c121a31173)

<br>

<br>

<br>

# OpenCV Compile 3.4 for Anaconda Python 3.7, 3.6, 3.5, 3.4 and 2.7

**Settings:**

- OS: ubuntu 16.04
- anaconda python: 3.6
- cuda: 9.0
- cuDNN: 7.x
- opencv: 3.4.0
- yolov3

### 1.opencv를 설치할 폴더를 만들고 opencv 3.4.0 버전을 다운받은후 압축을 풀어준다.

```
mkdir opencv
cd opencv
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.0.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.0.zip
unzip opencv_contrib.zip
```

### 2. opencv-3.4.0 폴더로 이동 후 빌드를 위해서 build 폴더를 만들어 준 후 해당 폴더로 이동한다.

```
cd opencv-3.4.0/
mkdir build
cd build
```

### 3. 컴파일 설정을 해준다.

```
cmake -DBUILD_TIFF=ON -DBUILD_opencv_java=OFF -DWITH_CUDA=OFF -DWITH_OPENGL=ON -DWITH_OPENCL=ON -DWITH_IPP=ON -DWITH_TBB=ON -DWITH_EIGEN=ON -DWITH_V4L=ON -DWITH_VTK=OFF -DBUILD_TESTS=OFF -DBUILD_PERF_TESTS=OFF -DCMAKE_BUILD_TYPE=RELEASE ..
```

> 다음과 같은 메시지가 보이면 정상적으로 된 것임:

> -- Configuring done

> -- Generating done

> -- Build files have been written to: /home/webnautes/opencv/opencv-3.4.0/build

> 또한 cmake의 결과에 아래와 같은 내용이 있어야 나중에 에러가 안남:

> Python 3:

> --     Interpreter:                 /usr/bin/python3 (ver 3.5.2)

> --     Libraries:                   /usr/lib/x86_64-linux-gnu/libpython3.5m.so (ver 3.5.2)

> --     numpy:                       /usr/lib/python3/dist-packages/numpy/core/include (ver 1.11.0)

> --     packages path:               lib/python3.5/dist-packages

### 4. 빌드하고 제대로 빌드가 되었는지 확인한다.

```
make -j -l 2
cat /etc/ld.so.conf.d/*
sudo ldconfig
```

> "/usr/local/lib"가 있으면 제대로 된 것. 없으면 레퍼런스 참조하여 수정

### 5. 최종적으로 빌드가 잘 되었는지 확인한다.

```
pkg-config --modversion opencv
```

> 결과가 3.4.0 이면 정상적으로 빌드 된 것

```
pkg-config --libs --cflags opencv
```

> 여러 문자가 출력 되면 정상적으로 빌드 된 것

### 6. 참조 : 빌드된 opencv를 지워야 할 경우

```
cd opencv/opencv-3.4.0/build
sudo make uninstall
pkg-config --modversion opencv
```

> 결과가 '없다'로 나오면 제대로 삭제 된 것



## 레퍼런스

- https://www.scivision.co/anaconda-python-opencv3/
- http://webnautes.tistory.com/1030



