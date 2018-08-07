# darkflow 사용법

### 1. 파이썬에서 darkflow 결과를 받아보는 방법

####   1) 터미널에서 ipython 또는 python을 실행시킨다. (root에서 실행함을 주의하자.)

![ipython_screenshot](/miscellaneous/ipython_screenshot.png)



####   2) 다음의 코드를 한줄 씩 실행한다.

~~~python
from darkflow.net.build import TFNet
import cv2

# 모델의 파라미터를 지정 해 준다. 
# 아래 명시된 파라미터 외의 다양한 파라미터는 "./darkflow/net/defaults.py" 파일을 참조하거나 터미널에서 "flow --h"를 실행시킨다.
# 상대경로를 주의하자.
options = {"model": "./darkflow/cfg/yolo.cfg", 
           "load": "./darkflow/bin/yolo.weights", 
           "config": "./darkflow/cfg", "threshold": 0.4, 
           "gpu": 0.9,
           "imgdir": "./darkflow/sample_img"}

# 파라미터를 이용하여 모델을 빌드한다.
tfnet = TFNet(options)

# numpy.ndarray 형태의 이미지만 인풋 시킬 수 있다.
imgcv = cv2.imread("./sample_img/sample_dog.jpg")
result = tfnet.return_predict(imgcv)
print(result)
~~~



####   3) result 객체에는 아래와 같은 결과가 담긴다.

![ipython_result](/miscellaneous/ipython_result.png)





---

### Reference

[darkflow github](https://github.com/thtrieu/darkflow)

[darkflow를 활용한 자동차 번호판 인식](https://park-ju-hyeong.github.io/2018/04/11/%E1%84%8C%E1%85%A1%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8E%E1%85%A1-%E1%84%87%E1%85%A5%E1%86%AB%E1%84%92%E1%85%A9%E1%84%91%E1%85%A1%E1%86%AB-%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8-(OCR)-with-YOLO-v2/)

