# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
# Edwin Kintu-Lubowa,11/16/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str = ""    # Hold the choice made by the user.
students: list = []      # a table of student data

# Removed all prior programs variable's; I'll be using the above listed variables for
# Assignment06
# # Define the Data Variables and constants
# student_first_name: str = ''   # Holds the first name of a student entered by the user.
# student_last_name: str = ''    # Holds the last name of a student entered by the user.
# course_name: str = ''          # Holds the name of a course entered by the user.
# student_data: dict = {}        # one row of student data
# students: list = []            # a table of student data
# csv_data: str = ''             # Holds combined string data separated by a comma.
# json_data: str = ''            # Holds combined string data in a json format.
# file = None                    # Holds a reference to an opened file.
# menu_choice: str               # Hold the choice made by the user.

# Processing----------------------------------------------------------------------------------#
class FileProcessor:
    """
    A Collection of Processing Layer Functions that work with JSON Files

    ChangeLog: (Who, When, What)
    Edwin Kintu-Lubowa,11/16/2024,Created Class
    Edwin Kintu-Lubowa,11/16/2024,Added Function to read data from file
    Edwin Kintu-Lubowa,11/16/2024,Added Function to write data to file
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This Function that extracts data using JSON module from a JSON file

        ChangeLog: (Who, When, What)
        Edwin Kintu-Lubowa,11/16/2024,Created Function
        :param file_name:
        :param student_list:
        :return:
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Please check that the file exists and that it is in a json format.", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!.", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This Function writes data to a JSON module

        ChangeLog: (Who, When, What)
        Edwin Kintu-Lubowa,11/16/2024,Created Function
        :param file_name:
        :param student_list:
        :return:
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except FileNotFoundError as e:
            IO.output_error_messages("Please check that the file exists!", e)
        except TypeError as e:
            IO.output_error_messages("There was a problem with writing to the file.", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


# Presentation-------------------------------------------------------------------------------#
class IO:
    """
    A Collection of Presentation Layer Functions that manage user input and output

    ChangeLog: (Who, When, What)
    Edwin Kintu-Lubowa,11/17/2024,Created Class
    Edwin Kintu-Lubowa,11/17/2024,Added menu output and input Functions
    Edwin Kintu-Lubowa,11/17/2024,Added a Function to display the data
    Edwin Kintu-Lubowa,11/17/2024,Added a Function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This Function displays custom error messages to the user

        ChangeLog: (Who, When, What)
        Edwin Kintu-Lubowa, 11/16/2024,Created Function
        :param message:
        :param error:
        :return:
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep="\n")

    @staticmethod
    def output_menu(menu: str):
        """
        This Function displays the Menu of Options to the user

        ChangeLog: (Who, When, What)
        Edwin Kintu-Lubowa,11/16/2024,Created Function
        :param menu:
        :return:
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """
        This Function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Edwin K<intu-Lubowa,11/16/2024,Created Function
        :return:
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays current student data

        ChangeLog: (Who, When, What)
        Edwin Kintu-Lubowa,11/16/2024,Created Function
        :param student_data:
        :return:None
        """
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This Function gets the first name, last name ,and Course name from the user

        ChangeLog: (Who, When, What)
        Edwin Kintu-Lubowa,11/16/2024,Created Function
        :param student_data:
        :return:
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!\n", e)
        return student_data

# End of function definitions


# Beginning of the main body of this script

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
# Exiting program gracefully
input("\nPausing until you use Enter key...")
