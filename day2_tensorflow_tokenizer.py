# -*- coding: utf-8 -*-
"""Day2_Tensorflow_Tokenizer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12CfgA1TfIzorSeaOv9qr2WbcpyFjUYW7
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = ['I love my Dog', 'I love my cat', 'everyone loves me', 'I love them']

tokenizer = Tokenizer(num_words=100) ## We are creating an instance of the Tensorflow tokenizer and are specifying that only top 100 frequent words be retained in case of a large corpus
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)
