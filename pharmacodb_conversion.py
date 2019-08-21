import csv
import re


input_file = './final_csv_files/cell_line_pharmacodb.csv'
input_file1 = './final_csv_files/Cellosaurus_pharmacodb_mapping_Final_File.csv'
output_file = './final_csv_files/final_cell_table.csv'


def readFile(readfile, readfile1, writefile):
    with open(readfile, 'r') as txt_file:
        with open(writefile, 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter = ",")
            csv_writer.writerow(['cell_id','accession_id','cell_name','tissue_id','created_at','updated_at','cell_line_uid'])
            for row in txt_file:
                if(re.search(r'\cell_id\b', row)):
                    print('not useful')
                else:
                    row = row.split(",")
                    with open(readfile1, 'r') as txt_file1:
                        for value in txt_file1:
                            if(re.search(r'\cell_line\b', value)):
                                print('not useful1')
                            else:
                                value = value.split(",")
                                if(value[0] == row[1] and value[1] == row[6].replace("\n", "") and value[2].replace("\n", "").replace("\r", "") == row[2]):
                                    csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6].replace("\n", "")])
                                    break
                                elif(value[1] == row[6].replace("\n", "") and value[2].replace("\n", "").replace("\r", "") == row[2]):
                                    csv_writer.writerow([row[0], value[0], row[2], row[3], row[4], row[5], row[6].replace("\n", "")])
                                    break

                    
               
readFile(input_file, input_file1, output_file)