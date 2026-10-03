# DCAP Tool - Data Cleaning and Processing Tool

Author: Michelle M. Prager
Hamburg, NJ - Aspiring Data Analyst and Python Developer

---

## Capstone Notes
This project was created as part of my NCLab Python Developer Capstone. It demonstrates:
- Python scripting
- Data cleaning logic
- Flask web development
- Project organization
- Real-world tool design

---

## Overview
The DCAP Tool is a Python application designed to clean, validate, and process CSV datasets.
It includes automated cleaning logic, duplicate detection, missing-value handling, and a
generated report summarizing the results.

A simple Flask web interface allows users to run the tool with one click, making it
accessible even for non-technical users.

---

## Features
- Automated CSV cleaning pipeline
- Duplicate and formatting checks
- Missing-value handling
- Etiquette and consistency checks
- Cleaned CSV output
- Generated report.txt summarizing the cleaning process
- Flask web interface for easy use

---

## Project Structure

Capstone_DCAP_Tool/
|
|-- app.py                  # Flask web interface
|-- cleaner.py              # Main data cleaning logic
|-- requirements.txt        # Python dependencies
|-- report.txt              # Generated cleaning report
|
|-- templates/
|   |-- index.html          # Web interface homepage
|   |-- results.html        # Cleaning results page
|
|-- data/
    |-- raw.csv
    |-- cleaned.csv
    |-- raw_cleaned_dcap.csv

---

## Installation

1. Clone the repository:
   git clone https://github.com/michellemprager-python-data-analyst/Capstone-DCAP-Tool.git

2. Navigate to the project folder:
   cd Capstone-DCAP-Tool

3. Install dependencies:
   pip install -r requirements.txt

---

## Sample Data
A sample messy dataset is included so you can test the tool immediately.

Location: data/raw.csv

The sample file contains intentional data quality issues including:
- Duplicate rows
- Missing values
- Inconsistent capitalization
- Leading and trailing spaces

To use the sample data:
- The file is already included at data/raw.csv
- Run the tool using Option A or Option B below
- Your cleaned file will be saved to data/raw_cleaned_dcap.csv
- A summary report will be saved to report.txt

To use your own data:
- Replace data/raw.csv with your own CSV file
- Keep the filename as raw.csv
- Run the tool the same way

---

## Running the DCAP Tool

Option A - Run the cleaning script directly:
   python cleaner.py

This will process the raw CSV, generate cleaned output, and create report.txt

Option B - Run the Flask web interface:
   python app.py

Then open your browser and go to:
   http://127.0.0.1:5000

Click Run DCAP Tool to execute the cleaning pipeline.

---

## Future Enhancements
- File upload support
- Downloadable cleaned CSV
- Downloadable report
- Improved interface
- Optional hosting on Render

---

## Training Program
Completed as part of the NCLab Python Developer Training Program
https://www.nclab.com
