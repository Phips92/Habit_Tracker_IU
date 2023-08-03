"""
Short instruction to the analysis.py:

Here the habits are displayed visually with matplotlib using pandas dataframes or simple text outputs are created. The data for the functions are obtained from the database using a functino from the database.py. 
The names of the functions describe the purpose. 
"""

import matplotlib.pyplot as plt
from database import  get_all_habits, get_check_off_dates, get_progress_all, count_id_by_rating, average_rating, lowest_average_rating, highest_average_rating, check_if_ID_exists
from datetime import timedelta, datetime
import database
import random
import pandas as pd
from debug import deprint
#You can turn off/on deprint inside the debug.py

import sys

#Calculate the longest streak for a given habit.
def calculate_longest_streak_for_id(numb):
    """
    Calculates the longest streak(days or weeks in a row) for a given habit ID.

    This function first calls the get_all_habits() function and receives the habit data from the habit table and creates instances of the class Habit and puts them into a list.
    It then creates a dictionary using this list in order to seperate between daily and weekly habits.
    It then checks if there is at least one entry in the list when calling the get_progress_all function and if not returns (data from habits_progress table).
    After that it checks if there are habits with daily and/or weekly, and sets a check variable = True/False.
    Then it calls the get_check_off_dates function for the numbe parameter set -> receiving a list check_offs with dates in the date format.
    The check_off list is used for calculation.
    Depending if the number is in the dictionary connected with daily or weekly it starts the calculation.
    The longest_streak is at least one (because the number is in the habits_progress table)
    The current streak is also set to 1 and is updated with + 1 in the for loop until the time between the dates is more than 1 day/ 1 week.
    If the current streak is bigger it makes the current streak the new longest streak.
    If not it resets the current streak to 1 and starts again until it iterated threw the whole list of dates for the number.
    
    Args:
        numb (int): Is used to calculate longest streak for this habit ID

    Returns:
        longest streak (int) single value     
    
    """


    #Make a dict with 'weekly': ID or 'daily': ID
    habits = get_all_habits()
    habits_dic = {habit.ID : habit.periodicity for habit in habits}
    deprint(type(numb))
    #if empty nothing to calulate (progress_all returns a list with all check-offs of an ID)
    nothing = all(item[0] != numb for item in get_progress_all())

    if nothing:
        return
    
    if "daily" in habits_dic[numb]:
        check_offs_daily = True
    
    else:
        check_offs_daily = False
 
    if "weekly" in habits_dic[numb]:
        check_offs_weekly = True

    else:
        check_offs_weekly = False

    #all check offs for an ID
    check_offs = get_check_off_dates(numb)
    longest_streak = 1
    current_streak = 1
    #first check-off made selected
    previous_check_off = check_offs[0]


    if check_offs_daily is True:
        #check if timedelta is 1 day if so current streak rais by 1
        for check_off in check_offs[1:]:
            if (check_off - previous_check_off) == timedelta(days=1):
                current_streak += 1
                #if current streak is new longest overwrite
                if current_streak > longest_streak:
                    longest_streak = current_streak

            else:
                current_streak = 1
            #new start point for iteration
            previous_check_off = check_off

        return longest_streak

    #same for weekly
    elif check_offs_weekly is True:
        
        for check_off in check_offs[1:]:
            if (check_off - previous_check_off <= timedelta(weeks=1)):
                current_streak += 1

                if current_streak > longest_streak:
                    longest_streak = current_streak

            else:
                current_streak = 1
    
            previous_check_off = check_off


        return longest_streak 



