from setuptools import setup, find_packages


setup(
    name='music_generator',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'create-music-catalog = music_generator.create_music_catalog:main',
            'train-model = music_generator.train_model:main',
            'generate-music = music_generator.generate_music:main',
            'score-to-midi = music_generator.score_to_midi:main',
            'show-midi-ports = music_generator.show_midi_ports:main',
            'play-score = music_generator.play_score:main',
        ]
    }
)
