import sys
import csv
from pathlib import Path

import questionary

# from actions.add import add
# from actions.delete import delete
# from actions.filter ipmort filter
# from actions.sort import sort

# ask user make an action
def add_headers():
    action = questionary.select(
        "Would you like to add column headers?",
        choices = ['Yes', 'No']
    ).ask()
    return action

# Ask user to identify headers
def create_header_list():
    header_list = []
    adding = True
    while adding:
        action = add_headers()
        if action == 'Yes':
            header_name = input("Enter the name of the column: ")
            header_list.append(header_name)
        else:
            adding = False

# Return header row contents
    return header_list

# initialize list of dictionaries with the header row
# Database info will go into the object returned by this function
def init_table(header_list):
    dict_header = {}
    table_list = []
    for header in header_list:
        for i in len(header_list):
            dict_header[header] = [header]
        table_list.append(dict_header)
    return table_list

# Write to csv - table data
def write_table():
    rows = init_table()
    csv_path = Path("./data/database.csv")

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)

# Show staged changes

# Update csv with new information