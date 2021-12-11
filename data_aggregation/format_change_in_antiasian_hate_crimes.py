"""Format the column "Change Anti-Asian Hate Crimes" in hate_crime_data.csv"""
import pandas


def format_column(hate_crime_data_df: pandas.DataFrame) -> pandas.DataFrame:
    """weflkn"""
    # instantiate a new column called size, I just needed to assign it placeholder dummy values
    hate_crime_data_df['size'] = hate_crime_data_df['US City']

    for i in range(len(hate_crime_data_df)):
        if hate_crime_data_df['Change Anti-Asian Hate Crimes'][i] == 'Unchanged':
            hate_crime_data_df['Change Anti-Asian Hate Crimes'][i] = '0%'
        elif hate_crime_data_df['Change Anti-Asian Hate Crimes'][i] == '-':
            hate_crime_data_df['Change Anti-Asian Hate Crimes'][i] = str(
                hate_crime_data_df['2020 Anti-Asian'][i] * 100) + '%'

    for i in range(len(hate_crime_data_df)):
        hate_crime_data_df['size'][i] = int(str(hate_crime_data_df['Change Anti-Asian Hate Crimes'][i]).strip('%'))
        if hate_crime_data_df['size'][i] <= 0:
            hate_crime_data_df['size'][i] = 5

    return hate_crime_data_df
