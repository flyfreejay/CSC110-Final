"""Helper functions to convert a two column csv to a dictionary"""
import csv


def read_csv_file_return_dict(filename: str) -> dict[str, str]:
    """Creates a dictionary mapping a of a csv mapping the elements of the first column to the
    corresponding element of the second column
    """

    with open(filename) as file:
        reader = csv.reader(file)
        headers = next(reader)
        dictionary = {}

        for row in reader:
            process_row(row, dictionary)

    return dictionary


def process_row(row: list[str], state_colour: dict[str, str]) -> None:
    """Convert a row to a mapping of a state and its colour
    """
    state_colour[row[0]] = row[1]
