import typer
from rich.console import Console, Group
from rich.table import Table, Column
from rich.progress import Progress, BarColumn, TextColumn
from rich.panel import Panel

from model import Habit
from Coach import Coach
from database import *
from debug import deprint
#You can turn off/on deprint inside the debug.py

from Analyse import plot_longest_streaks, plot_habits_by_ratings, calculate_longest_streak_for_id, plot_average_difficulty_of_habits, get_easiest_habit, get_hardest_habit, get_timeline_of_habit


console = Console()
app = typer.Typer()


@app.command(short_help = "adds new habit")
def add(habit_name: str, description: str):
    """
    Add a new habit to the database.

    This function takes name and description of a new habit as input. It creates a Habit object, and inserts it into the database.

    Args:
        habit_name (str): The name of the habit.
        description (str): The description of the habit.

    Returns:
        None

    """

    typer.echo(f"adding {habit_name}, {description}")
    habit = Habit(habit_name, description)
    insert_habit(habit)



@app.command(short_help = "delets a choosen habit by its ID")
def delete(numb: int):    
    """
    Deletes an existing habit from the database.
    
    This function first checks if the ID exists.
    It takes the ID of an existing habit as input. It deletes all attributes of the habit from the database .
    

    Args:
        habit_name (str): The name of the habit.
        description (str): The description of the habit.

    Returns:
        None

    """

    if numb != check_if_ID_exists(numb):
        sys.exit(f"Your ID: {numb} does not exist!❌ use -> app.py show ...to check your existing habits!")

    typer.echo(f"Try to delete {numb}...")  
    delete_habit(numb)



@app.command(short_help = "updates a choosen habit")
def update(numb: int, habit_name: str = None, description: str = None):
    """
    Updates an existing habit in the habits table. 

    This function takes the ID of an existing habit as input. 
    It first checks if the ID exists.
    The optional paramteres habit_name and description are used to change them respectively in the habits table. 
    If the numb does not exist as ID in the habits table a hint is displayed to use the 'show' command to check all existing habits.

    Args:
        numb (int): Identifies the row in the habit table.
        habit_name (str, optional): Used to change the name of an existing habit.
        description (str, optional): Used to change the description of an existing habit:
    Returns:
        None

    """

    if numb != check_if_ID_exists(numb):
        sys.exit(f"Your ID: {numb} does not exist!❌ use -> app.py show ...to check your existing habits!")

    typer.echo(f"updating {numb}")
    update_habit(numb, habit_name, description)



@app.command(short_help = "updates the period you want to finish a habit. You can choose between: 'daily' or 'weekly'")
def update_period(numb: int, periodicity: str):
    """
    Updates the periodicity of an existing habit in the habits table.

    This function takes the ID of an existing habit and a choosen periodicity as input. 
    It first checks if the ID exists.
    It then checks the input parameter periodicity, if it is 'daily' or 'weekly'. Otherwise a hint is displayed.

    Args:
        numb (int): Identifies the row in the habit table.
        periodicity (str): Can be set to 'daily' or 'weekly'

    Returns:
        None

    """

    if numb != check_if_ID_exists(numb):
        sys.exit(f"Your ID: {numb} does not exist!❌ use -> app.py show ...to check your existing habits!")

    if periodicity == "daily" or periodicity == "weekly":
        update_periodicity(numb, periodicity)
        print(f"Your habit with ID: {numb} is successfully set to: {periodicity}✅")

    else:
        print("You have to choose between 'daily' or 'weekly' for your habit periodicity!❌")



