from setuptools import setup, find_packages


setup(
    name='music_generator',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'create-music-catalog = music_generator.create_music_catalog:main',

        ]
    }
)