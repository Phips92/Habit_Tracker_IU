import pymysql
from tqdm import tqdm
from typing import List
from datetime import datetime, timedelta
from model import Habit
import rich
from rich.progress import Progress, BarColumn, TextColumn, Task, MofNCompleteColumn
from rich.table import Column
import time

import sys

from debug import deprint
#You can turn off/on deprint in the debug.py

db = pymysql.connect(host="localhost",user="phips",password="phips",database="db_test")
cursor = db.cursor()



def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS habits
                  (ID int,
                   habit_name text,
                   description text,
                   date_added text,
                   progress int,
                   periodicity text)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS habits_progress
                  (ID int,
                   rating int,
                   check_off_time text)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS activated_ids
                  (IDs int)""")
                
    
#create the tables in database if they don't exist yet 
create_table()



#insert a new habit into the table
def insert_habit(habit: Habit):
    """
    Insert a new habit into the database.

    This function inserts a Habit object into the table "habits" in the database db_test.
    It assigns a unique ID to the habit based on the current count of habits in the table.

    Args:
        habit (Habit): The Habit object to be inserted into the database.

    Returns:
        None



    """   
     
    sql = "SELECT COUNT(*) FROM habits"
    cursor.execute(sql)
    count = cursor.fetchone()[0]
    habit.ID = count if count else 0

    #with db: is used to manage the lifecycle of the connection -> __enter__ and __exit__ to clean up automatically 
    with db:
        sql = "INSERT INTO habits VALUES (%s, %s, %s, %s, %s, %s)"     
        data = (habit.ID, habit.habit_name, habit.description, habit.date_added, habit.progress, habit.periodicity)
        cursor.execute(sql, data)
        db.commit()



#get a list off all habits with details
def get_all_habits():   
    """
    Get data from the 'habits' table and creates instances of the class Habit.

    This function executes an SQL query to fetch all rows from the 'habits' table.
    Then it iterated over the results and creates instances of the class Habits using the fetched data.
    

    Returns:
        all habits - > list: A list of instances of the class Habits. 


    """

    sql = "SELECT habit_name, description, date_added, progress, ID, periodicity FROM habits"   
    cursor.execute(sql)
    results = cursor.fetchall()

    habits = []
    for result in results:
        #Habit(*result) -> creates an nstance of class Habit by passing result as argument
        habits.append(Habit(*result))

    return habits



#deletes a chosen habit
def delete_habit(habit_id):
    """
    Deletes an existing habit in all Tables from the database.

    This function delets an existing Habit identified by its ID from all Tables in the database db_test.
    First it slects the count of the habits table. 
    This is used to switch the possitions of the habits in the range of the ID from the deleted habit to the total amount of habits (IDs must change).
    It then deletes the habit with the given ID from all tables.
    It then calls the change_ID function to change the old_ID with the new_ID (old_ID -1).
    Then the 

    A short text is displayed with: f"ID {habit_id} is deleted" to let the user know it worked.


    Args:
        habit_id: The parameter to be used in the sql quere inside the databse.

    Returns:
        None


    """  
    sql = "SELECT COUNT(*) FROM habits"    
    cursor.execute(sql)
    count = cursor.fetchone()[0]

    with db:        
        sql = "DELETE FROM habits WHERE ID = %s"
        data = habit_id
        cursor.execute(sql, data)
        db.commit()

        sql = "DELETE FROM habits_progress WHERE ID = %s"
        data = habit_id
        cursor.execute(sql, data)
        db.commit()

        sql = "DELETE FROM activated_ids WHERE IDs = %s"
        data = habit_id
        cursor.execute(sql, data)
        db.commit()

        for old_ID in range(habit_id + 1 , count):
            change_ID(old_ID, old_ID - 1, commit = False)

    print(f"ID {habit_id} is deleted")   


#change ID to don't mess up table and have continous ID's
def change_ID(old_ID: int, new_ID: int, commit = True):
    """
    Updates the IDs in the tables habits, habits_progress and activated_ids. This is neccessary to not mess up if a habit gets deleted.
 
    Args:
        old_ID: The parameter to be used in the sql quere inside the database.
        new_ID: same as old_ID

    Returns:
        None
    """
    sql = "UPDATE habits SET ID = %s WHERE ID = %s"
    data = (new_ID, old_ID)
    cursor.execute(sql, data)    
    db.commit() 

    sql = "UPDATE habits SET ID = %s WHERE ID = %s"
    data = (new_ID, old_ID)
    cursor.execute(sql, data)    
    db.commit()    

    sql = "UPDATE habits SET ID = %s WHERE ID = %s"
    data = (new_ID, old_ID)
    cursor.execute(sql, data)    
    db.commit()    
   

    



#Update all or just the name or description of the habit
def update_habit(habit_id: int, habit_name: str, description: str):
    """
    Updates a habit in the habits table. 

    This function updates a habit identified by its ID with optional paramteres habit_name and description. 
    
    Args: 
        habit_id (int): Identifies the row in the habit table.
        habit_name (str, optional): Used to change the name of an existing habit.
        description (str, optional): Used to change the description of an existing habit:

    Returns:
        None


    """

    with db:
        if habit_name is not None and description is not None:

            sql = "UPDATE habits SET habit_name = %s, description = %s WHERE ID = %s"
            data = (habit_id, habit_name, description)
            cursor.execute(sql, data)
            db.commit()

        elif habit_name is not None:

            sql = "UPDATE habits SET habit_name = %s WHERE ID = %s"
            data = (habit_name, habit_id)            
            cursor.execute(sql, data)
            db.commit()

        elif description is not None:

            sql = "UPDATE habits SET description = %s WHERE ID = %s"
            data = (description, habit_id)
            cursor.execute(sql, data)
            db.commit()            
        
        else:
            print(f"There is nothing to update for your Habit with ID {habit_id}. -> use --help for explanation.")


#updates the periodicity of a chosen habit 
def update_periodicity(habit_id: int, periodicity: str):
    """
    Updates the habits periodicity in the habits table. 

    This function updates a habit identified by its ID. The periodicity can be 'daily' or 'weekly' 
    
    Args: 
        habit_id (int): Identifies the row in the habit table.
        periodicity (str): Can be set to 'daily' or 'weekly'


    Returns:
        None


    """

    with db:
        sql = "UPDATE habits SET periodicity = %s WHERE ID = %s"
        data = (periodicity, habit_id)
        cursor.execute(sql, data)
        db.commit()


#checks if a given ID even exists
def check_if_ID_exists(habit_id: int):
    """
    Checks if a habit with the given ID exists.
    Used for most functions in app.py

    This function selects the ID of the table habit where the ID = the parameter(habit_id)
    It return the number of the ID if it exists and otherwise ().
    
    Raises:
        TypeError: Occures if the sql quere returns empty set() 
        (TypeError: 'NoneType' object is not subscriptable)

    Args:
        habit_id (int): Identifies the row in the habit table.

    Returns:
        tupel: check (this is the habit_id) or -1
    """
    try:       
        sql = "SELECT ID FROM habits WHERE ID = %s;"
        data = habit_id        
        cursor.execute(sql, data)
        check = cursor.fetchone()[0]

        return check

    except TypeError:

        return -1



#check off habits if they are done
def check_off_habit(habit_id: int, rating: int):
    """
    Checks off a given habit with a rating. 

    This function first gets the progress from the habits table and checks if its zero. If so it sets check_alr_checked_off = ()
    check_alr_checked_off is used to check if there is a check-off already made this day or the last 7 days(if the habits periodicity is set weekly)
    If so a text is displayes that the habit is already checked-off.
    The sql queries first input the habit_id ,rating and the actual time (for the check_off_time) into the table habits_progress.
    The next querie counts the number off check offs for the ID and raises in the next one the number of progress in the habits table.

    The function get_all_habits is called to create a dictionary to use the respective name of the habit for display.

    Args: 
        habit_id (int): Identifies the row in the habits and habits_progress table.
        rating (int): Is inserted into the habits_progress table.

    Return:
        None

    """
   
    with db:
    
        sql = "SELECT check_off_time from habits_progress WHERE ID = %s"
        data = habit_id
        cursor.execute(sql, data)
        check_alr_checked_off = cursor.fetchall()
    

      #  deprint(datetime.now().strftime("%Y-%m-%d"))

        #split in daily weekly
        sql = "SELECT periodicity FROM habits WHERE ID = %s"
        data = habit_id
        cursor.execute(sql, data)

        period = cursor.fetchone()[0]
       # deprint(period)
       # deprint(check_alr_checked_off)                
        check_alr_checked_off = [check[0] for check in check_alr_checked_off]
       # deprint(check_alr_checked_off)                

        if period == "daily":

            if datetime.now().strftime("%Y-%m-%d") in check_alr_checked_off:
                sys.exit(f"Your Habit with ID: {habit_id} is already checked-off for today ✅")

        elif period == "weekly":
            # create a list with the dates of the last seven days
            today = datetime.now().date()
            deprint(today)

            check_date = [today - timedelta(days = x) for x in range(7)]
            check_date = [date.strftime("%Y-%m-%d") for date in check_date]
            deprint(check_date)
            deprint(check_alr_checked_off)
            for date in check_date:
                if date in check_alr_checked_off:
                    sys.exit(f"Your Habit with ID: {habit_id} is already checked-off for this week ✅")


        sql = "INSERT INTO habits_progress VALUES (%s, %s, %s)"
        data = (habit_id, rating, datetime.now().strftime("%Y-%m-%d"))
        cursor.execute(sql, data)
        db.commit()

        count_progress = ("SELECT COUNT(*) FROM habits_progress WHERE ID = %s")
        cursor.execute(count_progress, habit_id)
        progress = cursor.fetchone()[0]
        
        sql = "UPDATE habits SET progress = %s WHERE ID = %s"
        data = (progress, habit_id)
        cursor.execute(sql, data)
        db.commit()


        habits = get_all_habits()
        habit_name = {habit.ID: habit.habit_name for habit in habits}

        print(f"Your Habit {habit_name[habit_id]} is checked-off ✅ ")

  
        

def undo_check_off_habit(habit_id: int):
    """
    Undo a check-off at the same day (if accedentally checked off).
    
    This function first selects the check_off_time for the given habit from the habits_progress table and stores the date in a tuple.
    It then deletes the row with the habit ID and the todays date from the habits_progress table.
    If there was no check-off for this day uncheck is None.
    It then displays either success or that there was no check off for today.

    The function get_all_habits is called to create a dictionary to use the respective name of the habit for display.

    Args:
        habit_id (int): Identifies the row in the habits_progress table.
    
    Return:
        None

    """


    with db:

        sql = "SELECT check_off_time FROM habits_progress WHERE ID = %s ORDER BY check_off_time DESC"
        data = habit_id
        cursor.execute(sql, data)

        uncheck = cursor.fetchone()

        sql = "DELETE FROM habits_progress WHERE ID = %s AND check_off_time = %s"
        data = (habit_id, datetime.now().strftime("%Y-%m-%d")) 
        cursor.execute(sql, data)
        db.commit()

        deprint(uncheck)

        habits = get_all_habits()
        habit_name = {habit.ID: habit.habit_name for habit in habits}


        if uncheck == None:
            print(f"You have not checked-off your habit: {habit_name[habit_id]} for today ❌")

        else:
            print(f"Your check-off for the habit: {habit_name[habit_id]} is deleted. Now you have not finished your Habit: {habit_name[habit_id]} for today ❌")



#get a list of the progress table
def get_progress_all():
    """
    Shows the check-offs from every habit

    This function selects all rows from the habits_progress table and puts it in a list.    

    Args:
        None
    
    Return:
        list: A list of all check-offs [ID, rating, check_off_time]
    """


    sql = "SELECT ID, rating, check_off_time FROM habits_progress"
    cursor.execute(sql)

    results = cursor.fetchall()

    progress = []
    for result in results:
        progress.append(result)
    #deprint(progress)
    return progress




"""
For Analyzation
"""

#get a list of all check-offs from a given habit 

def get_check_off_dates(habit_id: int):
    """
    This function creates a list of all check off dates of a given habit ID.

    The function selects all rows of the habits_progress table in the check_off_date column by ascending form.
    It then brings the fetched data into a date format so it can be used for calculatnig time differences in other functions.

    Args:
        habit_id (int)

    Returns:
        list: A list of all check-off dates from a given habit ID -> date format 
    """


    sql = "SELECT check_off_time FROM habits_progress WHERE ID = %s ORDER BY check_off_time ASC"
    data = habit_id
    cursor.execute(sql, data)
    dates = cursor.fetchall()
    #bring str into date format for calculation
    formatted_dates = [datetime.strptime(correct_date[0], "%Y-%m-%d").date() for correct_date in dates]

    return formatted_dates



def count_id_by_rating():
    """
    This function returns a tuple of tuples with the counts of a habit for all ratings.

    It first selects all IDs and ratings, orders the tupels in descending form and counts the occurence of this constelation.

    Args:
        None
    
    Return:
        tuple: A tuple of tuples for all habits and their rating count. 
    """


    sql = "SELECT ID, rating, COUNT(*) as count FROM habits_progress GROUP BY ID, rating"
    cursor.execute(sql)
    count = cursor.fetchall()
    db.commit()
    return count


def average_rating():
    """
    This function returns a tuple of tuples with the ID and the average rating sorted by the ID in descending form.

    Args:
        None
    
    Return:
        tupel: A tupel of tuples with the ID and the average rating of the check-offs.
    """
    sql = "SELECT ID, AVG(rating) as avg_rating FROM habits_progress GROUP BY ID"
    cursor.execute(sql)
    average = cursor.fetchall()
    db.commit()
    deprint(average)
    return average


def lowest_average_rating():
    """
    This function returns a tuple of tuples with the ID and the average rating of the lowest average rating.

    Args:
        None

    Return:
        tuple: A tuple of tuple with a single tuple containing the ID and the average rating (DEZIMAL)
    """

    sql = "SELECT ID, AVG(rating) as avg_rating FROM habits_progress GROUP BY ID ORDER BY avg_rating ASC LIMIT 1 "
    cursor.execute(sql)
    lowest = cursor.fetchall()
    db.commit()
    return lowest


def highest_average_rating():
    """
    This function returns a tuple of tuples with the ID and the average rating of the highest average rating.

    Args:
        None

    Return:
        tuple: A tuple of tuple with a single tuple containing the ID and the average rating (DEZIMAL)
    """
    sql = "SELECT ID, AVG(rating) as avg_rating FROM habits_progress GROUP BY ID ORDER BY avg_rating DESC LIMIT 1 "
    cursor.execute(sql)
    hardest = cursor.fetchall()
    deprint(hardest)
    db.commit()
    return hardest




"""
For Coach
"""

def get_periodicity_for_ID(habit_id: str):
    """
    This function returns a tuple of tuple with the periodicity (daily or weekly) and the habit ID.

    Args:
        habit_id (int): To get the correct rows from the database table habits.

    Return:
        tuple: A tuple with a single tuple of the periodicity and the habit ID of a chosen habit.
        
    """

    sql = "SELECT periodicity FROM habits WHERE ID = %s"
    data = habit_id
    cursor.execute(sql, data)
    periodicity = cursor.fetchone()[0]


    return periodicity
 



def activated_ids():
    """
    This function returns a tuple of tuples with all IDs from habits which have activated the coach(email service).

    Args:
        None
    
    Return:
        tuple: A tuple of tuples with the IDs of activated habits.
    """
    sql = "SELECT IDs FROM activated_ids"
    cursor.execute(sql)
    IDs = cursor.fetchall()

    return IDs
 

   
def insert_habit_id(habit_id: int):
    """
    This function stores a habit ID into the table activated_ids from the database.

    Args:
        None
    
    Return:
        None 
    """
    sql = "INSERT INTO activated_ids VALUES (%s)"
    data = habit_id
    cursor.execute(sql, data)
    db.commit()


def delete_habit_id(habit_id: int):
    """
    This function deletes an ID of a habit with activated coach.

    Args:
        None
        
    Return:
        None
    """
    sql = "DELETE FROM activated_ids WHERE IDs = (%s)"
    data = habit_id
    cursor.execute(sql, data)
    db.commit()



def check_day_streak(habit_id: int):
    """
    This function tells if there is a 10, 30 or 60 days streak for a habit.
    
    It first calls the get_check_off_dates function to receive the dates from the database for the habit.
    It then reverses the dates to get the last date and start their to check backwards if the dates calculated are in the list.
    It returns a list with the number of days from the streak and the respective reward.

    Args:
        habit_id (int)

    Return:
        list: [count, reward] count = number of days of streak, reward = gold, silver or bronce for the streak
        Boolean: False (if their is no streak at all)
    """
    
    dates = get_check_off_dates(habit_id)
    
    #dates are ascending but we need descending
    dates.sort(reverse=True)

    #deprint(dates)
    #get the last date of check-off
    actual_date = dates[0]
    deprint(actual_date)    
    
    today = datetime.now().date()
    deprint(today)    

    if actual_date != today:
        return False

    count = 0
    reward = {60: "🥇", 30: "🥈",10: "🥉"}

    #check if the dates are the same in range of 60 days
    for day in range(1, 61):
        check_date = actual_date - timedelta(days = day)
        if check_date in dates:
            count += 1

        else:
            count = 0

    if count > 0:
        return [count, reward[count]]

    #check if the dates are the same in range of 30 days
    for day in range(1, 31):
        check_date = actual_date - timedelta(days = day)
        if check_date in dates:
            count += 1

        else:
            count = 0

    if count > 0:
        return [count, reward[count]]

    #check if the dates are the same in range of 10 days
    for day in range(1, 11):
        check_date = actual_date - timedelta(days = day)
        if check_date in dates:
            count += 1

        else:
            count = 0    
   
    #f no streak return false
    if count > 0:
        return [count, reward[count]]

    else:
        return False





def check_weeks_streak(habit_id: int):
    """
    This function tells if there is a 4, 8, or 15 weeks streak for a habit.

    It first calls the get_check_off_dates function to receive the dates from the database for the habit.
    It then creates a set of numbers (calender weeks) respectivels to the check-off dates.
    It then checks if there are x numbers in a row.
    If the count is not set to 0 in the range of a streak it returns the number of days and the respective reward in a list.

    Args:
        habit_id (int)

    Return:
        list: [count, reward] count = number of weeks of streak, reward = gold, silver or bronce for the streak
        Boolean: False (if their is no streak at all)

    """


    dates = get_check_off_dates(habit_id)
    dates.sort(reverse=True)

    #get calender weeks for each date
    weeks = [date.isocalendar() for date in dates]
    deprint(weeks)
    #last entry of database dates
    actual_week = weeks[0]
    deprint(actual_week)

    #check if the actual_week is the current week
    today = datetime.now().date()
    today = today.isocalendar()
    deprint(today)

    #get just the year and week from the tuple created isocalendar (year = , week = , weekday =) and check if not equal
    if actual_week.week != today.year and actual_week.week != today.week :
        return False
    
    #iterate throgh set and check if there are 4 weeks in a row
    count = 0
    reward = {15: "🥇", 8: "🥈",4: "🥉"}
    deprint(count)

    for week in range(1, 16):
        deprint(actual_week.week)
        #get only the weeks of the list of datetime.IsoCalendatDate objects.
        if actual_week.week - 1 in [only_week.week for only_week in weeks]:
            count += 1
        else:
            count = 0

    if count > 0:
        return [count, reward[count]]

    for week in range(1, 9):
        deprint(actual_week.week)
        #get only the weeks of the list of datetime.IsoCalendatDate objects.
        if actual_week.week - 1 in [only_week.week for only_week in weeks]:
            count += 1
        else:
            count = 0

    if count > 0:
        return [count, reward[count]]


    for week in range(1, 5):
        deprint(actual_week.week)
        #get only the weeks of the list of datetime.IsoCalendatDate objects.
        if actual_week.week - 1 in [only_week.week for only_week in weeks]:
            count += 1
        else:
            count = 0

    if count > 0:
        return [count, reward[count]]

    else:
        return False

    