@app.command(short_help = "shows all habits with details")
def show():
    """
    Fetch data from the 'habits' table from the database and creates instances of class Habits. 
    It then display the data in a table using the rich library.

    This function calls the function -> get_all_habits ..to fetch data from the 'habits' table and create instances of class Habits.
    It then uses a table object to organize and display the data in a 'nicer' format.

    Returns:
        None

    """

    habits = get_all_habits()
    deprint(habits)
    table = Table(show_header = True, header_style = "bold green")
    table.add_column("habit_name", min_width = 20, style="bold cyan")
    table.add_column("Description",  min_width = 12, style="bold magenta")
    table.add_column("Date_added", style = "blue", min_width = 12)
    table.add_column("Progress", min_width = 12, justify = "right")
    table.add_column("ID", style = "dim", width = 6, justify = "right")
    table.add_column("Periodicity", style = "dim", width = 12)
  
    for part in habits:        
        table.add_row(str(part.habit_name), str(part.description), str(part.date_added), str(part.progress), str(part.ID), str(part.periodicity))         
    
    console.print(table)



@app.command(short_help = "check-off a habit you finished today with a rating from 1-5 -> 1 is easy/ 5 is hard")
def check_off(numb: int, rating: int):
    """
    Checks off a given habit with a rating. 

    This function first checks if the ID exists.    
    It then checks if the rating is a number from 1 to 5 -> otherwise a hint is displayed.
    It then inserts a new row in the table habits_progress with the ID the rating and the check_off_time(the actual time)

    Args:
        numb (int): Identifies the row in the habit table.
        rating (int): Used to show difficulty of the checked-off habit (1-5).

    Returns:
        None
    """

    deprint(numb)
    if numb != check_if_ID_exists(numb):
        sys.exit(f"Your ID: {numb} does not exist!❌ use -> app.py show ...to check your existing habits!")

    if rating > 5 or rating < 1:
        print("The rating has to be a number from 1 -5!")
        return

    check_off_habit(numb, rating)


@app.command(short_help = "uncheck-off a habit you accidentally check-off today")
def uncheck_off(numb: int):
    """
    Unchecks a check-off if made today.

    This function first checks if the ID exists.    
    It then calls the undo_check_off_habit function from the database.py and Deletes if possible the row of the today made check-off from the habits_progress table

    Args:
        numb (int): Identifies the row in the habit table.
    
    Return:
        None

    """
    if numb != check_if_ID_exists(numb):
        sys.exit(f"Your ID: {numb} does not exist!❌ use -> app.py show ...to check your existing habits!")

    undo_check_off_habit(numb)



@app.command(short_help = "shows the check-off times off all habits and their rating")
def show_progress():
    """
    Displays the checkoff times from all habits.

    This function calls the get_progress_all function to receive a list of all check-offs from all habits.
    It then creates a Table and adds each row from the check-offs into the table.
    The Table is displayed.
    
    Args:
        None

    Return:
        None
    """

    progress = get_progress_all()
    table = Table(show_header = True, header_style = "bold blue")
    table.add_column("ID", min_width = 20)
    table.add_column("rating", min_width = 12, justify = "right")
    table.add_column("check_off_time", min_width = 12, justify = "right")
  
    for part in progress:       
        table.add_row(str(part[0]), str(part[1]), str(part[2]))
    
    console.print(table)



# Analysis.......................


#gives the count of the longest streak of a chosen habit
@app.command(short_help = "choose a habit by it's ID and check your longest streak")
def longest_streak_ID(numb):
    """
    Calculates the longest streak for a given habit ID.

    This function first displays a short message using typer.echo and then calls the calculate_longest_streak_for_id function.
    It prints the return of calculate_longest_streak_for_id.

    Args:
        numb
    
    Return:
        None
    """
    typer.echo(f"Longest streak for ID {numb} is calculated with:")   
    print(calculate_longest_streak_for_id(int(numb)))



#plots longest streak of each habit
@app.command(short_help = "shows the longest streak for each of your habits")
def longest_streaks():
    """
    Plots the longest streaks of all habits.
    
    It calls the plot_longest_streaks function which calls the calculate_longest_streak_for_id for every habit ID.
    The return of calculate_longest_streak_for_id for each habit ID is put into a dataframe and used to display the plot.
    The plots show all habits and their longest streaks. One for the daily and one for the weekly.
    On the x axis the Habit ID and on the y axis the streak.
    
    Args:
        None
    
    Return:
        None
    """
    plot_longest_streaks()



