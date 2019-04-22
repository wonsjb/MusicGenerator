import sys
from music_generator.music_model import build_model
from music_generator.converter import VocabConverter
import pickle
from tqdm import tqdm
import tensorflow as tf
import numpy as np
tf.enable_eager_execution()


def generate_music(model, start_notes, conv, num_generate, temperature):
    # Evaluation step (generating text using the learned model)

    # Converting our start string to numbers (vectorizing)
    input_eval = np.transpose(conv.score_to_int(start_notes))
    input_eval = tf.expand_dims(input_eval, 1)

    # Empty string to store our results
    score = []

    # Here batch size == 1
    model.reset_states()
    for _ in tqdm(range(num_generate), "Generating music"):
        predictions = model([x for x in input_eval])
        # remove the batch dimension
        predictions = [x[0] for x in predictions]

        # using a multinomial distribution to predict the word returned by the model
        if temperature == 0:
            predicted_ids = [tf.argmax(prediction[-1], output_type=tf.dtypes.int32) for prediction in predictions]
        else:
            predictions = [prediction / temperature for prediction in predictions]
            predicted_ids = [tf.multinomial(prediction, num_samples=1)[-1, 0].numpy() for prediction in predictions]

        # We pass the predicted word as the next input to the model
        # along with the previous hidden state
        input_eval = tf.transpose([[predicted_ids]], perm=[2, 0, 1])

        score.append(conv.int_to_score([predicted_ids])[0])

    return score


def main():
    if len(sys.argv) != 6:
        print("Usage: {} <music catalog> <model weight> <output score> <note count> <randomness>".format(sys.argv[0]))
        exit(0)


    f = open(sys.argv[1], 'rb')
    the_score = pickle.load(f)
    f.close()

    converter = VocabConverter(the_score)

    music_model = build_model(1, converter.vocab)
    music_model.load_weights(sys.argv[2])
    new_music = generate_music(music_model, the_score[:20], converter, int(sys.argv[4]), float(sys.argv[5]))


    f = open(sys.argv[3], 'wb')
    pickle.dump(new_music, f)
    f.close()
