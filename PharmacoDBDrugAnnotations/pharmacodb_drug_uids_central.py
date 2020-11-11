"""
This file is used to create the UIDs for compounds that are present in the central file.
"""
import csv

# input and output file variables.
inputFile = 'drugs_with_ids.csv'
outputFile = 'drugsUIDCentral.csv'
ACRONYM = 'PDBC'

# try catch block for reading and writing to the file.
try:
    # opening the file.
    with open(inputFile, 'r', encoding='utf-8') as input:
        with open(outputFile, 'w', encoding='utf-8') as output:
            csv_writer = csv.writer(output)
            first_line = True
            i = 1
            # looping through each line in the file
            # and appending the result to new file.
            for line in input:
                if first_line:
                    line = line.replace('\n', '') + ',' + 'PharmacoDB.uid'
                    output.write(line + '\n')
                    first_line = False
                else:
                    drug_uid = ACRONYM + format(i, '05d')
                    line = line.replace('\n', '') + ',' + drug_uid
                    output.write(line + '\n')
                    i += 1
except:
    print('Something went wrong!!')
