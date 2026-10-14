
from pathlib import Path
import pandas as pd

DATA_DIR = Path(r"D:\data_set_ecommerce")

csv_files = sorted(DATA_DIR.glob("*.csv"))

summary = []

for file in csv_files:
    df = pd.read_csv(file)

    summary.append({
        "file_name": file.name,
        "row_count": len(df),
        "column_count": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "columns": ", ".join(df.columns),
        "total_missing_values": int(df.isnull().sum().sum())
    })

summary_df = pd.DataFrame(summary)

print("\nSOURCE DATA INVENTORY")
print(summary_df.to_string(index=False))

print("\nTotal CSV files:", len(csv_files))
print("Total rows across files:", summary_df["row_count"].sum())
