import setuptools
import pkg_resources
import subprocess
import os
import shutil

from debug import deprint

def is_module_installed(module_name: str):
    """
    This function checks wether a python module is installed or not.

    It first calls from the pkg_resources library from setuptools the get_distribution function.
    If the module is found it return a message with the module version and return True.
    Else it returns false.
    .version checks the version of the module.

    Args:
         module_name (str): The module to be checked if installed or not.
    
    Return:
        Boolean: True -> module is already installed. False -> module is not installed.
    """
    try:
        dist = pkg_resources.get_distribution(module_name)
        print(f"{module_name} is already installed (version: {dist.version})")
        return True

    except pkg_resources.DistributionNotFound:
        print(f"{module_name} is not installed. Starting installation:")
        return False


def install_modules(module: str):
    """
    This function installs a python module.

    It first calls the is_module_installed function to check if already installed or not.
    It then uses the subprocess module and calls the call function to execute the pip3 install module_name command.

    Args:
        module (str): The module to install.

    Return:
        None
    
    """
    if is_module_installed(module) is False:

        subprocess.call(["pip3", "install", module])

"""
Installing all relevant packages for habit tracker app.
"""

install_modules("numpy")
install_modules("typer")
install_modules("rich")
install_modules("matplotlib")
install_modules("datetime")
install_modules("pandas")
install_modules("yagmail")
install_modules("python-crontab")




"""
Create a folder on Desktop and modify .bashrc
"""

def locate_folder():
    # Get the path of the location (https://docs.python.org/3/library/os.path.html)
    location = os.path.dirname(os.path.abspath(__file__))

    return location

deprint(locate_folder())



def relocate_habit_tracker_to_desktop():

    try:
        location = locate_folder()

        # Relocate a copy on the Desktop
        desktop = os.path.expanduser("~/Desktop")
        new_name = "Habit-Tracker"
        new_directory = os.path.join(desktop, new_name)
        #https://docs.python.org/3/library/shutil.html
        shutil.copytree(location, new_directory)
        print("Setting up new driectory")
    #if folder already on Desktop    
    except FileExistsError:
        print("You have already installed the Habit-Tracker on your Desktop✅")



def add_habit_tracker_to_bashrc():
    
    # Locate the current folder directory
    folder_dir = locate_folder()


    # all commands to run the app.py script (in alphabetical order)
    # activate-coach
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py activate-coach $@ "
    alias_command_activate_coach = "alias activate-coach='{}'".format(command)
    # add
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py add $@ "
    alias_command_add = "alias add='{}'".format(command)
    # average-rating-habits
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py average-rating-habits $@ "
    alias_command_average_rating_habits = "alias average-rating-habits='{}'".format(command)
    #check-off
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py check-off $@ "
    alias_command_check_off = "alias check-off='{}'".format(command)
    #delete
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py delete $@ "
    alias_command_delete = "alias delete='{}'".format(command)
    #easiest-habit
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py easiest-habit $@ "
    alias_command_easiest_habit = "alias easiest-habit='{}'".format(command)
    #habits-ratings
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py habits-ratings $@ "
    alias_command_habits_ratings = "alias habits-ratings='{}'".format(command)
    #hardest-habit
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py hardest-habit $@ "
    alias_command_hardest_habit = "alias hardest-habit='{}'".format(command)
    #inactivate-coach
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py inactivate-coach $@ "
    alias_command_inactivate_coach = "alias inactivate-coach='{}'".format(command)
    #longest-streak-id
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py longest-streak-id $@ "
    alias_command_longest_streak_id = "alias longest-streak-id='{}'".format(command)
    #longest-streaks
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py longest-streaks $@ "
    alias_command_longest_streaks = "alias longest-streaks='{}'".format(command)
    #show
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py show $@ "
    alias_command_show = "alias show='{}'".format(command)
    #show-progress
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py show-progress $@ "
    alias_command_show_progress = "alias show-progress='{}'".format(command)
    #timeline
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py timeline $@ "
    alias_command_timeline = "alias timeline='{}'".format(command)
    #uncheck-off
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py uncheck-off $@ "
    alias_command_uncheck_off = "alias uncheck-off='{}'".format(command)
    #update
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py update $@ "
    alias_command_update = "alias update='{}'".format(command)
    #update-periodicity
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py update-period $@ "
    alias_command_update_periodicity = "alias update-period='{}'".format(command)

    #extra --help for commands
    command = "cd ~/Desktop/Habit-Tracker && python3 app.py --help $@ "
    alias_command_help = "alias help='{}'".format(command)



    # Modify the user-specific bashrc file
    bashrc_path = os.path.expanduser("~/.bashrc")
    with open(bashrc_path, "a") as bashrc_file:
        bashrc_file.write("\n# Added by install.py for Habit-Tracker\n")
        #activate-coach command
        bashrc_file.write("{}\n".format(alias_command_activate_coach))
        #add
        bashrc_file.write("{}\n".format(alias_command_add))
        #average-rating-habits
        bashrc_file.write("{}\n".format(alias_command_average_rating_habits))
        #check-off
        bashrc_file.write("{}\n".format(alias_command_check_off))
        #delete
        bashrc_file.write("{}\n".format(alias_command_delete))
        #easiest-habit
        bashrc_file.write("{}\n".format(alias_command_easiest_habit))
        #habits-ratings
        bashrc_file.write("{}\n".format(alias_command_habits_ratings))
        #hardest-habit
        bashrc_file.write("{}\n".format(alias_command_hardest_habit))
        #inactivate-coach
        bashrc_file.write("{}\n".format(alias_command_inactivate_coach))
        #longest-streak-id
        bashrc_file.write("{}\n".format(alias_command_longest_streak_id))
        #longest-streaks
        bashrc_file.write("{}\n".format(alias_command_longest_streaks))
        #show
        bashrc_file.write("{}\n".format(alias_command_show))
        #show-progress
        bashrc_file.write("{}\n".format(alias_command_show_progress))
        #timeline
        bashrc_file.write("{}\n".format(alias_command_timeline))
        #uncheck-off
        bashrc_file.write("{}\n".format(alias_command_uncheck_off))
        #update
        bashrc_file.write("{}\n".format(alias_command_update))
        #update-periodicity
        bashrc_file.write("{}\n".format(alias_command_update_periodicity))

        #--help
        bashrc_file.write("{}\n".format(alias_command_help))        




relocate_habit_tracker_to_desktop()
add_habit_tracker_to_bashrc()

















