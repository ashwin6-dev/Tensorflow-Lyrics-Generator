import tensorflow as tf 
import numpy as np
from train import get_alphabet, text_to_vector
from autocorrect import Speller
spell = Speller()


def gen_text(model, inp, len):
    alphabet = get_alphabet()
    res = inp
    for i in range(len):
        vec = text_to_vector(inp)
        vec = np.expand_dims(vec, axis=0)
        index = np.argmax(model.predict(vec))
        letter = alphabet[index]
        res += letter
        inp += letter
        inp = inp[1:]

    return spell(res)

model = tf.keras.models.load_model("save")

while True:
    print ("============================")
    print (gen_text(model, input(""), 500))
    print ("============================")