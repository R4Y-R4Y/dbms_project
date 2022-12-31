import csv
import json

# Create a dictionary to store the combined rows
combined = {}

# Open the input file
with open('test.csv', 'r') as infile:
  # Create a CSV reader
  reader = csv.reader(infile, delimiter='|')

  # Iterate through the rows of the input file
  for row in reader:
    # Extract the ID, hours, and days from the current row
    id, hours, days = row
    days = days[:-1]
    # If the ID and hours are not in the dictionary, add them as a new entry
    if (id, hours) not in combined:
      combined[(id, hours)] = days
    # If the ID and hours are already in the dictionary, append the days to the existing entry
    else:
      combined[(id, hours)] += ',' + days

# Convert the combined rows to a list of dictionaries
data = [{'id': id, 'hours': hours, 'days': days.split(',')} for (id, hours), days in combined.items()]

# Open the output file
with open('chefmozhours4_final.json', 'w') as outfile:
  # Write the data to the output file as JSON
  json.dump(data, outfile)
