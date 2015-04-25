from BeautifulSoup import BeautifulSoup
import datetime
from time import sleep

#when doing actual scrape, could perform function that would use a variable in the URL that could 
#be populated by different case numbers

i = datetime.datetime.now()

html = open('caseylewisdocket.html', 'r').read()

soup = BeautifulSoup(html)
detail_table = soup.find('table', attrs={'class': 'detailRecordTable' })

output = []
for tr in detail_table.findAll('tr'):

    # print tr.find('td').attrs

    if tr.find('td')['class'] == 'detailSeperator':
        stuff = tr.findNextSibling('tr')
        for j in stuff.findAll('td', attrs ={'class': 'detailData'}):
            print j.text
    sleep(3)

    # output_row = []
    # table_row = tr.findAll('td')
    # if len(table_row) > 1:
    #     for td in table_row:
    #         output_row.append(td.text)
        
    #     output.append(output_row)
    #     print output_row
    #     sleep(5)

# print output