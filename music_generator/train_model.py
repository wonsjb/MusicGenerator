import pickle
from music_generator.converter import VocabConverter
import tensorflow as tf
from music_generator.music_model import build_model, loss_func
from tqdm import tqdm

tf.enable_eager_execution()


# When training, the length of sequences to train
seq_length = 100
# Batch size when training
BATCH_SIZE = 64


def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text


def train(model, dataset, epoch_count, weight_prefix):
    optimizer = tf.train.AdamOptimizer()
    count = 0
    for _ in dataset:
        count = count + 1

    for epoch in range(epoch_count):
        model.reset_states()
        loss = 0

        for (batch_n, (inp, target)) in tqdm(enumerate(dataset),
                                             "Training epoch {}/{}".format(epoch, epoch_count - 1),
                                             count):
            with tf.GradientTape() as tape:
                predictions = model([x for x in inp])
                loss = loss_func(target, predictions)

            grads = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))

        print('Epoch {} Loss {:.4f}'.format(epoch, loss))
        if weight_prefix.endswith(".h5"):
            model.save_weights(weight_prefix, save_format="h5")
        else:
            model.save_weights(weight_prefix)


def main(catalog_file, weight_prefix, epoch_count):

    the_score = pickle.load(catalog_file)
    catalog_file.close()

    converter = VocabConverter(the_score)
    the_score_as_int = converter.score_to_int(the_score)

    score_dataset = tf.data.Dataset.from_tensor_slices(the_score_as_int)
    sequences = score_dataset.batch(seq_length+1, drop_remainder=True)

    dataset = sequences.map(split_input_target)

    dataset = dataset.batch(BATCH_SIZE, drop_remainder=True).map(
        lambda x, y: (tf.transpose(x, perm=[2, 0, 1]), tf.transpose(y, perm=[2, 0, 1])))

    music_model = build_model(BATCH_SIZE, converter.vocab, True)
    try:
        music_model.load_weights(weight_prefix)
        print("Loaded weights from file {}".format(weight_prefix))
    except tf.errors.NotFoundError:
        pass

    train(music_model, dataset, epoch_count, weight_prefix)
