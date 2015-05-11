from BeautifulSoup import BeautifulSoup
from datetime import datetime, date
from time import sleep
import re

#when doing actual scrape, could perform function that would use a variable in the URL that could 
#be populated by different case numbers

curr_date = date(2015, 4, 23) # datetime.now().date()

html = open('caseylewisdocket.html', 'r').read()

soup = BeautifulSoup(html)
detail_table = soup.find('table', attrs={'class': 'detailRecordTable' })

output = []

keep_going = True

for tr in detail_table.findAll('tr'):

    # print tr.find('td').attrs

    if tr.find('td')['class'] == 'detailSeperator':
        date_cell = tr.findNextSibling('tr').find('td', attrs = {'class': 'detailData'})
        date_string = date_cell.text
        action_date = datetime.strptime(date_string, '%m/%d/%Y').date()

        if action_date == curr_date:

            print date_string

            while keep_going:
                for row in date_cell.findParent('tr').findNextSiblings('tr'):
                    if 'class' in row:
                        if row['class'] == 'detailSeperator':
                            keep_going = False
                    else:
                        for td in row.findAll('td'):
                            if td['class'] == 'detailData':
                                print td.text
                                sleep(3)
            print '-----------' 
        
        # for sib in tr.findNextSiblings('tr'):

        #     # if 'class' in sib:
        #     #     if sib['class'] == 'detailSeperator':
        #     #         continue 
        #     else:
        #         for td in sib.findAll('td', attrs ={'class': 'detailData'}):
        #             print td.text.strip().replace('&nbsp;', '').replace('\n', '').replace('\t', '')
        #         print '======' 
        #     sleep(2)

        # for sib in tr.():
        #     print sib
        # stuff = tr.findNextSibling('tr')
        # for j in stuff.findAll('td', attrs ={'class': 'detailData'}):
        #     print j.text
    

    # output_row = []
    # table_row = tr.findAll('td')
    # if len(table_row) > 1:
    #     for td in table_row:
    #         output_row.append(td.text)
        
    #     output.append(output_row)
    #     print output_row
    #     sleep(5)

# print output