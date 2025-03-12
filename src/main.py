from utils import open_chrome_with_profile, extract_content
import time
import pandas as pd
import os
import csv
import random

def main():
    driver = open_chrome_with_profile()  # Open Chrome with profile
    driver.get("https://www.fastpeoplesearch.com/")  # Navigate to FastPeopleSearch.com
    # if access denied, wait for user to enable vpn (only for the first time)
    if "Access Denied" in driver.page_source:
        print("Access Denied")
        time.sleep(random.uniform(5,15))  # Wait for the user to enable vpn extension
        driver.get("https://www.fastpeoplesearch.com/")  # Navigate to FastPeopleSearch.com
        if "Access Denied" in driver.page_source:
            return 1
    
    filename = '../output/result_data.csv'
    header = ['Id','Address', 'Name', 'Phone']

    # Check if the file exists before writing the header
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()  # Write header only if file is newly created

    start = 1
    data = pd.read_csv('../data/Philly PA List.csv') # Open the Csv file
    result_data = pd.read_csv('../output/result_data.csv')
    # for each row in the Excel file search for the person and write the phones to the Excel file
    for index, row in data.iterrows():
        # try searching for this person
        try:
            Id = row['Id']
            zip = row['Zip']
            address = row['Address']

            if (zip is None or address is None) or (result_data['Id'] == Id).any():
                print(f"Skipping {Id}")
                continue

            # search for this person
            zip = str(zip).replace(" ", "-")
            address = str(address).replace(" ", "-")
            driver.get("https://www.fastpeoplesearch.com/address/" + address + "_" + zip)
            time.sleep(random.uniform(6,10))  # wait 6-10 seconds for the page to load

            if start:
                print("CAPTCHA detected! Solve it manually...")
                input("Press Enter after solving the CAPTCHA...")
                start = 0

            # try to get all phones for this person as a list of strings
            print("Extracting Content of page")
            content = extract_content(Id, driver.page_source)
            if content:
                # write phones to Excel file
                print(f"Data Found {content}")
                # Append the found value to the dataframe
                result_data = pd.concat([result_data, pd.DataFrame([content])], ignore_index=True)
            else:
                print(f"No Data Found {content}")

            result_data.to_csv('../output/result_data.csv', index=False)
            # wait 1 second before searching for the next person
            time.sleep(random.uniform(1, 8))

        except Exception as e:
            print(str(e))
            continue
    
    result_data.to_csv('../output/result_data.csv', index=False)
    driver.close()


if __name__ == "__main__":
    main()
