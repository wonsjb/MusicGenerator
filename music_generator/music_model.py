import tensorflow as tf
from music_generator.converter import index_name


def loss_func(labels, logits):
    return tf.add_n([tf.losses.sparse_softmax_cross_entropy(label, logit) for label, logit in zip(labels, logits)])


def to_name(name, i):
    return "{}-{}".format(name, index_name[i])


def build_model(batch_size, vocab, training, embedding_dim=256, rnn_units=1024):
    inputs = [tf.keras.layers.Input(dtype='int32', batch_shape=[batch_size, None], name=to_name("input", i))
              for i, _ in enumerate(vocab)]
    model = [tf.keras.layers.Embedding(len(vocab[i]), embedding_dim, name=to_name("embedding", i))(model_input)
             for i, model_input in enumerate(inputs)]
    model = tf.keras.layers.concatenate(model)
    model = tf.keras.layers.GRU(rnn_units, return_sequences=True, recurrent_initializer='glorot_uniform', stateful=True,
                                recurrent_activation='sigmoid', name="gru-layer")(model)
    if training:
        model = tf.keras.layers.Dropout(0.5, name="drop-layer")(model)
    outputs = [tf.keras.layers.Dense(len(v), name=to_name("output", i))(model) for i, v in enumerate(vocab)]

    return tf.keras.Model(inputs, outputs)
