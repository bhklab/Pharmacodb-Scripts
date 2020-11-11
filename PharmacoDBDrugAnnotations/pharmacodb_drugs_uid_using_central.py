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
outputFile = "drugsUID.csv"
