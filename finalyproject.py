from BeautifulSoup import BeautifulSoup
from datetime import datetime, date
from time import sleep
import re
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os


curr_date = date(2015, 2, 25) # datetime.now().date()

html = open('caseylewisdocket.html', 'r').read()

soup = BeautifulSoup(html)
detail_table = soup.find('table', attrs={'class': 'detailRecordTable' })

# divide the html up using the detailSeperator tag, which is the tag that comes before each new entry

chunks = re.split("<td class=\"detailSeperator\" colspan=\"3\">", str(detail_table))

for chunk in chunks[1:]:

    chunk = BeautifulSoup(chunk) 
        
    if chunk.find('b').text != '':

        date_string = chunk.find('b').text
        action_date = datetime.strptime(date_string, '%m/%d/%Y').date()  
        
        if action_date == curr_date:
            # divide the html again so that it will recognize separate records within each new date's docket information
            seperator = re.split("<td class=\"detailThinSeperator\"", str(chunk))
            i = chunk.text.replace('&nbsp;', ' ')
            

            for thing in seperator:

                thing = BeautifulSoup(thing)

                i = thing.text.replace('&nbsp;', ' ').replace('&#039;', "'").replace("colspan=\"3\" style=\"font-weight: bold; background: #f5f5c0\">", " ")

                with open('chunk-basic.txt', 'a') as textfile:
                    textfile.write(i + "\n")
                    textfile.write('----------------------------------------' + "\n")

                print i
                
                print '--------------------'

# send an email with the above in an attachment
            
gmail_user = 'landonwoodroof@gmail.com'
gmail_pwd = '******'

def mail(to, subject, text, attach):
    msg = MIMEMultipart()

    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())

    mailServer.close()

mail("lewkk3@mail.missouri.edu", "A docket you are interested in has just been updated", "See the attached file to read the update to your docket", "chunk-basic.txt")


# output = []

# keep_going = True

# for tr in detail_table.findAll('tr'):

#     # print tr.find('td').attrs

#     if tr.find('td')['class'] == 'detailSeperator':
#         date_cell = tr.findNextSibling('tr').find('td', attrs = {'class': 'detailData'})
#         date_string = date_cell.text
#         action_date = datetime.strptime(date_string, '%m/%d/%Y').date()

#         if action_date == curr_date:

#             print date_string

#             while keep_going:
#                 for row in date_cell.findParent('tr').findNextSiblings('tr'):
#                     for tr in row.findAll('tr'):
#                         if tr['class'] == 'detailData':

#                                 print tr.text
                                
#                     for td in row.findAll('td'):
#                         if td['class'] == 'detailData':
                        
                            
                            
#                                 print td.text
                        
#                     else:
#                         if td['class'] == 'detailSeperator':
#                             break
                        
                                
#             print '-----------' 



        
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