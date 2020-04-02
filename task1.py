from bs4 import BeautifulSoup
import requests
import pandas as pd

#Making a output dictionary that will be appended with the scraped data of each url and maintaning a count for the same. 

number = int(input("Enter the number of pages to be scraped: "))
output = {}
count = 0

while (number):

    url = input("Enter the URL: ")

    response = requests.get(url)
    data = response.text
    #Parsing the data to desired format for easy extraction of the same.
    soup = BeautifulSoup(data, 'lxml')

    #Targetting the div which contains the required information.
    info = soup.find_all('div', {'class':'md-padding archive-project-card__header archive-project-card__header--mod-0'})

    for student in info:
        
        #Removing the '\n' so that the data looks nicer and for easy handling of the same.

        name = (student.find('h4').text).replace('\n', '')
        #Taking into account the two divs present in the parent div tag.
        project = student.find_all('div')[0].text
        organisation = student.find_all('div')[1].text
        output[count] = [name, organisation, project]
        count += 1

    number -= 1
    
    
#Creating the dataframe using pandas to store the output in desired format.
dataframe = pd.DataFrame.from_dict(output, orient = 'index', columns = ['Name', 'Organisation', 'Project'])

output_file = input("Enter the name of output csv file: ")
#Converting the dataframe created to csv file.
dataframe.to_csv(output_file)

