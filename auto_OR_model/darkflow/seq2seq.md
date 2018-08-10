# seq2seq 

### Reference

https://github.com/golbin/TensorFlow-Tutorials/blob/master/10%20-%20RNN/03%20-%20Seq2Seq.py



### 1. 학습된 darkflow에 이미지를 입력시켜서 결과 값을 얻는다 (파이썬 딕셔너리 형태)

~~~python
## 1. 필요한 모듈을 불러온다.
import tensorflow as tf
import numpy as np

## 2. 단어사전(dic)을 만든다.
'''
    <pad>: 시퀀스 최대 길이보다 문장의 길이가 짧으면 부족한 길이를 채우는 토큰.
    <start>: 디코더의 첫 인풋. 문장의 시작을 알리는 토큰.
    <end>: 디코더의 최종 아웃풋. 문장의 끝을 알리는 토큰.
'''

dic = ['dallas', 'chicago', 'losangeles', 'newyork', 'miami', 'take', 'off', 'land', 'from', 'plane', 'at',
       '<pad>','<start>', '<end>']
idx2word = {i: w for i, w in enumerate(dic)}; print(idx2word)
# word2idx = {w: i for i, w in enumerate(dic)}
word2idx = {item[1]: item[0] for item in idx2word.items()} ; print(word2idx)
dic_len = len(dic)

## 3. 학습데이터를 만든다.(현재 단계에서는 수기로 작성한다.)
# yolo_res = [['dallas', 'take', 'off'],
#             ['dallas', 'land'],
#             ['chicago', 'take', 'off'],
#             ['chicago', 'land'],
#             ['losangeles', 'take', 'off'],
#             ['losangeles', 'land'],
#             ['newyork', 'take', 'off'],
#             ['newyork', 'land'],
#             ['miami', 'take', 'off'],
#             ['miami', 'land']]
#
# sentence = [['plane', 'take', 'off', 'from', 'dallas'],
#             ['plane', 'land', 'at', 'dallas'],
#             ['plane', 'take', 'off', 'from', 'chicago'],
#             ['plane', 'at', 'chicago'],
#             ['plane', 'take', 'off', 'from', 'losangeles'],
#             ['plane', 'land', 'at', 'losangeles'],
#             ['plane', 'take', 'off', 'from', 'newyork'],
#             ['plane', 'land', 'at', 'newyork'],
#             ['plane', 'take', 'off', 'from', 'miami'],
#             ['plane', 'land', 'at', 'miami']]

seq_data = [[['dallas', 'take', 'off'], ['plane', 'take', 'off', 'from', 'dallas']],
            [['dallas', 'land'], ['plane', 'land', 'at', 'dallas']],
            [['chicago', 'take', 'off'], ['plane', 'take', 'off', 'from', 'chicago']],
            [['chicago', 'land'], ['plane', 'at', 'chicago']],
            [['losangeles', 'take', 'off'],['plane', 'take', 'off', 'from', 'losangeles'] ],
            [['losangeles', 'land'], ['plane', 'land', 'at', 'losangeles']],
            [['newyork', 'take', 'off'], ['plane', 'take', 'off', 'from', 'newyork']],
            [['newyork', 'land'], ['plane', 'land', 'at', 'newyork']],
            [['miami', 'take', 'off'], ['plane', 'take', 'off', 'from', 'miami']],
            [['miami', 'land'], ['plane', 'land', 'at', 'miami']]]

def make_batch(seq_data):
    enc_batch = [] # (batch size, enc_seq_len, input_dim)
    dec_batch = [] # (batch size, dec_seq_len, input_dim)
    target_batch = []

    for seq in seq_data:
        # 인코더 셀의 입력값. 입력단어의 글자들을 한글자씩 떼어 배열로 만든다.
        input = [word2idx[n] for n in seq[0]]
        # 디코더 셀의 입력값. 시작을 나타내는 S 심볼을 맨 앞에 붙여준다.
        output = [word2idx[n] for n in ['<start>'] + seq[1]]
        # 학습을 위해 비교할 디코더 셀의 출력값. 끝나는 것을 알려주기 위해 마지막에 E 를 붙인다.
        target = [word2idx[n] for n in seq[1] + ['<end>']]

        enc_batch.append(np.eye(dic_len)[input])
        dec_batch.append(np.eye(dic_len)[output])
        # 출력값만 one-hot 인코딩이 아님 (sparse_softmax_cross_entropy_with_logits 사용)
        target_batch.append(target)

    return enc_batch, dec_batch, target_batch

