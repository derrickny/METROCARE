#convert excel to csv
import pandas as pd
import os
import csv
import openpyxl

# Path to the excel file
path = "data/KCB STATISTICS 2023.xlsx"

# Load the excel file
wb = openpyxl.load_workbook(path)

# Get the sheet names
sheet_names = wb.sheetnames

# Loop through the sheets
for sheet in sheet_names:
    # Load the sheet into a dataframe
    df = pd.read_excel(path, sheet_name=sheet)
    # Save the dataframe to a csv file
    df.to_csv(f"data/{sheet}.csv", index=False)
    print(f"Saved {sheet}.csv")

print("Done")