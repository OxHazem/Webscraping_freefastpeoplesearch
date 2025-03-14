import undetected_chromedriver as uc
from config import profile_path, chromedriver_path
import pandas as pd 
import bs4
import csv
import subprocess


def open_chrome_with_profile():
    # Create a new Chrome session with the Chrome profile

    # options = Options()
    options = uc.ChromeOptions()
    options.add_argument("--user-data-dir=" + profile_path)

    # Create a new instance of the Chrome driver with the specified options
    # driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)
    driver = uc.Chrome(driver_executable_path=chromedriver_path, options=options)
    return driver


def open_Csv_file ():
    id_data=[]
    data=pd.read_csv('../data/Philly PA List.csv')
    df=pd.DataFrame(data)
    for index, row in df.iterrows():
        id_data.append({
            'Id': row['Id'],
            'Address': row['Address'],
            'Zip': row['Zip'],
        })
    return id_data


def save_to_csv(content):
    with open("../data/Cleaned_Data.csv", mode="w", newline="") as file:
        fieldnames = ["Id", "Address", "Zip"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  # Write column headers
        writer.writerows(content)  # Write data rows


def extract_content(Id, address, page_source):
    # Extract phones from the page source and return them as a list of strings
    # ID, New Name, New Phone

    try:
        # find phone number
        #returned_list=[]
        soup = bs4.BeautifulSoup(page_source, "html.parser")
        #Finding The Name
        print("Finding name")
        name = soup.find('h2', class_='card-title').find('span', class_='larger').text.strip()
        print("Finding Address")
        #Finding the Phone Number
        print("Finding Phone number")
        phone = soup.find('a', class_='nowrap').text.strip()

        #dont forget to return the list 
        return {
            'Id': Id,
            'Name': name,
            'Address' : address,
            'Phone': phone
        }
    except Exception as e:
        print(str(e))
        return {
            'Id': Id,
            "Name": "NOT FOUND",
            "Address" : "NOT Found",
            "Phone": "NOT FOUND",
        }

def connect_vpn():
    try:
        subprocess.run(['windscribe-cli', 'connect','US', 'stealth'], check=True)  # Connect to a US server
        print("✅ Connected to Windscribe (US Region)")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error connecting to VPN: {e}")
        exit(1)

# Function to disconnect from ProtonVPN
def disconnect_vpn():
    try:
        subprocess.run(['windscribe-cli', 'disconnect'], check=True)
        print("✅ Disconnected from Windscribe")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error disconnecting VPN: {e}")