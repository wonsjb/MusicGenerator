# MusicGenerator
Generating music using machine learning techniques.

Instruction to run it.
* Clone the repo
* cd into the repo
* create a virtual environment: `python3 -m venv venv`
* source the environment: `. venv/bin/activate`
* install dependencies: `pip3 install -r requirements.txt`
* install software into virtual environmnent: `python3 setup.py develop`
* create an empty directory: `mkdir learning`

Important note: For the first run, do not put anything in the learning directory. If you still do, do not clash with the files that are being generated. For instance, do not create a catalog directory in the learning directory.

* create a music catalog for the training: `create-music-catalog learning/catalog < directory with midi files to learn from >/*.mid`
* train a model: `train-model learning/catalog learning/weights 100`

That will take a while (over a day on my laptop)

* generate new music: `generate-music learning/catalog learning/weights learning/score 2000 0`

Slow, but much faster than previous step

* convert score to midi file: `score-to-midi learning/score learning/music.mid`
* Use your favorite midi player to listen to the result
  
Optional steps:
* Figure out the available midi ports on the machine: `show-midi-ports`
* Use this number to play a score directly: `play-score < number from previous run > learning/score`

Tip: Run the command with no arguments, to see what the parameters are, and maybe try other values.
