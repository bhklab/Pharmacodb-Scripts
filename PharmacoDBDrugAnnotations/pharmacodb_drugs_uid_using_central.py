"""
This file is used to create the UIDs for compounds that are present in PharmacoDB
using the UIDs created/present in the drugsUIDCentral.csv file.
Note: Nelfivir is mapped using the drug name Nelfinavir
      and Lisitinib to Linsitinib. These both are mapped manually.
      Also map OSI-906 for now.
"""

import csv

# input and output file variables.
# input file with pharmacodb drugs.
pharmacodb_input_drugs = 'drugs.csv'
# input central file with the drug UIDs.
main_input_drugs = 'drugsUIDCentral.csv'
# output file.
output_file = "drugsUID.csv"

# dictionary to map the wrong named drugs.
missing_drugs = {
    "Nelfivir": "PDBC49359",
    "Lisitinib": "PDBC00096",
    "OSI-906": "PDBC00096-R",
    "pazopanib": "PDBC00102-R",
    "tipifarnib": "PDBC00106-R",
}


# dictionary to store the drug and uid mapping.
drug_uid_mapping = {}

# list to maintained already used PharmacoDB.uids.
pharmacodb_uids = []

# column number/index that have to be mapped.
column = [1, 3, 5, 6, 8, 10, 11, 12, 14, 16, 20, 21]

# header for the new file.
header = ['drug_id', 'drug_name', 'drug_uid',
          'fda_status', 'created_at', 'updated_at']


# function to do the mapping.
def map_drug_to_uid(i, line):
    if '///' in line[i]:
        drug = line[i].split('///')
        for j in drug:
            drug_uid_mapping[j] = line[-1]
    else:
        drug_uid_mapping[line[i]] = line[-1]


# try except block.
try:
    # creates the mapping object.
    # puts the drugs from several datasets in the mapping.
    with open(main_input_drugs, 'r') as input:
        for line in csv.reader(input):
            for i in column:
                map_drug_to_uid(i, line)

    # generating the output file.
    with open(pharmacodb_input_drugs, 'r') as input_drugs:
        with open(output_file, 'w') as output:
            csv_writer = csv.writer(output, delimiter=',', quotechar="'")
            # looping through each line in the file
            # and appending the result to new file.
            for line in input_drugs:
                line = line.split(';')
                drug_uid = ''
                drug = line[1].replace('"', '').strip()
                last = line[4].replace('\n', '')
                if line[0] == 'drug_id':
                    drug_uid = 'drug_uid'
                elif drug in missing_drugs:
                    drug_uid = missing_drugs[drug]
                elif drug in drug_uid_mapping:
                    drug_uid = drug_uid_mapping[drug]
                elif drug.capitalize() in drug_uid_mapping:
                    drug_uid = drug_uid_mapping[drug.capitalize()]
                else:
                    print('This compound was not mapped!', line[1])
                    drug_uid = 'NA'
                # if the uid is already present or used then add an -R to it.
                if(drug_uid in pharmacodb_uids):
                    drug_uid = drug_uid + '-R'
                # appending uids to the list.
                else:
                    pharmacodb_uids.append(drug_uid)
                # write to the csv file.
                csv_writer.writerow(
                    [line[0], line[1], drug_uid, line[2], line[3], last])

except:
    print('Something went wrong!!')
    raise
