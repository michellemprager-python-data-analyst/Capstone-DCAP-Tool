import os
import pandas as pd

def check_file_exists(filepath):
    return os.path.exists(filepath)

def initial_scan(df):
    return {
        "columns": df.columns.tolist(),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "total_rows": len(df)
    }

def etiquette_check(df):
    issues = []
    protected_columns = ["email"]
    if df.isnull().sum().sum() > 0:
        issues.append("Missing values found")
    if df.duplicated().sum() > 0:
        issues.append("Duplicate rows found")
    for col in df.columns:
        if col in protected_columns:
            issues.append(f"Column '{col}' is protected and will not be cleaned")
            continue
        if df[col].dtype == "object":
            if df[col].astype(str).str.contains(r"^\s|\s$").any():
                issues.append(f"Leading/trailing spaces found in column '{col}'")
            if df[col].astype(str).str.contains("  ").any():
                issues.append(f"Double spaces found in column '{col}'")
            if not df[col].astype(str).str.islower().all():
                issues.append(f"Inconsistent casing found in column '{col}'")
    return issues

def clean_data(df):
    protected_columns = ["email"]
    df = df.drop_duplicates()
    df = df.fillna("MISSING")
    df.columns = df.columns.str.lower().str.strip()
    for col in df.columns:
        if col not in protected_columns:
            if df[col].dtype == "object":
                df[col] = df[col].astype(str).str.strip().str.replace("  ", " ").str.lower()

    for col in protected_columns:
        if col in df.columns:
            df[col] = df[col].astype(str)
    return df

def final_scan(df):
    return {
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "total_rows": len(df),
        "columns": df.columns.tolist()
    }

def save_outputs(df):
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_cleaned_dcap.csv", index=False)
    with open("report.txt", "w") as f:
        f.write("DCAP Tool Report\n")
        f.write("=================\n")
        f.write("Rows: " + str(len(df)) + "\n")
        f.write("Columns: " + str(len(df.columns)) + "\n")

def main():
    filepath = "data/raw.csv"
    if not check_file_exists(filepath):
        return {"error": f"File not found: '{filepath}'. Please add data/raw.csv to your project."}
    try:
        df = pd.read_csv(filepath)
        before = initial_scan(df)
        issues = etiquette_check(df)
        cleaned_df = clean_data(df)
        after = final_scan(cleaned_df)
        save_outputs(cleaned_df)
        return {
            "before": before,
            "after": after,
            "issues_found": issues,
            "rows_removed": before["total_rows"] - after["total_rows"],
            "columns": after["columns"]
        }
    except Exception as e:
        return {"error": str(e)}
