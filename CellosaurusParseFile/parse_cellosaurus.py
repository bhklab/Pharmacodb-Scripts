import csv
import re

# variables to set the file path and a dictionary for the data.
cellosaurus_txt_file = 'cellosaurus.txt'
output_parsed_file = 'cellosaurus_cell_line_output.csv'
cellosaurus_data = {
    'identifier': '',
    'accession': '',
    'as': '',
    'sy': '',
    'dr': '',
    'rx': '',
    'ww': '',
    'cc': '',
    'st': '',
    'di': '',
    'ox': '',
    'hi': '',
    'oi': '',
    'sx': '',
    'ag': '',
    'ca': '',
    'dt': ''
}
homosapiens = False

#function to output results.
def outputResult(row, csv_writer):
    global homosapiens
    if(re.search(r'\bID\b', row) and not (re.search(r'\bIdentifier\b', row))):
        cellosaurus_data['identifier'] = (cellosaurus_data['identifier'] + row.split('   ')[1].replace("\n",""))
    elif(re.search(r'\bAC\b', row) and not (re.search(r'\bAccession|Next\b', row))):
        cellosaurus_data['accession'] = (cellosaurus_data['accession'] + row.split('   ')[1].replace("\n",""))
    elif(re.search(r'\bSY\b', row) and not (re.search(r'\bSynonyms\b', row))):
        cellosaurus_data['sy'] = (cellosaurus_data['sy'] + row.split('   ')[1].replace("\n",""))
    elif(re.search(r'\b(AS|DR|RX|WW|CC|ST|DI|HI|OI|SX|AG|CA|DT)\b', row) and 
        not(re.search(r'\b(Secondary accession|Cross-references|References identifiers|Web pages|Comments|STR profile data|Diseases|Hierarchy|Originate from same individual|Sex|Age of donor at sampling|Category|Date|Once|Optional)\b', row))):
        cellosaurus_data[row.split('   ')[0].lower()] = (cellosaurus_data[row.split('   ')[0].lower()] + row.split('   ')[1].replace("\n","|"))
    elif(re.search(r'\bOX\b', row) and not (re.search(r'\bSpecies of origin\b', row))):
        cellosaurus_data['ox'] = (cellosaurus_data['ox'] + row.split('   ')[1].replace("\n","; "))
        if(re.search(r'\bHomo sapiens\b', row)):
            homosapiens = True
    elif(re.search(r'^//', row) and not (re.search(r'\bTerminator\b', row)) and homosapiens):
        #print(cellosaurus_data['dr'])
        csv_writer.writerow([cellosaurus_data['identifier'], cellosaurus_data['accession'], cellosaurus_data['as'], cellosaurus_data['sy'], cellosaurus_data['dr'], 
        cellosaurus_data['rx'], cellosaurus_data['ww'], cellosaurus_data['cc'], cellosaurus_data['st'], cellosaurus_data['di'], cellosaurus_data['ox'], 
        cellosaurus_data['hi'], cellosaurus_data['oi'], cellosaurus_data['sx'], cellosaurus_data['ag'], cellosaurus_data['ca'], cellosaurus_data['dt']])
        homosapiens = False
        for id in cellosaurus_data.keys():
            cellosaurus_data[id] = ''
    elif(re.search(r'^//', row) and not (re.search(r'\bTerminator\b', row)) and not (homosapiens)):
        for id in cellosaurus_data.keys():
            cellosaurus_data[id] = ''


#function to parse the cellosaurus.txt file.
def readFile(readfile, writefile):
    with open(readfile, 'r') as txt_file:
        with open(writefile, 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter = ',')
            csv_writer.writerow(['identifier', 'accession', 'as', 'sy', 'dr', 'rx', 'ww', 'cc', 'st', 'di', 'ox', 'hi', 'oi', 'sx', 'ag', 'ca', 'dt'])
            for row in txt_file:
                outputResult(row, csv_writer)



#calling readfile function.
readFile(cellosaurus_txt_file, output_parsed_file)