# OpenCV Compile 3.4 for Anaconda Python 3.7, 3.6, 3.5, 3.4 and 2.7

**Settings:**
- OS: ubuntu 16.04
- anaconda python: 3.6
- cuda: 9.0
- cuDNN: 7.x
- opencv: 3.4.0
- yolov3


### 1.opencv를 설치할 폴더를 만들고 opencv 3.4.0 버전을 다운받은후 압축을 풀어준다.
~~~
mkdir opencv
cd opencv
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.0.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.0.zip
unzip opencv_contrib.zip
~~~


### 2. opencv-3.4.0 폴더로 이동 후 빌드를 위해서 build 폴더를 만들어 준 후 해당 폴더로 이동한다.
~~~
cd opencv-3.4.0/
mkdir build
cd build
~~~


### 3. 컴파일 설정을 해준다.
~~~
cmake -DBUILD_TIFF=ON -DBUILD_opencv_java=OFF -DWITH_CUDA=OFF -DWITH_OPENGL=ON -DWITH_OPENCL=ON -DWITH_IPP=ON -DWITH_TBB=ON -DWITH_EIGEN=ON -DWITH_V4L=ON -DWITH_VTK=OFF -DBUILD_TESTS=OFF -DBUILD_PERF_TESTS=OFF -DCMAKE_BUILD_TYPE=RELEASE ..
~~~

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
~~~
make -j -l 2
cat /etc/ld.so.conf.d/*
sudo ldconfig
~~~
> "/usr/local/lib"가 있으면 제대로 된 것. 없으면 레퍼런스 참조하여 수정


### 5. 최종적으로 빌드가 잘 되었는지 확인한다.
~~~
pkg-config --modversion opencv
~~~

> 결과가 3.4.0 이면 정상적으로 빌드 된 것

~~~
pkg-config --libs --cflags opencv
~~~
> 여러 문자가 출력 되면 정상적으로 빌드 된 것

	
### 6. 참조 : 빌드된 opencv를 지워야 할 경우
~~~
cd opencv/opencv-3.4.0/build
sudo make uninstall
pkg-config --modversion opencv
~~~

> 결과가 '없다'로 나오면 제대로 삭제 된 것

## [Reference]
- https://www.scivision.co/anaconda-python-opencv3/
- http://webnautes.tistory.com/1030