enc_batch, dec_batch, target_batch = make_batch(seq_data)

enc_seq_len = [len(batch) for batch in enc_batch]
dec_seq_len = [len(batch) for batch in dec_batch]

# def make_batch_checker(batches):
#     for batch in batches:
#         if type(batch) == list:
#             print(' '.join([idx2word[idx] for idx in batch]))
#         else:
#             print(' '.join([idx2word[idx] for idx in np.argmax(batch, -1)]))

## 3. 하이퍼파라미터를 설정한다.
lr = 0.01
n_hidden = 128
epochs = 100
n_class = n_input = dic_len # 입력과 출력의 형태가 one-hot 인코딩으로 같으므로 크기도 같다.

## 4. seq2seq 모델을 구성한다.
# placeholder를 정의한다.
enc_input = tf.placeholder(tf.float32, [None, None, n_input]) # [batch size, time steps, input dim]
dec_input = tf.placeholder(tf.float32, [None, None, n_input]) # [batch size, time steps, input dim]
targets = tf.placeholder(tf.int64, [None, None]) # [batch size, time steps]

# 인코더 셀을 구성한다.
with tf.variable_scope('encode'):
    enc_cell = tf.contrib.rnn.BasicLSTMCell(n_hidden)
    # enc_cell = tf.nn.rnn_cell.DropoutWrapper(enc_cell, output_keep_prob=0.5)

    outputs, enc_states = tf.nn.dynamic_rnn(enc_cell, enc_input, sequence_length=enc_seq_len, dtype=tf.float32)

# 디코더 셀을 구성한다.
with tf.variable_scope('decode'):
    dec_cell = tf.contrib.rnn.BasicLSTMCell(n_hidden)
    # dec_cell = tf.nn.rnn_cell.DropoutWrapper(dec_cell, output_keep_prob=0.5)

    outputs, dec_states = tf.nn.dynamic_rnn(dec_cell, dec_input, sequence_length=dec_seq_len, initial_state=enc_states, dtype=tf.float32)

# model = tf.contrib.layers.fully_connected(outputs, n_class, activation=None)
model = tf.layers.dense(outputs, n_class, activation=None) # activation은 없음을 주의하자! (projection layer는 활성화 함수를 넣지 않는다.)
cost = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=model, labels=targets))
optimizer = tf.train.AdamOptimizer(lr).minimize(cost)

## 5. 모델을 학습 시킨다.
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for epoch in range(epochs):
    _, loss = sess.run([optimizer, cost], feed_dict={enc_input: enc_batch,
                                                     dec_input: dec_batch,
                                                     targets: target_batch})

    print('Epoch:', '%04d' % (epoch + 1),
          'cost =', '{:.6f}'.format(loss))

print('최적화 완료!')


#########
# 번역 테스트
######
# 단어를 입력받아 번역 단어를 예측하고 디코딩하는 함수
def translate(word):
    # 이 모델은 입력값과 출력값 데이터로 [영어단어, 한글단어] 사용하지만,
    # 예측시에는 한글단어를 알지 못하므로, 디코더의 입출력값을 의미 없는 값인 P 값으로 채운다.
    # ['word', 'PPPP']
    seq_data = [word, 'P' * len(word)]

    input_batch, output_batch, target_batch = make_batch([seq_data])

    # 결과가 [batch size, time step, input] 으로 나오기 때문에,
    # 2번째 차원인 input 차원을 argmax 로 취해 가장 확률이 높은 글자를 예측 값으로 만든다.
    prediction = tf.argmax(model, 2)

    result = sess.run(prediction,
                      feed_dict={enc_input: input_batch,
                                 dec_input: output_batch,
                                 targets: target_batch})

    # 결과 값인 숫자의 인덱스에 해당하는 글자를 가져와 글자 배열을 만든다.
    decoded = [char_arr[i] for i in result[0]]

    # 출력의 끝을 의미하는 'E' 이후의 글자들을 제거하고 문자열로 만든다.
    end = decoded.index('E')
    translated = ''.join(decoded[:end])

    return translated


print('\n=== 번역 테스트 ===')

print('word ->', translate('word'))
print('wodr ->', translate('wodr'))
print('love ->', translate('love'))
print('loev ->', translate('loev'))
print('abcd ->', translate('abcd'))

~~~



### 2. 결과를 전처리 하여 enc_input, dec_input, targets 형태의 배열로 변환한다.

~~~

~~~



### 3. seq2seq 모델을 학습시킨다.

~~~

~~~

