"""display a bubble map with color-coded bubbles corresponding to a state's political leaning
and size proportionate to the increase in hate crimes"""

import plotly.graph_objects as go
import csv
import pandas as pd


def process_row(row: list[str], state_colour: dict[str, str]) -> None:
    """Convert a row to a mapping of a state and its colour
    """
    state_colour[row[0]] = row[1]


with open('../data/state_colour_data.csv') as file:
    reader = csv.reader(file)
    headers = next(reader)
    state_colour = {}

    for row in reader:
        process_row(row, state_colour)

scale = 50
coordinates = pd.read_csv('../data/uscities.csv')
hate_crime_data_df = pd.read_csv('../data/hate_crime_data.csv')
# instantiate a new column called colour, I just needed to assign it placeholder dummy values
hate_crime_data_df['colour'] = hate_crime_data_df['US City']
# instantiate a new column called lat, I just needed to assign it placeholder dummy values
hate_crime_data_df['lat'] = hate_crime_data_df['US City']
# instantiate a new column called lon, I just needed to assign it placeholder dummy values
hate_crime_data_df['lon'] = hate_crime_data_df['US City']
# instantiate a new column called size, I just needed to assign it placeholder dummy values
hate_crime_data_df['size'] = hate_crime_data_df['US City']

# searches coordinates for cities that are also in hate_crime_data_df, and then assigns the
# corresponding latitudes and longitudes from coordinates to the matching city in hate_crime_data_df
for i in range(len(hate_crime_data_df)):
    for j in range(len(coordinates)):
        if str(hate_crime_data_df['US City'][i]).strip() == coordinates['city'][j]:
            if hate_crime_data_df['US State'][i] == coordinates['state_id'][j]:
                hate_crime_data_df['lat'][i] = float(coordinates['lat'][j])
                hate_crime_data_df['lon'][i] = float(coordinates['lng'][j])

# assigns each city in hate_crime_data_df it's proper colour(ie, political leaning) by indexing the
# dictionary state_colour
for i in range(len(hate_crime_data_df)):
    # this line will throw a warning, but the code still works as indented
    hate_crime_data_df['colour'][i] = state_colour[hate_crime_data_df['US State'][i]]

for i in range(len(hate_crime_data_df)):
    if hate_crime_data_df['Change Anti-Asian Hate Crimes'][i] == 'Unchanged':
        hate_crime_data_df['Change Anti-Asian Hate Crimes'][i] = '0%'
    elif hate_crime_data_df['Change Anti-Asian Hate Crimes'][i] == '-':
        hate_crime_data_df['Change Anti-Asian Hate Crimes'][i] = str(hate_crime_data_df['2020 Anti-Asian'][i] * 100) + '%'

hate_crime_data_df['size'] = hate_crime_data_df['2020 Anti-Asian'] - hate_crime_data_df['2019 Anti-Asian']

for i in range(len(hate_crime_data_df)):
    if hate_crime_data_df['size'][i] <= 0:
        hate_crime_data_df['size'][i] = 1
    hate_crime_data_df['size'][i] = hate_crime_data_df['size'][i] * scale

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    lon=hate_crime_data_df['lon'],
    lat=hate_crime_data_df['lat'],
    text=(hate_crime_data_df['US City'] + ', ' + hate_crime_data_df['Change Anti-Asian Hate Crimes'] + ' increase'),
    marker=dict(
        size=hate_crime_data_df['size'].to_numpy(dtype=int),
        color=hate_crime_data_df['colour'],
        line_color='rgb(40,40,40)',
        line_width=0.5,
        sizemode='area'
    ),
    name='US City'))

fig.update_layout(
    title_text='US City Colours (Fixed Increase)<br>(Click legend to toggle traces)',
    showlegend=True,
    geo=dict(
        scope='usa',
        landcolor='rgb(217, 217, 217)',
    )
)

fig.show()
