import pickle
import mido
import time
from tqdm import tqdm
from music_generator.score_util import score_to_events


def play_events(port_name, events):
    with mido.open_output(port_name) as port:
        current_time = 0
        for this_time in tqdm(sorted(events), "Playing"):
            time.sleep((this_time - current_time) / 1000)
            current_time = this_time
            for msg in events[this_time]:
                port.send(msg)


def main(score_file, midi_port):
    score = pickle.load(score_file)
    score_file.close()

    play_events(mido.get_output_names()[midi_port], score_to_events(score))
