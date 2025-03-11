import pandas as pd
data=pd.read_csv('D:\DownLoad\projects\webscraping_freefasrpeoplesaerch\Webscraping_freefastpeoplesearch\data\Philly PA List.csv')
data.head()
df=pd.DataFrame(data)
print(df.duplicated())