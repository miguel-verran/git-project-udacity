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
    print('\nHey people! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("\nWhat's the city would you like to select?n\new york, chicago or washington?\n").title()
        if city not in ('New York','Chicago','Washington'):
                     print('Sorry, couldn\'t find that. Please type one of the available options')
                     continue
                   else:
                     break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("What\'s the month would you like to select?\njanuary, february, march, april, may, june or all\n").title()
        if month not in ('January','February','March','April','May','June','all'):
                     print('Sorry, couldn\'t find that. Please type one of the available options')
                     continue
                   else:
                     break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("What\'s the weekday would you like to select?\nsunday, monday, tuesday, wednesday, thursday, friday, saturday or all\n").title()
        if day not in ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','all'):
                     print('Sorry, couldn\'t find that. Please type one of the available options')
                     continue
                   else:
                     break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])


# date is converted into date format by convert_datetime

    df['Start Time'] = pd.convert_datetime(df['Start Time'])

    df['End Time'] = pd.convert_datetime(df['End Time'])

    if month != 'all':
      months = ['January','February','March','April','May','June']
    # index of month
      month = months.index(month) +1

    df = df[df['Start Time'].dt.month == month]

# filter by day
    if day != 'all':
       df = df[df['Start Time'].dt.weekday_day == day.title()]
    print(df.head())
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("Most common month is: ", df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    print("Most common weekday is: ", df['weekday_day'].mode()[0], "\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("Most common start hour is: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most commonly used start station is: ", df['Start Station'].mode()[0], "\n")

    # TO DO: display most commonly used end station
    print("Most commonly used end station is: ", df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("Most frequent combination of start station and end station trip: ", df['combination'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is ", df['Trip Duration'].sum(), "\n")

    # display mean travel time
    print("Total mean travel time is ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df.groupby(['User Type'])['User Type'].count()
    print(user_type, "\n")
    if city != 'washington':

        # Display counts of gender
        gender = df.groupby(['Gender'])['Gender'].count()
        print(gender)
        # Display earliest, most recent, and most common year of birth
        early_y_b = sorted(df.groupby(['Birth Year'])['Birth Year'][0][0]
        most_r_y_b = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        most_c_y_b = df.['Birth Year'].mode()[0]
        print("Earliest year of birth is ", early_y_b, "\n")
        print("Most recent year of birth is ", most_r_y_b, "\n")
        print("Most common year of birth is ", most_c_y_b, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_rawdata (df):
    # display 5 lines of raw data
    counter = 5
    while True
        display_5lines_rawdata = input('\nDisplay 5 lines of Raw Data? Please type Yes or No...\n')
        if (display_5lines_rawdata.lower() == 'yes'):
            print(df.iloc[counter],'\n')
            counter = counter + 5
            countinue
        elif (display_5lines_rawdata.lower() == 'no'):
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
