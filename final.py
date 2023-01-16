import json

# Open the file
with open("chefmozhours4_final_final.json", "r") as file:
    # Load the JSON data from the file
    data = json.load(file)

# Create a dictionary to group the arrays by their placeID
grouped_arrays = {}

# Iterate over the arrays and group them by their placeID
for array in data:
    placeID = array["placeID"]
    if placeID not in grouped_arrays:
        grouped_arrays[placeID] = {"days": set(), "hours": []}
    grouped_arrays[placeID]["days"].update(array["days"])
    grouped_arrays[placeID]["hours"].extend(array["hours"])

# Create a new list with the concatenated data
concatenated_data = []
for placeID, value in grouped_arrays.items():
    concatenated_array = {"placeID": placeID, "hours": value["hours"], "days": list(value["days"])}
    concatenated_data.append(concatenated_array)

# Now you have a list containing the concatenated data with hours before days
with open('chefmozhours4_final_final_final.json', 'w') as outfile:
    json.dump(concatenated_data, outfile)