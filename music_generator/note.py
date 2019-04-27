from music_generator.midi_notes import data as midi_note_data

dictionary = {x.midi: x for x in midi_note_data}


class Note:
    def __init__(self, note, velocity, duration, pause):
        self.note = note
        self.velocity = velocity
        self.duration = duration
        self.pause = pause

    def human(self):
        return "{} {}ms {}".format(dictionary[self.note].english, self.duration, self.velocity)
