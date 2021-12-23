import numpy as np
import tensorflow as tf


def get_character_count():
    alphabet = get_alphabet()

    return len(alphabet)

def get_alphabet():
    return list("abcdefghijklmnopqrstuvwxyz \n")

def text_to_vector(text):
    alphabet = get_alphabet()
    vector = []

    for char in text:
        if char.lower() in alphabet:
            one_hot = [0] * get_character_count()
            index = alphabet.index(char.lower())
            one_hot[index] = 1
            vector.append(one_hot)

    return vector


def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(128, input_dim=get_character_count(), return_sequences=True),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
        tf.keras.layers.Dense(32),
        tf.keras.layers.Dense(get_character_count(), activation="softmax")
    ])

    model.compile(loss=tf.keras.losses.CategoricalCrossentropy(), optimizer=tf.keras.optimizers.Adam(0.01))

    return model

def train_model(model, x, y):
    print ("Training...")
    model.fit(x, y, epochs=30)
    model.save("save")

def prep_dataset(file):
    text = open(file, "r").read()
    vec = text_to_vector(text)
    xs = []
    ys = []
    i = 0
    while i < len(vec) - 15:
        x = vec[i:i+15]
        y = vec[i+15]
        xs.append(x)
        ys.append(y)

        i += 1

    return xs, ys

if __name__ == "__main__":
    model = build_model()
    x = []
    y = []

    for i in range(1, 9):
        a, b = prep_dataset(f"data{i}.txt")
        for i in a:
            x.append(i)
        for i in b:
            y.append(i)

    train_model(model, np.array(x, dtype=float), np.array(y, dtype=float))