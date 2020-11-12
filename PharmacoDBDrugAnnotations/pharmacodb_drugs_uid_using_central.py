"""
This file is used to create the UIDs for compounds that are present in PharmacoDB 
using the UIDs created/present in the drugsUIDCentral.csv file.
"""
import csv

# input and output file variables.
# input file with pharmacodb drugs.
pharmacodb_input_drugs = 'drugs.csv'
# input central file with the drug UIDs.
main_input_drugs = 'drugsUIDCentral.csv'
# output file.
output_file = "drugsUID.csv"

# dictionary to store the drug and uid mapping.
drug_uid_mapping = {}

# column number/index that have to be mapped.
column = [1, 3, 5, 6, 8, 10, 11, 12, 14, 16, 20, 21]


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
            csv_writer = csv.writer(output, delimiter=',')
            # header for the output file.
            csv_writer.writerow(['drug_id', 'drug_name', 'drug_uid',
                                 'fda_status', 'created_at', 'updated_at'])
            # looping through each line in the file
            # and appending the result to new file.
            for line in input_drugs:
                line = line.split(';')
                drug = line[1].replace('"', '')
                if line[0] != 'drug_id' and drug in drug_uid_mapping:
                    drug_uid = drug_uid_mapping[drug]
                    csv_writer.writerow(
                        [line[0], line[1], drug_uid, line[2], line[3], line[4].replace('\n', '')])
                elif drug.capitalize() in drug_uid_mapping:
                    drug_uid = drug_uid_mapping[drug.capitalize()]
                    csv_writer.writerow(
                        [line[0], line[1], drug_uid, line[2], line[3], line[4].replace('\n', '')])
                else:
                    print(line[1])
except:
    print('Something went wrong!!')
    raise
