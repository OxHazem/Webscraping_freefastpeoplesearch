from config import FIRST_NAME_COL, LAST_NAME_COL, ADDRESS_COL
from utils import open_chrome_with_profile, open_xlsx_file, extract_phones_from_page, write_phones_to_xlsx_file
import time


def main():
    driver = open_chrome_with_profile()  # Open Chrome with profile
    driver.get("https://www.fastpeoplesearch.com/")  # Navigate to FastPeopleSearch.com
    # if access denied, wait for user to enable vpn (only for the first time)
    if "Access Denied" in driver.page_source:
        print("Access Denied")
        time.sleep(60)  # Wait for the user to enable vpn extension
        driver.get("https://www.fastpeoplesearch.com/")  # Navigate to FastPeopleSearch.com
        if "Access Denied" in driver.page_source:
            return 1
    
    start = 1
    wb, ws = open_xlsx_file()  # Open the Excel file
    # for each row in the Excel file search for the person and write the phones to the Excel file
    for row in range(2, ws.max_row + 1):
        # try searching for this person
        try:
            first_name = ws[FIRST_NAME_COL + str(row)].value
            last_name = ws[LAST_NAME_COL + str(row)].value
            address = ws[ADDRESS_COL + str(row)].value

            if (first_name is None and last_name is None) or address is None:
                continue

            # search for this person
            first_name = first_name.replace(" ", "-")
            last_name = last_name.replace(" ", "-")
            address = address.replace(" ", "-")
            driver.get("https://www.fastpeoplesearch.com/name/" + first_name + "-" + last_name + "_" + address)
            time.sleep(10)

            if start:
                print("CAPTCHA detected! Solve it manually...")
                input("Press Enter after solving the CAPTCHA...")
                start = 0

            # try to get all phones for this person as a list of strings
            phones = extract_phones_from_page(driver.page_source)
            if phones:
                # write phones to Excel file
                print("Found " + str(len(phones)) + " phones for " + first_name + " " + last_name)
                write_phones_to_xlsx_file(wb, ws, phones, row)
            else:
                print("No phones found for " + first_name + " " + last_name)

            # wait 1 second before searching for the next person
            time.sleep(1)

        except Exception as e:
            print(str(e))
            continue

    wb.close()
    driver.close()


if __name__ == "__main__":
    main()
