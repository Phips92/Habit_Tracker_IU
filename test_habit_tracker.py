import unittest
from unittest.mock import patch, MagicMock
from app import *
from database import update_periodicity, get_all_habits
from model import Habit

class AppTests(unittest.TestCase):


    # mocks the insert_habit function -> the instertion into the databse is actually not performed
    @patch("app.insert_habit")
    def test_add(self, mock_insert_habit):
        """Test add() function"""

        habit_name = "Exercise"
        description = "Daily workout routine"
        add(habit_name, description)
        mock_insert_habit.assert_called_once()



    @patch("app.delete_habit")
    def test_delete(self, mock_delete_habit):
        """Test delete() function"""

        habit_id = 1
        delete(habit_id) 
        mock_delete_habit.assert_called_once_with(habit_id)



    @patch("app.update_habit")
    def test_update(self, mock_update_habit):
        """Test update() function"""

        habit_id = 1
        habit_name = "Update Exercise"
        description = "Update Daily workout routine"
        update(habit_id, habit_name, description)
        mock_update_habit.assert_called_once()



    @patch("app.update_periodicity")
    def test_update_period(self, mock_update_periodicity):
        """Test update_period() function"""

        habit_id = 1
        period = "weekly"
        update_period(habit_id, period)
        mock_update_periodicity.assert_called_once_with(habit_id, period)


    @patch("database.cursor")
    def test_get_all_habits(self, mock_cursor):
        """Test get_all_habits() function"""

        mock_results = [
            ("Exercise", "Daily workout routine", "2023-07-09", 0, 1, "daily"),
            ("Reading", "Read a book", "2023-07-10", 0, 2, "daily"),
        ]
        mock_cursor.fetchall.return_value = mock_results
    
        habits = get_all_habits()

        mock_cursor.execute.assert_called_once_with("SELECT habit_name, description, date_added, progress, ID, periodicity FROM habits")

        expected_habits = [
            f"Habit{str(mock_results[0])}",
            f"Habit{str(mock_results[1])}",
        ]
        actual_habits = [str(habit) for habit in habits]
        self.assertEqual(actual_habits, expected_habits)


    @patch("app.check_off_habit")
    def test_check_off(self, mock_check_off_habit):
        """Test check_off() function"""
        habit_id = 1
        rating = 4
        check_off(habit_id, rating)
        mock_check_off_habit.assert_called_once_with(habit_id, rating)



    @patch("app.check_if_ID_exists")
    @patch("app.undo_check_off_habit")
    def test_uncheck_off(self, mock_undo_check_off_habit, mock_check_if_ID_exists):
        """Test uncheck_off() function"""
        habit_id = 1
        mock_check_if_ID_exists.return_value = habit_id

        uncheck_off(habit_id)

        mock_check_if_ID_exists.assert_called_once_with(habit_id)
        mock_undo_check_off_habit.assert_called_once_with(habit_id)



    @patch("app.calculate_longest_streak_for_id")
    def test_longest_streak_ID(self, mock_calculate_longest_streak_for_id):
        """Test longest_streak_ID() function"""

        mock_calculate_longest_streak_for_id.return_value = 5

        with patch("typer.echo") as mock_echo:
            longest_streak_ID(1)

            mock_echo.assert_called_once_with("Longest streak for ID 1 is calculated with:")

        mock_calculate_longest_streak_for_id.assert_called_once_with(1)



    @patch("app.plot_longest_streaks")
    def test_longest_streaks(self, mock_plot_longest_streaks):
        """Test longest_streaks() function"""

        longest_streaks()

        mock_plot_longest_streaks.assert_called_once()



    @patch("app.plot_habits_by_ratings")
    def test_habits_ratings(self, mock_plot_habits_by_ratings):
        """Test habits_ratings() function"""

        habits_ratings()

        mock_plot_habits_by_ratings.assert_called_once()



    @patch("app.plot_average_difficulty_of_habits")
    def test_average_rating_habits(self, mock_plot_average_difficulty_of_habits):
        """Test average_rating_habits() function"""


        average_rating_habits()

        mock_plot_average_difficulty_of_habits.assert_called_once()


    @patch("app.get_easiest_habit")
    def test_easiest_habit(self, mock_get_easiest_habit):
        """Test easiest_habit() function"""

        easiest_habit()

        mock_get_easiest_habit.assert_called_once()



    @patch("app.get_hardest_habit")
    def test_hardest_habit(self, mock_get_hardest_habit):
        """Test hardest_habit() function"""

        hardest_habit()

        mock_get_hardest_habit.assert_called_once()



    @patch("app.get_timeline_of_habit")
    def test_timeline(self, mock_get_timeline_of_habit):
        habit_id = 1

        timeline(habit_id)

        mock_get_timeline_of_habit.assert_called_once_with(habit_id)



    @patch("app.Coach")
    def test_activate_coach(self, mock_coach):
        """Test activate_coach() function"""

        email = "test@example.com"
        habit_id = 1

        activate_coach(email, habit_id)

        mock_coach.assert_called_once_with(email, habit_id)

        mock_coach.return_value.send_reminder.assert_called_once()



    @patch("app.Coach")
    def test_inactivate_coach(self, mock_coach):
        """Test inactivate_coach() function"""

        email = "test@example.com"
        habit_id = 1

        inactivate_coach(email, habit_id)

        mock_coach.assert_called_once_with(email, habit_id)

        mock_coach.return_value.inactivate_id.assert_called_once()


if __name__ == '__main__':
    unittest.main()

