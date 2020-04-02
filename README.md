# pclub_secy_selection
This is a repository created as part of the task for the selection process.
This is a repository aimed at scraping a webpage to get some required information. This also contains a program to compare two files one csv and one json and then output the required items based on some queries.

Scraping is basically used to extract the information contained in the webpage in case there is no API available for the same. Python is commonly used for web-scraping although it can be done by other languages as well. Parsing is done using Beautiful Soup to the required format. 

How to run the program:

For task1.py:

Save the code in some directory in your machine. Be sure that all the libraries/packages are installed in your computer otherwise install them using pip3 install. Then on running the python program, first you will get a prompt to enter the number of urls you want to scrap. Then after entering the number you will be given the same number of prompts to enter the urls of the pages you wnat to scrap. Finally you will be prompted to give the name of the output file where you can give the name you want with a .csv extension.

For task2.py:

Save the code in the some directory. Be sure that all the packages/libraries required are installed in the computer. Now you will be prompted to enter the path of your two files. You can give either the relative or absolute path, both will work fine. After giving the files to be compared the program prints the unaccepted names first and then the details of the people who were matched.
