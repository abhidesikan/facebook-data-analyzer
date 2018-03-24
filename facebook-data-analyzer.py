#!/usr/bin/python
from bs4 import BeautifulSoup
import pandas as pd


def analyze_contact_info(soup):
    table = soup.find_all('table')[0]
    row_marker = 0
    total_contact_count = 0
    phone_contact_count = 0
    email_contact_count = 0
    new_table = pd.DataFrame(columns=range(0,2), index=[0])

    for row in table.find_all('tr'):
        column_marker = 0
        columns = row.find_all('td')
        for column in columns:
            for ele in column.find_all('span'):
                for li in ele.find_all('li'):
                    for child in li.children:
                        if(child.find("+") != -1):
                            phone_contact_count += 1
                        else:
                            email_contact_count += 1                       
            column_marker += 1
                
    print "Total contacts found (phone & email addresses): " + str(total_contact_count)
    print "Total phone contacts : " + str(phone_contact_count)
    print "Total email contacs : " + str(email_contact_count)

def main():
    contact_file = open('html/contact_info.htm')
    soup = BeautifulSoup(contact_file, 'lxml')
    analyze_contact_info(soup)

if __name__ == '__main__':
    main()

