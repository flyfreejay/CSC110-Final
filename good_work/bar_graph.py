"""CSC110 Fall 2021 Final Project Submission

Instructions (READ THIS FIRST!)
===============================

A module for our CSC110 Fall Final Project Submission includes functions that reads from
the csv files under the data folder, and draws a visual bar graph with that information

Copyright and Usage Information
===============================

TODO

This file is Copyright (c) 2021 Jay Lee, Andy Feng, and Jamie Yi
"""
import csv
import pandas as pd
import plotly.express as px

hate_crime_data = pd.read_csv('../data/hate_crime_data.csv')
state_colour_data = pd.read_csv('../data/state_colour_data.csv')


def draw_anti_asian_comparison() -> None:
    """Extract 'US State' column from hate_crime_data.csv and draw a bar-graph
    comparing the Anti-Asian hate crime numbers in 2019 and 2020 in each state in the data
    """
    fig = px.bar(hate_crime_data, x="US State", y=['2019 Anti-Asian', '2020 Anti-Asian'])
    fig.update_layout(barmode='group')
    fig.update_traces(marker_line_width=0)
    fig.update_layout(
        title="2019 Anti-Asian Hatecrimes vs 2020 Anti-Asian Hatecrimes",
        xaxis_title="US State",
        yaxis_title="Number of Hatecrime Cases",
    )
    fig.show()


# def draw_aapi_to_anti_asian_hatecrimes2019() -> None:
#     """
#     """
#     fig = px.bar(hate_crime_data, x="US State", y=['2019 Anti-Asian', '% of Population-AAPI'])
#     fig.update_layout(barmode='group')
#     fig.update_traces(marker_line_width=0)
#     fig.update_layout(
#         title="Correlation between ",
#         xaxis_title="US State",
#         yaxis_title="Number of Hatecrime Cases",
#     )
#     fig.show()

# def draw_total_hatecrime_to_anti_asian_hatecrime_2019() -> None:
#     """Extract 'US State' column from hate_crime_data.csv and draw a bar-graph
#     comparing the numbers of Asian hate crimes to total hate crime numbers
#     """
#     fig = px.bar(hate_crime_data, x="US State", y=['Total HateCrimes 2019', '2019 Anti-Asian'])
#     fig.update_layout(barmode='group')
#     fig.update_traces(marker_line_width=0)
#     fig.update_layout(
#         title="Total Hatecrimes vs Anti-Asian Hatecrimes in 2019",
#         xaxis_title="US State",
#         yaxis_title="Number of Hatecrime Cases",
#     )
#     fig.show()

# change the directory path if this file's location changes

# if __name__ == '__main__':
# import python_ta
#
# python_ta.check_all(config={
#     'extra-imports': ['csv', 'pandas', 'plotly.express'],
#     'allowed-io': ['print', 'open', 'input'],
#     'max-line-length': 100,
#     'disable': ['R1705', 'C0200']
# })
