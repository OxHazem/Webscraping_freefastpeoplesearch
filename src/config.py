import os

chromedriver_path = "D:\DownLoad\chromedriver-win64\chromedriver-win64\chromedriver.exe" # Path to ChromeDriver executable

CURR_SCRIPT_PATH = os.path.realpath(os.path.dirname(__file__))
# CURR_SCRIPT_PATH = os.path.dirname(sys.executable)
profile_path = CURR_SCRIPT_PATH + "/profile"  # Path to Chrome profile (you can put the full path to existing profile or keep it to create new profile and use it later)
