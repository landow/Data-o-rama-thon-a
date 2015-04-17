from BeautifulSoup import BeautifulSoup

# We're going to grab the HTML from a local file rather than the Internet, just so we don't irritate
# the Ethics Commission with a bunch of requests.
html = open('page.html', 'r').read()

soup = BeautifulSoup(html)
results_table = soup.find('table', attrs={'id': 'ctl00_ContentPlaceHolder_grvMain'})

# Again, this is where our output will live
output = []

for tr in results_table.findAll('tr'):
    
    output_row = []

    for span in tr.findAll('span'):
        data = span.text.replace('&nbsp;', '')
        output_row.append(data)
        if 'St. Louis, City Of' in output_row:
            output.append(output_row)

print output


# Your scraper should do several things:

# 1. First, grab all the lobbyist expenditures from the table
# 2. Skip, or ignore, the column that says "View"
# 3. If the transaction is for an official in Columbia, add it to the output list
# 4. Remove the &nbsp; string from all output where it appears
# 5. At the end, print the output list

########## YOUR CODE GOES HERE ##########