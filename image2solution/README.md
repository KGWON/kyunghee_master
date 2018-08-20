## image2solution 논문 컨셉

- YOLO + seq2seq + find OR model and optimal solution
  - YOLO를 통해 이미지의 객체를 탐지한 후 그 결과를 seq2seq 모델에 인풋시켜 원하는 sentence를 생성
  - sentence를 이용하여 이미지에 가장 적합한 OR model을 추천하고 최적의 해를 찾는 기능을 자동화하여 엑셀파일로 출력

## TODO

- [x] seq2seq 모델 구현
  - [x] 배치는 10개인데 8개만 들어가는 현상 수정하기. ===> toosl.py 내용 수정으로 해결.
  - [x] '\<pad\>'의 개수 잘못 들어간 것 수정하기. ===> tools.py 내용 수정으로 해결.
  - [x] `tf.nn.dynamic_rnn`함수의 `sequence_length` 파라미터를 사용하는 코드 구현하기.
  - [x] 추론과정 구현. => greedy embedding 함수.
  - [x] 배치학습 구현.
  - [ ] 가중치 파일 저장하는 것 구현.
  - [ ] 인코더 부분과 디코더 부분의 사전을 따로 만들기.
  - [ ] 인코더와 디코더의 weight를 어떻게 따로 저장하는지 알아보기.
  - [ ] 코드 좀더 간결하게 수정. (레퍼런스를 참조하자.)
  - [ ] 텐서플로우 코드를 파이토치 코드로 구현.
- [ ] darkflow(YOLO v2의 텐서플로우 버전)의 결과를 seq2seq 모델에 인풋시키는 코드 구현
- [ ] seq2seq 모델의 출력 문장을 통해 적합한 OR 모델을 제시 (교수님 부분)
- [ ] seq2seq 모델의 출력 문장을 query로 하여 DB에서 관련 수치를 꺼낸 후 수송모델의 틀을 짜는 코드 구현

<br>

## 레퍼런스

- yolo 레퍼런스
  - [darkflow github](https://github.com/thtrieu/darkflow)
  - [darkflow를 활용한 자동차 번호판 인식](https://park-ju-hyeong.github.io/2018/04/11/%E1%84%8C%E1%85%A1%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8E%E1%85%A1-%E1%84%87%E1%85%A5%E1%86%AB%E1%84%92%E1%85%A9%E1%84%91%E1%85%A1%E1%86%AB-%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8-(OCR)-with-YOLO-v2/)[darkflow github](https://github.com/thtrieu/darkflow)

- seq2seq 레퍼런스
  - [seq2seq 생소한 코드로 구현](https://towardsdatascience.com/seq2seq-model-in-tensorflow-ec0c557e560f)
  - [seq2seq_complete](https://github.com/deep-diver/EN-FR-MLT-tensorflow/blob/master/dlnd_language_translationv2.ipynb)
  - [텐서플로우 seq2seq API 사용법](https://github.com/j-min/tf_tutorial_plus/blob/master/RNN_seq2seq/contrib_seq2seq/01_TrainingHelper.ipynb)
  - [배치 학습 시 버퍼사이즈의 역할](https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle)
  - [텐서플로우 배치학습 방법_1](https://medium.com/trackin-datalabs/input-data-tf-data-%EC%9C%BC%EB%A1%9C-batch-%EB%A7%8C%EB%93%A4%EA%B8%B0-1c96f17c3696)
  - [텐서플로우 배치학습 방법_2](https://hiseon.me/2018/04/15/tensorflow-dataset/)
  - [word-rnn-tensorflow_hunkim](https://github.com/hunkim/word-rnn-tensorflow)
  - [모두의 딥러닝 - RNN 실습 슬라이드 - 김성훈 교수님](https://docs.google.com/presentation/d/1UpZVnOvouIbXd0MAFBltSra5rRpsiJ-UyBUKGCrfYoo/edit#slide=id.g1ed9069b96_0_184)
  - [모두의 딥러닝 메인 - 김성훈 교수님](https://hunkim.github.io/ml/)
  - [seq2seq로 뉴스 제목 추론하기](https://ratsgo.github.io/natural%20language%20processing/2017/03/12/s2s/)
  - [가장 많이 참고한 코드](https://nbviewer.jupyter.org/github/aisolab/CS20/blob/master/Lec12_Seq2Seq%20with%20Attention/Lec12_Seq2Seq%20by%20Encoder%20RNN%20and%20Decoder%20RNN.ipynb)