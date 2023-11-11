import argparse
import pandas as pd

def transform_csv(input_file, output_file):
    # Load your CSV data into a pandas DataFrame
    credit_card_data = pd.read_csv(input_file)

    # For some reason Discover thought it'd be a good idea to list all the
    # credits as negative and the debits as positive
    credit_card_data['Amount'] *= -1

    # Create a new DataFrame with the desired columns and transform the data
    transformed_data = pd.DataFrame({
        'date': credit_card_data['Trans. Date'],
        'payment': 1,
        'info': '',
        'payee': '',
        'memo': credit_card_data['Description'],
        'amount': credit_card_data['Amount'],
        'category': credit_card_data['Category'],
        'tags': ''
    })

    # Save the transformed data to a new CSV file
    transformed_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transform Discover credit card CSV data for Homebank financial software.')
    parser.add_argument('input_file', help='Input CSV file (from Discover credit card data)')
    parser.add_argument('output_file', help='Output CSV file (transformed data for Homebank)')

    args = parser.parse_args()

    transform_csv(args.input_file, args.output_file)