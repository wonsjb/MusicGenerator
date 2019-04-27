import mido
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


def save_to_midi(score, midi_file):
    midi = mido.MidiFile()
    midi_track = mido.MidiTrack()
    midi.tracks.append(midi_track)
    save_events(midi_track, score_to_events(score))
    midi.save(midi_file)


def main(score_file, midi_file):
    score = pickle.load(score_file)
    score_file.close()

    save_to_midi(score, midi_file.name)
