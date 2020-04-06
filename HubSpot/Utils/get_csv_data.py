import csv

def get_csv_data(csv_path_fileName):
    rows = []
    dataFile = open(csv_path_fileName, "r")  # open the CSV file
    content = csv.reader(dataFile)
    next(content, None)  # skip the headers
    for row in content:
        rows.append(row)  # add rows
    return rows
