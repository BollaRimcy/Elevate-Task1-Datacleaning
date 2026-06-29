Task 1 – Data Cleaning and Preprocessing

Internship: Data Analyst Internship (Elevate Labs)


Objective

Clean and prepare a raw Sales dataset by handling missing values, removing duplicates, standardizing formats, and fixing data types — making it ready for analysis.


Tools Used


Python 3.x
Pandas
NumPy



Dataset

Sales Data — downloaded from Kaggle

https://www.kaggle.com/datasets/kyanyoga/sample-sales-data


Steps Performed

StepAction1Loaded the raw CSV dataset2Cleaned column headers (lowercase, underscores, no special chars)3Removed duplicate rows4Handled missing values (median for numeric, 'Unknown' for text)5Standardized text columns (stripped whitespace, title case)6Converted date columns to consistent dd-mm-yyyy format7Fixed data types (strings to numeric where applicable)8Exported the cleaned dataset as CSV


Summary of Changes


Duplicate rows removed: checked and dropped using drop_duplicates()
Missing values handled: numeric columns filled with median; text columns filled with 'Unknown'
Column names cleaned: all headers made lowercase with underscores
Text standardized: stripped extra whitespace, applied title case
Dates formatted: all date columns converted to dd-mm-yyyy using pd.to_datetime()
Data types corrected: numeric columns stored as strings were converted appropriately



Files in This Repository

task1-datacleaning/
├── data_cleaning.py
├── sales_data.csv
├── cleaned_sales_data.csv
└── README.md


How to Run

bash# Install required libraries
pip install pandas numpy

# Run the script
python data_cleaning.py

The cleaned dataset will be saved as cleaned_sales_data.csv in the same folder.