#Plot the longest streak for each habit.
def plot_longest_streaks():
    """
    Plots the habits and the most days off check-offs in a row.

    Retrieves the habit_name and Id from the database.py with the get_all_habits function and the number of days/weeks in a row from the calculate_longest_streak_for_id function.
    It creates a list for all habit_IDs received from the get_all_habits function, with the calculated longest streaks (iterating through all IDs and if there is no streak it puts None into list).
    Then it checks if there is at least one calculated streak (check-off 2 days/weeks in row) otherwise exits and displays a hint.
    To get the habit names later for the legend it creates a habits_name list by iterating through the habits list.
    It complements the habits_dic with the calculated streaks.
    Two new lists data_weekly/data_daily for the dataframe are created and appended with the values and keys from the habits_dic depending wether daily or weekly.
    The dataframes are used to plot the streaks using the pivot -> Returns reshaped DataFrame organized by given column = habit_name and values = longest_streak.
    
    The plot shows a bar chart representing the counts of days/weeks in a row for a habit. 
    The x-axis represents the habits, and the y-axis represents the count of check-offs in a row.
    
    Args:
        None
    
    Return:
        None
    """
    #used to seperate IDs between daily and weekly
    habits = get_all_habits()
    habits_dic = {habit.ID : habit.periodicity for habit in habits}
    habit_name = {habit.ID: habit.habit_name for habit in habits}
    #creates a list with the counts for each habit_ID starting from ID = 0 to the last and None if no check-offs for ID
    longest_streaks = [calculate_longest_streak_for_id(habit.ID) for habit in habits]

    #If there is no check-off for any habit_ID quit
    if all(counts is None for counts in longest_streaks):
        sys.exit("You need to finish at least one Task -> check-off one habit first!❌")
        
    #Make a dict for daily and weekly to create 2 dataframes fro plotting
    habit_names = [f"{habit.habit_name}" for habit in habits]
    #Put the calculated longest streak into the dict as value respectively to the ID
    for key, value in habits_dic.items():
        habits_dic[key] = [value, longest_streaks[key]]
    
    #create a list for the dataframe input
    data_weekly = []
    data_daily = []

    for key, value in habits_dic.items():
        
        if "daily" in value:
            #append data_daily list with second value of the habits_dic (the longest streak of this ID) and the name, ID
            data_daily.append((habit_name[key], key, value[1]))

        if "weekly" in value:

            data_weekly.append((habit_name[key], key, value[1]))
            
    #create dataframe daily
    df_daily = pd.DataFrame(data_daily, columns = ["habit_name", "habit_ID", "longest_streaks"])
    deprint(df_daily)
    df_daily.pivot(columns = "habit_name", values = "longest_streaks").plot(kind = "bar", figsize = (15,8))
    
    #whole numbers for y axis
    plt.locator_params(axis="y", integer=True, tight=True)
    plt.xlabel("Habit ID")
    plt.ylabel("Longest Streak (days)")
    plt.title("Longest Streak of your daily Habits")
    plt.xticks(rotation=0) 
    plt.legend(loc = "upper right")


    #plot the weekly habits in another plot if exist

    df_weekly = pd.DataFrame(data_weekly, columns = ["habit_name", "habit_ID", "longest_streaks"])
    deprint(df_weekly)
    df_weekly.pivot(columns = "habit_name", values = "longest_streaks").plot(kind = "bar", figsize = (15,8))
    
    plt.locator_params(axis="y", integer=True, tight=True)
    plt.xlabel("Habit ID")
    plt.ylabel("Longest Streak (weeks)")
    plt.title("Longest Streak of your weekly Habits")
    plt.legend(loc = "upper right")
    plt.xticks(rotation=0) 

    plt.show()




def plot_habits_by_ratings():
    """
    Plots all habits by their ratings.

    Retrieves the habit ratings and counts from the database, and plots a bar chart
    representing the number of occurrences for each rating. The x-axis represents the ratings,
    and the y-axis represents the count of occurrences.
    Since the calculation for the average rating is the same for daily/weekly there is no seperation between them.

    Args:
        None

    Return:
        None

    """
    habits = get_all_habits()
    habit_name = {habit.ID: habit.habit_name for habit in habits}

    counts = count_id_by_rating()
    deprint(counts)
    data = []
    for row in counts:
        habit_ID, rating, count = row
        data.append((habit_name[habit_ID], rating, count))
    deprint(data)
        
    df = pd.DataFrame(data, columns = ["habit_name","rating","count"])
    deprint(df)
    df.pivot(index = "rating", columns = "habit_name", values = "count").plot(kind = "bar", figsize = (15,8))


    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.title("Habits Rating Summary")
    plt.legend(loc = "upper right")
    plt.show()

        



