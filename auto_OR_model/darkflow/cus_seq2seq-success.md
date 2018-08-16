

## References

[seq2seq 생소한 코드로 구현](https://towardsdatascience.com/seq2seq-model-in-tensorflow-ec0c557e560f)

[seq2seq_complete](https://github.com/deep-diver/EN-FR-MLT-tensorflow/blob/master/dlnd_language_translationv2.ipynb)

[seq2seq로 뉴스 제목 추론하기](https://ratsgo.github.io/natural%20language%20processing/2017/03/12/s2s/)

[배치학습 참조](https://medium.com/trackin-datalabs/input-data-tf-data-%EC%9C%BC%EB%A1%9C-batch-%EB%A7%8C%EB%93%A4%EA%B8%B0-1c96f17c3696)

[모두의 딥러닝 메인 - 김성훈 교수님](https://hunkim.github.io/ml/)

[모두의 딥러닝 - RNN 실습 슬라이드 - 김성훈 교수님](https://docs.google.com/presentation/d/1UpZVnOvouIbXd0MAFBltSra5rRpsiJ-UyBUKGCrfYoo/edit#slide=id.g1ed9069b96_0_184)

[word-rnn-tensorflow_hunkim](https://github.com/hunkim/word-rnn-tensorflow)

[텐서플로우 배치학습 방법](https://hiseon.me/2018/04/15/tensorflow-dataset/)

[텐서플로우 seq2seq API 사용법](https://github.com/j-min/tf_tutorial_plus/blob/master/RNN_seq2seq/contrib_seq2seq/01_TrainingHelper.ipynb)



## TODO

- [x] 배치는 10개인데 8개만 들어가는 현상 수정하기. ===> cus_tool.py 내용 수정으로 해결.

- [x] '\<pad\>'의 개수 잘못 들어간 것 수정하기. ===> cus_tool.py 내용 수정으로 해결.

- [x] `tf.nn.dynamic_rnn`함수의 `sequence_length` 파라미터를 사용하는 코드 구현하기.

- [x] 추론과정 구현.

- [x] 배치학습 구현.

- [ ] 인코더 부분과 디코더 부분의 사전을 따로 만들기.

- [ ] 인코더와 디코더의 weight를 어떻게 따로 저장하는지 알아보기.

- [ ] 코드 좀더 간결하게 수정. (레퍼런스를 참조하자.)

- [x] 패딩 안 넣고 플레이스홀더의 차원을 'None'으로 할 수 있는지 알아보기.

  => 불가능. 일단 패딩을 줘서 time step을 맞추고, sequence_length로 아웃풋 값을 조정해야함.

- [ ] 텐서플로우 코드를 파이토치 코드로 구현.



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

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

## 1. 필요한 모듈을 불러온다.
import tensorflow as tf
import numpy as np
import pandas as pd
import cus_tool # 직접 만든 tool 함수
tf.reset_default_graph() # 텐서플로우 그래프를 초기화 한다.

# 데이터 파일을 불러온 후 전처리를 진행한다.
corpus = pd.read_table("/Users/ku/Desktop/raw.csv", delimiter=",")
corpus = np.array(corpus)

dic, idx2word, word2idx, p_enc_batch, p_dec_batch, p_targets_batch = cus_tool.make_dic_and_split_data(corpus)
dic_len = len(dic)

# dic 
# idx2word 
# word2idx 
# p_enc_batch
# p_dec_batch
# p_targets_batch
# dic_len

## 3. 하이퍼파라미터를 설정한다.
lr = 0.01
n_hidden = 128
epochs = 100
n_class = n_input = dic_len # 입력과 출력의 형태가 one-hot 인코딩으로 같으므로 크기도 같다.
max_enc_size = max(map(len, p_enc_batch)) # 4
max_dec_size = max(map(len, p_dec_batch)) # 7
per_ckpt = 10
num_layer = 1
batch_size = 8

## 4. 모델을 만든다.
# 인덱스 값들은 정수이므로 dtype = "tf.int32"으로 한다! 안하면 나중에 에러난다.
encoder_input = tf.placeholder(dtype=tf.int32, shape=[None, None]) # (batch size=?, max_enc_size=4)
decoder_input = tf.placeholder(tf.int32, [None, None]) # (batch size=?, max_dec_size=7)
targets = tf.placeholder(tf.int32, [None, None]) # (batch size, max_dec_size=7)
# encoder_input = tf.placeholder(dtype=tf.int32, shape=[None, max_enc_size]) # (batch size=?, max_enc_size=4)
# decoder_input = tf.placeholder(tf.int32, [None, max_dec_size]) # (batch size=?, max_dec_size=7)
# targets = tf.placeholder(tf.int32, [None, max_dec_size]) # (batch size=?, max_dec_size=7)

# placeholder를 만든 직후에 one_hot 인코딩 코드를 넣어야 코드가 논리적인 순서가 맞음을 주의하자!!
oh_enc = tf.one_hot(encoder_input, dic_len); oh_enc # (batch size, max_enc_size, dic_len)
oh_dec = tf.one_hot(decoder_input, dic_len); oh_dec # (batch size, max_dec_size, dic_len)

cell = tf.contrib.rnn.BasicLSTMCell(n_hidden)
cell = tf.nn.rnn_cell.MultiRNNCell([cell] * num_layer) # multi-layer로 쌓고 싶으면 num_layer의 값을 수정한다.

# encoder의 output값은 의미 없으므로 사용하지 않는다.
_outputs, encoder_states = tf.nn.dynamic_rnn(cell, inputs=oh_enc, dtype=tf.float32)

# decoder의 states 값은 의미 없으로 사용하지 않는다.
outputs, _states = tf.nn.dynamic_rnn(cell, inputs=oh_dec, initial_state=encoder_states) # outputs : (batch siz=?, max_dec_size=7, n_hidden=128)

outputs = tf.reshape(outputs, [-1, n_hidden]) # (batch size*max_dec_size=?, n_hidden=128): 막 섞일 것 같은데... 의외로 안 섞인다 ㅎㅎ

# tf.contrib.layers.fully_connected(input, num_outputs): input 행렬을 받아서 (input의 행, num_outputs)를
# 생성하는 가중치 행렬과 바이어스 벡터를 임베드 하고 (input의 행, num_outputs)를 반환한다.
outputs = tf.contrib.layers.fully_connected(outputs, dic_len, activation_fn=None)

# reshape out for sequence_loss
outputs = tf.reshape(outputs, [-1, max_dec_size, dic_len]) # (batch size=10, max_dec_size, dic_len)
# outputs = tf.reshape(outputs, [batch_size, -1, dic_len]) # (batch size=10, max_dec_size, dic_len)

weights = tf.ones([batch_size, max_dec_size])

# tf.contrib.seq2seq.sequence_loss:
# logits: (batch size, max_dec_size, dic_len)
# targets: (batch size, max_dec_size)
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs, targets=targets, weights=weights)
loss = tf.reduce_mean(sequence_loss)

train = tf.train.AdamOptimizer(lr).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for eoch in range(epochs):
    _, b_loss = sess.run([train, loss], feed_dict={encoder_input: p_enc_batch, decoder_input: p_dec_batch, targets: p_targets_batch})
    print(b_loss)
```



