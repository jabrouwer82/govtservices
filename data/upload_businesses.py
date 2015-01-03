import csv
import requests
import os
import sys
import getopt

# Usage: python upload_businesses.py [(-i | --inputFile=)<Location of business csv>]
#                                    [(-o | --outputFile=)<Location of output file>]
#                                    [(-u | --url=)<URL to upload data to>]
# Example: python upload_business.py -i ~/Downloads/Services.csv
# Assumes the csv file has only a row of column names and then rows of real data.

# CMD options
opts_short = 'i:o:u:'
opts_long = ['inputFile=', 'outputFile=', 'url=']
opts = getopt.getopt(sys.argv[1:], opts_short, opts_long)
inputFile = './Services.csv'
outputFile = './failures.txt'
url = 'http://government-services.appspot.com/api/business'
for opt, arg in opts[0]:
    if opt in ('-i', '--inputFile'):
        inputFile = arg
    if opt in ('-o', '--outputFile'):
        outputFile = arg
    if opt in ('-u', '--url'):
        url = arg

failure_count = 0
success_count = 0
output = open(os.path.abspath(outputFile), 'w')
business_file = open(os.path.abspath(inputFile))
csv_reader = csv.DictReader(business_file)

for row in csv_reader:
    name = row['Service Name']
    description = row['Description of Service']
    physical_address = row['Physical Site Address 1'] + '\n' + row['Physical Site Address 2'] + '\n' + row['Physical Site City'] + ' ' + row['Physical Site State'] + ', ' + row['Physical Site Zip']
    mailing_address = row['Mailing Address 1'] + '\n' + row['Mailing Address 2'] + '\n' + row['Mailing City'] + ' ' + row['Mailing State'] + ', ' + row['Mailing Zip']
    phone_number = row['Main Phone']
    service_url = row['Web Address']
    # Taxonomies need to be searchable in the datastore, so they must be string properties and must be limited to 500 characters. I'm too lazy to do this properly and split it into multiple taxonomies for ones that are too long.
    taxonomy = row['Taxonomy Names'][:500]
    row_data = {'name': name,
                'description': description,
                'physical_address': physical_address,
                'mailing_address': mailing_address,
                'phone_number': phone_number,
                'url': service_url,
                'taxonomy': taxonomy,
                'z': 1}
    r = requests.post(url, row_data)
    if not r.ok:
        output.write(str(r.status_code))
        output.write(' - ')
        output.write(str(r.reason))
        output.write(' - ')
        output.write(str(row_data))
        output.write('\n')
        failure_count += 1
    else:
        success_count += 1
    
print success_count, 'rows uploaded to datastore.'
print failure_count, 'rows failed to upload. See', outputFile, 'for more details.'
   
