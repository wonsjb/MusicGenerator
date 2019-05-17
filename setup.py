from setuptools import setup, find_packages


setup(
    name='music_generator',
    packages=find_packages(),
    install_requires=[
        "mido",
        "python-rtmidi",
        "tensorflow==1.13.*",
        "tqdm",
        "click",
    ],
    entry_points={
        'console_scripts': [
            'music-generator = music_generator.music_generator:main',
            'csv-to-python = music_generator.csv_to_python:main',
        ]
    }
)
