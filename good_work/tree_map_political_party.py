import plotly.express as px
import pandas as pd
from bubble_map_with_color_and_scale import process_row



df_hate_crime = pd.read_csv('../data/state_colour_data.csv')
df_state_colour = pd.read_csv('../data/state_colour_data.csv')

df_hate_crime['Colour']= df_hate_crime['Population']
for row in range(len(df_hate_crime)):
    df_hate_crime['Colour'][row] = df_state_colour[]

fig= px.treemap()


