"""CSC110 Fall 2021 Final Project Submission

Instructions (READ THIS FIRST!)
===============================

A module for our CSC110 Fall Final Project Submission includes functions that reads from
the aggregates the data from hate_crime_data.csv

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Jay Lee, Andy Feng, and Jamie Yi
"""

import csv
import pandas


def process_hate_crime_csv() -> pandas.DataFrame:
    """Make a dataframe representing hate_crime_data.csv, and then add columns representing the
    city's latitude, longitude, colour (political leaning), and relative size of its 'bubble' on
    the bubble map.
    """

    # This block creates a dictionary mapping a state's name to its political leaning colour
    with open('../data/state_colour_data.csv') as file:
        reader = csv.reader(file)
        next(reader)
        state_colour = {}
        for row in reader:
            process_row(row, state_colour)

    coordinates = pandas.read_csv('../data/uscities.csv')
    hate_crime_data_df = pandas.read_csv('../data/hate_crime_data.csv')

    # In order to work with specific slices (single elements) of a Dataframe, I must instantiate
    # The new columns first (like in Java), so here I assign them a placeholder dummy column
    hate_crime_data_df['colour'] = hate_crime_data_df['US City']
    hate_crime_data_df['lat'] = hate_crime_data_df['US City']
    hate_crime_data_df['lon'] = hate_crime_data_df['US City']
    hate_crime_data_df['percentage'] = hate_crime_data_df['US City']

    # Searches coordinates for cities that are also in hate_crime_data_df, and then assigns the
    # Corresponding latitudes and longitudes from coordinates to the matching city in
    # hate_crime_data_df
    for i in range(len(hate_crime_data_df)):
        for j in range(len(coordinates)):
            # Making sure both the state and city are matching
            if str(hate_crime_data_df['US City'][i]).strip() == coordinates['city'][j] and \
                    hate_crime_data_df['US State'][i] == coordinates['state_id'][j]:
                # Whenever any value is trying to be set to be a copy of a slice
                # (single element) of a Dataframe, pandas will throw a warning, the code will
                # still run nonetheless
                hate_crime_data_df['lat'][i] = float(coordinates['lat'][j])
                hate_crime_data_df['lon'][i] = float(coordinates['lng'][j])

    # WHEN I USE i IN THE FOR LOOP, IT CANNOT BE SIMPLIFIED, I CANNOT ITERATE THROUGH A
    # pandas.Dataframe TO INDIVIDUALLY ACCESS ROWS, PLEASE IGNORE ANY PythonTA ERRORS AS I HAVE
    # FIXED EVERYTHING ELSE
    # Assigns each city in hate_crime_data_df it's proper colour(ie, political leaning) by indexing
    # the dictionary state_colour
    for i in range(len(hate_crime_data_df)):
        # this line will throw a warning, but the code still works as indented
        hate_crime_data_df['colour'][i] = state_colour[hate_crime_data_df['US State'][i]]

    # Reformatting the column so there are only percentages (check the Computational Overview) on
    # what the elif statement is
    for i in range(len(hate_crime_data_df)):
        if hate_crime_data_df['Change Anti-Asian Hate Crimes'][i] == 'Unchanged':
            hate_crime_data_df['Change Anti-Asian Hate Crimes'][i] = '0%'
        elif hate_crime_data_df['Change Anti-Asian Hate Crimes'][i] == '-':
            hate_crime_data_df['Change Anti-Asian Hate Crimes'][i] = str(
                hate_crime_data_df['2020 Anti-Asian'][i] * 100) + '%'

    # The size of the bubble should be equal to the percentage increase in hate crimes, if there is
    # a decrease or no change, the size of the bubble will be set to 5
    for i in range(len(hate_crime_data_df)):
        hate_crime_data_df['percentage'][i] = \
            int(str(hate_crime_data_df['Change Anti-Asian Hate Crimes'][i]).strip('%'))
        if hate_crime_data_df['percentage'][i] <= 0:
            hate_crime_data_df['percentage'][i] = 1

    return hate_crime_data_df


def process_row(row: list[str], state_colour: dict[str, str]) -> None:
    """Convert a row to a mapping of a its first column element and its second column element
    """
    state_colour[row[0]] = row[1]


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['pandas', 'plotly.express', 'plotly.graph_objects', 'csv'],
        'allowed-io': ['process_hate_crime_csv'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
