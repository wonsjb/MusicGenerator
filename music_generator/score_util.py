import mido
from tqdm import tqdm


def score_to_events(score):
    current_time = 0
    events = {}
    for msg in tqdm(score, "Loading score"):
        current_time += msg.pause
        if current_time not in events:
            events[current_time] = []
        if (current_time + msg.duration) not in events:
            events[current_time + msg.duration] = []
        events[current_time].append(mido.Message('note_on', note=msg.note, velocity=msg.velocity))
        events[current_time + msg.duration].append(mido.Message('note_on', note=msg.note, velocity=0))
    return events
