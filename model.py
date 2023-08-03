"""
Bref instruction about the class
"""

import datetime


"""
A class representing a habit that can be tracked by the habit tracker app.
"""

class Habit:
    def __init__(self, habit_name: str, description: str, date_added: str = None, progress: int = 0, ID: int = None, periodicity: str = "daily", email: str = None):


        """
        Initialize a new Habit object.

        Parameters:
        - habit_name (str): The name of the habit.
        - description (str): A detailed description of the habit.
        - date_added (str, optional): The date when the habit was added. Defaults to the current date.
        - progress (int, optional): The progress of the habit (in total counts). Defaults to 0.
        - ID (int, optional): The ID of the habit. Defaults to 0.
        - email (str: optional): The email adress to receive reminder emails from the Coach.
        - periodicity (str: optional): Is set to 'daily' and can be changed to ’weekly’ with a function called update_periodicity.
        """

        self.habit_name = habit_name
        self.description = description
        self.date_added = date_added if date_added is not None else datetime.datetime.now().strftime("%Y-%m-%d")  
        self.progress = progress 
        self.ID = ID 
        self.email = email 
        self.periodicity = periodicity if periodicity is not None else "daily"


    #opjekt printed in one string
    def __repr__(self) -> str:

        """
        Return a string representation of the Habit object.
        """

        #return f"Habit({self.habit_name}, {self.description}, {self.date_added}, {self.progress}, {self.ID}, {self.periodicity})"
        return f"Habit('{self.habit_name}', '{self.description}', '{self.date_added}', {self.progress}, {self.ID}, '{self.periodicity}')"














