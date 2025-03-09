#for the fuctions of the webscrapping 
# import undetected_chromedriver as uc
# from openpyxl import load_workbook
# from config import profile_path, chromedriver_path,csv_file
# import bs4
import pandas as pd 


# def open_chrome_with_profile():
#     # Create a new Chrome session with the Chrome profile

#     # options = Options()
#     options = uc.ChromeOptions()
#     options.add_argument("--user-data-dir=" + profile_path)

#     # Create a new instance of the Chrome driver with the specified options
#     # driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)
#     driver = uc.Chrome(driver_executable_path=chromedriver_path, options=options)
#     return driver


def open_Csv_file ():
    id_data={}
    data=pd.read_csv('D:\DownLoad\projects\webscraping_freefasrpeoplesaerch\Webscraping_freefastpeoplesearch\data\Philly PA List.csv')
    df=pd.DataFrame(data)
    for i in df['Id'].unique():
        id_data[i]={
            'Address' : df[]['Address'],
            'Zip' : df[i]['Zip'],

        }
    print(len(id_data),len(df['Id'].unique()))
    return id_data
dict_data= {}
dict_data=open_Csv_file()
print(dict_data)




  




