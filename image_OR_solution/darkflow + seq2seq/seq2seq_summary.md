

## 레퍼런스

[seq2seq 생소한 코드로 구현](https://towardsdatascience.com/seq2seq-model-in-tensorflow-ec0c557e560f)

[seq2seq_complete](https://github.com/deep-diver/EN-FR-MLT-tensorflow/blob/master/dlnd_language_translationv2.ipynb)

[seq2seq로 뉴스 제목 추론하기](https://ratsgo.github.io/natural%20language%20processing/2017/03/12/s2s/)

[모두의 딥러닝 메인 - 김성훈 교수님](https://hunkim.github.io/ml/)

[모두의 딥러닝 - RNN 실습 슬라이드 - 김성훈 교수님](https://docs.google.com/presentation/d/1UpZVnOvouIbXd0MAFBltSra5rRpsiJ-UyBUKGCrfYoo/edit#slide=id.g1ed9069b96_0_184)

[word-rnn-tensorflow_hunkim](https://github.com/hunkim/word-rnn-tensorflow)

[텐서플로우 배치학습 방법_1](https://medium.com/trackin-datalabs/input-data-tf-data-%EC%9C%BC%EB%A1%9C-batch-%EB%A7%8C%EB%93%A4%EA%B8%B0-1c96f17c3696)

[텐서플로우 배치학습 방법_2](https://hiseon.me/2018/04/15/tensorflow-dataset/)

[배치 학습 시 버퍼사이즈의 역할](https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle)

[텐서플로우 seq2seq API 사용법](https://github.com/j-min/tf_tutorial_plus/blob/master/RNN_seq2seq/contrib_seq2seq/01_TrainingHelper.ipynb)

[가장 많이 참고한 코드](https://nbviewer.jupyter.org/github/aisolab/CS20/blob/master/Lec12_Seq2Seq%20with%20Attention/Lec12_Seq2Seq%20by%20Encoder%20RNN%20and%20Decoder%20RNN.ipynb)



## 반성의 시간 및 교훈

- `placeholder`: 리스트나 넘파이 배열같은 데이터를 `tensor`로 전환 해주는 역할. 플레이스홀더를 코드 상단에서 먼저 선언해 주어야 코드를 계획할 때 혼돈이 없다.
- `tf.one-hot`: *(batch size, time steps)* ---> *(batch size, time steps, vocabulary size)*로 전환 해 준다. shape 변환에 주의하자. 이거 때문에… 거의 이틀을 코드만 보고 있었다...
- 셀을 쌓을 때 마다 shape를 주의하고 주의하고 또 주의하자… 꼭 중간중간 세션을 실행시켜서 실제 결과를 확인해 보자.
- RNN은 대부분 문자 데이터를 다루므로 CNN에 비해서 전처리에 시간이 많이 걸린다… 꾸준히 연습하자.
- 스크래치부터 개발을 할 때는 파이참보다 주피터노트북이 좋은 것 같다. 작은 코드 블럭 별로 인풋을 피드 시킨다음 아웃풋이 생각한 것과 같은 형태 (특히 shape!!)인지 확인 해보면서 블럭을 쌓자.
- `sess.run`: `Tensor`에 담긴 내용을 실행시켜주는 역할. **그 결과** 데이터 타입은 np.ndarray, list, scalr 등이 되는 것임.
- `tf.shape(tensor)`: 모델의 input을 dynamic shape로 하였으므로.. tf.shape(btc_enc_seq_len)로 해야 한다. btc_enc_seq_len.shape는 static shape일 때 사용 하는 것이다. `tensor.shape`하면 None의 shape를 구할 수 없으므로 에러가 난다.
- `텐서의 차원`: 에러는 거의 대부분 텐서의 차원을 제대로 맞추지 못해서 발생하는 문제이다. 따라서 디버깅 할 때는 `sess.run(의심되는 텐서).shape`를 통해서 텐서플로우가 기대하는 텐서의 차원과 내가 짠 코드로 만들어진 텐서의 차원이 어떻게 다른지… 그리고 왜 이런 결과가 발생했는지를 생각해보자. 




## 모델 그림으로 나타내기

![seq2seq_1](/miscellaneous/seq2seq_1.png)

![seq2seq_2](/miscellaneous/seq2seq_2.png)



## seq2seq에서 쓰이는 용어 정리

- mask(masking, weight, ...): seq2seq 셀을 쌓을 때 <pad> 토큰 부분의 해당하는 outputs은 '0'으로 하여 모델의 loss에 반영되지 않도록 하기 위한 테크닉.
- embedding layer: 데이터를 인덱스 값으로 변환 한 다음 그 값을 그대로 쓰는 것이 아니라 다른 형태로 임베딩(e.g. 원-핫 인코딩, word2vec)해 주는 레이어.



## 구현 코드

[텐서플로우 코드 보기](/auto_OR_model/darkflow_seq2seq/seq2seq_success_180816.ipynb)