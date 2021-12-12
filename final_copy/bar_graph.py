"""CSC110 Fall 2021 Final Project Submission

Instructions (READ THIS FIRST!)
===============================

A module for our CSC110 Fall Final Project Submission includes functions that reads from
the csv files under the data folder, and draws a visual bar graph with that information

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Jay Lee, Andy Feng, and Jamie Yi
"""
import pandas as pd
import plotly.express as px


def draw_anti_asian_comparison() -> None:
    """Extract 'US State' column from hate_crime_data.csv and draw a bar-graph
        comparing the Anti-Asian hate crime numbers in 2019 and 2020 in each state in the data
    """
    hate_crime_data = pd.read_csv('../data/hate_crime_data.csv')

    fig = px.bar(hate_crime_data, x='US State', y=['2019 Anti-Asian', '2020 Anti-Asian'])
    fig.update_layout(barmode='group')
    fig.update_traces(marker_line_width=0)
    fig.update_layout(
        title='2019 Anti-Asian Hatecrimes vs 2020 Anti-Asian Hatecrimes',
        xaxis_title='US State',
        yaxis_title='Number of Hatecrime Cases',
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
