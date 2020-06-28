import csv

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')

#     next(csv_reader)  # loop over the first line of the csv

#     for line in csv_reader:
#         print(line[2]) # using csv.reader, we need to open csv file to understand index 2 of the code

# Using Dict Reader instead of csvreader for ease of reading someone else codes
with open('CSVnames.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    with open('CSVnames_new.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:  # the first line header become the key
            # print(line[' email'])  # with DictReader, we know right away
            del line[' email']  # remove the email key
            csv_writer.writerow(line)
