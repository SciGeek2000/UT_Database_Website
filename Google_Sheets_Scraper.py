#This program requires a credentials-sheets.json file to function properly. Obtain one on the google API website. 
import ezsheets
import pandas as pd

#Gets spreadsheet from page id (found in url)
ss = ezsheets.Spreadsheet('1KjXGhOFzi0SZPsozpKzxGjVtfr4kkS_Hv5EigUwKOj8')

#Downloads data first as a Excel sheet (only way to preserve all of the sheets)
ss.downloadAsExcel('Google_Sheets_to_Excel.xlsx');

#Converts each relavent sheet of the Excel workbook into a .csv file
pd.read_excel('Google_Sheets_to_Excel.xlsx', sheet_name=ss[1].title).to_csv('CSV_Backplane.csv', index=False)
pd.read_excel('Google_Sheets_to_Excel.xlsx', sheet_name=ss[2].title).to_csv('CSV_DCB.csv', index=False)
pd.read_excel('Google_Sheets_to_Excel.xlsx', sheet_name=ss[3].title).to_csv('CSV_LVR.csv', index=False)
pd.read_excel('Google_Sheets_to_Excel.xlsx', sheet_name=ss[5].title).to_csv('CSV_CCM.csv', index=False)
