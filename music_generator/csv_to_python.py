import click
import csv


def is_number_tryexcept(s):
    """ Returns True is string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False


def print_class(headers, file):
    file.write("class Item:\n")
    file.write("    def __init__(self");
    for header in headers:
        file.write(", ")
        file.write(header)
    file.write("):\n")
    for header in headers:
        file.write("        self.{} = {}\n".format(header, header))
    file.write("\n\ndata = [\n")


def to_code(string):
    if len(string) == 0:
        return "None"
    if is_number_tryexcept(string):
        return string
    else:
        return "\"{}\"".format(string)


def print_item(data, file):
    data = [to_code(x) for x in data]
    file.write("    Item({}),\n".format(", ".join(data)))


@click.command()
@click.argument("csv-file", type=click.File('r'))
@click.argument("python-file", type=click.File('w'))
def cli(csv_file, python_file):
    reader = csv.reader(csv_file)
    header = True
    for row in reader:
        if header:
            header = False
            print_class(row, python_file)
        else:
            print_item(row, python_file)
    python_file.write("]\n")


def main():
    cli()
