import os
import pandas as pd

def check_file_exists(filepath):
    print("\nChecking if file exists...")
    if os.path.exists(filepath):
        print("✔ File found!")
        return True
    else:
        print("✘ File not found.")
        return False

def initial_scan(df):
    print("\nRunning initial scan...")
    print("Columns:", df.columns.tolist())
    print("Missing values per column:\n", df.isnull().sum())
    print("Duplicate rows:", df.duplicated().sum())

def etiquette_check(df):
    print("\nRunning etiquette check...")
    issues = []

    # Define protected and excluded columns
    protected_columns = ["email"]
    excluded_columns = []  # You can add columns here later

    # 1. Missing values
    if df.isnull().sum().sum() > 0:
        issues.append("Missing values found")

    # 2. Duplicate rows
    if df.duplicated().sum() > 0:
        issues.append("Duplicate rows found")

    # 3. Column-by-column etiquette checks
    for col in df.columns:

        # Protected columns
        if col in protected_columns:
            issues.append(f"Column '{col}' is protected and will not be cleaned")

        # Excluded columns
        if col in excluded_columns:
            issues.append(f"Column '{col}' is excluded from cleaning")

        # Only check text columns
        if df[col].dtype == "object":

            # Leading/trailing spaces
            if df[col].astype(str).str.contains(r"^\s|\s$").any():
                issues.append(f"Leading/trailing spaces found in column '{col}'")

            # Double spaces
            if df[col].astype(str).str.contains("  ").any():
                issues.append(f"Double spaces found in column '{col}'")

            # Mixed casing
            if not df[col].astype(str).str.islower().all():
                issues.append(f"Inconsistent casing found in column '{col}'")

    # Final report
    if len(issues) == 0:
        print("✔ No etiquette issues found!")
    else:
        print("✘ Issues found:")
        for issue in issues:
            print(" -", issue)


def clean_data(df):
    protected_columns = ['email']

    # 1. Drop duplicate rows
    df = df.drop_duplicates()

    # 2. Fill missing values
    df = df.fillna("MISSING")

    # ⭐ 3. Clean column names (lowercase + strip spaces)
    df.columns = df.columns.str.lower().str.strip()

    # 4. Smart cleaning for text columns
    for col in df.columns:
        if col not in protected_columns:
            if df[col].dtype == "object":
                df[col] = (
                    df[col]
                    .astype(str)
                    .str.strip()
                    .str.replace("  ", " ")
                    .str.lower()
                )


    # 4. Ensure protected columns stay untouched
    for col in protected_columns:
        if col in df.columns:
            df[col] = df[col].astype(str)

    return df


def final_scan(df):
    print("\nRunning final scan...")
    print("Missing values per column:\n", df.isnull().sum())
    print("Duplicate rows:", df.duplicated().sum())

def save_outputs(df):
    df.to_csv("data/raw_cleaned_dcap.csv", index=False)
    with open("report.txt", "w") as f:
        f.write("DCAP Tool Report\n")
        f.write("=================\n")
        f.write("Rows: " + str(len(df)) + "\n")
        f.write("Columns: " + str(len(df.columns)) + "\n")
    print("\n✔ Outputs saved: cleaned.csv and report.txt")

def run_dcap(filepath):
    print("\nWELCOME TO THE DCAP TOOL!")
    print("==========================")

    if not check_file_exists(filepath):
        return

    df = pd.read_csv(filepath)

    initial_scan(df)
    etiquette_check(df)

    df = clean_data(df)

    final_scan(df)
    save_outputs(df)

    print("\nDCAP Tool completed successfully!")


def main():
    import pandas as pd

    # Load your raw file
    df = pd.read_csv("data/raw.csv")

    # Run your cleaning function
    cleaned_df = clean_data(df)

    # Run your final scan
    final_scan(cleaned_df)

    # Save outputs
    save_outputs(cleaned_df)

    print("\nDCAP Tool completed successfully!")
