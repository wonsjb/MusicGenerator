import sys
from tqdm import tqdm
import mido
from .note import Note
import pickle


def midi_to_score(midi, score, score_time):
    start_times = {}
    current_time = 0
    if len(score_time) > 0:
        current_time = score_time[-1]
    for msg in midi:
        msgtime = int(msg.time * 1000)
        current_time = current_time + msgtime

        if isinstance(msg, mido.MetaMessage):
            continue

        if msg.type == 'note_on':
            if msg.velocity == 0:
                if msg.note in start_times:
                    current_length = current_time - start_times[msg.note][1]
                    score[start_times[msg.note][0]].duration = current_length
                    del start_times[msg.note]
            else:
                if msg.note in start_times:
                    current_length = current_time - start_times[msg.note][1]
                    score[start_times[msg.note][0]].duration = current_length

                start_times[msg.note] = (len(score), current_time)
                pause = 0
                if len(score) > 0:
                    pause = current_time - score_time[-1]
                score.append(Note(msg.note, msg.velocity, 0, pause))
                score_time.append(current_time)

    return score


def main():
    if len(sys.argv) < 3:
        print("Usage: {} <music catalog> <midi files>".format(sys.argv[0]))
        exit(0)

    the_score = []
    the_score_time = []

    for file in tqdm(sys.argv[2:], "Opening files"):
        if file.endswith(".mid"):
            try:
                midi_to_score(mido.MidiFile(file), the_score, the_score_time)
            except:
                print("Could not read file:", file)


    f = open(sys.argv[1], 'wb')
    pickle.dump(the_score, f)
    f.close()
