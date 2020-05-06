#############################
LCHb DATABASE DISPLAY WEBISTE
#############################

This repository contains three distinct section:
1.) Google Sheets Scraper
2.) Python Parsing Script
3.) Hosted html pages

**************************************************************************
SECTION 1: GOOGLE SHEETS SCRAPER (Google_Sheets_Scraper.exe)

The google sheets scraper is a very short but powerful program that converts the data from the online google sheets database into four csv files: CSV_Backplane, CSV_CCM, CSV_DCB, and CSV_LVR. These four files have had no processing done to them and are simply saved in the local directory. This script was unable to be transformed into a .exe file so is only available as a .py file.

**************************************************************************
SECTION 2: PYTHON PARSING SCRIPT (Database_Parser.exe)

This python script takes the four .csv files outputted from section 1 and performs a number of operations on them to process the data. This data is then formatted into pyplots internally and these pyplots are saved in the local directory. Text files that contain data with anamolous flags are also saved to the directory. More information regarding the specifics of this process can be found within the file itself. This script can be found in both a .exe form and a .py form. NOTE: The .exe form takes significantly longer to run that a real-time complile of the .py form because of the size of the pyplot module.

**************************************************************************
Section 3: HOSTED HTML PAGES

This set of six webpages (Backplanes, CCMs, CONTACT, DCBs, LVRs, and index) together make the github hosted website. These pages display both the pyplots (as .png files) and the text files that section 2 outputs. The github hosting of this page is limited in traffic rates and commit rates. If the commit rate is exceeded, the hosted website will only show the last commit that the website registered. However, given enough time (>1 hour), the website will update to the latest commit.

**************************************************************************
PERPOSED METHOD OF OPERATION:

A microprocessor, such as a rasberry pi, would first be loaded with all of the files listed above. A small terminal script would then be run that is executed twice(?) a day. This script first runs the google scraper(1). After this is done, the script runs the .exe database paraser on the newly created .csv files(2). The updated pyplots and .txt files are then pushed to the github website and commited so that the hosted .html files can display the updated information(3).


CREDITS: Thomas Ersevim, Raymond Su, Claudio Pineda

~FIN~