#plot the average difficulty of all habits 
def plot_average_difficulty_of_habits():
    """
    Plots all habits by their average ratings.

    Retrieves the habit ID and the average rating of all entries for this ID from the database, and plots a bar chart
    representing the average rating for each habit. The x-axis represents the IDs,
    and the y-axis represents the average rating.
    Since the calculation for the average difficulty is the same for daily/weekly there is no seperation between them.

    Args:
        None
    
    Return:
        None
    """  

    habits = get_all_habits()
    habit_name = {habit.ID: habit.habit_name for habit in habits}
    #set size for plot
    plt.rcParams["figure.figsize"] = (15, 8)

    for average in average_rating():
        habit_id, avg_rating = average
        #average_difficulties.append((habit_id, avg_rating))
        
        label = habit_name[habit_id]
        plt.bar(habit_id, avg_rating, label = label)

    plt.xlabel('Habit ID')
    plt.ylabel('Average Difficulty')
    plt.title('Average Difficulty of your Habits')
    plt.legend(loc = "upper right")
    plt.xticks(range(0, len(habits)))
    plt.show()   


#Tells easiest habit
def get_easiest_habit():
    """
    This function returns a string with the name and the average rating of the easiest habit.

    Args:
        None

    Return:
        string: A string with the information for the easiest habit.
    """   

    for lowest in lowest_average_rating():
        habit_id, avg_rating = lowest

    habits = get_all_habits()
    habit_name = {habit.ID: habit.habit_name for habit in habits}

    easiest = habit_name[habit_id]

    feedback = f"Your easiest Habit is -> {easiest} | and has an average rating off: {avg_rating}"

    return feedback



#Tells hardest habit
def get_hardest_habit():
    """
    This function returns a string with the name and the average rating of the hardest habit.

    Args:
        None

    Return:
        string: A string with the information for the hardest habit.
    """ 

    for hardest in highest_average_rating():
        habit_id, avg_rating = hardest

    habits = get_all_habits()
    habit_name = {habit.ID: habit.habit_name for habit in habits}

    hardest = habit_name[habit_id]
    
    feedback = f"Your hardest Habit is -> {hardest} | and has an average rating off: {avg_rating}"

    deprint(type(avg_rating))
    return feedback



def get_timeline_of_habit(habit_id: int):
    """
    This function creates the plot for the timeline of a chosen habit.

    It first checks if the habit exists.
    Then it calls the get_progress_all nd puts it into a list by iterating through the list of tuples.
    It creates a dataframe for the plot. And a second dataframe to make some calculations for the "Big Break" message inside the plot.
    It calculated the time difference beteween the days and if its bigger than 8 days it plot a message.
    The message "Big Break more than 8 days" is set to the position between those dates and between the bars.

    Args:
        habit_id (int): identifies the habit to plot

    Return:
        None
    """

    if habit_id != check_if_ID_exists(habit_id):
        sys.exit(f"Your ID: {habit_id} does not exist!❌ use -> app.py show ...to check your existing habits!")

    habits = get_all_habits()
    habit_name = {habit.ID: habit.habit_name for habit in habits}

    times = get_progress_all()

    data = []
    for row in times: 
        if row[0] == habit_id:
            ID, rating, time = row
            time = datetime.strptime(time, '%Y-%m-%d').date()
            data.append((rating, time))

    deprint(data)
    
    df = pd.DataFrame(data, columns = ["rating", "time"])
    deprint(df)
    df_pivot = df.pivot(index='time', columns='rating')

    fig, xaxis = plt.subplots(figsize=(15, 10))
    plt.bar(df["time"], df["rating"])
    plt.xlabel("Check-off date")
    plt.ylabel("Rating")
    plt.title(f"Timeline of your habit {habit_name[habit_id]} ")
    plt.xticks(rotation=45) 
    plt.xticks(df["time"])

    #little extra to make longer breaks more visible
    prev_date = df_pivot.index[0]
    deprint(prev_date)
    for i, date in enumerate(df_pivot.index):
        
        diff = date - prev_date
        deprint(diff)
        if diff.days > 8:
            location_x = date - (date - prev_date) / 2
            location_y = 0.1
            xaxis.text(location_x, location_y, "B\nI\nG\n \nB\nR\nE\nA\nK\n \n__\n \nM\nO\nR\nE\n \nT\nH\nA\nN\n \n8\n \nD\nA\nY\nS\n", color = "red", weight = "bold")
        prev_date = date


    plt.show()


















