import plotly.express as px
import pandas as pd
import csv


def read_csv_file_return_dict(filename: str) -> dict[str, str]:
    """skhwjfn"""

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


df_hate_crime = pd.read_csv('../data/hate_crime_data.csv')
dic = read_csv_file_return_dict('../data/state_colour_data.csv')

df_hate_crime['colour'] = df_hate_crime['Population']
df_hate_crime['party'] = df_hate_crime['Population']

for row in range(len(df_hate_crime)):
    df_hate_crime['colour'][row] = dic[df_hate_crime['US State'][row]]
    if df_hate_crime['colour'][row] == 'crimson':
        df_hate_crime['party'][row] = 'Republican'
    else:
        df_hate_crime['party'][row] = 'Democratic'

fig = px.treemap(df_hate_crime, path=[px.Constant('USA'), 'party', 'US State', 'US City'],
                 values='Total Hate Crimes 2020', color='colour')
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.show()
