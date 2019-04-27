import tensorflow as tf


def loss_func(labels, logits):
    return tf.add_n([tf.losses.sparse_softmax_cross_entropy(label, logit) for label, logit in zip(labels, logits)])


def build_model(batch_size, vocab, embedding_dim=256, rnn_units=1024):
    inputs = [tf.keras.layers.Input(dtype='int32', batch_shape=[batch_size, None]) for _ in vocab]
    embedding = [tf.keras.layers.Embedding(len(vocab[n]), embedding_dim)(i) for n, i in enumerate(inputs)]
    joined_input = tf.keras.layers.concatenate(embedding)
    rnn = tf.keras.layers.GRU(rnn_units, return_sequences=True, recurrent_initializer='glorot_uniform', stateful=True,
                              recurrent_activation='sigmoid')(joined_input)
    outputs = [tf.keras.layers.Dense(len(v))(rnn) for v in vocab]

    return tf.keras.Model(inputs, outputs)
