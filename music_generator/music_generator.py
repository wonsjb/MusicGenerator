import click

import music_generator.create_music_catalog as create_music_catalog_main
import music_generator.train_model as train_model_main
import music_generator.score_to_midi as score_to_midi_main
import music_generator.generate_music as generate_music_main
import music_generator.show_midi_ports as show_midi_ports_main
import music_generator.play_score as play_score_main
import music_generator.print_score as print_score_main


def fix_weight_prefix(weights_prefix, catalog_file):
    if len(weights_prefix) == 0:
        weights_prefix = catalog_file.name + ".weights"
    return weights_prefix


@click.group()
def cli():
    pass


@cli.command()
@click.argument("catalog-file", type=click.File('wb'))
@click.argument("midi-files", nargs=-1, type=click.Path(exists=True))
def create_music_catalog(catalog_file, midi_files):
    create_music_catalog_main.main(catalog_file, midi_files)


@cli.command()
@click.argument("catalog-file", type=click.File('rb'))
@click.option('-e', '--epoch-count', type=int, default=100, show_default=True)
@click.option('-w', '--weights-prefix', default='')
def train_model(catalog_file, epoch_count, weights_prefix):
    weights_prefix = fix_weight_prefix(weights_prefix, catalog_file)
    train_model_main.main(catalog_file, weights_prefix, epoch_count)


@cli.command()
@click.argument("catalog-file", type=click.File('rb'))
@click.option('-w', '--weights-prefix', default='')
@click.argument("output-file", type=click.File('wb'))
@click.option('-p', '--prime-count', type=int, default=1000, show_default=True)
@click.option('-c', '--note-count', type=int, default=2000, show_default=True)
@click.option('-r', '--randomness', type=float, default=1.0, show_default=True)
def generate_music(catalog_file, weights_prefix, output_file, prime_count, note_count, randomness):
    weights_prefix = fix_weight_prefix(weights_prefix, catalog_file)
    generate_music_main.main(catalog_file, weights_prefix, output_file, prime_count, note_count, randomness)


@cli.command()
@click.argument("score-file", type=click.File('rb'))
@click.argument("midi-file", type=click.File('wb'))
def score_to_midi(score_file, midi_file):
    score_to_midi_main.main(score_file, midi_file)


@cli.command()
def show_midi_ports():
    show_midi_ports_main.main()


@cli.command()
@click.argument("score-file", type=click.File('rb'))
@click.option('-p', '--midi-port', type=int, default=0, show_default=True)
def play_score(score_file, midi_port):
    play_score_main.main(score_file, midi_port)


@cli.command()
@click.argument("score-file", type=click.File('rb'))
def print_score(score_file):
    print_score_main.main(score_file)


def main():
    cli()
