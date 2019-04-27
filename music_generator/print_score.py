import pickle
import datetime


def print_notes(current_time, notes):
    d = datetime.timedelta(milliseconds=int(current_time))
    print(d, [x.human() for x in notes])


def main(score_file):
    score = pickle.load(score_file)
    score_file.close()

    current_time = 0
    notes = []
    for note in score:
        if note.pause > 0:
            current_time += note.pause
            print_notes(current_time, notes)
            notes = []
        notes.append(note)
    print_notes(current_time, notes)
