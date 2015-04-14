import urllib2, csv
from BeautifulSoup import BeautifulSoup

# Part 1

html = urllib2.urlopen('http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchResults.aspx?last=%25&first=&year=2015&agency=200').read()

#Part 2

soup = BeautifulSoup(html)
results_table = soup.find('table', attrs={'id': 'grdEmployees'})

#Part 3

output = []

for tr in results_table.findAll('tr'):

    output_row = []
    
    for td in tr.findAll('td'):
        data = td.text.replace('&nbsp;', '')
        output_row.append(data)

    output.append(output_row)
