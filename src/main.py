from utils import open_chrome_with_profile, extract_content, connect_vpn, disconnect_vpn
import time
import pandas as pd
import os
import csv
import random

def main():
        connect_vpn()
        driver = open_chrome_with_profile()  # Open Chrome with profile
        driver.get("https://www.fastpeoplesearch.com/")  # Navigate to FastPeopleSearch.com
        # if access denied, wait for user to enable vpn (only for the first time)
        if "Access Denied" in driver.page_source:
            print("Access Denied")
            time.sleep(random.uniform(5,15))  # Wait for the user to enable vpn extension
            driver.get("https://www.fastpeoplesearch.com/")  # Navigate to FastPeopleSearch.com
            if "Access Denied" in driver.page_source:
                return 1
        
        filename = 'D:\DownLoad\projects\webscraping_freefasrpeoplesaerch\Webscraping_freefastpeoplesearch\output\\result_data.csv'
        header = ['Id','Address', 'Name', 'Phone']

        # Check if the file exists before writing the header
        if not os.path.exists(filename):
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()  # Write header only if file is newly created

        start = 1
        data = pd.read_csv("D:\\DownLoad\\projects\\webscraping_freefasrpeoplesaerch\\Webscraping_freefastpeoplesearch\\data\\Philly PA List.csv") # Open the Csv file
        result_data = pd.read_csv('D:\DownLoad\projects\webscraping_freefasrpeoplesaerch\Webscraping_freefastpeoplesearch\output\\result_data.csv')
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
                time.sleep(random.uniform(6,15))  # wait 6-10 seconds for the page to load

                if start:
                    print("CAPTCHA detected! Solve it manually...")
                    input("Press Enter after solving the CAPTCHA...")
                    start = 0

                # try to get all phones for this person as a list of strings
                print("Extracting Content of page")
                content = extract_content(Id,address,driver.page_source)
                if content:
                    if content['Name'] == "NOT FOUND":
                        print("Rebooting VPN...")
                        disconnect_vpn()
                        driver.quit()
                        connect_vpn()
                        time.sleep(random.uniform(60,120))
                        driver = open_chrome_with_profile()

                        driver.get("https://www.fastpeoplesearch.com/address/" + address + "_" + zip)
                        time.sleep(random.uniform(15,45)) #wait 6-10 seconds for the page to load
                        content = extract_content(Id, address,driver.page_source)
                    # Append the found value to the dataframe
                    result_data = pd.concat([result_data, pd.DataFrame([content])], ignore_index=True)
                else:
                    print(f"No Data Found {content}")

                result_data.to_csv('D:\DownLoad\projects\webscraping_freefasrpeoplesaerch\Webscraping_freefastpeoplesearch\output\\result_data.csv', index=False)
                # wait 1 second before searching for the next person
                time.sleep(random.uniform(15, 45))

            except Exception as e:
                print(str(e))
                continue
        
        result_data.to_csv('D:\DownLoad\projects\webscraping_freefasrpeoplesaerch\Webscraping_freefastpeoplesearch\output\\result_data.csv', index=False)
        disconnect_vpn()  # Disconnect from VPN after all searches are done
        driver.close()


if __name__ == "__main__":
    main()
