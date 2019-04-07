import pickle
import mido
import time
import sys
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


if len(sys.argv) != 3:
    print("Usage: {} <midi port id> <score>".format(sys.argv[0]))
    exit(0)


f = open(sys.argv[2], 'rb')
music = pickle.load(f)
f.close()


play_events(mido.get_output_names()[int(sys.argv[1])], score_to_events(music))
