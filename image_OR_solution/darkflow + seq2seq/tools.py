import pandas as pd
from tensorflow.python.keras.preprocessing.sequence import pad_sequences

def make_vocab(corpus): 
    """
    args:        
        corpus: 넘파이 배열.
    
    return:
        vocab: 단어사전
        enc_input: 인코더의 인풋으로 들어갈 값들. 인덱스로 인코딩. 예) dallas take off
        dec_input: 디코더의 인풋으로 들어갈 값들. 인덱스로 인코딩. 예) <start> plane take off from dallas
        dec_output: 디코더의 아웃풋. 인덱스로 인코딩. 예) plane take off from dallas <end>    
    """
    
    # 1) 단어사전을 리스트 형태로 만든다.
    vocab = []
   
    for doc in corpus:
        # (영어로 된 문장만 있을 때) 모든 단어를 소문자로 바꾼 후 다시 리스트에 담는다.
        # map 함수와 lambda함수를 중첩해서 사용!! 이런식으로 많이 쓰니깐 사용법을 꼭 익혀두자.
        temp = list(map(lambda x: x.lower(), ''.join(doc).split(' ')))
        vocab.extend(temp)
        
    vocab = list(set(vocab)) + ['<start>', '<end>', '<pad>', '<unk>']
    
    ## 2) 만들어진 단어사전으로 word2idx, idx2word 딕셔너리를 만들고 인풋과 타겟값을 만든다.
    idx2word = {i: w for i, w in enumerate(vocab)}
    word2idx = {w: i for i, w in enumerate(vocab)}
    vocab_size = len(idx2word)
    
    return idx2word, word2idx, vocab_size
    
    
def make_temp_data(corpus, idx2word, word2idx):     
    temp_encoder_data = []
    temp_decoder_data = []
    temp_targets_data = []
        
    for doc in corpus:
        temp_encoder_data.append([word2idx[word.lower()] for word in doc[0].split()])
        temp_decoder_data.append([word2idx[word.lower()] for word in doc[1].split()])
        temp_targets_data.append([word2idx[word.lower()] for word in doc[1].split()])
   
    return temp_encoder_data, temp_decoder_data, temp_targets_data
   
    
def insert_tokens(temp_encoder_data, temp_decoder_data, temp_targets_data, word2idx, maxlen=15):
    max_decoder_steps = maxlen
    encoder_data = pad_sequences(temp_encoder_data, padding='post', value=word2idx['<pad>'])
    decoder_data = pad_sequences(list(map(lambda x: [word2idx['<start>']] + x, temp_decoder_data)), padding='post', value=word2idx['<pad>'], maxlen=15)
    targets_data = pad_sequences(list(map(lambda x: x + [word2idx['<end>']], temp_targets_data)), padding='post', value=word2idx['<pad>'], maxlen=15)

    return encoder_data, decoder_data, targets_data, max_decoder_steps

def data_checker(sequence_data, idx2word):
    for row in sequence_data:
        print(' '.join(list(map(lambda x: idx2word[x], row))))

def sequence_length_maker(sequence_data, word2idx):
    '''
    Arguments:
        sequence_data: [batch size, time steps]
        mode: 1이면 인코더 부분 sequence_length를 반환, 2이면 디코더 부분의 sequence_length를 반환.
    '''
    sequnece_length = []

    for row in sequence_data:
        if sum(row == word2idx['<pad>']) >= 1:
            sequnece_length.append(list(row).index(word2idx['<pad>']))
        else:
            sequnece_length.append(len(list(row)))

    return sequnece_length   