# MusicGenerator
Generating music using machine learning techniques.

Instruction to run it.
* Clone the repo
* cd into the repo
* create a virtual environment: python3 -m venv venv
* install dependencies: venv/bin/pip install -r requierements.txt
* create an empty directory: mkdir learning
* create a music catalog for the training: PYTHONPATH=. venv/bin/python3 music_generator/create_music_catalog.py learning/catalog < directory with midi files to learn from >/*.mid
* train a model: PYTHONPATH=. venv/bin/python3 music_generator/train_model.py learning/catalog learning/weights 100

That will take a while (over a day on my laptop)
* generate new music: PYTHONPATH=. venv/bin/python3 music_generator/generate_music.py learning/catalog learning/weights learning/score 2000 0

Slow, but much faster than previous step
* convert score to midi file: PYTHONPATH=. venv/bin/python3 music_generator/score_to_midi.py learning/score learning/music.mid
* Use your favorite midi player to listen to the result
  
Optional steps:
* Figure out the midi ports on the machine: PYTHONPATH=. venv/bin/python3 music_generator/show_midi_ports.py
* Use this number to play a score directly: PYTHONPATH=. venv/bin/python3 music_generator/play_score.py 1 learning/chopin.score

Tip: Run the command with no arguments, to see what the parameters are, and maybe try other values.
