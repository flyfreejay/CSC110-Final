"""CSC110 Fall 2021 Final Project Submission

Instructions (READ THIS FIRST!)
===============================

A module for our CSC110 Fall Final Project Submission includes functions that reads from
the csv files under the data folder, and displays a bubble map with color-coded bubbles
corresponding to a state's political leaning and size proportionate to the increase in hate crimes

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Jay Lee, Andy Feng, and Jamie Yi
"""

import pandas
import plotly.graph_objects as go
from process_hate_crime_csv import process_hate_crime_csv


def draw_bubble_map() -> None:
    """Draw the bubble map"""
    traces = separate_red_and_blue()
    labels = ('Republican', 'Democratic')

    fig = go.Figure()

    # Iterating through the two traces (Dataframes) in traces
    for i in range(len(traces)):
        # fig.add_trace takes go.Scattergeo objects as a parameter
        fig.add_trace(go.Scattergeo(
            # Longitude parameter
            lon=traces[i]['lon'],
            # Latitude parameter
            lat=traces[i]['lat'],
            # The text parameter for a given bubble is the name of the city plus the city's percent
            # increase in anti AAPI hate crimes
            text=(traces[i]['US City'] + ', ' + traces[i]['Change Anti-Asian Hate Crimes']
                  + ' increase'),
            # The marker parameter takes a dictionary as a parameter, with the specific keys
            # corresponding to some attribute of the bubble itself
            marker=dict(
                size=traces[i]['percentage'].to_numpy(dtype=int),
                color=traces[i]['colour'],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode='area'
            ),
            # name is for the names of all the data points in the set collectively, so since I have
            # two Dataframes for the two political parties, the name will correspond to the
            # Dataframe's political party
            name=labels[i]))

    # Update the figure with the newly added properties above
    fig.update_layout(
        title_text='Percentage Increase in anti-AAPI Hate Crimes in American Cities'
                   '<br>(Click legend to toggle traces)',
        showlegend=True,
        geo=dict(
            scope='usa',
            landcolor='rgb(217, 217, 217)',
        )
    )

    # Display the bubble map
    fig.show()


# MUST READ: DESPITE WHAT PythonTA MIGHT SAY, pandas.Dataframe.iloc IS A EXISTING METHOD AND
# IT IS BEING USED PROPERLY HERE,
# SEE: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
# WHEN I USE i IN THE FOR LOOP, IT CANNOT BE SIMPLIFIED, I CANNOT ITERATE THROUGH A
# pandas.Dataframe TO INDIVIDUALLY ACCESS ROWS, PLEASE IGNORE ANY PythonTA ERRORS AS I HAVE
# FIXED EVERYTHING ELSE
def separate_red_and_blue() \
        -> tuple[pandas.DataFrame, pandas.DataFrame]:
    """Return the rows of hate_crime_data.csv separated into two dataframes, one for only 'crimson'
    (Republican) states and one for only 'royalblue' (Democratic) states
    """

    hate_crime_data_df = process_hate_crime_csv()

    # Create two empty Dataframes with the same columns as hate_crime_data_df
    hate_crimes_red = pandas.DataFrame(columns=tuple(hate_crime_data_df.columns))
    hate_crimes_blue = pandas.DataFrame(columns=tuple(hate_crime_data_df.columns))

    for i in range(len(hate_crime_data_df)):
        if hate_crime_data_df.iloc[i]['colour'] == 'crimson':
            hate_crimes_red = hate_crimes_red.append(hate_crime_data_df.iloc[i])

    for i in range(len(hate_crime_data_df)):
        if hate_crime_data_df.iloc[i]['colour'] == 'royalblue':
            hate_crimes_blue = hate_crimes_blue.append(hate_crime_data_df.iloc[i])

    return (hate_crimes_red, hate_crimes_blue)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['pandas', 'plotly.express', 'plotly.graph_objects',
                          'csv', 'process_hate_crime_csv'],
        'allowed-io': ['process_hate_crime_csv'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
