import pandas as pd
import numpy as np

# ─────────────────────────────────────────
# STEP 1: Loaded the dataset
# ─────────────────────────────────────────
# Downloaded from Kaggle: " Sales Data"
df = pd.read_csv("sales_data.csv",encoding="latin1")

print("=" * 50)
print("INITIAL DATA OVERVIEW")
print("=" * 50)
print(f"Shape: {df.shape}")
print(f"\nColumn Names:\n{df.columns.tolist()}")
print(f"\nData Types:\n{df.dtypes}")
print(f"\nMissing Values:\n{df.isnull().sum()}")
print(f"\nDuplicate Rows: {df.duplicated().sum()}")
print(f"\nFirst 5 rows:\n{df.head()}")

# ─────────────────────────────────────────
# STEP 2: Cleaned Column Headers
# lowercase, strip spaces, replace spaces with underscore
# ─────────────────────────────────────────
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^a-z0-9_]", "", regex=True)
)
print("\n[✔] Column headers cleaned.")

# ─────────────────────────────────────────
# STEP 3: Removed Duplicate Rows
# ─────────────────────────────────────────
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"[✔] Duplicates removed: {before - after} rows dropped.")

# ─────────────────────────────────────────
# STEP 4: Handled Missing Values
# ─────────────────────────────────────────
# For numeric columns → filled with median
# For text/object columns → filled with 'Unknown'
for col in df.columns:
    missing = df[col].isnull().sum()
    if missing > 0:
        if df[col].dtype in [np.float64, np.int64]:
            df[col].fillna(df[col].median(), inplace=True)
            print(f"[✔] '{col}': {missing} missing values filled with median.")
        else:
            df[col].fillna("Unknown", inplace=True)
            print(f"[✔] '{col}': {missing} missing values filled with 'Unknown'.")

# ─────────────────────────────────────────
# STEP 5: Standardize Text Values
# Strip whitespace and converted to title case for object columns
# ─────────────────────────────────────────
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip().str.title()
print("[✔] Text columns standardized (stripped & title-cased).")

# ─────────────────────────────────────────
# STEP 6: Fixed Date Columns
# ─────────────────────────────────────────
date_cols = [col for col in df.columns if "date" in col]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")
    df[col] = df[col].dt.strftime("%d-%m-%Y")
    print(f"[✔] '{col}' converted to dd-mm-yyyy format.")

# ─────────────────────────────────────────
# STEP 7: Fixed Data Types
# ─────────────────────────────────────────
for col in df.columns:
    if df[col].dtype == "object":
        try:
            df[col] = pd.to_numeric(df[col])
            print(f"[✔] '{col}' converted to numeric.")
        except (ValueError, TypeError):
            pass 

# ─────────────────────────────────────────
# STEP 8: Saved Cleaned Dataset
# ─────────────────────────────────────────
df.to_csv("cleaned_sales_data.csv", index=False)
print("\n[✔] Cleaned dataset saved as 'cleaned_sales_data.csv'")

# ─────────────────────────────────────────
# STEP 9: Printed Final Summary
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("FINAL DATA OVERVIEW")
print("=" * 50)
print(f"Shape: {df.shape}")
print(f"\nData Types:\n{df.dtypes}")
print(f"\nMissing Values:\n{df.isnull().sum()}")
print(f"\nFirst 5 rows:\n{df.head()}")
print("\n[✔] Data Cleaning Complete!")
