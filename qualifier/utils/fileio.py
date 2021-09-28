# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(output_path, data_results, header = None):
    """Saves the qualifying loans to a CSV file.

    Args:
        output_path (str) : The Path provided by the user.
        data_results (list of lists): The qualifying bank loans.
        head: No header is asigned
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # header = ["Lender", "Max_loan_Amount", "Max_LTV", "Max_DTI","Min_Credit_Score","Interest_Rate"]
    # set the output path
    # output_path = Path("qualifying_loans.csv")
    # Use the csv library and `csv.writer` to write the header row
    # and each row of the `qualifying_loans` list.
    with open (output_path, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        #csvwriter.writerow(header)
        # for row in data_results:
            # csvwriter.writerow(row)
        if header:
            csvwriter.writerow(header)
        csvwriter.writerows(data_results)
