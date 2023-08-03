"""
explanation of the coach class

"""

import smtplib
from email.mime.text import MIMEText
import yagmail
from model import Habit
from datetime import datetime, timedelta

from database import activated_ids, insert_habit_id, delete_habit_id, get_periodicity_for_ID, check_if_ID_exists, get_all_habits, get_check_off_dates, check_day_streak, check_weeks_streak
from debug import deprint
#You can turn off/on deprint inside the debug.py

import sys

from crontab import CronTab

class Coach(Habit):

    def __init__(self, email: str, habit_id: str):
        #""is for description
        super().__init__(habit_id, "", email = email)
        self.periodicity = get_periodicity_for_ID(habit_id)
        self.email = email
        self.habit_id = habit_id

        """
        Initialize a new Coach object. Inherites from Habit.

        Paramters:
        - habit_id (int, optional): The ID of the habit. Defaults to 0.
        - email (str: optional): The email adress to receive reminder emails from the Coach.
        - periodicity (str: optional): Is set to 'daily' and can be changed to ’weekly’ with a function called update_periodicity.

        
        """

    def setup_cron_job(habit_id: int):
        """
        Starts the Cron job by writing the time and the habit_id into the crone tab file.
        The cron object is an instance of the CronTab class from the python-crontab library.
        First the CronTab class is used to instantiate a cron object, 
        then the cron object is used to declaratively manipulate the cron. 
        Lastly, declared changes get written to the cron tab by calling write on the object.
        Args: 
            habit_id (int): To write the job for a chosen habit into the cron tab.

        Return:
            None
        """
        cron = CronTab(user = True)
        job = cron.new(command = f"/usr/bin/python3 {__file__} {habit_id}")
        #day hour .... 0 10 means 10 am every day
        job.setall("0 10 * * *") 
        cron.write()


    def send_reminder(self):
        """
        This function activates the coach and sends email to a given adress.

        The habit_name is received from the get_all_habits function.

        In the beginning the function first checks if the habit ID even exists (if not message displyed).
        It first checks if the habit ID is already in the activated_ids table by calling the activated_ids function.
        If not it calls the insert_habit_id function to store the ID into the activated_ids table from the database.
        
        After creating variables with the actual date and two to calculate the timedifference for 2 days and 1 week,
        it checks the periodicity from the habit by calling the get_periodicity_for_ID function (self.periodicity = get_periodicity_for_ID(habit_id)).
        Wether its daily or weekly it starts the calculation inside the respective if statement. 
        The calculation is the same with one differnce if the habit is weekly .
        If weekly it checks only on sunday to make sure you check off your weekly habit.
        First it receives all check-off times for the habit by calling the get_progress_by_ID function.
        It iterates through the check_off_times and checks if any of the check_off_times - 2 days (or 1 week) is smaller or equal the todays date.
        If there is none this means there is no check off for the last two days and the function creates an email using the yagmail library.
        It puts the name into the body of the email message and sends it to the receiver email.
        At the end a short message is displayed to let the user know it worked.

        Args:
            habit_id (int): The ID of the habit to set the cron job for a specific habit.
            email (str): The email adress to receive reminder emails from the Coach.
            periodicity (str): To get the correct calculation to send the reminder email at hte correct time.
            
        Return:
            None
        """

        #check existence of ID
        if check_if_ID_exists(self.habit_id) == -1:
            sys.exit("Your ID does not exist❌. To check your exsting IDs use -> python3 app.py show")

        habits = get_all_habits()
        habit_name = {habit.ID: habit.habit_name for habit in habits}

        deprint(activated_ids())
        #check if already activated
        if str(self.habit_id) in str(activated_ids()):
            print(f"You have already activated the Coach for your Habit: {habit_name[self.habit_id]}")
            return
        #insert into activated_ids table
        else:
            insert_habit_id(self.habit_id)


        today = datetime.now().date()
        two_days_ago = today - timedelta(days=2)
        week_ago = today - timedelta(weeks=1)
        #check periodicity  
        deprint(today)
        deprint(self.periodicity)

        if self.periodicity == "daily":
            #receive check off times for the habit
            check_off_times = get_check_off_dates(self.habit_id)
            deprint(check_off_times)
            #iterate through the check off times of the habit and if there are no matches where the timedelta is less then 2 days continue
            if not any(two_days_ago <= check_off_time < today for check_off_time in check_off_times):

                subject = 'Habit Reminder'
                body = f"Don't forget to check off your habit {habit_name[self.habit_id]}! It just needs a little bit more effort 🤏🏿"
                #email adress ofsender email and generated key (generated by gmail account)
                yag = yagmail.SMTP("phil92.mcg@gmail.com", "dsiiwhynrztcpdnd")
                yag.send(to = self.email, subject = subject, contents = body)
                yag.close()

            #Send congrets for streak
            deprint(check_day_streak(self.habit_id))
            if type(check_day_streak(self.habit_id)) == list:
                subject = f"Habit Streak of {check_day_streak(self.habit_id)[0]} days🔥🚀 "
                body = f"Congratulation you have reached a streak of {check_day_streak(self.habit_id)[0]} days in a row for your habit: {habit_name[self.habit_id]} \n You have received a reward: {check_day_streak(self.habit_id)[1]} \n Keep Going🚀"
                yag = yagmail.SMTP("phil92.mcg@gmail.com", "dsiiwhynrztcpdnd")
                yag.send(to = self.email, subject = subject, contents = body)
                yag.close()
                

        elif self.periodicity == "weekly":
            #only on sunday
            deprint(today.weekday())
            if today.weekday() == 4:  

                check_off_times = get_check_off_dates(self.habit_id)
                if not any(week_ago <= check_off_time <= today for check_off_time in check_off_times):

                    subject = 'Habit Reminder'
                    body = f"Don't forget to check off your habit {habit_name[self.habit_id]}! It just needs a little bit more effort 🤏🏿"
              
                    yag = yagmail.SMTP("phil92.mcg@gmail.com", "dsiiwhynrztcpdnd")
                    yag.send(to = self.email, subject = subject, contents = body)
                    yag.close()

                #Send congrets for streak
                deprint(check_weeks_streak(self.habit_id))
                if type(check_weeks_streak(self.habit_id)) == list:

                    subject = f"Habit Streak of {check_weeks_streak(self.habit_id)[0]} weeks🔥🚀 "
                    body = f"Congratulation you have reached a streak of {check_weeks_streak(self.habit_id)[0]} weeks in a row for your habit: {habit_name[self.habit_id]}\n You have received a reward: {check_weeks_streak(self.habit_id)[1]} \n Keep Going🚀"

                    yag = yagmail.SMTP("phil92.mcg@gmail.com", "dsiiwhynrztcpdnd")
                    yag.send(to = self.email, subject = subject, contents = body)
                    yag.close()


        print(f"Coach is successfully activated for your Habit : {habit_name[self.habit_id]} ✅")

        Coach.setup_cron_job(self.habit_id)


    def end_cron_job(habit_id: int):
        """
        This function ends the cron job for a given habit ID by deleting it from the cron tab file.

        It deletes the the writen line (when activated the crone job for an ID) from the cron tab.

        Args:
            habit_id (int): Used to delete the correct line in the cron tab.

        Return:
            None
        """
        cron = CronTab(user=True)  
        cron.remove_all(command=f"/usr/bin/python3 {__file__} {habit_id}") 
        cron.write() 
    

    def inactivate_id(self):
        """
        This function inactivates the cron job for a chosen habit ID.

        Checks if ID even exists!
        It first checks if the chosen habit is activated or not and displays a message respectively.
        If active it ends the cron job by calling the end_cron_job function.
        Then it also deletes the habit id from the activated_ids table from the database by calling the delete_habit_id function.

        Args:
            habit_id (int): Used to delete the correct line in the cron tab.

        Return:
            None
        """
        if check_if_ID_exists(self.habit_id) == -1:
            sys.exit("Your ID does not exist❌. To check your exsting IDs use -> python3 app.py show")

        habits = get_all_habits()
        habit_name = {habit.ID: habit.habit_name for habit in habits}


        deprint(activated_ids())
        if str(self.habit_id) in str(activated_ids()):

            Coach.end_cron_job(self.habit_id)

            delete_habit_id(self.habit_id)
            print(f"Your Coach is successfully inactivated for the Habit with ID: {self.habit_id} ✅") 

        else:
            print(f"You have no active Coach for your Habit with ID: {self.habit_id} ❌")







