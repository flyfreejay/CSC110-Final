"""CSC110 Fall 2021 Final Project Submission

Instructions (READ THIS FIRST!)
===============================

A module for our CSC110 Fall Final Project Submission includes functions that reads from
the csv files under the data folder, and draws visual scatter plots with various information

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Jay Lee, Andy Feng, and Jamie Yi
"""

import pandas as pd
import plotly.express as px


def draw_aapi_to_asian_hatecrime() -> None:
    """Draws a scatter plot that uses % of Population-AAPI as x axis and
    2019/2020 Anti-Asian hate crime cases as the y axis. Used to visually check whether
    there is a correlation between the dataset.
    """

    # remove '%' character at the end and parse the data to float datatype so that
    # plotly can sort them
    hate_crime_data = pd.read_csv('../data/hate_crime_data.csv')
    hate_crime_data['% of Population-AAPI-int'] = \
        hate_crime_data['% of Population-AAPI'].str.strip("%").astype('float64')
    fig = px.scatter(hate_crime_data, x='% of Population-AAPI-int',
                     y=['2019 Anti-Asian', '2020 Anti-Asian'])

    fig.update_layout(
        title="Asian Population % to Anti-Asian hatecrime cases in 2019",
        xaxis_title="% of Asian Population",
        yaxis_title="Number of Asian Hate crime Cases",
    )

    fig.show()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['pandas', 'plotly.express'],
        'allowed-io': ['print', 'open', 'input'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
