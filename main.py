import argparse
import pandas as pd
import json

def load_category_mapping(categories_file):
    try:
        with open(categories_file, 'r') as f:
            category_mapping = json.load(f)
        return category_mapping
    except FileNotFoundError:
        print(f"Error: Configuration file '{categories_file}' not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{categories_file}'.")
        exit(1)

def transform_discover_csv(input_file, output_file, categories_file):
    # Load your CSV data into a pandas DataFrame
    credit_card_data = pd.read_csv(input_file)

    # For some reason Discover thought it'd be a good idea to list all the
    # credits as negative and the debits as positive
    credit_card_data['Amount'] *= -1

    # Apply category mapping if config file is provided
    if categories_file:
        # Load category mapping from the config file
        category_mapping = load_category_mapping(categories_file)

        # Map credit card categories to custom categories
        credit_card_data['Category'] = credit_card_data['Category'].map(category_mapping)

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

def transform_bmo_alto_csv(input_file, output_file, categories_file):
    data = pd.read_csv(input_file)
    transformed_data = pd.DataFrame({
        'date': data['Date'],
        'payment' : '',
        'info' : '',
        'payee': '',
        'memo' : data['Description'],
        'amount' : data['Credits(+)'],
        'category' : '',
        'tags' : ''
    })
    transformed_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transform CSV data for Homebank financial software.')
    parser.add_argument('input_file', help='Input CSV file')
    parser.add_argument('output_file', help='Output CSV file')
    parser.add_argument('--mode', help="One of {DISCOVER, BMO_ALTO}")
    parser.add_argument('--categories', help='Path to the category mapping config file')
    args = parser.parse_args()

    if args.mode == 'DISCOVER':
        transform_discover_csv(args.input_file, args.output_file, args.categories)
    elif args.mode == 'BMO_ALTO':
        transform_bmo_alto_csv(args.input_file, args.output_file, args.categories)
    else:
        print(f"No conversion found for mode {args.mode}")