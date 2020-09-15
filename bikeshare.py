import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). 
    # HINT: Use a while loop to handle invalid inputs
    
    while True:
        try:
            city = input ('Enter your city of choice: ').lower()
            if city == 'chicago' or city == 'new york city' or city == 'washington':
               break
            else:
                print('Please choose among Chicago, New York City, or Washington')
        except Exception as e:
            print(e)

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        try:
            month = input ('Enter your month of choice: ').lower()
            if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june':
                break
            else:
                print('Choose between January and June')
        except Exception as e:
            print(e)
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ('Enter your weekday of choice: ').lower()
   
    # TEST
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) yes - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.lower()]

    return df

def raw_data(df):
    """
    Asks user to answer if they want to see 5 lines of raw data.

    Args:
        (str) yes - answer "yes" to see 5 lines of raw data, or "no" to skip
    Returns:
        df - Displays 5 lines of raw data based on user input
    
    """
    
    # get user input for month 
    
    while True:
           i = 0
           j = 6
           data_view = input ('Do you want to view 5 lines of data? Enter yes or no.\n')
           if data_view.lower() == 'yes':
                i += 5
                j += 5
                display_data = df.iloc[i:j] 
                print(display_data)
           if data_view.lower() != 'yes':
                break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()
    print('most common month: {}'.format(popular_month))

    
    # TO DO: display the most month day
    popular_day = df['day_of_week'].mode()
    print('most common day: {}'.format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()
    print('most common hour: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()
    print('most popular start station: {}'.format(popular_start))

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()
    print('most popular end station: {}'.format(popular_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'] + df['End Station']
    popular_start_end = df['Start End'].mode()
    print('most ppular end points: {}'.format(popular_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Trip Duration'] = df['Trip Duration'].astype(int)
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    df['Trip Duration'].fillna(0, inplace=True)
    average_travel_time = df['Trip Duration'].mean()
    print('average travel time: {}'.format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    
    except KeyError:
        print('Gender is not available in this data')
    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        df['Birth Year'].fillna(0, inplace=True)
        earliest_birth = df['Birth Year'].min()
        print('earlest birth year: {}'.format(earliest_birth))
        latest_birth = df['Birth Year'].max()
        print('latest birth year: {}'.format(latest_birth))
        common_birth = df['Birth Year'].mode()
        print('most common birth year: {}'.format(common_birth))
    except KeyError:
        print('Birth Year is not available in this data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)       
        raw_data(df)            
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
