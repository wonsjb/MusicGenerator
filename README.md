# MusicGenerator
Generating music using machine learning techniques.

Instruction to run it.
* Clone the repo
* Cd into the repo
* Create a virtual environment: `python3 -m venv venv`
* Source the environment: `. venv/bin/activate`
* Install software and dependencies into virtual environmnent: `python3 setup.py develop`
* Create an empty directory: `mkdir learning`

Important note: For the first run, do not put anything in the learning directory. If you still do, do not clash with the files that are being generated. For instance, do not create a catalog directory in the learning directory.

* Create a music catalog for the training: `music-generator create-music-catalog learning/catalog < directory with midi files to learn from >/*.mid`

Make sure to have a couple midi files. If you don't have enough data to train on, the next step will fail with an obscure error.

* Train a model: `music-generator train-model learning/catalog`

That will take a while (over a day on my laptop). If you want a quick result just to test it all works, add `-e 1` at the end of the previous command.

* Generate new music: `music-generator generate-music learning/catalog learning/music.mid`

Slow, but much faster than previous step. Note, if the last parameter ends with mid extension, it will produce a midi file. Otherwise, it will produce a score file (the internal format for this application).

* Use your favorite midi player to listen to the result.

Optional steps:
* Convert score file to midi file: `music-generator score-to-midi learning/score-file learning/music.mid`
* Figure out the available midi ports on the machine: `music-generator show-midi-ports`
* Use this number to play a score directly: `music-generator play-score -p < number from previous run > learning/score`
* Print a score: `music-generator print-score learning/score-file`

Tip: Run the command with `--help`, to see what the parameters are, and try other values.
