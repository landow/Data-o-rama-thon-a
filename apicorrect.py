import urllib2, json

# Replace this with your own
API_KEY = '3b069134ea8a41f3b2bc0b570ec0d7bb'


########## YOUR CODE GOES HERE ##########


def get_bills(state, type):
    '''
    This function should accomplish the following tasks:
      - Open a connection to the /bills/ endpoing of Sunlight Foundation's OpenStates API:
        http://sunlightlabs.github.io/openstates-api/bills.html#methods/bill-search
      - Retrieve an API response with bills from the current legislative session in Missouri
      - print the titles of bills that contain "Transportation" in the "subjects" list
    '''

    response = urllib2.urlopen('http://openstates.org/api/v1/bills/?search_window=session&state=%s&subject=%s&apikey=%s' % (state, type, API_KEY))
    json_object = json.load(response)
    
    for bill in json_object:
        print bill['title']

    return

########## RUN FUNCTIONS HERE ##########
# Uncomment this to run your function with the appropriate arguments, as specified above

get_bills('mo', 'Transportation')

