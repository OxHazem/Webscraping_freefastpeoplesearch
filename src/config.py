import os

chromedriver_path = "D:\DownLoad\chromewww\chromedriver-win64\chromedriver-win64\chromedriver.exe" # Path to ChromeDriver executable
csv_file = "D:\DownLoad\projects\webscraping_freefasrpeoplesaerch\Webscraping_freefastpeoplesearch\data\Philly PA List.csv"  # Path to Excel file with names and addresses

CURR_SCRIPT_PATH = os.path.realpath(os.path.dirname(__file__))
# CURR_SCRIPT_PATH = os.path.dirname(sys.executable)
profile_path = CURR_SCRIPT_PATH + "/profile"  # Path to Chrome profile (you can put the full path to existing profile or keep it to create new profile and use it later)

