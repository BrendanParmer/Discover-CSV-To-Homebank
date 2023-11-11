# Discover-CSV-To-Homebank
Convert Discover credit card CSV exports into a CSV format readable by Homebank software

## Installation
### Unix
1. In the directory where you'd like to store the script, clone the repository

    ```git clone https://github.com/BrendanParmer/Discover-CSV-To-Homebank```

2. Move into the directory

    ```cd Discover-CSV-To-Homebank```

3. Create a virtual environment

    ```python3 -m venv .venv```

4. Activate the virtual environment

    ```source .venv/bin/activate```

5. Install the requirements

    ```pip install -r requirements.txt```

## Usage
### Unix
```
usage: main.py [-h] input_file output_file

Transform Discover credit card CSV data for Homebank financial software.

positional arguments:
  input_file   Input CSV file (from Discover credit card data)
  output_file  Output CSV file (transformed data for Homebank)

options:
  -h, --help   show this help message and exit
```
Example
```
python3 main.py Discover-Statement-yyyymmdd.csv Homebank-Discover-yyyymmdd.csv
```
Make sure you have the virtual environment activated before running