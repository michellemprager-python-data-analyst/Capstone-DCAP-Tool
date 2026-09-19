📘 DCAP Tool — Data Cleaning & Processing Tool
    1   Author
Michelle M Prager  
Hamburg, NJ
Aspiring Data Analyst & Python Developer

    Capstone Notes
This project was created as part of my NCLab Python Developer Capstone.
It demonstrates:

Python scripting

Data cleaning logic

Flask web development

Project organization

Real‑world tool design

🧹 Overview
The DCAP Tool (Data Cleaning & Processing Tool) is a Python application designed to clean, validate, and process CSV datasets.
It includes automated cleaning logic, etiquette checks, duplicate detection, missing‑value handling, and a generated report summarizing the results.

A simple Flask web interface allows users to run the tool with one click, making it accessible even for non‑technical users.

🚀 Features
Automated CSV cleaning pipeline

Duplicate and formatting checks

Missing‑value handling

Etiquette and consistency checks

Cleaned CSV output

Generated report.txt summarizing the cleaning process

Flask web interface for easy use

Improved interface planned for future versions

📁 Project Structure
Code
Capstone_DCAP_Tool/
│
├── app.py                 # Flask web interface
├── cleaner.py             # Main data cleaning logic
├── requirements.txt       # Python dependencies
├── report.txt             # Generated cleaning report
│
├── templates/
│   └── index.html         # Web interface homepage
│
└── data/
    ├── raw.csv
    ├── cleaned.csv
    └── raw_cleaned_dcap.csv
🛠️ Installation
1. Clone the repository
Code
git clone <your-repo-url>
cd Capstone_DCAP_Tool
2. Install dependencies
Code
pip install -r requirements.txt
▶️ Running the Tool
Option A — Run the cleaning script directly
Code
python cleaner.py
This will:

Process the raw CSV

Generate cleaned output

Create report.txt

Option B — Run the Flask web interface
Code
python app.py
Then open your browser and go to:

Code
http://127.0.0.1:5000
Click Run DCAP Tool to execute the cleaning pipeline.

🌐 Future Enhancements
File upload support

Downloadable cleaned CSV

Downloadable report

Improved interface

Optional hosting on Render with custom domain