# Habit Tracker

The Habit Tracker is a command-line application that helps users track and analyze their daily and weekly habits. It provides features for adding habits, checking off completed habits, visualizing habit streaks, and receiving reminder emails from a virtual coach.


## Table of Contents

- [Installation](#installation)
- [Usage examples](#usage)
- [Features](#features)
- [Modules](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)
- [Contact Information](#contact-information)


## Installation

To use the Habit Tracker application, follow these steps:

1. Run `python3 install_app.py` to install the required dependencies and set up the application on your system.
2. Update the database configurations in the `database.py` module to match your database setup. (To install a datatbase if you dont have any follow the install_database.pdf instruction)
3. After installing use the terminal to execute the commands. You can check all available commands with the "help" command.
4. Use the available commands to add habits, check off completed habits, and analyze habit data.


## Usage examples

Here are some usage examples for the Habit Tracker application:

- Add a new habit:

$ add "Sport" "20 sit-ups every day"

- Check off a completed habit with his ID (ID = 1 for example):

$ check-off 1

- View the habit streaks:

$ longest-streaks

- Activate the virtual coach for a habit by its ID (ID = 1 for example):

$ activate-coach 1 "some@example.com"

- Deactivate the virtual coach for a habit by its ID:

$ inactivate-coach 1

- For more available commands and options, refer to the help:

$ help


## Features

- Add new habits with descriptions.
- Check off completed habits.
- Track streaks for each habit.
- Receive reminder emails for unchecked habits.
- View habit statistics and progress.


## Modules

### app.py

This module contains the main application logic. It defines command-line commands using the `typer` library for adding habits and interacting with the Habit Tracker.

### database.py

The `database.py` module handles the interaction with the underlying database. It provides functions for creating a database connection, inserting and retrieving habit data, and performing data analysis queries.

### Coach.py

The `Coach.py` module implements the virtual coach functionality. It defines the `Coach` class, which handles sending reminder or motivating emails and activating/deactivating the coach for specific habits.

### module.py

The `module.py` module contains the `Habit` class, which represents a single habit in the Habit Tracker. It provides methods for setting habit attributes, checking off habits, and calculating streaks.

### Analyse.py

The `Analyse.py` module includes functions for analyzing habit data and generating visualizations. It utilizes the `matplotlib` and `pandas` libraries to plot habit streaks, ratings, average difficulty, etc.

### install_app.py

The `install_app.py` module is used to install the required dependencies and set up the Habit Tracker on your system. It checks for the presence of required modules, installs them if necessary, creates a copy of the application on your desktop, and adds aliases to the `bashrc` file for convenient command usage.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please submit them. How ?


## License

This project is licensed under the GNU General Public License v3.0


## Credits

I would like to acknowledge [ Patrick Loeber ] for their video on [Create a Task Tracker App for the Terminal with Python (Rich, Typer, Sqlite3)], which served as a valuable reference for this project. Their explanation of the habit tracker schema and use of certain tools greatly influenced the development of this project.

You can find the video that inspired this work [here](https://www.youtube.com/watch?v=ynd67UwG_cI).

- The Habit Tracker application uses the following external libraries:
- numpy
- typer
- rich
- matplotlib
- datetime
- pandas
- yagmail
- python-crontab


## Contact Information

For any questions or inquiries, please contact [philipp92.mcguire@gmail.com](mailto:philipp92.mcguire@gmail.com).



