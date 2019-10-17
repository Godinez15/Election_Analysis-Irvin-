import csv

with open ('names.csv', 'r') as csv_file:
    csv_reader= csv.DictReader(csv_file)

#for line in csv_reader:
    print(line['email'])

with open('new_names.csv','w') as new_file:
    fielnames= ['first_name', 'last_name','email']
    csv_writer= csv.writer(new_file, delimiter='\t')

csv_writeheader()

for line in csv_reader:
  del line['email']
    csv_writer.writerow(line)

