from .note import Note
import numpy as np


class VocabConverter:
    def __init__(self, score):
        vocab = [set(), set(), set(), set()]
        for score_item in score:
            vocab[0].add(score_item.note)
            vocab[1].add(score_item.velocity)
            vocab[2].add(score_item.duration)
            vocab[3].add(score_item.pause)

        vocab = [sorted(x) for x in vocab]

        self.vocab = vocab
        self.vocab2idx = [{u: i for i, u in enumerate(v)} for v in vocab]
        self.idx2vocab = [np.array(v) for v in vocab]

    def score_to_int(self, score):
        score_as_int = []
        for score_item in score:
            score_as_int.append((self.vocab2idx[0][score_item.note], self.vocab2idx[1][score_item.velocity],
                                self.vocab2idx[2][score_item.duration], self.vocab2idx[3][score_item.pause]))
        return score_as_int

    def int_to_score(self, score_as_int):
        score = []
        for score_item in score_as_int:
            note = Note(self.idx2vocab[0][score_item[0]],
                        self.idx2vocab[1][score_item[1]],
                        self.idx2vocab[2][score_item[2]],
                        self.idx2vocab[3][score_item[3]])
            score.append(note)
        return score
