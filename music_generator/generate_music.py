from music_generator.music_model import build_model
from music_generator.converter import VocabConverter
from music_generator.score_to_midi import save_to_midi
import pickle
from tqdm import tqdm
import tensorflow as tf
import numpy as np
tf.enable_eager_execution()


def generate_next_note(model, input_eval, randomness):
    predictions = model([x for x in input_eval])
    # remove the batch dimension
    predictions = [x[0] for x in predictions]

    # using a multinomial distribution to predict the word returned by the model
    if randomness == 0:
        predicted_ids = [tf.argmax(prediction[-1], output_type=tf.dtypes.int32) for prediction in predictions]
    else:
        predictions = [prediction / randomness for prediction in predictions]
        predicted_ids = [tf.multinomial(prediction, num_samples=1)[-1, 0].numpy() for prediction in predictions]

    return tf.transpose([[predicted_ids]], perm=[2, 0, 1]), predicted_ids


def generate_music(model, prime_count, converter, note_count, randomness):
    # Creating a start with a single note
    input_eval = np.transpose([[0, 0, 0, 0]])
    input_eval = tf.expand_dims(input_eval, 1)

    model.reset_states()
    for _ in tqdm(range(prime_count), "Priming state"):
        input_eval, predicted_ids = generate_next_note(model, input_eval, randomness)

    # Empty string to store our results
    score = []

    for _ in tqdm(range(note_count), "Generating music"):
        input_eval, predicted_ids = generate_next_note(model, input_eval, randomness)
        score.append(converter.int_to_score([predicted_ids])[0])

    return score


def main(music_catalog_file, weight_prefix, output_score, prime_count, note_count, randomness):
    the_score = pickle.load(music_catalog_file)
    music_catalog_file.close()

    converter = VocabConverter(the_score)

    music_model = build_model(1, converter.vocab)
    music_model.load_weights(weight_prefix)
    new_music = generate_music(music_model, prime_count, converter, note_count, randomness)

    if output_score.name.endswith(".mid"):
        save_to_midi(new_music, output_score.name)
    else:
        pickle.dump(new_music, output_score)
        output_score.close()
