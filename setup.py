from setuptools import setup, find_packages


setup(
    name='music_generator',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'music-generator = music_generator.music_generator:main',
            'csv-to-python = music_generator.csv_to_python:main',
        ]
    }
)