#plots the count of each habit for each rating
@app.command(short_help = "shows for each rating the count of your checked off habits")
def habits_ratings():
    """
    Plots all habits and there counts per rating.
    
    It calls the plot_habits_by_ratings function which calls the count_id_by_rating. 
    The return of count_id_by_rating is put into a dataframe and used to display the plot.
    The plots show all habits and their occurence in each rting (1-5). Daily and weekly are displayed together.
    On the x axis the rating and on the y axis the count of occurence.
    
    Args:
        None
    
    Return:
        None
    """
    plot_habits_by_ratings()



@app.command(short_help = "shows for each rating the count of your checked off habits")
def average_rating_habits():
    """
    Plots the all habits and the level of difficulty in average.
    
    It calls the plot_average_difficulty_of_habits function which calls the average_rating and creates bars by iterating through it. 
 
    The plots show all habits and their avergage difficulty. Daily and weekly are displayed together.
    On the x axis the ID and on the y axis the Difficulty.
    
    Args:
        None
    
    Return:
        None
    """
    plot_average_difficulty_of_habits()



@app.command(short_help = "shows you your easiest habit you have managed to do so far")
def easiest_habit():
    """
    Displayes a short message with the name and the average rating of the easiest habit (lowest average rating).
    
    This function prints the return of the called funtion get_easiest_habit which calls the lowest_average_rating.
    The lowest_average_rating returns an ID and the average rating of the lowest average rating.
    The get_easiest_habit uses the get_all_habits to receive the name of the habit for the given ID.

    Args:
        None

    Return:
        string: A string with the information for the hardest habit.
    
    """
    print(get_easiest_habit())



@app.command(short_help = "shows you your hardest habit you have managed to do so far")
def hardest_habit():
    """
    Displayes a short message with the name and the average rating of the hardest habit (highest average rating).
    
    This function prints the return of the called funtion get_hardest_habit which calls the highest_average_rating.
    The highest_average_rating returns an ID and the average rating of the highest average rating.
    The highest_average_rating function uses the get_all_habits to receive the name of the habit for the given ID.

    Args:
        None

    Return:
        string: A string with the information for the hardest habit.
    
    """
    print(get_hardest_habit())


@app.command(short_help = "shows timeline of a chosen habit with dates and ratings")
def timeline(habit_id: int):
    """
    Plots the timeline of a chosen habit.

    This function calls the get_timeline_of_habit function.

    A plot is displayed with rating on the y axis and the dates of check-offs on the x axis.
    
    Args:
        habit_id (int): The ID of the chosen habit.

    Return:
        None
    """


    print(get_timeline_of_habit(habit_id))


#Coach......................


@app.command(short_help = "Receive emails from a coach to be remindet to finish your choose task")
def activate_coach(email: str, habit_id: int):
    """
    This function activates the coach (an email service) for a chosen habit.

    It first creates an instance of the Coach class for the given habit.
    Then it calls the send_reminder function from the Coach class.

    Args:
        email (str): Email adress from the receiver
        habit_id (int): The ID of the chosen habit.

    Return:
        string: A short message if or if not successful
    """

    coach = Coach(email, habit_id)
    coach.send_reminder()


@app.command(short_help = "Inactivate the Coach for a given ID")
def inactivate_coach(email, habit_id):
    """
    This function inactivates the coach (an email service) for a chosen habit.

    It first creates an instance of the Coach class for the given habit.
    Then it calls the inactivate_id function from the Coach class to inactivate the email service..

    Args:
        email (str): Email adress from the receiver.
        habit_id (int): The ID of the chosen habit.

    Return:
        string: A short message if or if not successful
    """

    coach = Coach(email, habit_id)
    coach.inactivate_id()


#run app 
if __name__ == "__main__":
    
    app()
