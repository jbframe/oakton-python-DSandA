# import the keras applications
import keras_preprocessing as kp
from keras_preprocessing.text import one_hot
from keras_preprocessing.text import hashing_trick
from keras_preprocessing.text import Tokenizer

# define the text document or sentence
scene1 = "sub plot: the drone has been launched"
# tokenize the text document or sentence
result = kp.text.text_to_word_sequence(scene1)
print (result)

# estimate the size of the vocabulary
words = set(kp.text.text_to_word_sequence(scene1))
print (sorted(words))
vocabulary_size = len(words)
print (vocabulary_size)

# encode the document as an integer
result = one_hot(scene1, round(vocabulary_size * 2.0))
print (result)

# perform hashing
result = hashing_trick(scene1, round(vocabulary_size * 2.0), hash_function = "md5")
print (result)

# create the tokenizer
ratings = ["Superb", "Good", "Great", "Excellent", "Average"]
t = Tokenizer()
# fit the tokenizer on the document
t.fit_on_texts(ratings)

# summarize the tokens
print (t.word_counts)
print (t.document_count)
print (t.word_index)
print (t.word_docs)

# integer encode the document
encoded_docs = t.texts_to_matrix(ratings, mode = "count")
print (encoded_docs)
