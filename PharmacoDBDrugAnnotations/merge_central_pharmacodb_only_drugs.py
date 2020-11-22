"""
This python code will grab the details of the compounds that are present in the pharmacodb database from the
drugUIDCentral.csv file.
"""
import csv

# input and output file variables.
# input file with pharmacodb drugs and corresponding UIDs.
pharmacodb_input_drugs = 'drugsUID.csv'
# input central file with the drug UIDs.
main_input_drugs = 'drugsUIDCentral.csv'
# output file.
output_file = "drugsMerge.csv"


# dictionary to map the drug_uid to drug_name from drugsUID.csv file.
drug_uid_mapping = {}

try:
    with open(pharmacodb_input_drugs, 'r') as pharmacodb:
        for line in csv.reader(pharmacodb):
            drug_uid_mapping[line[2]] = line[1]
    print(drug_uid_mapping)

    with open(main_input_drugs, 'r') as input:
        with open(output_file, 'w') as output:
            for line in csv.reader(input):
                if line[-1] == 'PharmacoDB.uid':
                    line = ','.join(line) + ',' + 'PharmacoDB.drugid'
                    output.write(line + '\n')
                elif line[-1] in drug_uid_mapping:
                    line = ','.join(line) + ',' + \
                        drug_uid_mapping[line[-1]]
                    output.write(line + '\n')
except:
    print('Something went wrong!!')
    raise
