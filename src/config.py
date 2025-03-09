import os

chromedriver_path = "/usr/local/bin/chromedriver" # Path to ChromeDriver executable
xlsx_path = "data.xlsx"  # Path to Excel file with names and addresses

CURR_SCRIPT_PATH = os.path.realpath(os.path.dirname(__file__))
# CURR_SCRIPT_PATH = os.path.dirname(sys.executable)
profile_path = CURR_SCRIPT_PATH + "/profile"  # Path to Chrome profile (you can put the full path to existing profile or keep it to create new profile and use it later)

FIRST_NAME_COL = 'A'  # (input)
LAST_NAME_COL = 'B'  # (input)
ADDRESS_COL = 'K'  # (input)
PHONEs_COLs = ['L', 'M', 'N', 'O', 'P']  # columns to output phone numbers  # (output)
