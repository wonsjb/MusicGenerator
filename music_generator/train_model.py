import sys
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


def train(model, dataset, epoch_count):
    optimizer = tf.train.AdamOptimizer()
    # Training step
    for epoch in range(epoch_count):
        # initializing the hidden state at the start of every epoch
        # initally hidden is None
        hidden = model.reset_states()

        count = 0
        for (_, _) in dataset:
            count = count + 1

        for (batch_n, (inp, target)) in tqdm(enumerate(dataset), "Training epoch {}".format(epoch), count):
            with tf.GradientTape() as tape:
                # feeding the hidden state back into the model
                # This is the interesting step
                predictions = model([x for x in inp])
                loss = loss_func(target, predictions)

            grads = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))

        print('Epoch {} Loss {:.4f}'.format(epoch, loss))


def main():
    if len(sys.argv) != 4:
        print("Usage: {} <music catalog> <model weight> <epoch count>".format(sys.argv[0]))
        exit(0)

    f = open(sys.argv[1], 'rb')
    the_score = pickle.load(f)
    f.close()

    converter = VocabConverter(the_score)
    the_score_as_int = converter.score_to_int(the_score)

    # print([len(x) for x in converter.vocab])

    score_dataset = tf.data.Dataset.from_tensor_slices(the_score_as_int)
    examples_per_epoch = len(the_score_as_int)//seq_length
    sequences = score_dataset.batch(seq_length+1, drop_remainder=True)

    dataset = sequences.map(split_input_target)

    steps_per_epoch = examples_per_epoch//BATCH_SIZE

    dataset = dataset.batch(BATCH_SIZE, drop_remainder=True).map(
        lambda x, y: (tf.transpose(x, perm=[2, 0, 1]), tf.transpose(y, perm=[2, 0, 1])))

    music_model = build_model(BATCH_SIZE, converter.vocab)
    train(music_model, dataset, int(sys.argv[3]))
    music_model.save_weights(sys.argv[2])
