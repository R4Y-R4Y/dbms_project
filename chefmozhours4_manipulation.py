import csv

# Open the input and output files
with open('chefmozhours4.csv', 'r') as infile, open('test.csv', 'w', newline='') as outfile:
  # Create CSV readers and writer
  reader = csv.reader(infile, delimiter='|')
  writer = csv.writer(outfile, delimiter='|')

  # Skip the first line of the input file
  next(reader)

  # Iterate through the rows of the input file
  for row in reader:
    print(row)
    # If the row has only one set of hours, write it to the output file
    if len(row[1].split(',')) == 2:
      row[1] = row[1].split(',')[0]
      writer.writerow(row)
