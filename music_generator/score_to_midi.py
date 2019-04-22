import mido
import sys
import pickle
from tqdm import tqdm
from music_generator.score_util import score_to_events


def save_events(track, events):
    current_time = 0
    for this_time in tqdm(sorted(events), "Writing midi events"):
        sleep_time = this_time - current_time
        current_time = this_time
        for msg in events[this_time]:
            msg.time = sleep_time
            sleep_time = 0
            track.append(msg)


def main():
    if len(sys.argv) != 3:
        print("Usage: {} <score> <midi file>".format(sys.argv[0]))
        exit(0)


    midi_file= mido.MidiFile()
    midi_track = mido.MidiTrack()
    midi_file.tracks.append(midi_track)

    f = open(sys.argv[1], 'rb')
    music = pickle.load(f)
    f.close()

    save_events(midi_track, score_to_events(music))

    midi_file.save(sys.argv[2])
