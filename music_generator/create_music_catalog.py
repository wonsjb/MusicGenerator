from tqdm import tqdm
import mido
from .note import Note
import pickle


def midi_to_score(midi, score, start_time, channel):
    current_time = start_time
    previous_time = current_time
    currently_played_notes = {}
    for msg in midi:
        msgtime = int(msg.time * 1000)
        current_time = current_time + msgtime
        if isinstance(msg, mido.MetaMessage):
            continue

        if msg.type == 'note_on':
            if msg.channel != channel:
                continue

            end_note_and_set_duration(current_time, msg, currently_played_notes)

            if msg.velocity != 0:
                pause = current_time - previous_time
                previous_time = current_time
                new_note = Note(msg.note, msg.velocity, 0, pause)
                currently_played_notes[msg.note] = (new_note, current_time)
                score.append(new_note)

        elif msg.type == 'note_off':
            if msg.channel != channel:
                continue

            end_note_and_set_duration(current_time, msg, currently_played_notes)
        elif msg.type == 'program_change':
            pass
        elif msg.type == 'control_change':
            pass
        elif msg.type == 'sysex':
            pass
        elif msg.type == 'pitchwheel':
            pass
        elif msg.type == 'aftertouch':
            pass
        else:
            print("Unknown message type:", msg.type)

    if len(currently_played_notes) > 0:
        print(currently_played_notes)
    return current_time


def end_note_and_set_duration(current_time, msg, currently_played_notes):
    if msg.note in currently_played_notes:
        current_length = current_time - currently_played_notes[msg.note][1]
        currently_played_notes[msg.note][0].duration = current_length
        del currently_played_notes[msg.note]


def main(music_catalog_file, midi_files):

    catalog = []
    start_time = 0

    for file in tqdm(midi_files, "Reading files"):
        if file.endswith(".mid"):
            try:
                start_time = midi_to_score(mido.MidiFile(file), catalog, start_time, 0)
            except mido.midifiles.meta.KeySignatureError:
                print("Could not read file:", file)

    pickle.dump(catalog, music_catalog_file)
    music_catalog_file.close()
