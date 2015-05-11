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

for tr in detail_table.findAll('tr'):

    if tr.findAll('td')[0]['class'] == 'detailSeperator':

        print tr.next_sibling('tr').text


# second attempt

output = {}
counter = 0

for tr in detail_table.findAll('tr'):

    if tr.findAll('td')[0]['class'] == 'detailSeperator':
        
        counter += 1

        output[counter] = {'contents': []}
        continue

    tds = tr.findAll('td')

    for td in tds:
        if td['class'] == "detailData":
            if re.compile(r'\d{2}.\d{2}.\d{4}').search(td.text):

                output[counter]['date'] = datetime.strptime(td.text, '%m/%d/%Y').date()

            else:
                output[counter]['contents'].append(td.text)

        if output[counter]['date'] == curr_date:
            print output[counter]['contents']


    print '===================='

    sleep(3)


first attempt

    if len(tds) >= 2: #
        for td in tds:
            if td.b:
                if re.compile(r'\d{2}.\d{2}.\d{4}').search(td.text):
                    output[counter]['date'] = td.text
                else:
                    output[counter]['contents'].append(td.text)


    for j in tr.findAll('td', attrs ={'class': 'detailData'}):

    if tr.find('td')['class'] == 'detailSeperator':
        continue
    sleep(3)

    output_row = []
    table_row = tr.findAll('td')
    if len(table_row) > 1:
        for td in table_row:
            output_row.append(td.text)
        
        output.append(output_row)
        print output_row
        sleep(5)

for i in output.itervalues():
    print i