import csv
import re

# input and output file variables.
inputFile = 'drugs.csv'
outputFile = 'drugsUID.csv'
ACRONYM = 'PDBC'

# try catch block for reading and writing to the file.
try:
    # opening the file.
    with open(inputFile, 'r', encoding='utf-8') as input:
        with open(outputFile, 'w', encoding='utf-8') as output:
            csv_writer = csv.writer(output, delimiter=',')
            # header for the output file.
            csv_writer.writerow(['drug_id', 'drug_name', 'drug_uid',
                                 'fda_status', 'created_at', 'updated_at'])
            # looping through each line in the file
            # and appending the result to new file.
            for line in input:
                line = line.split(';')
                if line[0] != 'drug_id':
                    uid = format(int(line[0]), '05d')
                    drug_uid = ACRONYM + uid
                    last = line[4].replace('\n', '')
                    csv_writer.writerow(
                        [line[0], line[1], drug_uid, line[2], line[3], last])
except:
    print('Something went wrong!!')
