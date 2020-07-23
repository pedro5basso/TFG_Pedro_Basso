import csv

with open('C:/Users/Pedro/Desktop/TFG/Code_Python/d3/prueba_c_tsv.csv','r') as csvin, open('C:/Users/Pedro/Desktop/TFG/Code_Python/d3/transformer.txt', 'w') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')

    for row in csvin:
        tsvout.writerow(row)