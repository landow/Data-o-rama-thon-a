# This variable represents the data from the nycdonors-cleanme.csv file as a
# list, with each item representing a string for each row. 
data = open('nycdonors-cleanme.csv', 'r').read().split('\r\n')[1:]

# You'll add your output data here, using the .append() method
output = []

# Hint: Start by looping over the data variable, turn each item into a list,
# and perform the necessary transformations. Once the row has been transformed,
# append it into the output list, like this: output.append(cleaned_row)

########## YOUR CODE GOES HERE ##########
for row in data:
	row_list = row.split(',')
	
	row_list[11] = row_list[11].upper()
	row_list[15] = row_list[15].replace('&nbsp;', ' ')
	row_list[-1] = float(row_list[-1])
	row_list[-4] = str(row_list[-4])
	if row_list[-1] > 5000.0:
	    print row_list
	if row_list[-5] != 'NY':
		print row_list

output = []
output.append(row_list)

