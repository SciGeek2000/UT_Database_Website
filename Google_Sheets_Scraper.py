import ezsheets
import pandas as pd
ss = ezsheets.Spreadsheet('1KjXGhOFzi0SZPsozpKzxGjVtfr4kkS_Hv5EigUwKOj8')
ss.downloadAsExcel('Google_Sheets_to_Excel.xlsx');
pd.read_excel('Google_Sheets_to_Excel.xlsx', sheet_name=ss[1].title).to_csv('CSV_Backplane.csv', index=False)
pd.read_excel('Google_Sheets_to_Excel.xlsx', sheet_name=ss[2].title).to_csv('CSV_DCB.csv', index=False)
pd.read_excel('Google_Sheets_to_Excel.xlsx', sheet_name=ss[3].title).to_csv('CSV_LVR.csv', index=False)
pd.read_excel('Google_Sheets_to_Excel.xlsx', sheet_name=ss[5].title).to_csv('CSV_CCM.csv', index=False)