import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('dark_background')


def handle_rate(value):
    # removing 'NEW', '-' and  '/5' from values
    if value == 'NEW' or value == '-':
        return np.nan
    else:
        value = str(value).split('/')
        return float(value[0])


def handle_comma(value):
    value = value.replace(",", "")
    return float(value)


def handle_others_type(value, others_df):
    if value in others_df:
        return 'others'
    else:
        return value


if __name__ == "__main__":

    """ Data Cleaning """

    # Read csv data file
    df = pd.read_csv('/Users/mitalisoni/Documents/DataAnalyst/Zomato Bengaluru Restaurants/zomato.csv')
    print(df.shape)  # 51717 rows
    print(df.columns)

    # Dropping nonessential columns
    df = df.drop(['url', 'address', 'phone', 'menu_item', 'dish_liked', 'reviews_list'], axis=1)

    # Find if null values exist in columns
    print(df.info())

    # Dropping duplicates
    df.drop_duplicates(inplace=True)

    # Cleaning up rate column
    print(df['rate'].unique())
    df['rate'] = df['rate'].apply(handle_rate)

    # Filling up null values in rate column with mean

    mean_rate = df['rate'].mean()
    df.fillna({'rate': mean_rate}, inplace=True)

    # Dropping null values
    df.dropna(inplace=True)

    # Renaming columns
    df.rename(columns={'approx_cost(for two people)': 'Cost2people', 'listed_in(type)': 'Type'}, inplace=True)

    # Dropping listed_in(city) column
    df = df.drop(['listed_in(city)'], axis=1)

    # removing commas from Cost2people and making it float
    df['Cost2people'] = df['Cost2people'].apply(handle_comma)

    # Cleaning rest_type column
    rest_types_count = df['rest_type'].value_counts(ascending=False)  # 93 unique values
    rest_types_others = rest_types_count[rest_types_count < 400]  # 13 unique values and others

    rest_type_new = []
    for i in df['rest_type']:
        value = handle_others_type(i, rest_types_others)  # replacing relevant entries by others category
        rest_type_new.append(value)
    df['rest_type'] = rest_type_new

    # Cleaning locations column
    locations_count = df['location'].value_counts(ascending=False)  # 93 unique values
    location_others = locations_count[locations_count < 300]

    location_new = []
    for i in df['location']:
        value = handle_others_type(i, location_others)  # replacing relevant entries by others category
        location_new.append(value)
    df['location'] = location_new

    # Cleaning Cuisines column
    cuisines_count = df['cuisines'].value_counts(ascending=False)  # 2704 uniques values
    cuisine_others = cuisines_count[cuisines_count < 100]

    cuisine_new = []
    for i in df['cuisines']:
        value = handle_others_type(i, cuisine_others)  # replacing relevant entries by others category
        cuisine_new.append(value)
    df['cuisines'] = cuisine_new

    print(df.columns)

    """ Data Visualization """

    # Count of restaurants to location plot
    plt.figure(figsize=(16, 10))
    ax = sns.countplot(df['location'])
    plt.xticks(rotation=90)

    # Analysing count of restaurants having/not having online order facility
    plt.figure(figsize=(6, 6))
    sns.countplot(df['online_order'])

    # Analysing count of restaurants having/not having book table facility
    plt.figure(figsize=(6, 6))
    sns.countplot(df['book_table'])

    # Analysing relation between rating and online order facility
    plt.figure(figsize=(6, 6))
    sns.boxplot(x=df['online_order'], y=df['rate'], hue=df['online_order'], palette='rainbow')

    # Analysing relation between rating and table booking facility
    plt.figure(figsize=(6, 6))
    sns.boxplot(x=df['book_table'], y=df['rate'], hue=df['book_table'], palette='rainbow')

    # Analysing no. of restaurants having/not having online order facility by location
    df1 = df.groupby(['location', 'online_order'])['name'].count()
    df1.to_csv('location_online.csv')
    df1 = pd.read_csv('location_online.csv')
    df1 = pd.pivot_table(df1, values=None, index=['location'], columns=['online_order'], fill_value=0, aggfunc="sum")
    df1.plot(kind='bar', figsize=(16, 10))

    # Analysing no. of restaurants having/not having book table facility by location
    df2 = df.groupby(['location', 'book_table'])['name'].count()
    df2.to_csv('location_book.csv')
    df2 = pd.read_csv('location_book.csv')
    df2 = pd.pivot_table(df2, values=None, index=['location'], columns=['book_table'], fill_value=0, aggfunc="sum")
    df2.plot(kind='bar', figsize=(16, 10))

    # Analysing type of restaurant and rating
    plt.figure(figsize=(14,8))
    sns.boxplot(x=df['rest_type'], y=df['rate'], hue=df['rest_type'], palette='rainbow')
    plt.xticks(rotation=90)

    # Analysing type of restaurant grouped by location
    df3 = df.groupby(['location', 'rest_type'])['name'].count()
    df3.to_csv('location_type.csv')
    df3 = pd.read_csv('location_type.csv')
    df3 = pd.pivot_table(df3, values=None, index=['location'], columns=['rest_type'], fill_value=0, aggfunc="sum")
    df3.plot(kind='bar', figsize=(36, 10))

    # Analysing top cuisines

    df6 = df[['cuisines', 'votes']]
    df6.drop_duplicates()
    df7 = df6.groupby(['cuisines'])['votes'].sum()
    df7 = df7.to_frame()
    df7 = df7.sort_values('votes', ascending=False)
    df7 = df7.iloc[1:, :] # removing others category
    plt.figure(figsize=(15, 8))
    sns.barplot(x=df7.index, y=df7['votes'])
    plt.xticks(rotation=90)
    plt.show()

